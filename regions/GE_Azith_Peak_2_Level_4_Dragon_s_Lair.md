# `GE Azith, Peak 2 Level 4 Dragon's Lair`

**Classification:** DANGEROUS · **Difficulty Die:** d4 · **Tags:** The Crater, A Sleeping Wyrm, The Queen's Untouched Rooms

*Region file. Companion to the Drakenhold Setting Outline and the Setting Relational Diagram. Tables are authored at the location-stub pass (procedure step 7); location stubs, outlines and the region relational diagram follow in the engineer phase.*

---

**Overview:** The lair, and the region a party is meant to route around. The holding was once a long stately corridor with the King and his retinue at one end and the Queen and her staff at the other, private rooms opening off it. The King's end is gone — a crater gapes from the exterior and the chambers are open to weather. Vermakith sleeps in that crater atop what he has been given, fat and slow, roused only by fire in the vents, theft at scale, or the sound of his own name. The d4 is a warning printed on the region. The Queen's end of the corridor is largely intact and entirely untouched, because nothing there was gold, and the single most valuable thing in this region sits in her undisturbed apartments rather than anywhere in the hoard.

**Ambiance:** Weather. Wind through a hole in the mountain, rain when it rains, and daylight where there should be none. Heat off the sleeping bulk, and a low resonance in the stone that is breathing. The Queen's end of the corridor is still, dry, and lit only by what leaks down the length of it.

**Layout:** A long stately corridor with private rooms opening off it. The King's end is a crater, open to the exterior, and Vermakith sleeps in it atop what he has been given. The Queen's end is largely intact and entirely untouched. Ten to twenty rooms, and every one of them is a decision.

**Features:** The crater, the hoard beneath the dragon, and the three things that wake him — fire in the vents, theft at scale, and the sound of his own name. The Queen's apartments, untouched because nothing in them was gold. The single most valuable thing in this region sits there rather than anywhere in the hoard.

**Dangers:** The d4 is a warning printed on the region. A lair fight against Vermakith is fought against the room, the crater, the crumbling floor and the heat, and a straight exchange of blows is never a viable line of play. Everything else here is quiet.

**Creatures:** Vermakith. Lizardmen at the approach, not within.

**Secrets:** The Queen's rooms, entire — her correspondence, her household, and what she knew about the artifact that her husband did not. A servants' route into the corridor that does not pass the crater.

**Treasure:** The hoard, which is unmovable in any quantity that matters and lethal in any quantity that does. The Queen's apartments, which are portable, unguarded, and worth more.

---

## CONNECTIONS

*Authored against the Setting Relational Diagram. Edge types: open, gated by tile, gated by rod, hidden, secret, vertical, one-way, conditional on restored mechanism, conditional on faction relation.*

- **GD Valdmor** — vertical, the great ramp down.
- **I Brynaz** — one-way, vertical, open. Down through the crater from the outer face, and it arrives on top of the dragon.
- **Servants' passages** — secret. A route into the corridor that does not pass the crater, arriving at the Queen's end.
- **GA Grathdun** — secret, vertical. That route is the Peak 2 warren's third standing reward, running up from the capillary maze at GA.22. Written at both ends at step 8.

## TABLES

**Danger** — d6, presented at 6 on entry, counting down one face with each failed Difficulty roll. Resets to 6 on leaving the region.

| d6 | Danger |
|---|---|
| 6 | **Breathing.** A low resonance in the stone on a slow measure, felt through the soles before it is heard. Heat down the corridor. Weather from the far end. |
| 5 | **The hoard shifts.** Coin and plate sliding somewhere out of sight as the bulk on top of it resettles. Loud, sourceless, and over before anyone has decided what to do. |
| 4 | **Daylight and weather.** Wind through the crater at a working strength, rain if it is raining, and a floor at the King's end that is open to a very long drop. |
| 3 | **An eye opens.** Not both. The dragon is not asleep in the way the party assumed and has not decided that anything here is worth standing up for. Yet. |
| 2 | **The floor goes.** Fire-eaten stone at the crater's rim giving way, into the crater, onto the hoard, onto him. |
| 1 | **Awake.** Vermakith is up, and the fight is against the room — the crater, the crumbling floor, the heat and the drop. A straight exchange of blows is never a viable line of play and never becomes one. |

## LOCATION STUBS

*Procedure step 7. Code, name and three thematic tags per location. The working note under each is scaffolding for step 8. Block-level material — the tribute chain, Valdgir and the three wake conditions — lives in `PEAK_2_BLOCK.md`.*

*16 rooms budgeted; **9 are stubbed as locations** and the balance is unnamed fill — retinue rooms open to weather, a household's ordinary chambers, two rooms of nothing but furniture. **The region a party is meant to route around**, and every room in it is a decision.*

**The corridor**

### `GE.1 The Head of the Ramp` — Lizardmen Stop Here, Nothing Guards Beyond, Nothing Needs To
*Working note: the escort turns back at the threshold. What is past this point does not require guarding and the Lizardmen's refusal to go further is the clearest warning in the module.*

**Connections:** `GD.16` the ramp to the lair below — **vertical**, checkpointed · `GE.2` the stately corridor. The escort turns back here, and their refusal to go further is the clearest warning in the module.

### `GE.2 The Stately Corridor` — Long, Formal, One End Gone
*Working note: the spine of the level, King's end to Queen's end, private rooms off it. Standing at the Queen's end a party can see daylight the whole length of it, which means anything in the corridor can see them.*

**Connections:** `GE.1` the head of the ramp · `GE.3` the crater, at the King's end · `GE.6` the King's chambers · `GE.7` the Queen's apartments, at the far end · `GE.9` the servants' way. Daylight runs the whole length of it, which means anything in it can see the whole length of it too.

**The King's end**

### `GE.3 The Crater` — A Hole in the Mountain, Open to Weather, Something In It
*Working note: where the exterior came in and where he settled. Daylight, rain, wind, and a slope of tribute running down into the dark of it. `I` arrives here one-way from the outer face, on top of him.*

**Connections:** `GE.2` the stately corridor · `GE.4` Vermakith · `GE.5` the hoard beneath him · `GE.6` the King's chambers · `I.15` the crater descent — **one-way, vertical**, down the outer face and onto him.

### `GE.4 Vermakith` — Fat, Slow, Three Things Wake Him
*Working note: fire in the vents, theft at scale, and the sound of his own name. He is not a puzzle and not a boss. He is terrain with an appetite, and the module's spine is extraction, not this.*

**Connections:** `GE.3` the crater · `GE.5` the hoard beneath him. Terrain with an appetite, and the module's spine is extraction rather than this.

### `GE.5 The Hoard Beneath Him` — Unmovable in Any Quantity That Matters, Lethal in Any That Does, Thirty Years of Tribute
*Working note: thirty years of tribute under a sleeping weight. The joke of the region is that the most famous treasure in the setting is the least worth taking, and the module never explains the joke.*

**Connections:** `GE.3` the crater · `GE.4` Vermakith, on top of it.

### `GE.6 The King's Chambers` — Open to the Sky, Stripped by Weather, Nothing Kept
*Working note: Baldrun Azkelith's own rooms, ruined by thirty years of rain rather than by anything with intent. His name is not struck here — nobody came this far to chisel it — and that is the only place in Peak 2 it survives in the open.*

**Connections:** `GE.2` the stately corridor · `GE.3` the crater, which took the end of them. His name is not struck here, because nobody came this far to chisel it.

**The Queen's end**

### `GE.7 The Queen's Apartments` — Untouched, Because None of It Was Gold, Dry and Still
*Working note: entirely undisturbed. Nothing here was worth a dragon's attention and everything here is worth a party's. Portable, unguarded, and worth more than the hoard.*

**Connections:** `GE.2` the stately corridor · `GE.8` her correspondence · `GE.9` the servants' way. Untouched, because none of it was gold.

### `GE.8 The Queen's Correspondence` — Her Household, Her Own Hand, What She Knew and He Did Not
*Working note: **the single most valuable thing in the region.** The only account of the artifact written by somebody with nothing to defend — not the Crown's version, not the guilds', not the Runemasters'. She understood what it was before the ban and said so in letters to people outside the mountain. Some of those people may still be alive.*

**Connections:** `GE.7` the Queen's apartments. The only account of the artifact written by somebody with nothing to defend.

### `GE.9 The Servants' Way` — Arrives at the Queen's End, Does Not Pass the Crater, Small
*Working note: the whole reason this region is survivable. A secret route into the corridor that puts a party in the untouched half without ever entering the King's end. **Every gate has an answer that is not the gate**, and this is the module's clearest statement of it — the answer to the dragon is a servants' door.*

**Connections:** `GE.2` the stately corridor · `GE.7` the Queen's apartments · `GA.22` the capillary maze in the GA warren — **secret, vertical**. It does not pass the crater. **Every gate has an answer that is not the gate**, and the answer to the dragon is a servants' door.

## REGION RELATIONAL DIAGRAM

*Procedure step 8. Drawn from the stubs, before the location outlines. Reconciled against the finished outlines before the region closes. The diagram is authoritative: the **Connections:** field under each stub is checked against it, never the reverse. Worked as one block with the other three levels of Peak 2 against `blocks/PEAK_2_BLOCK.md`, because one thing moves through all four.*

*Tier 3 first — the region's location groups and how they interconnect — then one tier-4 diagram per group, resolving to locations. **Connection type is drawn at tier 4 and nowhere else**, and a destination outside the group is drawn on the group's own diagram. Each diagram is a file in `diagrams/`, spliced in here by the build.*

<!-- DIAGRAM: T3_GE.md -->

<!-- DIAGRAM: T4_GE_CORRIDOR.md -->

<!-- DIAGRAM: T4_GE_KING.md -->

<!-- DIAGRAM: T4_GE_QUEEN.md -->

**Reading the diagram.** Nine nodes and one dotted edge. The single arrow is `I.15`, the crater descent, which is one-way and arrives on top of him. Everything else on this level is an open walk, which is precisely the problem.

**What the drawing found.**

- **The region is one corridor with two ends, and both ends can see each other.** `GE.2` carries four edges and the stub already says daylight runs its whole length. The graph says the same thing structurally: there is no route from the ramp to the Queen's apartments that does not pass the mouth of the crater. **Unless the party did not come up the ramp.**
- **`GE.9` is the region's entire reason for being survivable and it is drawn as exactly two edges.** The servants' way lands on `GE.2` at the Queen's end and directly into `GE.7`. A party that arrives this way reaches the most valuable thing in the region — `GE.8`, the only account of the artifact written by somebody with nothing to defend — **without ever entering the King's half of the corridor.** The answer to the dragon is a servants' door, and the drawing is where that stops being a slogan.
- **The King's end is a closed cluster of four and everything in it touches the crater.** `GE.3`–`GE.4`–`GE.5`–`GE.6`. There is nothing at that end that can be reached without standing at the rim, including `GE.6`, the King's own rooms — which hold the only surface in Peak 2 where Baldrun Azkelith's name survives in the open, because nobody came this far to chisel it. **The one place the erased name is simply written down is fifteen feet from a sleeping dragon**, and the module never points at the joke.
- **`GE.5` is a leaf on the crater and `GE.8` is a leaf on the Queen's rooms.** The most famous treasure in the setting and the most valuable object in the region are both dead ends, and they sit at opposite ends of the corridor behind opposite kinds of risk. One is unmovable in any quantity that matters. The other fits in a satchel.
- **`I.15` is the only one-way route in the whole peak.** It arrives at `GE.3` down the outer face and there is no climbing back up it. A party that comes down the outer face into the crater has entered a region whose only other exits are the checkpointed ramp and a servants' door it does not yet know exists — and it has landed on the hoard, which is one of the three things that wakes him.
- **Nothing here is gated.** Not one lock in the region. `GE` is the module's demonstration that the hardest ground in Drakenhold can be entirely open and still be the place a party is meant to route around: **the d4 is the lock.**

**Route ends recorded.** Three edges leave region `GE`. `GD.16`–`GE.1` is the last climb. `I.15`⇢`GE.3` is the crater descent, one-way. `GA.22`–`GE.9` is the servants' way, **new at this pass and a reconciliation** — the block document and the setting diagram have always carried a servants' route into the lair corridor, and it had no end in any region file. `GA` is amended to carry it.
