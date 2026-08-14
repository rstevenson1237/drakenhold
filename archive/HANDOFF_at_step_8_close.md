# DRAKENHOLD — HANDOFF

*State of the project as of the close of step 8 at `I` and `J`. **Step 8 is complete. All twenty-two regions are drawn.** Written for a fresh conversation picking up step 9 — location outlines — one region per conversation, preceded by the reconciliation pass procedure 12 requires over steps 1–8.*

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

**Step 8 — region relational diagrams — is complete for all twenty-two regions:** the approach (`A`–`E`), the first-level block (`FA`, `GA`, `HA`), the Peak 1 block (`FB`, `FC`, `FD`, `FE`), the Peak 2 block (`GB`, `GC`, `GD`, `GE`), the Peak 3 block (`HB`, `HC`, `HD`, `HE`), and `I` and `J` together. **Twenty-two of twenty-two — step 8 is complete.** Step 9 has not begun anywhere.

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

**Next: step 9 — location outlines — one region per conversation.** Every region now carries a diagram and a `**Connections:**` field under every stub. Procedure 12 requires a reconciliation pass over steps 1–8 before step 9 begins; procedure 9 requires each region's diagram to be reconciled again against its finished outlines before that region closes, because outlines generate edges the stubs did not anticipate. **The reconciled diagram is the deliverable, not the one drawn at step 8.**

~~**`I` and `J` inherit fourteen route ends.**~~ *All reciprocated at the `I`/`J` step 8 pass, unchanged and without a decision needed for any of them: `FD.15`–`I.1`, `GD.2`–`I.3`, `HD.3`–`I.4`, `FE.7`–`I.13`, `GD.12`–`I.14`, `I.15`–`GE.3`, and `FB.14`/`HB.19` at `J.2` with `FB.4`/`FD.16`/`GB.20` at `J.3`. **No cross-region route end anywhere in the module is now drawn from one side only, except `J.9`–`D.6`, which is one-way outward and asks nothing of `D`.***

**Answered at the Peak 2 pass:** `GA.17`'s landing at `GB.5` is confirmed from `GB`'s side, drawn exactly as `GA` drew it. **Still open and still not to be assumed:** which entry in `GB.14`'s register the Crown's own stair explains. It is now a question with a route attached and it is `GB`'s and `GC`'s to answer at step 9.

*Superseded, kept for the record:* **Two things the next Peak 2 pass inherits and must not resolve by assumption.** `GA.17`'s armoury support ways are drawn down onto `GB.5`, behind the formation — `GB` confirms the landing at its own pass. And the Crown's own stair `GC.13`→`GB.12` makes `GB.14`'s one entry without a charge a question with somewhere to go; **which entry, and whether the stair explains it, is not decided and is not to be assumed.**

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

## WHAT STEP 8 AT C DECIDED

One thing, additive, within the region, and flagged rather than assumed:

- **The nest has a second way in.** `C.8` is a fallen trunk over a hole and the stub tag reads *One Way In*, which would put the region's real haul behind one fight in one throat. The answer that is not the gate came out of ground the stubs already describe: at the back of `C.7`, where the raked trees have died and gone over, roots have pulled the roof off the nest chamber and left a **root sink** into `C.9`. Priced worse than the fight — narrow enough that armour comes off, no way back up in a hurry, and it drops a party into the chamber with the haul and the trunk on the far side. Drawn as a hidden edge `C.7`–`C.9`. **If the den was meant to stay a single-throat fight, say so and the edge comes out.**

The rest the drawing only made explicit. `C.4` is the hub and also the open way west into owlbear country, which is the drawn reason the ground is contested. `C.3` is the only camp with an edge onto `C.7`, which is the whole of Hessa's problem in one line. `C.5` serves `C.1` and `C.2` and not `C.3`, which is why two chiefs are proud and one is frightened. No camp connects directly to another — every chief-to-chief move routes through `C.4`.

## THE C→E SCAVENGER TRACK, RATIFIED

Batched at C's step 8 pass and **answered: option 1, write the edge.** `C.5` ↔ `E.1`, the guard wall, at one of its four breaches — which is how a goblin salvage file gets in and out of a walled city unseen and how the tile came out. Open, not conditional, not goblin-only. Written into four places: `C`'s `## CONNECTIONS`, `E`'s `## CONNECTIONS`, `C`'s region diagram, and both the overview and approach graphs in `diagrams/Drakenhold_Relational_Diagram.md`.

**The consequence is accepted, not mitigated.** `D` is now skippable. A party that leaves the road at `B.7`, deals with the camps and walks west reaches the Outer City having paid no toll, met no hobgoblins and never seen the Charter camp — and arrives at the great doors without the watch log, the outpost cache or any outside account of what is inside. The module does not warn anyone and never performs that subtraction. Referee-facing text in `D` and `E` may note the bypass exists; player-facing text may not.

## WHAT STEP 8 AT D DECIDED

One thing, and it was owed rather than invented:

- **The old course under the far booth.** `C`'s Secrets and `B`'s Encounter table both already promise that *the goblins know the safe passage past the far booth and will trade it*. Nothing behind that promise had been drawn. It is now a hidden edge `D.7`–`D.11`: the original approach the three spans were built to serve, running below the modern road on broken rock above fast water. Single file, hands needed, worse in the wet. Priced as the rule requires — it lands a party on the far bank with the hobgoblins between them and the bridge, so getting in free means getting out by paying anyway, by fighting, or by going back down it in the dark. The goblins know it because they use it; the hobgoblins cannot watch it from a lit booth at night. `D`'s `## CONNECTIONS` bullet for `E` is amended to say the toll is the price of the bridge, not of the region.

The rest the drawing only made explicit. The five-minute reading of the region is a five-node chain, `D.1`→`D.5`→`D.7`→`D.8`→`D.11`, and every rewarding location hangs off it by a single edge and is on the way to nothing. `D.10` touches both `D.1` and `D.5`, which makes the Charter unavoidable — necessary, since they will not raise the missing surveyor first. `D.11` has three ways onto it and all three pass within sight of hobgoblins, which is why scouting `D.9` before negotiating changes the negotiation.

## WHAT STEP 8 AT E DECIDED

Nothing that needed asking. The drawing resolved one ambiguity in the stubs and made three things structural:

- **`E.2`'s "Three Roads Meet" resolved as the three hill roads.** The gate road and the processional to the doors are one straight axis, `E.1`–`E.2`–`E.12`, and the three hill roads meet it at the square. This keeps the tag literal and gives the region an express route, the same shape `D` has: a party that stops for nothing crosses Girkel in three nodes and learns nothing, and the module lets them.
- **The registry's hill is the hostile one.** `E.6` carries both `E.7` and `E.8`. There is no route to the module's first big-picture account that does not pass Ashen's squat or the barracks, and the obvious answer — go at night — hands the party the wolves. Two priced options, no third door.
- **The third hill is a loop with nothing on it.** `E.9`–`E.10`–`E.11` close on each other, no faction, no monster, no lock — and it holds the quietest evidence in the region. The least defended ground is around the thing nobody thought was worth taking, and that is never said where a player can read it.
- **`E.5` hangs hidden off `E.3`, not `E.4`.** The quiet treasure and the loud one are on the same hill, so the party chooses what to carry.

## WHAT STEP 8 AT THE FIRST-LEVEL BLOCK DECIDED

Worked as one pass across `FA`, `GA` and `HA` against `blocks/FIRST_LEVEL_BLOCK.md`, because the three share a warren and cannot be drawn independently. **Nothing was invented and nothing needed asking.** The block-level findings are written into `FIRST_LEVEL_BLOCK.md` under a new *PASS 4 — THE REGION DIAGRAMS*; the per-region findings are under each region's own diagram. In summary:

- **The three arteries are now edges rather than prose.** `FA.17`–`GA.10` and `GA.11`–`HA.14` are the two tile-gated faces of the seal; `FA.18`–`GA.12` is the Ash Run; `GA.13`–`HA.13` is the Cold Run. The block document's central claim — that the seal's answer is the Ash Run and the Cold Run in series at three times the distance — is now topology and can be checked.
- **The sealed segment touches no warren, so the Long Run is transit and nothing else.** With the tile a party crosses the hold underneath it without entering a single warren. Without it, the crossing is paid for in `GA.22`, the featureless capillary maze that both arteries hang off.
- **The Peak 2 pocket is reachable without a tile, by one hidden run they watch.** `GA.22`–`GA.18`. This is what makes taking the second tile by force a real line of play rather than a paradox, and the watchers' nest sitting on the only approach is why they always see the party first.
- **Every hall opens into its warren twice.** The single-throat correction made at region `A` was not needed anywhere in this block; the second doors were already in the stubs.
- **`E.12` ⇒ `FA.1` is reciprocated.** The thread the handoff carried open since the approach closed is written at both ends. `FA` draws the doors undirected — they are broken open and pass both ways; `E`'s arrowhead is emphasis, not a one-way type. *Flagged rather than changed: `E`'s diagram is left as it stands.*
- **`GA.17` is drawn down onto `GB.5`, the armoury, behind the formation's line.** The stub said *ways down to GB* plainly, so drawing it is owed rather than invented. Written from `GA`'s side and flagged for `GB` to confirm.
- **`HA.21` and `HB.17` are one cutting through two regions.** `HB` already promised that the survivors' burials connect through; the edge is now hidden and drawn. The Peak 3 pocket therefore has two independent ways into the crypts — the burials, and the warded access at `HA.29`.

## WHAT STEP 8 AT THE PEAK 1 BLOCK DECIDED

Worked as one pass across `FB`, `FC`, `FD` and `FE` against `blocks/PEAK_1_BLOCK.md`. **Nothing needed asking.** Two edges were reconciled and one aggregate corrected; everything else the drawing only made explicit. Block-level findings are in `PEAK_1_BLOCK.md` under a new *PASS 3*; per-region findings sit under each diagram.

- **The great ramp reaches `FB`.** `FB.16`–`FC.1`, open and vertical. It was owed from three directions — `FB.16`'s stub is named *where the ramp meets the floor*, `FB`'s Encounter table has the collectors coming *down the ramp*, and the toll road runs from `FD.15` down through FD and FC without stopping — and it was in neither region's connections nor in the setting diagram. Written at both ends and at block and setting level.
- **The FA warren touches Khorven.** `FA.33`–`FB.4`, hidden and size-conditional. *Inherited threads* has always said the vent gallery is the warren's own way onto the chimney; it was never an edge. **`FA` is amended to carry it** — the one change made to an already-closed region at this pass, and it is a reconciliation rather than new content.
- **`FC.14` corrected to `FC.15`.** The block document said the bypass arrives at the craftsmen's gate; it arrives at the bypass mouth *inside* the gate. Regions right, aggregate loose.
- **`FD.8` is the peak's freight hub, and that is what makes the Automatons answerable.** Three ways in — the timed crossing at `FD.7`, the chutes at `FC.5`, the hidden access at `FC.21`. Without the two bought a level below, the stock rooms would sit behind the only thing in Peak 1 that will actually kill a party.
- **The flow gate is off every route.** `FD.9`–`FD.10`–`FD.3` and nothing passes through it. The kobolds' winter cannot be taken by accident, which is what keeps `FD.10` a faction decision rather than a trap.
- **`FB`'s two prizes are hidden behind the two places the tribe will not go.** The undeclared reserve past the Ooze at `FB.12`; the skimmed count under a script nobody on the level can read at `FB.13`. Neither hiding place is a trap and both are characterisation.
- **`FB.11` does not touch the granary floor.** The sealed bins are reached only through the tally gallery, so the room that says what is *in* them is on the only way to them.
- **`FE` is a legitimate single throat.** One ramp, one orphaned Skybridge run at `FE.7`–`I.13` that must be solved from outside. Stated in the region's own Connections, priced, and the reason the level pays what it pays. The star shape is the design: no route on `FE` is a decision because every decision on `FE` is a sentence.

## WHAT STEP 8 AT THE PEAK 2 BLOCK DECIDED

Worked as one pass across `GB`, `GC`, `GD` and `GE` against `blocks/PEAK_2_BLOCK.md`. **Nothing needed asking.** One edge reconciled, one aggregate corrected, one gap recorded and deliberately not filled. Block-level findings are in `PEAK_2_BLOCK.md` under a new *PASS 3*.

- **The deep cells were a closed loop and the drawing found the way out.** `GB.16` is rod-gated and `GB.15` states the rod is held by the wraith *below* it — a door that cannot be opened from the side a party is on. The answer is `GB.20`–`J.3`, the hole the Elder Wyrm was using before anyone built a cell over it, and it is priced about as steeply as anything in the module: **it arrives inside `GB.19`.** The honest route is a conversation through a locked floor, which the region's own Danger 6 already establishes carries sound. **The honest release of the jailer's oath is still unwritten and was not written here.**
- **`GA.22`–`GE.9` reconciled.** The servants' way into the lair corridor has been in the block document and the setting diagram since step 6 and had no end in any region file. It leaves the Peak 2 warren from the capillary maze and climbs three levels to the Queen's end. **`GA` is amended to carry it** — the one change to an already-closed region at this pass.
- **Not one gate on this peak is answered on its own floor.** `GB.11` by the Crown's stair from two levels up; `GB.16` by `J` from below; `GC.1` by the bypass from the warren beneath; `GD`'s count by the orphaned run at `I.14`; `GE`'s crater by `GA.22`, three levels down. That is the structural difference between Peak 2 and Peak 1 and it is worth carrying into the location passes.
- **`GC.3` touches three rooms and pointedly not `GC.10`.** The defacing is on the throne room, the chancery and the petition rooms; the line of kings stands untouched one edge away. The region's whole lesson — royal names are collected, not found — is now drawn rather than asserted.
- **`GC.13` is the level's real junction.** The order, the seventh chair and the secret stair down to a prison all open off the Steward's rooms, and the revelation about Vessa Rudgir is a closed triangle with one leaf that cannot be entered except through her handwriting.
- **On `GD` the hub is the scales, not the vault.** `GD.7` carries six edges. The busiest node in the busiest region is where a party is measured.
- **On `GE` nothing is gated at all.** Not one lock in the region; the d4 is the lock. Every route from the ramp to the Queen's end passes the mouth of the crater — unless the party came up `GE.9`.
- **`GC.12`, not `GC.13`, holds the rod schedule.** Corrected in the block document.

**One gap recorded and not filled.** `GB`'s Connections claim *Peak 2's declared descent* into `J`, and no `GB` stub carries it, where `FB.14` and `HB.19` carry the other two. Naming it would mean inventing a stub against a ratified count of twenty, so it is left in unnamed fill. **Whether to name it at step 9 is `GB`'s to decide and is not decided here.**

## WHAT STEP 8 AT `I` AND `J` DECIDED

Worked as one pass across both regions against `blocks/I_AND_J_BLOCK.md`, and it is the last pass of step 8 anywhere. **Nothing was invented, one thing was decided inside a region, one route was drawn outward, and one open item was deliberately left open.** Block-level findings are in `I_AND_J_BLOCK.md` under a new *PASS 2*.

- **The two regions have the same structural signature and it is not the one either looks like.** `I.7`, the assessment, carries six edges and is not a place. `J.1`, the great tunnel, carries nine and is a corridor. In any other region either would be the failure this step exists to catch; here both are the design stated out loud. `I.7` is also the same shape as `HE.5` — the mechanism is the corridor a party walks rather than an obstacle it meets — arrived at independently in the two regions furthest apart in the module.
- **The span is not a bypass.** `I.1`–`I.2`–`I.3`–`I.5`–`I.4` is a chain with Valdgir in the middle, so **there is no traverse of the only horizontal route in the hold that misses the checkpoint.** What bypasses gates in `I` is the runs, and every one worth having is conditional on a mechanism. `I` has to be earned before it pays; `J` pays immediately and charges in watches and light afterwards.
- **Every descent lands on `J`'s spine, which is why the light rule can be taught once.** `J.2` and `J.3` hang off `J.1` and off nothing else, so six ways down from three peaks all deliver a party into the same quiet facing the same nine choices. `J.6`, the burnt-out torch, is one edge off the tunnel and therefore unmissable rather than lucky.
- **`J.16` is drawn as the edge between the only two places where light does not matter.** `J.14`, the vents, and `J.20`, the deep dark. The answer to the light rule is literally the line between its two exceptions.
- **The vents and the hidden descents are one system.** `J.3`–`J.14`. A party that came down Khorven running from something is already standing in the territory that restores all of Peak 1, and the chain from Peak 1's prize to Peak 2's crater is walkable.
- **The seventh piece is off the spine, behind the module's own stated boredom.** `J.1`→`J.10`→`J.17`→`J.18`. `HE.10` gives a party a name and no place; the place is two territories deep, through the workings described as *nothing left worth digging*.
- **Nothing in `J` is gated at all**, and nothing in `HE` or `GE` was either. Three regions running where the drawing found no lock. In `J` the locks are the dark and the distance, and both are procedures rather than doors.
- **The two prizes in `I` hang off the fallen runs**, which is owed by `I.12`'s own stub: what is *not* there is the index to what is. The region's three most valuable routes are findable only through its negative space.
- **`I.15` is the only directed edge in `I`** and it points at a sleeping dragon.

**Decided inside `I`, additive and flagged:** the ice stretch sits east of the checkpoint, between `I.3` and `I.4`. Valdgir's patrols stop at the wet, so the quiet half of the span is the half beyond the ice, and `HD.3` is unwatched from both ends because reaching it is seasonal work nobody is paid for.

**Drawn outward, and no peak could have drawn it:** `J.9`–`D.6`, **one-way, hidden, water the whole way.** `J.9` already promised the outfall is an exit for a party thinking sideways and nothing had been drawn behind the promise. It comes up below the near bank at the river crossing and nothing goes back up it. **`D` is closed and is not amended**, because a one-way edge asks nothing of it.

**Not answered:** `I.16`, the undefended approach. See OPEN ITEMS.

**Carried, not filled:** Peak 2's marked descent still has no named stub in `GB`. `J.2` is drawn to accommodate it and the diagram does not pretend it exists.

## WHAT STEP 8 AT THE PEAK 3 BLOCK DECIDED

Worked as one pass across `HB`, `HC`, `HD` and `HE` against `blocks/PEAK_3_BLOCK.md`. **One thing needed asking and it is batched.** One landing fixed that a closed region asked for in writing, one open item answered from the existing bestiary, no aggregate corrections. Block-level findings are in `PEAK_3_BLOCK.md` under a new *PASS 3*; per-region findings sit under each diagram.

- **The peak has an express route and it is four rooms long.** `HA.10`→`HC.1`→`HD.1`→`HE.1`. Every ramp head is one node carrying both directions of the great ramp, so a party that stops for nothing crosses all four levels without meeting the squat, the circuit, the crypts or one rung of the clue chain — and arrives at the Sanctuary holding none of the three things that make it survivable. The module performs no subtraction, exactly as at `D` and `E`.
- **Not one gate on this peak is answered on its own floor, and all of them are answered one floor *up*.** `HC.18` by `HD.10` or `HD.15`; `HD.11` by the circuit rather than by any door; `HE` by `HD.16`, three levels of preparation earlier. Peak 1 answers downward, Peak 2 answers from anywhere but the floor itself, Peak 3 answers in the direction the party is already climbing. The block's claim that the chain runs upward and the price runs upward with it is now topology.
- **`HD`'s circuit is a closed ring with the grant on it, and the ring is the lock.** No chord, no room hanging off it, and the route imposes an attempt at every segment in either direction. Walking it backwards to collect the rod means running the same trials in reverse order. **The shortcut costs more than the road because the shortcut is priced in the road** — the rod that opens `HD.11` is the rod at the far end of the circuit.
- **The two live edges do not touch each other.** `HC.12` lands on `HD.4`, the plain circuit ground, and nowhere near `HD.11`. The clock cannot deliver the observation rooms to anybody. It shortcuts the explanation, not the ordeal.
- **`HB` is a funnel and its two answers are priced in the region's own currency.** The tiering is a chain, richest and worst first, with the niche, the lance, piece five and the descent into `J` all at the far end of it. `HA.29`→`HB.3`→`HB.12` and `HA.21`→`HB.17` are the ways past, and the second lands in the survivors' own graves. **The shortest route to the niche runs over the dead of the faction whose good opinion is Peak 3's largest asset**, and nothing about it is stealthy.
- **The niche is two steps and only one of them is the name.** `HB.14`–`HB.20`–`HB.15`. It is cut into the older course where it surfaces in the blank wall, not into the blank wall directly, so a party must first notice that unworked stone is not unworked.
- **`HB.13` is the only edge on the level that crosses a station.** The watch that stayed were interred with their post rather than their station, which makes `HB.4`–`HB.13`–`HB.11` a route stepping three tiers in one cutting, and gives `HB.18`'s *never past their own tier* rule its one architectural exception.
- **`HE.5` is the hub and the hub is not a room.** Six of sixteen edges. The broken geometry is the corridor a party walks rather than a hazard it meets, and `HE.3` is the only fixed point on the floor — which retroactively prices `HD`'s circuit correctly: **the rod does not buy treasure, it buys a way back out.**
- **`HE` has no lock of any kind**, the same finding `GE` produced from the opposite direction. The lock is the map.

**`HA.19`'s landing, fixed.** `HC.15`, the instruction rooms. Directed by `HA.19`'s own stub, which stated the landing was `HC`'s to fix. **`HA` is amended to carry the edge** — the one change to an already-closed region at this pass, and a reconciliation the closed region asked for.

**The survey line's terminus, batched and since ratified: `HD.11`, the observation rooms.** Leadership's own stair from the chapel to their own floor, bypassing the receiving room, the stated terms and the circuit entire — planned, surveyed, never cut. It explains why the survey exists, it gives `HD.11` a third door that does not exist, and it turns *redirect* — already one of the three things a party can do to `HC.12` — into **the only action in the module that would hand the most heavily gated room on Peak 3 to somebody who did not pay for it.** The level's argument survives on one already-established contingency: Vekkut cannot read the line he is following, so left alone he breaks into `HD.4` and shortcuts the explanation rather than the ordeal. Written into `HC.11`, both regions' diagram findings, and `PEAK_3_BLOCK.md`. **Not drawn as an edge, because it does not exist.**

**One phrasing flagged rather than changed.** `HC`'s region-level Connections bullet calls the excavation *one-way*. Both diagrams draw it undirected, because once it is through it is a hole in a floor. The bullet is left as it stands.

## THE CROWN'S OWN STAIR, RATIFIED

**Directed, and written at four levels.** A secret stairwell runs two levels from `GC.13`, the Steward's rooms, straight down to `GB.12`, the cell corridors — no landing on `GA`, on no plan of either level, and arriving **past the rod-locked gate at `GB.11`**. Undeclared access from leadership to the prisons, cut for captives whose names were not going to appear in the register.

Written into `GB`'s `## CONNECTIONS`, `GC`'s `## CONNECTIONS`, `blocks/PEAK_2_BLOCK.md` (prose and skeleton) and section 4 of `diagrams/Drakenhold_Relational_Diagram.md`. It does three things at once: it gives `GB.11` an answer that is not the gate, priced — the stair begins on the level a party reaches last and lands them inside a locked prison with the gate between them and the stair-foot; it puts the Steward's rooms and the prison register on one short line, which the `GB.4`/`GC.13`/`GC.14` thread will want; and it gives `GB.14`'s one entry without a charge somewhere to go. **The last of those is not resolved and is not to be assumed.**

## THE ROOT SINK AT `C.7`–`C.9`, RATIFIED

Batched at `C`'s step 8 pass and **answered: keep it.** The nest is not a single-throat fight; the edge stands as drawn, priced worse than the fight — narrow enough that armour comes off, no way back up in a hurry, and it drops a party into the chamber with the haul and the trunk on the far side. No change to `C`.

## THE `GC` RAMP BULLET, CONFIRMED AND EXTENDED

The correction from "**GB Karmor** — by way of GA" to "**GA Grathdun** — the great ramp down" is **confirmed correct**. The through-route from the throne to the prisons that the old phrasing gestured at is real, but it is not the ramp: it is the Crown's own stair above, secret and direct, and it does not touch `GA` at all.

## THE APPROACH, CLOSED AT STEP 8

`A` through `E` are one connected graph. The spine is `A.1`→`B.1`…`B.9`→`D.1`…`D.11`→`E.1`→`E.2`→`E.12`⇒`FA.1`. Two branches leave it and both rejoin: the camps at `C`, entered from `B.7` and rejoining at `E.1` by the scavenger track, and the drain from `B.4a`, rejoining at `D.6`. Four hidden edges carry the approach's priced answers — the yard hatch at `A.14`–`A.17`, the walled processional at `A.18`–`A.20`, the root sink at `C.7`–`C.9`, and the old course at `D.7`–`D.11` — plus the two-region drain `B.4a`–`D.6` and the sealed cellar `E.3`–`E.5`.

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
- ~~**`B.7` ↔ `C.1`/`C.2`/`C.3`.**~~ *Closed at C's step 8 pass. Each camp takes one trace; the drawing offers no reason to rank them, so the party's first camp is whichever trace it follows.*
- ~~**`C.5` the scavenger track west to the Outer City.**~~ *Ratified as an open edge `C.5`–`E.1`. Written at all four levels. E's step 8 pass reciprocates from its own side and should give `E.1` the goblin traffic in its outline.*
- ~~**`B.9` ↔ `D.1`** and **`B.4a` ↔ `D.6`**.~~ *Both closed at D's step 8 pass, reciprocated unchanged.*
- ~~**`D.11` ↔ `E.1`.**~~ *Closed at E's step 8 pass. `E.1` carries both roads; what differs is what the party arrives holding, and the registry at `E.6` is where the gap first shows.*
- ~~**`E.12` ⇒ `FA.1`.**~~ *Closed at the first-level block's step 8 pass. Written into `FA.1`'s Connections field and `FA`'s diagram, undirected. The hold's only outside opening is now drawn from both ends.*
- ~~**`FA.30` → `FC.15`, `FA.8` → `FB.9`, `GA.26` → `GC.7`, `HA.30` → `HC.7`, `HA.29` → `HB.3`, `HA.21` → `HB.17`.**~~ *All drawn from the main-level side. `HA.30`–`HC.7`, `HA.29`–`HB.3` and `HA.21`–`HB.17` are reciprocated unchanged at the Peak 3 block's step 8 pass. All six are closed.*
- ~~**`HA.19` the scholars' stair.**~~ *Closed at the Peak 3 block's step 8 pass. The landing is `HC.15`, the instruction rooms — the servants' route comes up where the initiates were prepared rather than where they were received. `HA` is amended to carry the edge, as its own stub asked.*
- **`GA.17` → `GB.5`.** The armoury support ways down, landing behind the formation. Written from `GA`'s side; `GB` confirms at its own pass.
- **`GC.13` → `GB.12`.** The Crown's own stair, ratified this pass. See above.
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
- ~~`FA.30` bypass lands at `FC.15`; `FA.8` chute lands at `FB.9`.~~ *Both closed at the Peak 1 block's step 8 pass, reciprocated unchanged. `FA.12`'s second panel at `FE.8` is placed and drawn off `FE.5`, and remains a reading thread rather than a route.*
- ~~`FC.21` → `FD.8`, `FB.15` → `FD.9`, `FB.8` → `FC.4`, `FC.5` → `FD.8`, `FD.15` → `I.1`, `FE.7` → `I.13`, `FB.14` → `J.2`, `FB.4`/`FD.16` → `J.3`.~~ *All drawn at the Peak 1 block's pass. `I` and `J` reciprocate at their own passes; none of them needs a decision to do it.*
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
- **`D.6` the drain outfall.** `J.9`–`D.6` is now drawn one-way outward from `J`'s side. Whether `D.6` should carry a referee-facing line about what else comes out of that culvert is **proposed and batched**; `D` is closed and was not amended.
- `GC.11` who ordered the defacing — named as a revelation, not yet named as a person.
- ~~Undead variety in `HB` rests on Skeletal Warrior and Shadow alone.~~ *Answered at the Peak 3 block's step 8 pass, from the existing bestiary and with no new template: **Dwarven Wraiths** on the royal and Runemaster tiers, **Skeletal Warriors** in the guild and guard galleries, **Shadows** below the tiers. The variety is tiered like everything else on the level, and the wraiths are why collecting royal names upstairs is collecting a weapon. Written into `HB`'s Creatures field and flagged there.*
- ~~The light mechanic in the deep.~~ *Resolved as a Referee procedure in `I_AND_J_BLOCK.md` and wired into `J`'s Encounter table. Teaching site at `J.6`, navigation answer at `J.16`.*
- **`I.16` the undefended approach — still open.** *Not answered at step 8 and deliberately so:* the stub itself defers *which level and from which direction* to the location pass, and naming it would settle by side effect which of three closed regions has a hole in it. Drawn in `I` with its far end absent, hanging off `I.7` and `I.12`. **Batched; resolves at `I`'s step 9 pass or by direction before it.**
- `J.24` is deliberately unanswered and stays that way.
- `HB.6` Baldrun Azkelith's empty interment is **the last unanswered question in the module**, and that is deliberate.
- The properties of the lance, unfixed. `HB.16` holds the line that nothing about how it was laid suggests it was meant to be used again.
- Hireling statlines, postponed to Referee ruling.
- ~~`B.4a` drain outfall.~~ *Closed at `J.9`.* `B.4a` outfall confirmed at `D.6` and drawn as an edge at B's step 8 pass; `B.5`'s two named destinations (Thurgan, Azost) are permanent flavour and owe no answer.
- ~~The Knight's fate.~~ *Resolved at `HB.15` — laid in the niche by the last dwarves who could reach him, the lance with him, his name carved nowhere on the level. `HA.5` does not carry him and that absence is the lock.*
- `HB.6` Baldrun Azkelith's interment was prepared and never filled. What happened to the last king is open in both `GC` and `HB`.
- `HC.9` the whispers are one side of a conversation with somebody who is not Vekkut. Who, unwritten, and deliberately not answered at step 8. `HC.19`, the shaft they come down, is drawn as a leaf in `HC` and as no edge at all in `HE`: nothing can travel it.
- ~~**`HC.11` the survey line's intended terminus.**~~ *Ratified: `HD.11`, the observation rooms — leadership's own stair from the chapel to their own floor, planned, surveyed and never cut. Not drawn as an edge, because it does not exist. See the Peak 3 section below.*
