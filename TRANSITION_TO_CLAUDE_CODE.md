# TRANSITION TO CLAUDE CODE

*Manual steps first, then the bootstrap prompt to paste into Claude Code once the repo exists.*

---

## PART 1 — MANUAL STEPS (you)

**1. Create the repo.** Private, name it `drakenhold`. Initialise with nothing — no README, no .gitignore, no licence. You are bringing your own.

**2. Lay out the files locally** in the structure `README.md` describes. Everything currently in outputs, rearranged:

```
drakenhold/
├── CLAUDE.md
├── README.md
├── PROCEDURES_AND_RULES.md
├── RECONCILIATION.md
├── HANDOFF.md
├── Setting_Playbook_Template.md
├── Drakenhold_Setting_Outline.md
├── blocks/          ← FIRST_LEVEL_BLOCK, PEAK_1..3_BLOCK, I_AND_J_BLOCK
├── regions/         ← 22 region files + 00_INDEX.md
├── diagrams/        ← create empty, with 00_setting.md holding the current setting diagram
└── archive/         ← Drakenhold_Gazetteer.md, and Setting_Playbook_Template__1_.md if it differs
```

**Watch for:** the duplicate files in the current outputs (`Setting_Playbook_Template__1_.md`, `Drakenhold_Gazetteer__1_.md`, `Changes_Needed__12_.md`, `Drakenhold_Setting_Outline__2_.md`). Diff them before discarding — pick one, archive or delete the rest. Do this **before** the first commit, so the history starts clean and a later reader is never choosing between two files that both look authoritative.

**3. First commit** on `main`, message: `Initial import — engineer step 7 complete, 22 regions, 395 stubs`. Tag it `step-7-complete`. That tag is your known-good state and it costs nothing.

**4. Install Claude Code**, open the repo directory, and paste the bootstrap prompt from Part 2.

**5. Branch per region** from then on: `git checkout -b region/FA`. Merge when the region closes and `check.sh` passes. This is what makes the additive-revision rule enforced by the tool instead of by discipline.

---

## GOTCHAS

**The one that will actually bite:** `HANDOFF.md` was written to carry context across conversations that had no shared filesystem. Once the repo exists, most of it is better expressed as files — phase position belongs in the README, open items belong in the setting outline's Unanswered Questions, cross-region threads belong in the block documents. Let the handoff shrink to *what the next conversation should do first*. If it stays comprehensive it becomes a fourth place the truth lives and it will drift.

**Do not let Claude Code reformat on import.** The first instinct of any agent handed 30 markdown files is to tidy them. That would be a silent rewrite of every file in the project, which is exactly what the additive-revision rule exists to prevent. The bootstrap prompt says so explicitly; hold the line if it drifts.

**CLAUDE.md is loaded every turn — keep it short.** It is at roughly 600 words on purpose. Every rule that can live in `PROCEDURES_AND_RULES.md` and be read on demand should. Resist appending to it.

**Diagrams before scripts.** The check script needs a stable file format to parse. Write one region's step-8 diagram by hand first, agree the format, *then* have Claude Code write the parser against a real example.

**Mermaid in CI.** GitHub renders mermaid in markdown natively, so the web view is nearly free. PDF export needs mermaid-cli and a headless browser in the Action — budget an afternoon for that specifically, and do it after the content pipeline works, not before.

---

## PART 2 — BOOTSTRAP PROMPT

*Paste this as your first message in Claude Code, in the repo root.*

---

This repository holds Drakenhold, a tabletop RPG setting in active development. Read `README.md`, `CLAUDE.md`, `PROCEDURES_AND_RULES.md` and `RECONCILIATION.md` before doing anything.

**Do not reformat, tidy, restructure or "clean up" any existing file.** Every file here is authored content under an additive-revision rule. Changes to established content are proposed and flagged, never applied without direction. If you notice formatting inconsistencies, list them and stop.

Your first task is tooling, not content. Build `scripts/check.sh` implementing the mechanical checks M1 through M8 in `RECONCILIATION.md`. Requirements:

- Python or shell, no dependencies beyond what a standard system has. Portable.
- Each check runs independently and can be invoked alone (`check.sh M1`).
- Output is a report: check name, pass/fail, and for failures the file, line and the specific problem. Not a stack trace.
- Exit non-zero if any check fails.
- **Report, never repair.** The script does not edit content files under any circumstance.

Start with **M1, reference integrity** — every location code (pattern: two-or-fewer uppercase letters, a dot, digits, optional lowercase suffix) appearing anywhere in the corpus resolves to a stub heading that exists in `regions/`. Build it, run it against the current repo, and show me what it finds before writing anything else. I expect it to find real problems and I want to see them before you build check two.

Before you begin, tell me: what did you find in the four documents you read that you think is ambiguous, underspecified, or likely to make a check unimplementable as written? I would rather fix the specification now than debug your interpretation of it later.

---

## AFTER BOOTSTRAP

Once `check.sh` passes on the current corpus, the sequence is:

1. **`scripts/build.sh`** — assembles the Playbook from the template's section order. Content is concatenated, never generated. Assembly failures are format failures and should point at the offending file.
2. **GitHub Action on `main`** — run `check.sh`, then `build.sh`, publish the web view to Pages.
3. **PDF target** — same source, paginated for the table. After the web view works.
4. **Then step 8.** One region per branch, diagram first, outlines second, reconcile, merge.
