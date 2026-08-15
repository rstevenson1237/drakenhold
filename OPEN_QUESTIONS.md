# DRAKENHOLD — OPEN QUESTIONS

*The architect's register. **This is the single authoritative list of what the module has not yet decided.** It is process material, not play material: it is not assembled into the Playbook and it is not published to the web view.*

*It exists because open items were previously tracked in three places at once — the setting outline, the handoff, and inline in region files — and the three disagreed. The setting outline is the root of referee-facing information and keeps only the questions the module leaves open **at the table, on purpose**. Everything an author still has to decide lives here.*

---

## HOW THIS FILE IS RUN

**Opened.** A pass that raises a question adds it here, with the ground it belongs to and the pass that will answer it. `RECONCILIATION.md` J1 requires this and it is not optional: nothing is resolved silently and nothing is resolved by assumption.

**Answered.** The item is **struck through**, and a note says where the answer now lives. The record of what was open is kept, because the same question resurfaces and the answer needs a provenance. Struck items are never deleted.

**Inline duplicates are allowed and are not the register.** A question attached to the ground that will answer it — `GB`'s unnamed descent, `I.16`'s absent far end — stays written in the region file where the next author will meet it. This file is where it is *counted*.

**Mechanical questions do not resolve here.** `Rules_Light_TTRPG_Design_Notes.md` is the source of truth for game mechanics and is read-only in this repo. A gap in it is recorded below under *Mechanical dependencies*, raised in the pass's question batch, and answered **in the rules project**. Rulings received are recorded in `DECISIONS.md`.

---

## OPEN — CONTENT

- **`I.16`, the undefended approach.** Drawn in `I` with its far end absent, hanging off `I.7` and `I.12`. Which level and from which direction is deferred by the stub itself, and naming it settles by side effect which of three closed regions has a hole in it. **Resolves at `I`'s step 9 pass or by direction before it.**
- **Peak 2's declared descent into `J`.** `GB`'s region Connections claim it; no `GB` stub carries it, where `FB.14` and `HB.19` carry the other two peaks'. Naming it means inventing a stub against a ratified count of twenty, so it sits in unnamed fill. **Whether to name it is `GB`'s to decide at step 9.**
- **`GB.14`'s one entry without a charge.** The Crown's own stair, `GC.13`→`GB.12`, gives it somewhere to go. **Which entry, and whether the stair explains it, is not decided and is not to be assumed.** `GB`'s and `GC`'s, at their own passes.
- **`GB.17`, the jailer's oath.** Two releases exist and one of them is a lie. Which lie, unwritten.
- **`GC.11`, who ordered the defacing.** Named as a revelation and answered as one — Vessa Rudgir, the Steward. Not yet written as a person: what she was, what it cost her, and what `GB.4` does to the account.
- **`HC.9`, the whispers.** One side of a conversation with somebody who is not Vekkut. Who, unwritten, and deliberately not answered at step 8. `HC.19`, the shaft they come down, is a leaf in `HC` and no edge at all in `HE`: nothing can travel it.
- **M3 must be repointed before the `Connections:` field can be dropped.** *Opened at `A`'s step-9 pass, alongside the ratified call in `DECISIONS.md`.* `check.py`'s `_parse_location_connections_in_region` reads the `**Connections:**` field and nothing else; the final pass removes that field in favour of the `->` pointers inside feature entries. **The parser change and the field removal are one pass, not two** — either alone leaves the diagram unchecked against anything. Not a mechanical gap in the Notes and not a content question: a builder-phase task, recorded here so it is not discovered by a failing check.
- ~~**The waystone crown mark.**~~ *Opened and answered at `B`'s step-9 pass. **It is the general device of an authority that no longer exists, and nothing in the module names it.** Not the King's mark, not connected to the defacing inside the hold, and no later region owes it a payoff — it is a sign of the decay the region has met with over the decades, sitting with the ruts, the gutter and the ledger. Written at `B.5` and `B.8`; no edge, no stub, no thread.*
- **`PEAK_3_BLOCK`'s Kelmor citation.** *Raised at `A`'s step-9 pass.* The thread list reads "`A.20` **Brannek Kelmor** — a party that buried him recognises him on the obelisk and can find his people's interment at `HB.7`." `HB.7` is the Runemaster gallery; the Guild gallery holding Kelmor is `HB.8`, as `HB`'s own stub says. `M1` cannot see this because both codes exist. **A one-code correction in a block document, proposed and not applied — `HB`'s ground.** *Direction received: leave it, documented.* The block's thread list now carries the dispute inline, marked, naming `HB.8` as the likely destination and `A.18`'s two Kelmor name-stones as the support, so `HB`'s pass meets the question on the ground that answers it. **`HB` owns both the correction and the alternative** — that the refugees' own people lie somewhere the Guild gallery is not.
- ~~**`D.6`, the drain outfall.**~~ *Written at `D`'s step-9 pass, as small as the direction asked.* `D.6` now carries **the other mouth**: a second opening forty feet downstream, underwater, older and rougher than the service drain, running hard cold water in weather that is giving the river nothing, and unenterable from this side against the flow. **No edge, no code, no answer.** `J.9`–`D.6` stays one-way outward and drawn from `J`'s side only; `D`'s diagram is unchanged and `D.6`'s Connections field names only `D.5` and `B.4a`. The line states the phenomenon and says plainly that nothing in `D` explains it, that it is not evidence of anything larger, and that a Referee may answer it, use it once, or leave it standing. The missing grating is answered in the only way it can be from this end: it is not here either.

- **The calls made at `E`'s step-9 pass.** Five, all written into the region and all batched rather than ratified. **The doors fell outward** at `E.12` — leaves on the road, hinge sockets torn out of the jamb — and with the four fans of rubble lying outside the wall at `E.1` the physical evidence in this region consistently says the destruction came from inside the line. **The agent is deliberately unnamed** and no location names it. **This gate is the Hammer Gate**, one of the three the waystone at `B.8` names, and the one standing open; the other two are untouched and unpointed-at. **The confiscation racks at `E.6`** hold the provenance of every scavenged tile in the setting — counted, shelved, never sent up, and now empty — which is where `C.1`'s goblin chief and `A.7`'s attics got theirs, and which explains what a tile *is* without saying what one *does*. **The city guard went up the road** before the descent, as escort and labour for the evacuation, which is why the muster roll at `E.8` is two-thirds short and why nothing held at the wall. **Ashen is a woman**; the unidentified House rod is carried by one of the two crew who read runic, which keeps the Creatures field's wording exact.
- **`E`'s Treasure field says "Nothing concentrated" and the outlines have qualified it.** *Flagged under rule 17 rather than applied silently — the change is in the file and can be reverted in one edit.* The field now reads *nothing concentrated except by weight*, because `E.4` is a shed of metal that needs mules and `E.5` is a packed cellar, and both are on the same hill so the choice is forced. The original clause predates both step-7 notes it was already in tension with.

- ~~**The naming and the calls made at `D`'s step-9 pass.**~~ *All four answered by direction and ratified in `DECISIONS.md`: the garrison at `D.2` was killed by the hold's own people at the Descent, two years after the courier; the toll at `D.8` has two numbers and only the small one is ever quoted; Vashek, Halvard Grellick, Emmet Tarr and `Brynost` stand as written. Nothing amends a closed region — the `C.9` satchel is described from `D`'s side only.*

---

## OPEN — RAISED BY THE STEPS 1–8 SWEEP

*Procedure 12's reconciliation pass, run before step 9 begins anywhere. `scripts/check.sh` M1–M8 all pass; every item here is a judgement finding. The five contradictions the sweep raised were batched and **answered by direction** — they are struck below and the calls are in `DECISIONS.md`. What remains are the watch items, each naming the pass that owns it. J2 was not run: it is a closing check and belongs to each region's own step-9 pass.*

**Truths**

- **"Royal names open what nothing else will" has a teaching site and no lock.** `GC.9` and `GC.10` teach that royal names are collectable and that the King's is not a master key. No location anywhere is opened by a royal name; the two name-opened locks in the module, `FA.22` and `HB.15`, are both non-royal. **`GD`'s Royal sub-vaults and `HB`'s royal gallery at their step-9 passes.**

**Rumours**

- **Rumour 8's sleep cycle is neither confirmed nor falsified.** *He sleeps a year at a stretch and wakes for a year.* `GE` and `PEAK_2_BLOCK` give three wake triggers and no cycle. Rumours 1 and 12 are marked wrong in Vermakith's faction Knowledge; 8 is not, and the Lizardmen's "roughly how long the Dragon has been asleep" does not settle it.

**History**

- **The Driving Down's obelisk trace is half-placed.** *The first King's is the first name cut on the black obelisk.* `HA.5` exists and is the name-index; nothing states the first cut, and the first King is unnamed anywhere. Against Truth 1 — Clan Azkelith "now largely unwritten in the upper halls" — this is a hook rather than a hole. **`HA`'s step-9 pass.**

**Factions**

- ~~**The Hobgoblins' lean-season raid on Thornhaven has no site in `A`.**~~ *Answered at `A`'s step-9 pass: **it stays unsited, on purpose.** Thornhaven is the module's only SAFE region and nothing attacks a party inside it. What was missing was not a site but a trigger, and that is now written into the Hobgoblins' faction entry as a Referee ruling — the toll drying up, a hard winter, a loss at the crossing to make good, or word that the town's fighting strength has walked up the road — with the outlying holdings as the target and the town hearing about it rather than fighting it. The timing is recorded in the outline's Unanswered Questions as a Referee call. No stub, no Events result, no Hobgoblins in `A`'s Creatures field.*

**Bestiary**

- **`HD` names its creatures as "Constructs"**, which is a category rather than an entry. `Automaton` and `Living Statue` both exist; `HD.8`'s trial post is neither yet. **`HD`'s step-9 pass.**

---

## OPEN — DELIBERATELY, AND STAYING THAT WAY

*These are answered by being unanswered. They are listed so that a later pass does not "fix" them.*

- **`HB.6`, Baldrun Azkelith's empty interment.** The last unanswered question in the module. `GC`, `HB`, `I` and `J` have all been drawn and none of them answers it.
- **`J.24`.** Unanswered on purpose.

## OPEN — MECHANICAL DEPENDENCIES

*Raised against `Rules_Light_TTRPG_Design_Notes.md`. Answered in the rules project, never in a region file. Answers received are written into `DECISIONS.md`.*

*The four gaps raised after step 8 — the light rule, Rest inside a DANGEROUS region, Weather on the span, and the Danger Die's reset — are all answered. See `DECISIONS.md`. Three proposals are open.*

**The test these are held to, and the test anything else must pass:** a one-off procedure earns its place where **the players are already keeping score in their heads and the procedure only makes the scoring visible.** Bloat is a procedure that tracks something the table was not already tracking. All three below are proposals for the rules project. **None of them is written, and none may be written into a region file.**

- **Buying the warrens.** `DECISIONS.md` records the standing call for the three arteries: *no landmark system, no service marks, no mechanic — a sheer numbers game of twisting paths and trying to keep track.* That call stands and this does not overturn it. But the survivors' stated advantage is **thirty years of memory a party cannot buy** — which is precisely the thing a party will try to buy, and there is no procedure for what a bought or coerced guide is worth, what a wrong guide costs, or what happens when the guide leaves. The table will want that negotiation scored. **Proposed as a rules-project question, not a mapping system.**
- **The `HD` circuit.** A closed ring, no chord, an attempt imposed at every segment in either direction, with the rod that opens `HD.11` at the far end of it. It is already a mini-game in everything but name and the fiction is fully built. What it lacks is a stated order and a stated cost for a failed segment. **The smallest of the three, and the one players will most visibly engage with as a system.**
- **Weight against the way out.** The module's spine is extraction, and the Notes carry Encumbrance as slots. Every treasure decision here is a slot decision made hours from the door, and the earned rod at `HD.10` already **buys a way back out rather than treasure.** A light procedure for hauling under load back through a region already crossed — not a new subsystem, only what the existing slots cost on the return leg — would make the module's central tension mechanical instead of implied. **The largest in scope and the one most worth getting right.**

**Deliberately not proposed:** any further scoring of the light rule. It works because it is three states and a Referee call, and `J.6` teaches it without a table.

---

## ANSWERED

*Struck, with where the answer lives. Never deleted.*

*The five contradictions the steps 1–8 sweep raised, all answered in the batch that closed it. The calls are in `DECISIONS.md`.*

- ~~**The tile Truth over-promises.**~~ *Answered: **tiles gate sideways, never up.** The Truth named four applications where the corpus drew two. Narrowed to the Skybridge termini and the seal, with the ramps and both Processionals staying open and priced in exposure — the reading all three peaks reached independently. Rewritten in the setting outline; ratified in `DECISIONS.md`.*
- ~~**Rumour 19 points nowhere.**~~ *Answered: **half true, and the true half is readable rather than walkable.** The northern road existed, was cut off at the Driving Down, and is sealed with words at `J.4` like everything else there. Written into `J.4`'s note. No edge, no stub, nothing passes.*
- ~~**Ashen's Crew have no landing site inside the hold.**~~ *Answered: **they are a clock, not a location.** Still at `E.7` when the party arrives — rumour 14 runs ahead of the fact — and they go up on a schedule the Referee advances regardless. Written at `E.7`; inherited by `PEAK_3_BLOCK`.*
- ~~**The Silver Veins trace is written nowhere.**~~ *Answered: **ambient in the three level-2 regions.** `FC`, `GC` and `HC` each carry the join at their own step-9 passes. Written three times rather than once, because the repetition is how a party learns it is hold-wide. No stub.*
- ~~**Three Bestiary entries are never used.**~~ *Answered: `Sellsword` at `D.10`, `Delver` at `E.7`, `Camp Hand` at `A`'s hiring. The prose already describes all three; only the names are missing, and they are added when those locations are written. Nothing cut.*
- ~~**Four citation defects `M1` cannot see.**~~ *Answered: all five corrections applied. The earned rod is `HD.10` in `PEAK_3_BLOCK`, `DECISIONS.md` and this file; `I_AND_J_BLOCK`'s descent sentence is rewritten without the self-correction and without the wrong code; `HB.14` and `HD.14` read "ratified"; the `GAG` spacer node and both notes recording it as owed are gone.*

- ~~**`HC`'s one-way phrasing.**~~ *Answered. `DECISIONS.md` ratifies the `HC.12`–`HD.4` excavation as bidirectional, gated by time and intervention rather than by direction, and `HC`'s region-level Connections bullet now reads that way and carries the ratification note. Struck at the steps 1–8 sweep, which found it still listed as open after the correction had landed.*
- ~~**`E`'s arrowhead on `E.12` ⇒ `FA.1`.**~~ *Answered. `DECISIONS.md`: emphasis is carried by the heavy edge alone, never by an arrowhead. `E`'s diagram draws `E12 === FA1` undirected, matching `FA`. Struck at the steps 1–8 sweep, same reason.*
- ~~**The seventh chair at `GA.2`.**~~ *Answered at `GC.14` — the Steward removed her own seat and kept it whole in her rooms. Why is open and is `GB.4`'s to complicate.*
- ~~**Artifact piece count and placement.**~~ *Seven, ratified. All placed: `E.5`, `D.3`, `FD.14`, `GD.10`, `HB.14`, `HD.14`, `J.18`. Two ever left the mountain and the evacuation register at `E.6` proves it. **The count is itself a clue** and the module never performs the subtraction.*
- ~~**`GD.10`, the third sub-vault.**~~ *Ratified as **artifact piece four**, placed under Royal authority in the season of the Breaking. The proposal stood from the Peak 2 block's pass; ratified in full at the post-step-8 cleanup. The count of seven is now settled at every one of its seven placements.*
- ~~**A second horror for `HE`.**~~ *No second template. One singular collared Drakmorith at `HE.6`, addressable rather than negotiable. The existing Horror-type entry already supports arriving-as-geometry; no new entry drafted and none needed.*
- ~~**Undead variety in `HB`.**~~ *Answered at the Peak 3 block's step 8 pass from the existing bestiary, with no new template: **Dwarven Wraiths** on the royal and Runemaster tiers, **Skeletal Warriors** in the guild and guard galleries, **Shadows** below the tiers. Written into `HB`'s Creatures field.*
- ~~**The thing in `GB`'s deep cells.**~~ *An Elder Wyrm taken alive during the expansion and kept for study — which is how the Runemasters learned to build the yoke at all. Uses the existing Bestiary entry; what it knows, wants and has become in thirty-two years is written into `GB`.*
- ~~**Who ordered the defacing.**~~ *Vessa Rudgir, the Steward, in her own hand through proper channels with no government left to sign for. `GC.11` + `GC.13` + `GC.14` + `GB.4` are one answer. Naming her as a person is still open, above.*
- ~~**The Knight's fate.**~~ *Resolved at `HB.15` — laid in the niche by the last dwarves who could reach him, the lance with him, his name carved nowhere on the level. `HA.5` does not carry him and that absence is the lock. History still preserves it as unknown, which is intentional: check at each pass that no other section contradicts the public record.*
- ~~**The light mechanic in the deep.**~~ *Resolved as a Referee procedure in `blocks/I_AND_J_BLOCK.md` and wired into `J`'s Encounter table. Teaching site at `J.6`, navigation answer at `J.16`. **Ratified as a legitimate one-off region procedure** — see `DECISIONS.md`.*
- ~~**`HC.11`, the survey line's intended terminus.**~~ *Ratified: `HD.11`, the observation rooms — leadership's own stair from the chapel to their own floor, planned, surveyed and never cut. Not drawn as an edge, because it does not exist.*
- ~~**`B.4a`, the drain outfall.**~~ *Confirmed at `D.6` and drawn as an edge at `B`'s step 8 pass. Closed again at `J.9` from the other direction. `B.5`'s two named destinations, Thurgan and Azost, are permanent flavour and owe no answer.*
- ~~**The C→E scavenger track.**~~ *Ratified as an open edge `C.5`–`E.1` at the guard wall. The consequence is accepted, not mitigated: `D` is now skippable, and the module never performs that subtraction.*
- ~~**The root sink at `C.7`–`C.9`.**~~ *Ratified: keep it. The nest is not a single-throat fight.*
- ~~**Hireling statlines.**~~ *Deliberately postponed to Referee ruling. Recorded in the setting outline, where a referee will meet it.*
- ~~**The properties of the lance.**~~ *Deliberately unfixed. Recorded in the setting outline. `HB.16` holds the line that nothing about how it was laid suggests it was meant to be used again.*
