#!/usr/bin/env python3
"""
The Drakenhold diagram layer: five tiers, one file per diagram, all in
`diagrams/`.

    Tier 1  the setting          shows the region blocks
    Tier 2  a region block       shows the regions it contains
    Tier 3  a region             shows the location groups it contains
    Tier 4  a location group     shows the locations it contains
    Tier 5  a location           has no diagram; it is the leaf

Each diagram shows **only the tier below it** and how those elements
interconnect. Connection type — the edge vocabulary in
`diagrams/Drakenhold_Relational_Diagram.md` — is drawn at tier 4 and nowhere
else; tiers 1 to 3 draw a single untyped `---` between two children however
many typed edges run between them. Where a tier-4 edge leaves its group, the
destination location is drawn on that diagram, outside the group frame.

**Tier 4 is authored. Tiers 1 to 3 are derived from it** by `--write` below,
and `check.py` M11 fails if a committed tier-1-to-3 file does not match what
this module derives. There is therefore exactly one place any given fact about
the graph is written down.

Host files carry a marker line and no mermaid of their own:

    <!-- DIAGRAM: T4_FA_WARREN.md -->

`splice()` replaces each marker with the diagram file's contents. `build.py`
and `scripts/pdf/render_web.mjs` both call it, so the PDF and the web build
reassemble every diagram into place.

Usage:
    diagrams.py            report the derived tiers against what is on disk
    diagrams.py --write    regenerate the tier-1 to tier-3 files
"""

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DIAGRAM_DIR = REPO / "diagrams"
REGION_DIR = REPO / "regions"
INDEX = REGION_DIR / "00_INDEX.md"

# ---------------------------------------------------------------------------
# The block map — tier 1's children, and tier 2's frames.
# Five blocks. Note this is not the same partition as `blocks/`, which is an
# authoring partition: FA, GA and HA are stubbed together because they share a
# warren, but each belongs to its own peak on the graph, and a peak whose main
# level is missing is not a legible diagram.
# ---------------------------------------------------------------------------
BLOCKS: list[tuple[str, str, list[str]]] = [
    ("APPROACH", "The approach", ["A", "B", "C", "D", "E"]),
    ("PEAK_1", "Peak 1 · Trade and Craft", ["FA", "FB", "FC", "FD", "FE"]),
    ("PEAK_2", "Peak 2 · Authority and the Dragon", ["GA", "GB", "GC", "GD", "GE"]),
    ("PEAK_3", "Peak 3 · Spirit and the Dead", ["HA", "HB", "HC", "HD", "HE"]),
    ("I_AND_J", "The Skybridge and the Lost Caverns", ["I", "J"]),
]

BLOCK_OF_REGION = {r: key for key, _, regions in BLOCKS for r in regions}

MARKER_RE = re.compile(r'^<!--\s*DIAGRAM:\s*(T[1-4]_[A-Z0-9_]+\.md)\s*-->\s*$')

_INDEX_ROW_RE = re.compile(r'^\|\s*([A-Z]{1,2})\s*\|\s*([^|]+?)\s*\|')
_NODE_RE = re.compile(r'^\s*(\w+)\["([^"]*)"\]\s*$')
_SUBGRAPH_RE = re.compile(r'^\s*subgraph\s+(\w+)\["([^"]*)"\]\s*$')
_EDGE_RE = re.compile(
    r'^\s*(\w+)\s*'
    r'(-\.->|-\.-|-->|---|==>|===)\s*'
    r'(?:\|\s*"?([^|]*?)"?\s*\|\s*)?'
    r'(\w+)\s*$'
)
_CODE_RE = re.compile(r'^([A-Z]{1,2}\.[0-9]+[a-z]?)\b')

GENERATED_NOTE = (
    "Derived from the tier-4 diagrams by `scripts/diagrams.py --write`. "
    "Do not hand-edit: `check.py` M11 re-derives it and fails on drift. "
    "One untyped edge per connected pair — connection type is drawn at "
    "tier 4 only."
)


# ---------------------------------------------------------------------------
# Reading
# ---------------------------------------------------------------------------
def region_names() -> dict[str, str]:
    """Region code → short display name, from 00_INDEX.md's table."""
    names: dict[str, str] = {}
    for line in INDEX.read_text(encoding="utf-8").splitlines():
        m = _INDEX_ROW_RE.match(line.strip())
        if m and m.group(1) != "Code":
            names[m.group(1)] = m.group(2).split(",")[0].strip()
    return names


def node_code(label: str) -> str | None:
    """`FA.30 · The Bypass` → `FA.30`. None if the label carries no code."""
    head = label.split("·")[0].strip() if "·" in label else label.strip()
    m = _CODE_RE.match(head)
    return m.group(1) if m else None


class Tier4(dict):
    """One parsed tier-4 file: group key, title, members, edges."""


def parse_tier4(path: Path) -> Tier4:
    """Parse a tier-4 diagram file.

    Returns {region, group, key, title, members, labels, edges} where members
    is the ordered list of location codes inside the group frame, labels maps
    every code the file draws to its display label, and edges is the ordered
    list of (code_a, code_b) pairs the file draws, type discarded.
    """
    text = path.read_text(encoding="utf-8")
    body_m = re.search(r'```mermaid\n(.*?)\n```', text, re.S)
    if not body_m:
        raise ValueError(f"{path.name}: no mermaid block")

    labels: dict[str, str] = {}          # node id → label
    members: list[str] = []
    edges: list[tuple[str, str, bool, int]] = []   # a, b, directed, lineno
    key = title = ""
    inside = False

    offset = text[:body_m.start(1)].count("\n") + 1
    for n, raw in enumerate(body_m.group(1).splitlines(), offset):
        line = raw.rstrip()
        if not line.strip():
            continue
        m = _SUBGRAPH_RE.match(line)
        if m:
            key, title = m.group(1), m.group(2)
            inside = True
            continue
        if line.strip() == "end":
            inside = False
            continue
        m = _NODE_RE.match(line)
        if m:
            labels[m.group(1)] = m.group(2)
            if inside:
                members.append(m.group(1))
            continue
        m = _EDGE_RE.match(line)
        if m:
            edges.append((m.group(1), m.group(4), m.group(2).endswith(">"), n))
            continue
        if line.strip().startswith("graph "):
            continue
        raise ValueError(f"{path.name}: unparsed diagram line: {line.strip()!r}")

    def code_of(node_id: str) -> str:
        label = labels.get(node_id)
        code = node_code(label) if label else None
        if not code:
            raise ValueError(f"{path.name}: node {node_id} carries no location code")
        return code

    region, group = key.split("_", 1) if "_" in key else (key, "")
    return Tier4(
        path=path, region=region, group=group, key=key, title=title,
        members=[code_of(i) for i in members],
        labels={code_of(i): labels[i] for i in labels},
        edges=[(code_of(a), code_of(b)) for a, b, _, _ in edges],
        typed=[(code_of(a), code_of(b), d, n) for a, b, d, n in edges],
    )


def load_tier4() -> list[Tier4]:
    """Every tier-4 file, ordered by region (index order) then by file name."""
    order = {code: i for i, code in enumerate(region_names())}
    files = sorted(DIAGRAM_DIR.glob("T4_*.md"))
    parsed = [parse_tier4(f) for f in files]
    parsed.sort(key=lambda d: (order.get(d["region"], 99), d["path"].name))
    return parsed


# ---------------------------------------------------------------------------
# Deriving
# ---------------------------------------------------------------------------
def _render(header_note: str, lines: list[str]) -> str:
    while lines and not lines[-1]:
        lines = lines[:-1]
    body = "\n".join(("  " + l) if l else "" for l in lines)
    return f"<!-- {header_note} -->\n\n```mermaid\ngraph TD\n{body}\n```\n"


def _untyped_edges(pairs: list[tuple[str, str]]) -> list[tuple[str, str]]:
    """Collapse a list of ordered pairs to one undirected edge per pair,
    in first-seen order."""
    seen: set[frozenset[str]] = set()
    out: list[tuple[str, str]] = []
    for a, b in pairs:
        if a == b:
            continue
        k = frozenset((a, b))
        if k in seen:
            continue
        seen.add(k)
        out.append((a, b))
    return out


def derive(tier4: list[Tier4]) -> dict[str, str]:
    """Derive every tier-1 to tier-3 file. Returns {file name: contents}."""
    names = region_names()

    # code → group key, from the tier-4 group frames.
    group_of: dict[str, str] = {}
    group_title: dict[str, str] = {}
    groups_in_region: dict[str, list[str]] = {}
    for d in tier4:
        group_title[d["key"]] = d["title"]
        groups_in_region.setdefault(d["region"], []).append(d["key"])
        for code in d["members"]:
            group_of[code] = d["key"]

    # Every edge any tier-4 file draws, as group-key pairs.
    group_pairs: list[tuple[str, str]] = []
    for d in tier4:
        for a, b in d["edges"]:
            ga, gb = group_of.get(a), group_of.get(b)
            if ga and gb:
                group_pairs.append((ga, gb))

    def region_of_group(key: str) -> str:
        return key.split("_", 1)[0]

    out: dict[str, str] = {}

    # --- Tier 3: one per region, its location groups ---
    for region, keys in groups_in_region.items():
        # The frame titles carry the region code so a tier-4 file reads alone.
        # Here the whole diagram is the region, so the prefix is dropped.
        lines = [f'{k}["{group_title[k].removeprefix(region + " · ")}"]' for k in keys]
        inside = [(a, b) for a, b in group_pairs
                  if region_of_group(a) == region and region_of_group(b) == region]
        lines.append("")
        lines += [f"{a} --- {b}" for a, b in _untyped_edges(inside)]
        note = (f"Tier 3 · region {region} · the location groups and how they "
                f"interconnect. {GENERATED_NOTE}")
        out[f"T3_{region}.md"] = _render(note, lines)

    # --- Tier 2: one per block, its regions ---
    region_pairs = _untyped_edges([
        (region_of_group(a), region_of_group(b)) for a, b in group_pairs
    ])
    for key, title, regions in BLOCKS:
        lines = [f'{r}["{r} · {names.get(r, r)}"]' for r in regions if r in groups_in_region]
        inside = [(a, b) for a, b in region_pairs if a in regions and b in regions]
        lines.append("")
        lines += [f"{a} --- {b}" for a, b in inside]
        note = (f"Tier 2 · {title} · the regions in the block and how they "
                f"interconnect. {GENERATED_NOTE}")
        out[f"T2_{key}.md"] = _render(note, lines)

    # --- Tier 1: the setting, its blocks ---
    lines = [f'{key}["{title}"]' for key, title, _ in BLOCKS]
    block_pairs = _untyped_edges([
        (BLOCK_OF_REGION[a], BLOCK_OF_REGION[b]) for a, b in region_pairs
        if a in BLOCK_OF_REGION and b in BLOCK_OF_REGION
    ])
    lines.append("")
    lines += [f"{a} --- {b}" for a, b in block_pairs]
    note = ("Tier 1 · the setting · the region blocks and how they "
            f"interconnect. {GENERATED_NOTE}")
    out["T1_SETTING.md"] = _render(note, lines)

    return out


# ---------------------------------------------------------------------------
# Splicing — used by build.py and, in its own implementation, render_web.mjs
# ---------------------------------------------------------------------------
def splice(markdown: str, source: str = "") -> str:
    """Replace every `<!-- DIAGRAM: NAME.md -->` marker with that file's body."""
    out: list[str] = []
    for line in markdown.split("\n"):
        m = MARKER_RE.match(line)
        if not m:
            out.append(line)
            continue
        path = DIAGRAM_DIR / m.group(1)
        if not path.is_file():
            raise FileNotFoundError(
                f"{source or 'markdown'}: diagram marker points at a missing "
                f"file: diagrams/{m.group(1)}"
            )
        out.append(path.read_text(encoding="utf-8").rstrip())
    return "\n".join(out)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def main() -> int:
    write = "--write" in sys.argv[1:]
    derived = derive(load_tier4())
    changed = []
    for name, content in sorted(derived.items()):
        path = DIAGRAM_DIR / name
        current = path.read_text(encoding="utf-8") if path.is_file() else None
        if current == content:
            continue
        changed.append(name)
        if write:
            path.write_text(content, encoding="utf-8")
    if not changed:
        print(f"{len(derived)} derived diagrams, all current.")
        return 0
    verb = "rewrote" if write else "stale (run --write)"
    print(f"{len(derived)} derived diagrams, {len(changed)} {verb}:")
    for name in changed:
        print(f"  {name}")
    return 0 if write else 1


if __name__ == "__main__":
    sys.exit(main())
