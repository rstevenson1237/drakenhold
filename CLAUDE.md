# CLAUDE.md

Drakenhold — a tabletop RPG setting delivered as a Setting Playbook. Read `README.md` for structure and current phase. Read `PROCEDURES_AND_RULES.md` before any authoring work. Read `RECONCILIATION.md` before any pass that closes a region.

## Non-negotiables

1. **Additive revision only.** Existing material is preserved unless a change is explicitly directed. Propose and flag changes; never rewrite silently. One commit per pass, message stating what changed and why.
2. **Never invent an answer to an open item.** Open items live in `Drakenhold_Setting_Outline.md` under Unanswered Questions and in `HANDOFF.md`. If a task requires one, stop and ask.
3. **Phase discipline.** No blending steps. The current step is stated in `HANDOFF.md`.
4. **One region per conversation.** Inputs: the region file, its block document, the setting outline, the handoff. Output: a closed region file, an updated handoff, a commit.
5. **Names compound from the recorded root vocabulary** in the setting outline. New roots are proposed, never coined in passing.
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
- **Tables follow Classification, not terrain.** SAFE→Events, WILD→Encounters, DANGEROUS→Dangers. Danger tables count down from 6; all others ascend.
- **Half a region's room budget is stubbed.** The rest is unnamed fill. Rooms may be empty.
- **Every gate has an answer that is not the gate**, and the answer is priced — longer, darker, or watched by something worse.
- **Region fields narrow as locations develop.** Anything true of one named location belongs in that location, not the field.
- **A field may be empty.** State "None" with a brief reason. Never pad.

## Repo hygiene

- Region files in `regions/` are authoritative for region content.
- `Drakenhold_Gazetteer.md` is a frozen archive. Never edit it, never cite it as current.
- Run `scripts/check.sh` before committing. It must pass.
