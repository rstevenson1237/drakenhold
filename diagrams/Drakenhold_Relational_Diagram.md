# DRAKENHOLD — SETTING RELATIONAL DIAGRAM

*Procedure step 6, and the head of the diagram layer. Diagrams are authoritative: the Connections section in each region file is checked against them, never the reverse.*

---

## THE FIVE TIERS

Every diagram in the module is a file of its own in `diagrams/`, and every one of them shows **only the tier below it** and how those elements interconnect.

| Tier | The diagram | Shows | File |
|---|---|---|---|
| 1 | the setting | the region blocks | `T1_SETTING.md` |
| 2 | a region block | the regions in it | `T2_<BLOCK>.md`, five of them |
| 3 | a region | the location groups in it | `T3_<REGION>.md`, one per region |
| 4 | a location group | the locations in it | `T4_<REGION>_<GROUP>.md` |
| 5 | a location | nothing — it is the leaf | — |

**Connection type is drawn at tier 4 and nowhere else.** Above it, two children that are connected at all are joined by one plain untyped edge, however many typed routes actually run between them and whatever kind they are. Counting the ways from Peak 1 to Peak 2 is a tier-4 question and the tier-1 graph refuses to answer it.

**A destination outside the group is drawn on the group's own diagram.** When a location connects to a location in another group — in this region or another — that destination location appears on the tier-4 diagram, outside the group's frame. That is the only duplication the layer permits, and it is what makes a group diagram readable alone.

**Tier 4 is authored. Tiers 1 to 3 are derived from it** by `scripts/diagrams.py --write`, and `check.py` M11 re-derives them and fails on drift. Every fact about the graph is therefore written down in exactly one place: the tier-4 file for the group the location belongs to. Nothing above tier 4 is edited by hand.

**Diagrams are spliced into their host documents by the build.** A host carries a marker line — `<!-- DIAGRAM: T3_FA.md -->` — and `scripts/build.py` and `scripts/pdf/render_web.mjs` replace it with the file's contents. Tiers 1 and 2 are hosted here; tiers 3 and 4 are hosted in the region files, under `## REGION RELATIONAL DIAGRAM`. M11 fails if a marker names a file that is not there, or if a file is spliced in twice or not at all.

---

## EDGE VOCABULARY

Drawn at tier 4. Not a closed list: new types are proposed and added here rather than coined in passing.

| Type | Mermaid style | Meaning |
|---|---|---|
| open | solid line, plain label | Walk it. No key, no climb, no trick. |
| gated by tile | solid line, `[tile]` | A whole carved stone tile in a matching receptacle grants passage. |
| gated by rod | solid line, `[rod]` | A runed metal rod of the stated tier makes the mechanism act. |
| hidden | dashed line, `[hidden]` | Physically there and unmarked. Found by searching the right place. |
| secret | dashed line, `[secret]` | Concealed on purpose, and knowing it exists is itself a discovery. |
| vertical | any line, `[vert]` | Climb, fall, ramp or shaft. Movement costs and encumbrance bite. |
| one-way | arrow, single-headed | Passable in the stated direction only. |
| conditional — mechanism | dotted line, `[mech]` | Opens only once something is restored, relit or re-sequenced. |
| conditional — faction | dotted line, `[faction]` | Opens only at a stated relation level, or by toll, escort or bargain. |
| conditional — size | dotted line, `[size]` | Passable only by the small, the unarmoured or the desperate. |

---

## TIER 1 — THE SETTING

<!-- DIAGRAM: T1_SETTING.md -->

**Reading it.** Everything above the peaks is the road in, and it is a single chain with one branch **and one bypass**. The scavenger track runs `C`→`E` direct, two days west, and does not pass the crossing at `D` — the goblins have been using it for thirty years and it is how the tile came out of the Outer City. A party that leaves the road to deal with the camps can come back onto the road past `D` entirely, paying no toll, meeting no hobgoblins and never seeing the Charter camp. That is the price of the branch and it is deliberate: `D` is skippable, and skipping it is a choice made in ignorance of what is being skipped.

Everything below and around them is the answer to a locked door: the Skybridge is the horizontal cheat, the servants' passages are the lateral one, and the Lost Caverns are the vertical one. **FA is the only opening to the outside world.** Every other way in — the Skybridge termini, the crater, the hidden descents — is a way *out* first, discovered from inside, and only becomes an entrance on a second visit.

**The rule the three answers encode.** Every gate in Drakenhold has at least one answer that is not the gate. A party that cannot pay the Lizardmen's toll can go under the mountain or over it; a party that cannot open a Royal lock can come at the room from a direction the room was never defended against. The cost is always the same shape — the alternate route is longer, darker, or watched by something worse.

**The approach edge that runs the other way.** `I_AND_J`—`APPROACH` is one edge and it is `J.9`→`D.6`: the drain's far mouth, forty feet downstream and underwater, one-way outward and unenterable against the flow. It is drawn from `J`'s side alone, which is why it is the only tier-1 edge with nothing at the other end to meet it.

---

## TIER 2 — THE APPROACH

<!-- DIAGRAM: T2_APPROACH.md -->

*Held for the location pass on B: the culverted dwarven drain, and the waystones' two unheard-of destinations. The drain's far end is likeliest to surface on the near bank at D rather than at E — the Outer City is a long way off and the river lies between.*

---

## TIER 2 — PEAK 1 (F), TRADE AND CRAFT

<!-- DIAGRAM: T2_PEAK_1.md -->

**Notes.** The dispatch floor on FC is the level's puzzle and also its map: correct sequencing opens a hidden access that appears on no plan, and wrong sequencing strands a party between FB and FD. The chimney is the peak's spine — it is the only thing touching the Under Level, Level 3 and the caverns at once, and it is the flow that relighting the forge depends on. **The great ramp reaches FB** at `FB.16`, the collectors' landing, and the toll road runs down it from `FD.15`. **The FA warren touches Khorven** by the vent gallery at `FA.33`, size-conditional, which is the warren's own way onto the shaft.

The peak's edges to the Skybridge and the Lost Caverns are cross-block and do not appear here: `FD` and `FE` reach `I`, and `FB` and `FD` reach `J`. Tier 1 carries them as one edge apiece, and tier 4 carries them typed.

---

## TIER 2 — PEAK 2 (G), AUTHORITY AND THE DRAGON

<!-- DIAGRAM: T2_PEAK_2.md -->

**Notes.** The direct horizontal route between peaks runs through the dragon's counting house, and the counting house is held by people who assess before they reach. That is the design. GC's balcony has no Skybridge access and is drawn with none. The crater is the one place the outside gets in, and it gets in on top of the dragon — the edge is one-way for a reason.

**The Crown's own stair**, `GC.13`→`GB.12`, is secret and vertical, running two levels from the Steward's rooms to the cell corridors without a landing on `GA` and arriving past the rod-locked gate at `GB.11`. Undeclared access from leadership to the prisons, for captives who were not going to appear in the register. It is `GB.11`'s answer that is not the gate and it is priced: it begins on the level a party reaches last and ends on the wrong side of a lock.

**The deep cells descend into J.** It is how the Elder Wyrm came up, it is how the Runemasters learned the yoke without hauling their subject the length of the marked descent, and it is why the mad Runemaster has had something to listen to for thirty-two years.

---

## TIER 2 — PEAK 3 (H), SPIRIT AND THE DEAD

<!-- DIAGRAM: T2_PEAK_3.md -->

**Notes.** Peak 3 is the only peak whose internal routes are all earned rather than walked. The circuit can be run honestly for a rod or cheated from the observation rooms, and the shortcut costs more than the road. The kobold chieftain's excavation is a live edge that completes on a clock whether or not the party touches it — accelerating, redirecting or collapsing it are three different campaigns, and one of them hands HE to something that cannot read what it finds.

**HE has no edge except from HD.** The dragon never came, nothing has been carried out in thirty-two years, and the only ways in are the ramp and the observation-room route. This is deliberate and is why HE pays what it pays.

---

## TIER 2 — THE SKYBRIDGE AND THE LOST CAVERNS

<!-- DIAGRAM: T2_I_AND_J.md -->

**Notes.** `I` and `J` are the horizontal answer and the vertical one, and the graph of the block they share is two nodes and no edge between them. That is the finding, not an omission: the top of the mountain and the bottom of it are connected only by going through the mountain. Everything either region is *for* is a cross-block edge — `I` reaches `FD`, `FE`, `GD`, `GE` and `HD`; `J` reaches `FB`, `FD`, `GB` and `HB`, and `D.6` one way outward. Tier 1 carries the fact that they connect; the tier-4 diagrams carry which shaft, at what price, in which direction.

**The two orphaned Skybridge runs.** One arrives in `FE`, which is otherwise reachable only by the `FD` ramp, and one arrives in `GD`, inside the vaults without passing the Lizardman checkpoint. Both are intact and both have lost their approach; restoring either is a mechanism problem and each is a major prize.

---

## AUDIT

Standing findings, carried forward through the retiering:

- **FA is the sole exterior entrance.** GA and HA have none; E connects only to FA. Held.
- **GC has no Skybridge access.** The balcony is a nobles' balcony. Held, and drawn with no edge to I.
- **One ramp up, one stairwell down between peak levels.** Held. All additional vertical edges are chutes, chimneys, channels or excavations, and each is typed at tier 4.
- **The servants' passages interconnect all three peaks**, as the second internal cross-connection alongside the Processionals. **They are no longer a node.** `S` was a fiction the old overview needed because it had no tier below it: the passages are location groups inside `FA`, `GA` and `HA` and always were, and the runs between them are ordinary region-to-region edges now that the graph resolves that far. The Long Run passes through a **sealed segment** with a tile lock at each face, and the way around is the **Ash Run** and the **Cold Run** in series, at three times the distance.
- **Sub-region nodes are gone with it.** The deep cells, the observation rooms and Torvin Ganthur's niche were drawn as boxes hanging off a region because the overview could not reach a location. Each is a location, each sits in its group's tier-4 diagram, and each is now named by its code rather than by a paraphrase.
- **The three detail graphs the old file carried for the Skybridge, the passages and the caverns are gone, and nothing was lost with them.** Every edge they drew is drawn once, at tier 4, in the group it belongs to. What they were really carrying was the argument above about gates and answers, which is prose and has been kept as prose.
- **Graph legibility, resolved.** The old overview was known to be unreadable as routes accumulated, and was held as-is until the per-region diagrams existed to hold the specifics. They exist, and the tiering is the collapse that was promised: five nodes at tier 1, five regions at most per tier 2, and no diagram in the module larger than one location group.
