# CLAUDE.md

Drakenhold — a tabletop RPG setting delivered as a Setting Playbook. Read `README.md` for structure and current phase. Read `PROCEDURES_AND_RULES.md` before any authoring work. Read `RECONCILIATION.md` before any pass that closes a region. Before writing a location, read `DESIGN_PATTERNS.md` and **exactly one** file from `patterns/` — `<MODE>_<WEIGHT>.md` for the cell being written, never the other eight.

## Non-negotiables

1. **Additive revision only.** Existing material is preserved unless a change is explicitly directed. Propose and flag changes; never rewrite silently. One commit per pass, message stating what changed and why.
2. **Never invent an answer to an open item.** Open items live in `OPEN_QUESTIONS.md`, the single register. Ratified calls live in `DECISIONS.md`. If a task requires an open item, stop and ask.
3. **Phase discipline.** No blending steps. The current step is stated in `HANDOFF.md`, which is a one-page pointer and stays that way.
4. **One region per conversation.** Inputs: the region file, its block document, the setting outline (`Drakenhold_Setting_Outline.md` and the field files in `outlines/`), `DECISIONS.md`, `OPEN_QUESTIONS.md`, the handoff. Output: a closed region file, an updated register, a commit.
5. **Names compound from the recorded root vocabulary** in `outlines/01_TRUTHS.md`. New roots are proposed, never coined in passing.
6. **Question batches** end any pass that decided something requiring direction. Batched, whole, with genuine alternatives — not only the conservative option. Omit the batch if nothing needs a decision.

## The three registers

| Audience | Where | Voice | Test |
|---|---|---|---|
| **Player** | Player's Overview, and anything read aloud | Tolkien — lyrical, hinting at a wider world | Shows. Never states a conclusion the player should reach. |
| **Referee** | Referee Overview, Features, region fields, tables | Hemingway — hard-bounded, spatially precise, measurements and cardinal directions stated | Enough to rule without instruction. |
| **Architect** | Working notes only | Anything | **Must not survive.** Struck when its content is absorbed. |

**Show don't tell is a player-facing rule.** A region is not dangerous because a field says so; it is dangerous because its Danger table, its features and its creatures make it so. A hidden door does not exist until the fresco that conceals it and the mechanism that opens it are written as features a player can search. A patrol does not exist until its sound, its wear on the floor, or its schedule is findable. Referee text may state facts plainly — that is its job. Player text may not.

## Structural rules that are easy to break

- **Diagrams are authoritative.** Connection bullets are checked against them, never the reverse.
- **One diagram, one file, in `diagrams/`, in five tiers** — setting, block, region, location group, location. Each shows only the tier below it. **Edge type is drawn at tier 4 and nowhere else**; above it a connected pair gets one plain untyped edge. A tier-4 edge leaving its group draws the destination location outside the frame. **Tier 4 is authored; tiers 1–3 are derived** by `scripts/diagrams.py --write`. Never hand-edit a derived file, and never write a mermaid block outside `diagrams/` — hosts carry `<!-- DIAGRAM: NAME.md -->` and the build splices.
- **Tables follow Classification, not terrain.** SAFE→Events, WILD→Encounters, DANGEROUS→Dangers. Danger tables count down from 6; all others ascend.
- **Half a region's room budget is stubbed.** The rest is unnamed fill. Rooms may be empty.
- **Every gate has an answer that is not the gate**, and the answer is priced — longer, darker, or watched by something worse.
- **No secret is gated on a search roll.** Gates are physical: standing somewhere, clearing something, opening something, speaking a name, looking back.
- **`HIGH` is one location per ten, two at most in a region.** That is a cap on the form, not the negative-space thirds, which are a different measure. A `LOW` location may not contain a find.
- **Region fields narrow as locations develop.** Anything true of one named location belongs in that location, not the field.
- **A field may be empty.** State "None" with a brief reason. Never pad.
- **Two inline marks, and only two.** `(SECTION, key)` references a setting-outline field — `(BESTIARY, Goblin)`, `(TREASURE, II)` — survives to the finished playbook, becomes a link, and is checked by M9. `[[ ... ]]` is an editorial note, is designer register, and must not survive; M10 reports them and `check.sh --final` fails on them. Location codes stay backticked and belong to M1. Single brackets are already spoken for.

## Repo hygiene

- Region files in `regions/` are authoritative for region content.
- `Rules_Light_TTRPG_Design_Notes.md` is the source of truth for game mechanics. Read-only here — never edited, never extended, replaced wholesale on upload. No mechanic is invented in setting content; gaps are raised as questions for the rules project.
- `Drakenhold_Gazetteer.md` is a frozen archive. Never edit it, never cite it as current.
- Run `scripts/check.sh` before committing. It must pass.
