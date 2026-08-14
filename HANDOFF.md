# DRAKENHOLD — HANDOFF

*State of the project as of the close of step 8 for region B. Written for a fresh conversation picking up step 8 at region C.*

---

## PROJECT SHAPE

A tabletop RPG setting built as a complete adventure module, delivered as a Setting Playbook. Ruined dwarven mountain hold in three peaks, occupied by a red dragon, robbed by whoever dares. Touchstones: *The Hobbit* for the road, Conan and sword-and-sorcery for the halls, pulp treasure-hunter fiction throughout, OSR design philosophy for structure. The spine is extraction and survival, not a boss fight.

**Working documents**, all in `/mnt/user-data/outputs/`:

- `Setting_Playbook_Template.md` — the general-purpose template
- `Drakenhold_Setting_Outline.md` — steps 1–2, current
- `Drakenhold_Relational_Diagram.md` — step 6, current
- `regions/` — 22 region files plus `00_INDEX.md`. **The authoritative home for all region content.**
- `FIRST_LEVEL_BLOCK.md` — connective document for FA/GA/HA, which share a warren
- `Drakenhold_Gazetteer.md` — **frozen archive**, superseded by `regions/`, kept for comparison
- `HANDOFF.md` — this file

---

## PHASE POSITION

Architect (steps 1–6) complete. **Engineer (steps 7–9) in progress.**

Step 7 — location stubs and region tables — is **complete for A, B, C, D, E, FA, GA, HA, FB, FC, FD, FE, GB, GC, GD, GE, HB, HC, HD, HE, I, J**. **Twenty-two of twenty-two — step 7 is complete.**

**Step 8 — region relational diagrams — is complete for `A` and `B`, and has not begun elsewhere.** Step 9 has not begun anywhere.

A diagram is written into the region file's `## REGION RELATIONAL DIAGRAM` section as a mermaid `graph TD`, with a `**Connections:**` field added under every location stub. Check M3 holds the two against each other and the diagram is authoritative. Node ids are the code without the dot (`A18`); the display label is `"A.18 · Name"` and the checker reads the code from the label. Working notes stay until step 9 absorbs them.

**Region order, settled:** approach (A–E) → first level (FA/GA/HA as one block) → **peak by peak: F, then G, then H** → I and J last.

---

## WHAT EXISTS AT STEP 7

| Region | Stubs | Rooms | Table |
|---|---|---|---|
| A Thornhaven | 20 | — | d6 Events |
| B Ironwood Trail | 13 + 1 sub | — | d6 Encounter |
| C Goblin Camps | 9 | — | d6 Encounter |
| D River Crossing | 11 | — | d6 Encounter |
| E Girkel | 12 | — | d6 Encounter |
| FA Takdun | 34 | 65 | d6 Danger |
| GA Grathdun | 27 | 52 | d6 Danger |
| HA Thaldun | 33 | 63 | d6 Danger |
| FB Brankel | 20 | 40 | d6 Encounter |
| FC Mekdun | 21 | 40 | d6 Danger |
| FD Khorvak | 16 | 30 | d6 Danger |
| FE Aztak | 10 | 16 | d6 Danger |
| GB Karmor | 20 | 40 | d6 Danger |
| GC Azdun | 15 | 30 | d6 Danger |
| GD Valdmor | 16 | 30 | d6 Danger |
| GE Azith | 9 | 16 | d6 Danger |
| HB Nurmor | 20 | 40 | d6 Danger |
| HC Sigdun | 20 | 40 | d6 Danger |
| HD Zarkel | 16 | 30 | d6 Danger |
| HE Sigaz | 10 | 16 | d6 Danger |
| I Brynaz | 16 | 30 | d6 Encounter |
| J Mordrak | 24 | 50 | d6 Encounter |

**Stub ratio, ratified:** roughly half the room budget is stubbed as named locations; the balance is unnamed fill inside the stated groupings. This is what makes the negative-space rule real rather than stated.

---

## NEXT TASK

**`PROCEDURES_AND_RULES.md` is now the authoritative procedure document and supersedes the working list used through step 7.** Two amendments, ratified at the close of step 7:

- **Steps 8 and 9 are swapped.** The region relational diagram is drawn from the stubs *before* the location outlines, as a working instrument for catching topology errors cheaply, then reconciled against the finished outlines before the region closes. The reconciled diagram is the deliverable.
- **One region per conversation** for the remainder of the project. Inputs: the region file, its connective block document, the setting outline and this handoff. Output: a closed region file and an updated handoff.

Each new step is preceded by a reconciliation pass over every step before it. Before step 10 begins anywhere, steps 1–9 are read back through as a body of work.

**Next: step 8 at region `C`, then D, E, then FA/GA/HA, then peak by peak, then I and J.** `A` and `B` are closed at step 8.

**Step 8 at region A decided one thing and it is recorded rather than asked:** the farmstead cellar was a single-throat corridor in the stubs, and the diagram found it. The yard hatch at `A.14`–`A.17` is the second way in — the cold store's old loading way, barred from within. Additive, within the region, consistent with rule 6.

**Next: step 8 (region diagrams) and step 9 (location outlines), region by region.** Suggested order, matching how the stubs were built: approach regions A–E, then FA/GA/HA as the first-level block, then peak by peak F, G, H, then I and J. Robert is handling the breakdown into per-region conversations.

**All twenty-two regions closed at step 7.** Connective documents: `FIRST_LEVEL_BLOCK.md`, `PEAK_1_BLOCK.md`, `PEAK_2_BLOCK.md`, `PEAK_3_BLOCK.md`, `I_AND_J_BLOCK.md`. All survive the split. `PEAK_1_BLOCK.md` is the connective document and survives the split: it holds the five kinds of movement, the skeleton diagram, Khorven, the dispatch floor, the order, the toll road and the room budget.

---

## WHAT STEP 8 AT B DECIDED

Nothing that needed asking. Three things the drawing settled inside the region, all additive and all consistent with the standing rules:

- **The deadfall's answer that is not the deadfall.** `B.6` is the region's one gate — the goblin toll at the chokepoint. The bypass was already in the stubs and only needed drawing: `B.5`→`B.10`→`B.7`, off-road around it through the webbed thickets. Priced as the rule requires — the toll is cheap and sells a fact the party wants at `D.8`; the bypass is free of goblins and costs the one thing in the region that can kill outright. The module never says which is the mistake.
- **`B.10` and `B.11` share the old spur** that once served the waystation. That is how the waystation is findable from the thickets side, and it makes the off-road locations a string rather than four leaves.
- **`B.12` is a loop, not a leaf.** The sprite hollow attaches to both `B.8` and `B.9`, so a party losing its way there loses it on the run-out to D with the whole wood behind them.

The road itself is a single chain with no shortcuts, `B.1` through `B.9`, and that was left alone — a road is a corridor by construction and the safety is the region's job. The single-throat correction made at A does not apply here.

## MECHANICAL RECONCILIATION, CLEARED

`scripts/check.sh` passes all eight checks as of this commit. Four pre-existing failures were cleared alongside step 8 at A. One of them changed content and is **flagged rather than assumed**:

- **`GC` named the wrong region at the foot of its ramp.** Its CONNECTIONS bullet read "**GB Karmor** — vertical, the great ramp down by way of GA", which made `GA`→`GC` unreciprocated and asserted an edge `GB` does not carry. Corrected to "**GA Grathdun** — vertical, the great ramp down", matching `FC`→`FA` and `HC`→`HA` on the other two peaks and matching `GA`'s own bullet. **If the "by way of GA" phrasing was deliberate — a through-route from the throne to the prison — say so and it goes back with `GB` reciprocating.**
- `PEAK_1_BLOCK.md` stated 66 stubbed for the block; FB+FC+FD+FE sum to 67. The regions are right and the aggregate was stale.
- The five roots `B` proposed — *rok*, *lath*, *ven*, *ost*, *vir* — were never written into the outline's TRUTHS catalogue. Added there as a third roots bullet. No new roots coined.
- Nine stub headings carried two, one or four tags instead of three. Third tags authored from each stub's own working note; `HA.24`'s four merged to three. `I.16`'s two new tags decide nothing — which level is open still resolves at its own pass.

---

## STANDING DESIGN DECISIONS FROM THIS PHASE

**The seal.** One tile-gated door on the lateral run between the Peak 1 and Peak 2 warrens, closed since the civil war. Hard lock, and the tile is at `C.1` on a goblin chief's neck. The network's answer is not a second door but the Ash Run and Cold Run in series, at three times the distance through the worst-mapped ground in the block. A second, copied tile is held by the Peak 2 survivor pocket at `GA.19`, who live inside the sealed segment. Taking it by force is legitimate, priced, and the module never says which line is correct.

**Three arteries, no procedure.** Long Run (F→G→H), Ash Run (F→G), Cold Run (G→H). Veins between groupings, capillaries between everything. No landmark system, no service marks, no mechanic — a sheer numbers game of twisting paths and trying to keep track. The survivors' only advantage is thirty years of memory a party cannot buy.

**Survivor pockets are not a faction in practice.** Three groups, discrete, no leader, no council, at least two actively disliking each other. Smallest and failing in Peak 1 (three, needing food/light/medicine, too frightened to leave, hiding a walled-in fourth). Most hostile in Peak 2 (nine, behind the seal). Largest in Peak 3 (fourteen or more, the only one with a goal beyond survival). Credit does not transfer between pockets.

**The Processionals are not two accounts of one history.** The Living proclaims the wealth and greatness of a never-ending hold, present tense, standing in its own ruin. The Dead reveres the ancestors' foreknowledge while carving the literal wedge that came down. Both hazardous to cross badly; both carry secrets for anyone who reads rather than walks. The **Monument of the Driving Down** stands where they meet, in GA — mostly untouched, the longest continuous bilingual surface in the hold, and its few defacings are late, specific and informative.

**The waystones are the module's entire teaching method for runic script.** Full bilingual text is written at `B.2`, `B.5`, `B.8`, with roots hyphenated and numbers as tally strokes. Nothing is translated for players. Five roots added: *rok* road, *lath* league, *ven* toward, *ost* water, *vir* wood. Thornhaven's unused dwarven name is **Ostgir**.

**Artifact pieces.** Seven, ratified at the close of the Peak 1 stub pass. Two ever left the mountain — `E.5` and `D.3` — and the evacuation register at `E.6` proves it. Five remain inside, one to each interior peak-level cluster: `FD.14` placed, one to Peak 2, two to Peak 3, one to `J`. **The count is itself a clue** — seven broken at `HE`, two carried out at `E.6`, and the module never performs the subtraction. The Peak 3 clue chain is no longer gated.

All pass-4 decisions (room budgets, difficulty dice, mode rationale, three tiers of detail, Secrets/Treasure split, empty fields, unique NPCs held for the location pass, authorial registers, B/X cameo, tags) remain in force and are not to be re-litigated.

---

## CROSS-REGION THREADS OPEN

- ~~**`A.12`/`A.13` ↔ `B.13`.**~~ *Closed at B's step 8 pass. Both edges are now drawn from both ends, unchanged, and `A.1` ↔ `B.1` with them.*
- **`B.7` ↔ `C.1`/`C.2`/`C.3`.** B's diagram draws three edges west out of the turning, honouring C's `## CONNECTIONS` line "three separate ways in for three camps". **C has not been worked at step 8 and the edges are not written into C.** Reconcile at C's pass; which trace leads to which camp is C's to detail.
- **`B.9` ↔ `D.1`** (the last rise runs out to the overlook) and **`B.4a` ↔ `D.6`** (the drain, hidden at both ends). Drawn in B's diagram. **D has not been worked at step 8 and neither edge is written into D.** Reconcile at D's pass.
- `C.1` tile → `FA.17` seal. Copy at `GA.19`.
- `A.20` Brannek Kelmor → obelisk at `HA.5`, niche at `FA.22`.
- `C.9` surveyor's satchel — half right, half confidently wrong, same hand. The Charter wants it back.
- `FA.12` cut-down panels → one with the Peak 1 survivors, one hanging in `FE`.
- Bypasses land at `FC` (craftsmen's areas), `GC` (administration), `HC` (chapel side cells).
- `GA.21` clerk's cache settles the ban dispute between `GC` and `FE`.
- `A.13` Wyla Fenn's price is her trial assessment in `HD`'s observation rooms.
- `HA.29` is a loaded trigger into `HB`, fired by action or inaction.
- `HA.31` is the first evidence `HE` is unfinished.
- `FA.34` / `GA.25` / `HA.28` / `FC.18` — older, unmarked cutting surfacing throughout all three warrens and behind the craftsmen's gate.
- `FA.30` bypass lands at `FC.15`; `FA.8` chute lands at `FB.9`; `FA.12`'s second panel hangs at `FE.8`.
- `FB.5` chieftain vacancy → `HC`. `FB.17` skimmed count → the Lizardmen and `GD`.
- `FD.10` flow gate: relighting the forge takes Khorven's draught off `FB`. Faction consequence, never stated in text.
- `FC.19` → `FE.9` — the Guild contact who fled with stolen rods, and who sent him.
- `FD.13` Durnek Balvak → `FE.3` Dovrek Balvak. Kin, unraised, answered when asked.
- **`FD.10` → `GE.3`. Fire in the vents.** Relighting the forge is one of the three things that wakes Vermakith. Evidence placed in advance across `FD.3`, `FD.4` and the flow schedule. Never stated in play, never sprung as a gotcha.
- `GB.4` Karn Rudgir ↔ `GC.13`/`GC.14` Vessa Rudgir. Brother and sister, same night, neither account complete.
- `GB.18` Morgrin Thurvak → `HC`, `HE`. `GB.19`/`GB.20` the Elder Wyrm and the hole it was already using → `J`.
- `GC.12` rod schedule → `GD.8` Royal locks; two rods at `FE.6`.
- `FB.17` ↔ `GD.5` — both halves of the skim proof.
- `GA.25` older course surfaces in `GB.16`, the deep cells, where it should not be.

---

## OPEN ITEMS

- ~~The seventh chair at `GA.2`.~~ *Answered at `GC.14` — the Steward removed her own seat and kept it whole in her rooms. Why is open and is `GB.4`'s to complicate.*
- **Artifact pieces: seven, ratified.** Two out (`E.5`, `D.3`), five in. Third placed at `FD.14`. Remaining four allocated one to Peak 2, two to Peak 3, one to `J`, placed as those blocks are stubbed. The subtraction is never stated in text.
- ~~Second horror for `HE`.~~ *No second template. One singular collared Drakmorith at `HE.6`, addressable rather than negotiable.*
- ~~**Artifact pieces.**~~ *All seven placed: `E.5`, `D.3`, `FD.14`, `GD.10`, `HB.14`, `HD.14`, `J.18`. Closed.*
- ~~Who ordered the defacing.~~ *Vessa Rudgir, the Steward, in her own hand through proper channels with no government left to sign for. `GC.11` + `GC.13` + `GC.14` + `GB.4` are now one answer.*
- The Horror-type bestiary entry: `HE.6` treats Drakmorith as arriving-as-geometry, which the existing entry already supports. No new entry drafted and none needed.
- `GD.10` third sub-vault — **proposed** as artifact piece four. Awaiting ratification.
- `GB.17` the jailer's oath — two releases exist, one of which is a lie. Which lie, unwritten.
- `GC.11` who ordered the defacing — named as a revelation, not yet named as a person.
- Undead variety in `HB` rests on Skeletal Warrior and Shadow alone. **Due at step 8.**
- ~~The light mechanic in the deep.~~ *Resolved as a Referee procedure in `I_AND_J_BLOCK.md` and wired into `J`'s Encounter table. Teaching site at `J.6`, navigation answer at `J.16`.*
- `I.16` the undefended approach — which level, and from which direction, resolves at step 8.
- `J.24` is deliberately unanswered and stays that way.
- `HB.6` Baldrun Azkelith's empty interment is **the last unanswered question in the module**, and that is deliberate.
- The properties of the lance, unfixed. `HB.16` holds the line that nothing about how it was laid suggests it was meant to be used again.
- Hireling statlines, postponed to Referee ruling.
- ~~`B.4a` drain outfall.~~ *Closed at `J.9`.* `B.4a` outfall confirmed at `D.6` and drawn as an edge at B's step 8 pass; `B.5`'s two named destinations (Thurgan, Azost) are permanent flavour and owe no answer.
- ~~The Knight's fate.~~ *Resolved at `HB.15` — laid in the niche by the last dwarves who could reach him, the lance with him, his name carved nowhere on the level. `HA.5` does not carry him and that absence is the lock.*
- `HB.6` Baldrun Azkelith's interment was prepared and never filled. What happened to the last king is open in both `GC` and `HB`.
- `HC.9` the whispers are one side of a conversation with somebody who is not Vekkut. Who, unwritten.
