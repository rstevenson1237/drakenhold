# DRAKENHOLD — HANDOFF

*What a fresh conversation does first. **Nothing else lives here.** This file was previously a 45KB parallel copy of the project — region table, standing decisions, cross-region threads, open items, and a narrative of every pass — which made it a fourth place the truth lived, and it drifted. The full record as it stood at the close of step 8 is kept at `archive/HANDOFF_at_step_8_close.md`.*

---

## WHERE THE TRUTH LIVES NOW

| You want | Read |
|---|---|
| What the project is, how it is built, what the deliverable is | `README.md` |
| The rules of authoring, and the eleven-step procedure | `PROCEDURES_AND_RULES.md` |
| **How an open item gets closed** — the six routes, and why architectural ones regenerate rather than get patched | `OPEN_QUESTIONS.md`, `## THE SIX ROUTES` |
| What a closing pass must check | `RECONCILIATION.md` |
| How a location is built — the classification scheme and the rules binding across it | `DESIGN_PATTERNS.md` |
| **The one file to open before writing a location** — `mode × weight`, nine of them | `patterns/` |
| Game mechanics — **source of truth, read-only here** | `Rules_Light_TTRPG_Design_Notes.md` |
| Setting-level content: Truths, Rumours, History, Factions, Bestiary, Treasure, Traps, Graffiti, Procedural Tables, Standing Mysteries | `outlines/`, one file per field. `Drakenhold_Setting_Outline.md` is the index and carries the Overview |
| Documentary items with a far end — an index, never a source | `LORE_INDEX.md` |
| Which regions exist, their Mode, Die, stub count and room budget | `regions/00_INDEX.md` |
| Region content — **authoritative** | `regions/` |
| Shared routes, budgets and **cross-region threads** | `blocks/` |
| What has been ratified and is not to be re-litigated | `DECISIONS.md` |
| **What is still undecided, and who decides it** | `OPEN_QUESTIONS.md` |

---

## PHASE POSITION

Architect (steps 1–6): **complete.**
Engineer step 7, location stubs and region tables: **complete, all twenty-two regions.**
Engineer step 8, region relational diagrams: **complete, all twenty-two regions**, and **retiered** — every diagram in the module is now its own file in `diagrams/`, in five tiers, with tier 4 authored and tiers 1 to 3 derived. See `DECISIONS.md` and the head of `diagrams/Drakenhold_Relational_Diagram.md`.
Engineer step 9, location outlines: **the approach is closed — `A` Thornhaven, `B` Ironwood Trail, `C` Goblin Camps, `D` River Crossing and `E` Girkel. Seventeen regions to go, and all of them are inside the mountain.**

---

## WHAT THE NEXT CONVERSATION DOES

**Step 9 — location outlines — one region per conversation.**

0. **`A` through `E` are the worked examples.** They are the only regions with step-9 outlines in them and they are where the shape of the step was settled: the stub heading is kept, a labelled Player's Overview and Referee Overview follow it, then **Features:** as a bullet list whose exits carry `->` pointers, then the step-7 **Connections:** field unchanged. **The `Connections:` field stays** — `M3` reads it and the region's tier-4 diagrams are checked against it — and the `->` pointers inside features are additional, not a replacement. Feature entries are a line or two: full descriptions are step 10 and do not start early. **All four of those labels come off at the final pass, and the `Connections:` field goes entirely** — italic means Player's Overview, plain text means Referee Overview, bullets mean Features, and every exit is a feature with a `->` pointer. See `DECISIONS.md`. **What this asks of a step-9 pass now: every edge in the `Connections:` field must also be written as a feature pointer**, so that dropping the field later loses nothing. **J2 demotion is automatic at the close and its procedure is in `RECONCILIATION.md`** — clause by clause, destination named for each, destination written before the clause is cut, then the pre-pass field re-read from git. The ledger goes in the commit message. It caught a real loss in `A` and it is not optional.
1. **The steps 1–8 reconciliation pass is run and its batch is answered.** Practice 2 is satisfied and step 9 may begin. `scripts/check.sh` M1–M8 all pass. The sweep raised five contradictions and they are **ratified in `DECISIONS.md`** — tiles gate sideways and never up; rumour 19 is half true and sealed at `J.4`; Ashen's Crew are a clock rather than a location; the Silver Veins seam is ambient in `FC`, `GC` and `HC`; the three Man-type Bestiary entries are named where they already belong. **Four of those five land on regions early in the order, so read `DECISIONS.md` before choosing one.** Five citation defects were corrected. Six watch items stay open in `OPEN_QUESTIONS.md`, each naming its owning pass. J2 was deliberately not run: it is a closing check and belongs to each region's own pass.
2. **Read the inputs:** the region file, its block document in `blocks/`, the setting outline, `DECISIONS.md`, `OPEN_QUESTIONS.md`, and this file. **Plus `DESIGN_PATTERNS.md` and exactly one file from `patterns/`** — `<MODE>_<WEIGHT>.md`, the region's Classification and the weight being written. Not the other eight.
3. **Write the outlines.** A Player's Overview, a Referee Overview, and the features the location contains. **Working notes are absorbed and struck** — M8 fails if one survives in a location that has been written.
4. **Reconcile the region's diagrams against the finished outlines before the region closes.** Outlines generate edges the stubs did not anticipate — doors, shafts, sightlines, drops. **The reconciled diagram is the deliverable, not the one drawn at step 8.** The region's diagrams are now files in `diagrams/`, not a mermaid block in the region file: **edit the tier-4 file for the group the edge leaves**, add the edge at the far group too — including the destination location as a node outside the frame — and then run `python3 scripts/diagrams.py --write` so tiers 1 to 3 catch up. Never hand-edit a `T1_`, `T2_` or `T3_` file; M11 re-derives them.
5. **Run `scripts/check.sh`.** All eleven must pass. `M11` holds the diagram layer together — every stub in exactly one group, every drawn destination resolving, cross-group edges drawn at both ends, and tiers 1 to 3 matching their derivation. `M9` holds every `(SECTION, key)` reference to something that exists; `M10` lists the `[[ ... ]]` editorial notes still outstanding and passes, and fails on them only under `check.sh --final`.
6. **Close:** update `OPEN_QUESTIONS.md` for anything opened or answered, `regions/00_INDEX.md` if a count moved, and end with the question batch if the pass decided anything needing direction. Omit the batch rather than manufacture one.

**Suggested region order**, matching how the stubs and diagrams were built: approach `A`–`E`, then `FA`/`GA`/`HA` as the first-level block, then peak by peak `F`, `G`, `H`, then `I` and `J` last. **The approach `A`–`E` is done. `FA`/`GA`/`HA`, the first-level block, is next**, and it is the first step-9 unit that is a block rather than a region: read `blocks/FIRST_LEVEL_BLOCK.md` first, because the three halls share a warren, a seal and a room budget, and practice 4 works them together in staged passes. What each closed region hands forward is written at the foot of its own diagram section, not here.

---

## WHAT STEP 9 INHERITS THAT IT MUST NOT ASSUME

*The full list is in `OPEN_QUESTIONS.md`. These four are the ones that will be met early and are easy to close by accident.*

- **What broke the great doors.** The very next pass meets it: `FA.1` is the same doorway `E.12` describes, seen from the inside. The leaves lie outward, the sockets are torn out of the jamb, and the wall at `E.1` fell outward too. **The evidence is written and the agent is not, by direction.** Naming it at `FA.1` would answer, in one sentence, a question the whole approach was built to leave standing.
- **`I.16`, the undefended approach.** Its far end is deliberately absent. Naming it settles by side effect which of three closed regions has a hole in it.
- **Peak 2's declared descent into `J`.** No `GB` stub carries it. Naming it means inventing a stub against a ratified count of twenty.
- **`GB.14`'s one entry without a charge.** The Crown's own stair gives it somewhere to go. Which entry, and whether the stair explains it, is `GB`'s and `GC`'s and is not to be assumed.
- **`GD.10`, the third sub-vault**, is placed as artifact piece four but the placement is proposed, not ratified.

---

## THE ONE STRUCTURAL WARNING

Every cross-region route end in the module is now drawn from both sides, with one deliberate exception: `J.9`–`D.6` is one-way outward and asks nothing of `D`. **A step-9 pass that adds an edge adds it at both ends**, in both region files and in both diagrams, or M2 and M3 will say so.
