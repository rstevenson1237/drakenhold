# DRAKENHOLD — HANDOFF

*What a fresh conversation does first. **Nothing else lives here.** This file was previously a 45KB parallel copy of the project — region table, standing decisions, cross-region threads, open items, and a narrative of every pass — which made it a fourth place the truth lived, and it drifted. The full record as it stood at the close of step 8 is kept at `archive/HANDOFF_at_step_8_close.md`.*

---

## WHERE THE TRUTH LIVES NOW

| You want | Read |
|---|---|
| What the project is, how it is built, what the deliverable is | `README.md` |
| The rules of authoring, and the ten-step procedure | `PROCEDURES_AND_RULES.md` |
| What a closing pass must check | `RECONCILIATION.md` |
| Game mechanics — **source of truth, read-only here** | `Rules_Light_TTRPG_Design_Notes.md` |
| Setting-level content: Truths, Rumours, History, Factions, Bestiary | `Drakenhold_Setting_Outline.md` |
| Which regions exist, their Mode, Die, stub count and room budget | `regions/00_INDEX.md` |
| Region content — **authoritative** | `regions/` |
| Shared routes, budgets and **cross-region threads** | `blocks/` |
| What has been ratified and is not to be re-litigated | `DECISIONS.md` |
| **What is still undecided, and who decides it** | `OPEN_QUESTIONS.md` |

---

## PHASE POSITION

Architect (steps 1–6): **complete.**
Engineer step 7, location stubs and region tables: **complete, all twenty-two regions.**
Engineer step 8, region relational diagrams: **complete, all twenty-two regions.**
Engineer step 9, location outlines: **`A` Thornhaven is closed. Twenty-one regions to go.**

---

## WHAT THE NEXT CONVERSATION DOES

**Step 9 — location outlines — one region per conversation.**

0. **`A` is the worked example.** It is the only region with step-9 outlines in it and it is where the shape of the step was settled: the stub heading is kept, a labelled Player's Overview and Referee Overview follow it, then **Features:** as a bullet list whose exits carry `->` pointers, then the step-7 **Connections:** field unchanged. **The `Connections:` field stays** — `M3` reads it and the diagram is checked against it — and the `->` pointers inside features are additional, not a replacement. Feature entries are a line or two: full descriptions are step 10 and do not start early. **All four of those labels come off at the final pass, and the `Connections:` field goes entirely** — italic means Player's Overview, plain text means Referee Overview, bullets mean Features, and every exit is a feature with a `->` pointer. See `DECISIONS.md`. **What this asks of a step-9 pass now: every edge in the `Connections:` field must also be written as a feature pointer**, so that dropping the field later loses nothing. J2 demotion was run on `A`'s region fields at the close, once the locations existed to carry the detail.
1. **The steps 1–8 reconciliation pass is run and its batch is answered.** Procedure 12 is satisfied and step 9 may begin. `scripts/check.sh` M1–M8 all pass. The sweep raised five contradictions and they are **ratified in `DECISIONS.md`** — tiles gate sideways and never up; rumour 19 is half true and sealed at `J.4`; Ashen's Crew are a clock rather than a location; the Silver Veins seam is ambient in `FC`, `GC` and `HC`; the three Man-type Bestiary entries are named where they already belong. **Four of those five land on regions early in the order, so read `DECISIONS.md` before choosing one.** Five citation defects were corrected. Six watch items stay open in `OPEN_QUESTIONS.md`, each naming its owning pass. J2 was deliberately not run: it is a closing check and belongs to each region's own pass.
2. **Read the inputs:** the region file, its block document in `blocks/`, the setting outline, `DECISIONS.md`, `OPEN_QUESTIONS.md`, and this file.
3. **Write the outlines.** A Player's Overview, a Referee Overview, and the features the location contains. **Working notes are absorbed and struck** — M8 fails if one survives in a location that has been written.
4. **Reconcile the region's diagram against the finished outlines before the region closes.** Outlines generate edges the stubs did not anticipate — doors, shafts, sightlines, drops. **The reconciled diagram is the deliverable, not the one drawn at step 8.**
5. **Run `scripts/check.sh`.** All eight must pass.
6. **Close:** update `OPEN_QUESTIONS.md` for anything opened or answered, `regions/00_INDEX.md` if a count moved, and end with the question batch if the pass decided anything needing direction. Omit the batch rather than manufacture one.

**Suggested region order**, matching how the stubs and diagrams were built: approach `A`–`E`, then `FA`/`GA`/`HA` as the first-level block, then peak by peak `F`, `G`, `H`, then `I` and `J` last. **`A` is done; `B` is next in that order.**

---

## WHAT STEP 9 INHERITS THAT IT MUST NOT ASSUME

*The full list is in `OPEN_QUESTIONS.md`. These four are the ones that will be met early and are easy to close by accident.*

- **`I.16`, the undefended approach.** Its far end is deliberately absent. Naming it settles by side effect which of three closed regions has a hole in it.
- **Peak 2's declared descent into `J`.** No `GB` stub carries it. Naming it means inventing a stub against a ratified count of twenty.
- **`GB.14`'s one entry without a charge.** The Crown's own stair gives it somewhere to go. Which entry, and whether the stair explains it, is `GB`'s and `GC`'s and is not to be assumed.
- **`GD.10`, the third sub-vault**, is placed as artifact piece four but the placement is proposed, not ratified.

---

## THE ONE STRUCTURAL WARNING

Every cross-region route end in the module is now drawn from both sides, with one deliberate exception: `J.9`–`D.6` is one-way outward and asks nothing of `D`. **A step-9 pass that adds an edge adds it at both ends**, in both region files and in both diagrams, or M2 and M3 will say so.
