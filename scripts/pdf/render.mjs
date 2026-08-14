#!/usr/bin/env node
// Renders build/Drakenhold_Playbook.md to a paginated build/Drakenhold_Playbook.pdf.
//
// Usage: node render.mjs [INPUT.md] [OUTPUT.pdf]
//
// Pipeline: mermaid fenced blocks -> static SVG (via mermaid-cli), the rest
// of the markdown -> HTML (via marked), wrapped in print CSS, printed to a
// paginated PDF by a headless browser (puppeteer). Each `# ` heading (the
// setting title, and every region's own title) starts a fresh page, so the
// PDF is flippable at the table the same way the source files are read.
//
// This step is not part of check.sh/build.sh's zero-dependency guarantee —
// it needs mermaid-cli and a headless browser.

import { execFileSync } from "node:child_process";
import { mkdtempSync, readFileSync, writeFileSync, rmSync, mkdirSync } from "node:fs";
import { tmpdir } from "node:os";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { marked } from "marked";
import puppeteer from "puppeteer";

const HERE = path.dirname(fileURLToPath(import.meta.url));
const REPO = path.resolve(HERE, "..", "..");

const inputPath = path.resolve(process.argv[2] || path.join(REPO, "build", "Drakenhold_Playbook.md"));
const outputPath = path.resolve(process.argv[3] || path.join(REPO, "build", "Drakenhold_Playbook.pdf"));

function fail(message) {
  console.error(`pdf render failed: ${message}`);
  process.exit(1);
}

let markdown;
try {
  markdown = readFileSync(inputPath, "utf8");
} catch {
  fail(`missing input file: ${inputPath} (run scripts/build.sh first)`);
}

const MERMAID_BLOCK_RE = /```mermaid\n([\s\S]*?)```/g;
const MMDC = path.join(HERE, "node_modules", ".bin", "mmdc");

const workDir = mkdtempSync(path.join(tmpdir(), "drakenhold-pdf-"));
const puppeteerConfigPath = path.join(workDir, "puppeteer-config.json");
writeFileSync(puppeteerConfigPath, JSON.stringify({ args: ["--no-sandbox"] }));

let diagramCount = 0;
let renderFailures = 0;

function renderMermaidToSvg(code) {
  diagramCount += 1;
  const inFile = path.join(workDir, `diagram-${diagramCount}.mmd`);
  const outFile = path.join(workDir, `diagram-${diagramCount}.svg`);
  writeFileSync(inFile, code);
  try {
    execFileSync(MMDC, ["-i", inFile, "-o", outFile, "-p", puppeteerConfigPath, "-b", "transparent"], {
      stdio: ["ignore", "ignore", "pipe"],
    });
  } catch (e) {
    renderFailures += 1;
    console.error(`  diagram ${diagramCount}: mermaid render failed — ${e.stderr?.toString().trim() || e.message}`);
    return `<div class="diagram-error">[diagram ${diagramCount} failed to render — see build log]</div>`;
  }
  const svg = readFileSync(outFile, "utf8");
  return `<div class="diagram">${svg}</div>`;
}

console.log(`Rendering mermaid diagrams from ${path.relative(REPO, inputPath)}...`);
const withDiagramsInlined = markdown.replace(MERMAID_BLOCK_RE, (_match, code) => renderMermaidToSvg(code));
console.log(`  ${diagramCount} diagram(s) processed, ${renderFailures} failed`);

if (renderFailures > 0) {
  rmSync(workDir, { recursive: true, force: true });
  fail(`${renderFailures} of ${diagramCount} mermaid diagram(s) failed to render`);
}

// ---------------------------------------------------------------------------
// Connection pointers
// ---------------------------------------------------------------------------
// Location text writes connection pointers as plain ASCII "->" so that the
// source stays human-writable in any editor. The reader gets a single
// typographic arrow. Substitution happens on marked's output rather than on
// the markdown, so that pre/code blocks — mermaid source, sample markup —
// keep the ASCII they were authored with.
const _PRE_OR_CODE_RE = /<pre[\s\S]*?<\/pre>|<code[\s\S]*?<\/code>/g;
const _ARROW_RE = /(^|\s)-&gt;(\s|$)/g;

function arrowify(html) {
  const out = [];
  let last = 0;
  for (const m of html.matchAll(_PRE_OR_CODE_RE)) {
    out.push(html.slice(last, m.index).replace(_ARROW_RE, "$1\u2192$2"));
    out.push(m[0]);
    last = m.index + m[0].length;
  }
  out.push(html.slice(last).replace(_ARROW_RE, "$1\u2192$2"));
  return out.join("");
}

const bodyHtml = arrowify(marked.parse(withDiagramsInlined));

const page = `<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Drakenhold</title>
<style>
  @page { size: Letter; margin: 0.75in; }
  body {
    font-family: Georgia, "Times New Roman", serif;
    font-size: 11pt;
    line-height: 1.4;
    color: #1a1a1a;
  }
  h1 { break-before: page; font-size: 20pt; border-bottom: 2px solid #333; padding-bottom: 0.15em; }
  h1:first-of-type { break-before: avoid; }
  h2 { font-size: 15pt; margin-top: 1.4em; border-bottom: 1px solid #999; padding-bottom: 0.1em; }
  h3 { font-size: 12.5pt; margin-top: 1.2em; }
  code, pre { font-family: "Courier New", monospace; }
  table { border-collapse: collapse; width: 100%; margin: 0.8em 0; font-size: 9.5pt; }
  th, td { border: 1px solid #999; padding: 0.3em 0.5em; text-align: left; vertical-align: top; }
  th { background: #eee; }
  blockquote { border-left: 3px solid #999; margin: 0.5em 0; padding-left: 1em; color: #444; }
  .diagram { break-inside: avoid; margin: 1em 0; text-align: center; }
  .diagram svg { max-width: 100%; height: auto; }
  .diagram-error { color: #b00; font-style: italic; }
  em { font-style: italic; }
  hr { border: none; border-top: 1px solid #ccc; margin: 1.5em 0; }
</style>
</head>
<body>
${bodyHtml}
</body>
</html>`;

console.log("Printing to PDF...");
const browser = await puppeteer.launch({ args: ["--no-sandbox"] });
try {
  const tab = await browser.newPage();
  await tab.setContent(page, { waitUntil: "load" });
  mkdirSync(path.dirname(outputPath), { recursive: true });
  await tab.pdf({ path: outputPath, format: "Letter", printBackground: true });
} finally {
  await browser.close();
  rmSync(workDir, { recursive: true, force: true });
}

console.log(`Wrote ${path.relative(REPO, outputPath)}`);
