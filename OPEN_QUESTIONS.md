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

## THE SIX ROUTES

*Added at the open-item resolution pass, because the register had grown to roughly forty live items and they are not one kind of thing. **Every open item carries exactly one route**, written into the item so the next author does not re-derive it. An item whose route is not yet obvious is routed by direction, not by guess.*

**A · Strike as already answered.** The work that answers it demonstrably landed in a later pass and nobody came back to close the item. **No content changes.** Strike it, with an italic note naming the file and the pass where the answer now lives. If it states a standing call rather than a fact about one location, restate the call positively in `DECISIONS.md` first.

**B · Direct edit.** Local, in scope, one location or one field, no procedure implicated. Edit, then strike. **Practice 7 still binds** — a change that removes established content is proposed and flagged, never applied in passing because the item invited it.

**C · Editorial note.** The step that answers it has not yet run on that ground. Write a `[[ ... ]]` note at the exact spot the next author will meet it, naming the owning step. **The item stays open.** The note is the inline duplicate this file already permits; it is not a resolution and does not shorten the register.

**D · Regenerate by re-running the step.** The item is architectural: it changes how the content was *produced* rather than what it says. **Re-run the owning numbered step over that region or block**, with the single correct `patterns/<MODE>_<WEIGHT>.md` open, under practice 3. Do not hand-patch prose toward the new shape — patching closes the symptom and leaves the region unable to survive its own re-run, which is the failure this route exists to prevent. Each D item is a booked pass of its own and is not done in passing by whatever pass discovers it.

**E · Ratify only.** The item is a call, not a content gap. Write it into `DECISIONS.md` and strike here with a pointer. The content that follows from it is a separate D item, and saying so is part of the ratification.

**F · Refer out.** A mechanical dependency owned by the rules project. It stays open, tagged as not ours. `OPEN — MECHANICAL DEPENDENCIES` is this route entire.

**Two items carry no route and never will.** `OPEN — DELIBERATELY, AND STAYING THAT WAY` is not a backlog. A pass that routes an item out of that section has made a decision it was not asked to make.

**A route may be carried by a section.** *Found at the route-A sweep, which discovered most sections are route-homogeneous.* Where every item under a heading resolves the same way — the mechanical dependencies are all `F`, the sweep's watch items are all `C` — **the route is stated once in the section's italic preamble and an item carries a tag only where it differs.** Tagging forty-five items individually would have said the same thing forty-five times and buried the exceptions, which are the part worth seeing.

**Not everything here is an open item.** Two sections hold material that carries no route and never will: `OPEN — DELIBERATELY`, which is answered by being unanswered, and the *techniques noticed and not yet used*, which are candidates rather than questions. **A section that carries no route says so.** A pass that routes something out of either has made a decision it was not asked to make.

**The order the routes are worked.** A first, because it is free and shrinks the register furthest. Then E, because the D passes are not decidable until the calls exist. Then the checker predicate backlog and M3's repoint, both recorded below. **Then D, and not before** — regenerating a region before the predicates that would check it exist means regenerating it twice. B and C are opportunistic and ride along with whatever pass is already standing on that ground.

---

## OPEN — CONTENT

*Route `C` unless an item says otherwise. Every one of these is ground a named future pass will stand on, and the question is already written into the region file where that author will meet it — which is the inline duplicate this register permits. **They do not shorten by being worked; they shorten by their pass arriving.** The exceptions carry their own tag.*

- **`I.16`, the undefended approach.** Drawn in `I` with its far end absent, hanging off `I.7` and `I.12`. Which level and from which direction is deferred by the stub itself, and naming it settles by side effect which of three closed regions has a hole in it. **Resolves at `I`'s step 9 pass or by direction before it.**
- **Peak 2's declared descent into `J`.** `GB`'s region Connections claim it; no `GB` stub carries it, where `FB.14` and `HB.19` carry the other two peaks'. Naming it means inventing a stub against a ratified count of twenty, so it sits in unnamed fill. **Whether to name it is `GB`'s to decide at step 9.**
- **`GB.14`'s one entry without a charge.** The Crown's own stair, `GC.13`→`GB.12`, gives it somewhere to go. **Which entry, and whether the stair explains it, is not decided and is not to be assumed.** `GB`'s and `GC`'s, at their own passes.
- **`GB.17`, the jailer's oath.** Two releases exist and one of them is a lie. Which lie, unwritten.
- **`GC.11`, who ordered the defacing.** Named as a revelation and answered as one — Vessa Rudgir, the Steward. Not yet written as a person: what she was, what it cost her, and what `GB.4` does to the account.
- **`HC.9`, the whispers.** One side of a conversation with somebody who is not Vekkut. Who, unwritten, and deliberately not answered at step 8. `HC.19`, the shaft they come down, is a leaf in `HC` and no edge at all in `HE`: nothing can travel it.
- **M3 must be repointed before the `Connections:` field can be dropped.** *Opened at `A`'s step-9 pass, alongside the ratified call in `DECISIONS.md`.* **Still open, and narrowed at the retiering:** M3 now reads the region's tier-4 diagram files rather than a mermaid block inside the region file, so the diagram half of the check is already repointed and the field half is not. `check.py`'s `_parse_location_connections_in_region` reads the `**Connections:**` field and nothing else; **step 12 removes that field** in favour of the `->` pointers inside feature entries. **The parser change and the field removal are one pass, not two** — either alone leaves the diagram unchecked against anything. Not a mechanical gap in the Notes and not a content question: a builder-phase task, recorded here so it is not discovered by a failing check. **Route `D`, and it is now named in step 12's gate**: the strike may not run until this is done, which is what turns it from a task nobody had scheduled into a precondition for shipping.
- ~~**The waystone crown mark.**~~ *Opened and answered at `B`'s step-9 pass. **It is the general device of an authority that no longer exists, and nothing in the module names it.** Not the King's mark, not connected to the defacing inside the hold, and no later region owes it a payoff — it is a sign of the decay the region has met with over the decades, sitting with the ruts, the gutter and the ledger. Written at `B.5` and `B.8`; no edge, no stub, no thread.*
- **`PEAK_3_BLOCK`'s Kelmor citation.** *Raised at `A`'s step-9 pass.* The thread list reads "`A.20` **Brannek Kelmor** — a party that buried him recognises him on the obelisk and can find his people's interment at `HB.7`." `HB.7` is the Runemaster gallery; the Guild gallery holding Kelmor is `HB.8`, as `HB`'s own stub says. `M1` cannot see this because both codes exist. **A one-code correction in a block document, proposed and not applied — `HB`'s ground.** *Direction received: leave it, documented.* The block's thread list now carries the dispute inline, marked, naming `HB.8` as the likely destination and `A.18`'s two Kelmor name-stones as the support, so `HB`'s pass meets the question on the ground that answers it. **`HB` owns both the correction and the alternative** — that the refugees' own people lie somewhere the Guild gallery is not. **Route `C`, and the note is already written** — the dispute sits inline in the block's thread list, which is exactly what `C` asks for; the item stays open until `HB`'s pass meets it.
- ~~**`D.6`, the drain outfall.**~~ *Written at `D`'s step-9 pass, as small as the direction asked.* `D.6` now carries **the other mouth**: a second opening forty feet downstream, underwater, older and rougher than the service drain, running hard cold water in weather that is giving the river nothing, and unenterable from this side against the flow. **No edge, no code, no answer.** `J.9`–`D.6` stays one-way outward and drawn from `J`'s side only; `D`'s diagram is unchanged and `D.6`'s Connections field names only `D.5` and `B.4a`. The line states the phenomenon and says plainly that nothing in `D` explains it, that it is not evidence of anything larger, and that a Referee may answer it, use it once, or leave it standing. The missing grating is answered in the only way it can be from this end: it is not here either.

- **What broke the great doors, and threw the wall outward.** *Written at `E`'s step-9 pass and, by direction, left standing rather than ratified.* The evidence is on the ground and it is consistent: the leaves at `E.12` lie **outward** on the road with the hinge sockets torn out of the jamb, and all four fans of rubble at `E.1` lie outside the line of the wall. Whatever went through Girkel went through it from the inside. **No location names it, and none may name it by accident.** The next pass that meets the question is the first-level block, at `FA.1`, which is the same doorway seen from the other side; it may answer it, or leave it, and the direction so far is to leave it. *Nothing else in the corpus names an agent, and the History entry for the Descent does not either.*
- **The confiscation racks at `E.6`.** *Written and, by direction, left as it stands for now.* The registry counted, shelved and never sent up the carved stone tiles taken at the gate, and the racks in the back room are empty — the provenance of the tile at `C.1` and of the ones in the attics at `A.7`. **It adds no lock and no fourth tile application**, and it explains what a tile *is* without saying what one *does*. Not ratified: a later pass may narrow it or cut it, and the standing call that tiles gate sideways and never up is unaffected either way.
- ~~**Ashen is a woman, and the House rod is carried by one of the two crew who read runic.**~~ *Route `E`, **ratified by direction** at the route-A sweep's batch and recorded in `DECISIONS.md`. The content was already written at `E.7`; only the call was missing.* Written at `E.7` and recorded here because the Creatures field's wording — *one carrying a House rod he cannot identify* — was preserved exactly and a later pass should not undo that by accident.
- ~~**`E`'s Treasure field said "Nothing concentrated".**~~ *Flagged under rule 17 and **approved by direction.** The field reads *nothing concentrated except by weight*, because `E.4` is a shed of metal that needs mules and `E.5` is a packed cellar, and both sit on the same hill so the choice is forced. The answer lives in `E`'s Treasure field.*

- ~~**The naming and the calls made at `D`'s step-9 pass.**~~ *All four answered by direction and ratified in `DECISIONS.md`: the garrison at `D.2` was killed by the hold's own people at the Descent, two years after the courier; the toll at `D.8` has two numbers and only the small one is ever quoted; Vashek, Halvard Grellick, Emmet Tarr and `Brynost` stand as written. Nothing amends a closed region — the `C.9` satchel is described from `D`'s side only.*

---

## OPEN — RAISED BY THE STEPS 1–8 SWEEP

*Practice 2's reconciliation pass, run before step 9 begins anywhere. `scripts/check.sh` M1–M8 all pass; every item here is a judgement finding. The five contradictions the sweep raised were batched and **answered by direction** — they are struck below and the calls are in `DECISIONS.md`. What remains are the watch items, each naming the pass that owns it. J2 was not run: it is a closing check and belongs to each region's own step-9 pass.*

***Route `C` throughout.** Every remaining item is a watch with a named owning pass, and one — rumour 8's sleep cycle — had no owner and is given one below.*

**Truths**

- **"Royal names open what nothing else will" has a teaching site and no lock.** `GC.9` and `GC.10` teach that royal names are collectable and that the King's is not a master key. No location anywhere is opened by a royal name; the two name-opened locks in the module, `FA.22` and `HB.15`, are both non-royal. **`GD`'s Royal sub-vaults and `HB`'s royal gallery at their step-9 passes.**

**Rumours**

- **Rumour 8's sleep cycle is neither confirmed nor falsified.** *Owner: `GE`'s step-9 pass, assigned at the route-A sweep, which found this the one item in the section carrying no owner at all.* **`GE` is where the Dragon is and is the only pass that can settle a cycle without settling it by side effect from outside.** *He sleeps a year at a stretch and wakes for a year.* `GE` and `PEAK_2_BLOCK` give three wake triggers and no cycle. Rumours 1 and 12 are marked wrong in Vermakith's faction Knowledge; 8 is not, and the Lizardmen's "roughly how long the Dragon has been asleep" does not settle it.

**History**

- **The Driving Down's obelisk trace is half-placed.** *The first King's is the first name cut on the black obelisk.* `HA.5` exists and is the name-index; nothing states the first cut, and the first King is unnamed anywhere. Against Truth 1 — Clan Azkelith "now largely unwritten in the upper halls" — this is a hook rather than a hole. **`HA`'s step-9 pass.**

**Factions**

- ~~**The Hobgoblins' lean-season raid on Thornhaven has no site in `A`.**~~ *Answered at `A`'s step-9 pass: **it stays unsited, on purpose.** Thornhaven is the module's only SAFE region and nothing attacks a party inside it. What was missing was not a site but a trigger, and that is now written into the Hobgoblins' faction entry as a Referee ruling — the toll drying up, a hard winter, a loss at the crossing to make good, or word that the town's fighting strength has walked up the road — with the outlying holdings as the target and the town hearing about it rather than fighting it. The timing is recorded in the outline's Unanswered Questions as a Referee call. No stub, no Events result, no Hobgoblins in `A`'s Creatures field.*

**Bestiary**

- **`HD` names its creatures as "Constructs"**, which is a category rather than an entry. `Automaton` and `Living Statue` both exist; `HD.8`'s trial post is neither yet. **`HD`'s step-9 pass.**

---

## OPEN — DELIBERATELY, AND STAYING THAT WAY

*These are answered by being unanswered. They are listed so that a later pass does not "fix" them.* ***No route, and never one.***

- **`HB.6`, Baldrun Azkelith's empty interment.** The last unanswered question in the module. `GC`, `HB`, `I` and `J` have all been drawn and none of them answers it.
- **`J.24`.** Unanswered on purpose.

## OPEN — RAISED BY WIRING IN THE DESIGN PATTERN CATALOGUE

*The catalogue landed as `DESIGN_PATTERNS.md` and `patterns/`. What it decided is in `DECISIONS.md`; what it assumed without confirmation, or named and did not build, is below. Its own reasoning is archived at `archive/DESIGN_PATTERNS_HANDOFF_at_harvest_close.md`.*

**Booked passes — work with a name and no date.**

- **The `A`–`E` retrofit to the three location forms.** *Owner: a pass of its own, before the builder phase.* The five closed approach regions were written before `HIGH`/`MEDIUM`/`LOW` existed as forms, and the forms bind only from `FA`/`GA`/`HA` forward. Ruled: retrofit, but separately, so that this pass stayed additive. They are read against: the form each location should take by feature count and Overview length; **`LOW` may not contain a find**; the adjacency floor of no more than two consecutive locations sharing a weight class; and the `HIGH` cap of one per ten, maximum two. **`A` is the region most likely to move**, at twenty locations with one honestly `LOW` entry. **Route `B`, applied per location under a `D`-shaped audit** — *a named exception to route `D`, ratified at the route-A sweep and recorded in `DECISIONS.md`.* The audit reads every written location against the four constraints above and changes only what violates one; it does not regenerate. **Sequenced before `FA`/`GA`/`HA`** by direction, because these five are the worked examples every later step-9 pass opens, and an example that is wrong teaches wrong. It runs *after* the predicates exist, so that the audit is checked rather than eyeballed.
- **The checker.** *Owner: a pass of its own; nothing of it is written yet. Route `E` then `D` — **and it is now a hard block**, ratified at the strike pass: no further step-9 region is opened while the backlog is non-empty, so `FA`/`GA`/`HA` waits on it.* ~~*Two things must land before any predicate does: a severity concept, and one shared location-entry parser — the field grammar this item says it is blocked on.*~~ ***Both landed at the checker foundation pass.*** `check.py` now carries `ERROR`/`WARN`/`REPORT` in the registry, a `Location` grammar parsing all 393 entries — 66 written, 327 stubs, with `written` stated once rather than buried in `M8` — and a `--repo` override so fixtures are possible. **The unblocking is done and the predicates are not**, which is what keeps this item open. The backlog is in `RECONCILIATION.md` under `MECHANICAL — NOT YET BUILT`. Build order: the structural and pointer checks first, because they are exact, catch the most common real failure and need no judgement; then the mode-conditional checks, which need the region header parsed; the document-level checks last. **The pattern-conditional predicates are deliberately not in that backlog** — they are judgement checks at J11 and stay there.
- **The trope pass.** *Owner: **step 10, the decorator phase**, ratified at the strike pass. Route `D`.* It had no owner at all, which is why nine inventories were written and none spent; step 10 was one sentence long and is now the step that spends them. **Still open**, because step 10 has not begun anywhere — what closes this item is the first decorator pass, not the naming of one. Every cell file ends with a `FOR THE TROPE PASS` section naming where classic furniture would land and under what constraint. Nothing was inserted. Two cautions to carry: a `HIGH` location carries **one** central mechanism, and a `WILD` region carries **one** lethal off-road site — three means leaving the road is forbidden rather than chosen.

**Assumptions in the catalogue that may want revisiting.**

- **`WILD LOW` "does not exist as locations" rests on one worked WILD region.** *Owner: the first WILD step-9 pass after the approach.* The module has six WILD regions — `B`, `C`, `D`, `E`, `I` and `J` — and the conclusion was drawn from one. `C`, the goblin camps, and `J`, the lost caverns, are the two most likely to want keyed thin locations. **Check the file against them before treating it as binding, and revise the file rather than follow it if they disagree.**
- **Mode is a property of the region, not the location.** One exception is already live: a boundary location may belong to two regions of different modes, with identical edges at both ends. If more appear, mode may need to become a per-location field with the region carrying a default.
- **`Extent` and `shared node` have no template slot.** Both are named in tier one as things the grid does not capture — a location may occupy six rooms or run under half a region — and both are currently stated by convention in the Referee Overview. If a checker ever needs them structured, they need a home. Same shape of problem as the pattern tag, which was ruled to have no slot at all.

**The four unmarked rumours.** *Opened when the truth-marker scheme was adopted. Sixteen of the twenty carry `(T)`, `(P)` or `(F)`; these four carry nothing, because each rests on a question the module has not answered and a marker would settle it by side effect. **The blank is the honest state and is not a defect** — `RECONCILIATION.md` names it as a warning, never a failure.*

- ~~**Rumour 4 — the lance that killed a dragon once, and will do it again for the right arm.**~~ *Route `A`, struck at the route-A sweep. **The answer is that it is not a question**, and it was ratified as such when the truth-marker scheme was adopted: `DECISIONS.md`, `## THE DESIGN PATTERN CATALOGUE` — "rumour 4, the lance, stays unmarked permanently, because its properties are a Standing Mystery." The other three here wait on a pass; this one waited on nothing and was carried as open for want of anyone striking it. The lance's properties stay `[setting]` in `outlines/10_STANDING_MYSTERIES.md`, and marking the rumour would fix them, which is the whole reason for the blank.*
- **Rumour 7 — the far guard booth at the river crossing is manned again, and they are charging.** *Owner: `D`'s step-9 pass.* Whether the far booth is occupied, by whom, and whether a toll is actually being taken is `D`'s to write. The rumour is marked once it is.
- **Rumour 9 — kobolds hold the granaries under the first peak and would rather trade than fight.** *Owner: `FB`'s step-9 pass.* The tribe is written and the trade posture is broadly right, but the contender, the old guard and the undeclared reserve are `FB`'s business, and "would rather trade than fight" is exactly what that pass decides how far to honour.
- **Rumour 15 — the third peak was never touched.** *Owner: Peak 3's block pass.* This is the largest of the four. `H` is the peak the module holds back, and marking this rumour either confirms or denies the premise the whole peak is built on. **Not to be marked in passing by any region pass that merely touches `H`.**

**Named and not settled.**

- **The mine and quarry source material was never supplied.** The `CONNECTIVE` gap was closed from *The Hole in the Oak* instead — the noun-phrase headline form and the directional sense-cue rule — and the original request for real mine workings, haulage ways and underground industrial architecture was withdrawn as unnecessary. **If the deep levels want an industrial texture the current files do not supply, that source request is still open.**

**Techniques noticed and not yet used. Not tasks; candidates.** ***No route.** These are not questions and nothing is waiting on them; they are here so that a pass looking for a technique finds one it already owns. Two have been struck as having gone where they were going.*

- **The single-character sighting.** One player sees the thing and the others do not. A one-clause technique that produces table behaviour nothing else does. Used nowhere in Drakenhold.
- **An unreliable informant must be right once**, or the players simply discount them and the source is wasted. Drakenhold has unreliable sources; **check that at least one has a verified truth attached.**
- ~~**Ambient-to-actionable ratio on event and encounter tables.**~~ *Route `A`, struck at the route-A sweep. **It already went where it was going**: 15–35% across two independent sources, and it sits in `RECONCILIATION.md`'s predicate backlog as **report-only**, which is the disposition a soft target should have. It is the checker pass's to implement and nothing about it is undecided.*
- **The Danger, Encounter and Events tables are state machines, not draw tables.** The `DANGEROUS` countdown from 6 escalating to *the way back is gone* is better than anything in the corpus, and predicates written against random-draw tables do not describe it. **Anything written about table composition elsewhere should be re-read against this.**
- ~~**Sub-lettering.**~~ *Route `A`, struck at the route-A sweep — **the correction it asks for was the pass that wrote it**, and what remains is a fact rather than a question.* The catalogue claimed two live instances and there is one: `B.4a`, the drain outfall, load-bearing and closed at `D.6` and `J.9`. The other code it cited is the template's own illustrative example and names nothing. **Recorded so nobody prunes the real one for tidiness**, which is the only reason the line survives at all.

---

## OPEN — MECHANICAL DEPENDENCIES

*Raised against `Rules_Light_TTRPG_Design_Notes.md`. Answered in the rules project, never in a region file. Answers received are written into `DECISIONS.md`.* ***Route `F` entire — this section is that route.***

*The four gaps raised after step 8 — the light rule, Rest inside a DANGEROUS region, Weather on the span, and the Danger Die's reset — are all answered. See `DECISIONS.md`. Three proposals are open.*

**The test these are held to, and the test anything else must pass:** a one-off procedure earns its place where **the players are already keeping score in their heads and the procedure only makes the scoring visible.** Bloat is a procedure that tracks something the table was not already tracking. All three below are proposals for the rules project. **None of them is written, and none may be written into a region file.**

*Narrowed at the trope content pass, by direction, and the sentence above is left standing because it is still true of everything in this section.* **What was narrowed is its reach, not its content:** a table that only supplies colour — what is on the board, who is drinking, what forages in a clearing — scores nothing, is content rather than procedure, and **may now be written into a location or region description.** A table that keeps state, escalates, or asks the players to hold a number is a procedure and still belongs here. The dividing line and the two mechanical constraints on a region-file table are ratified in `DECISIONS.md` under *Trope Content*.

- **Buying the warrens.** `DECISIONS.md` records the standing call for the three arteries: *no landmark system, no service marks, no mechanic — a sheer numbers game of twisting paths and trying to keep track.* That call stands and this does not overturn it. But the survivors' stated advantage is **thirty years of memory a party cannot buy** — which is precisely the thing a party will try to buy, and there is no procedure for what a bought or coerced guide is worth, what a wrong guide costs, or what happens when the guide leaves. The table will want that negotiation scored. **Proposed as a rules-project question, not a mapping system.**
- **The `HD` circuit.** A closed ring, no chord, an attempt imposed at every segment in either direction, with the rod that opens `HD.11` at the far end of it. It is already a mini-game in everything but name and the fiction is fully built. What it lacks is a stated order and a stated cost for a failed segment. **The smallest of the three, and the one players will most visibly engage with as a system.**
- **Weight against the way out.** The module's spine is extraction, and the Notes carry Encumbrance as slots. Every treasure decision here is a slot decision made hours from the door, and the earned rod at `HD.10` already **buys a way back out rather than treasure.** A light procedure for hauling under load back through a region already crossed — not a new subsystem, only what the existing slots cost on the return leg — would make the module's central tension mechanical instead of implied. **The largest in scope and the one most worth getting right.**

**Deliberately not proposed:** any further scoring of the light rule. It works because it is three states and a Referee call, and `J.6` teaches it without a table.

---

## OPEN — RAISED BY THE TROPE CONTENT PASS

*The pass added sixteen Bestiary entries and authored the setting outline's Treasure, Traps, Graffiti and Procedural Tables sections, plus `LORE_INDEX.md`. **By direction it edited no region file.** What follows is therefore a register of recommendations addressed to each region's own step-9 pass, not a set of instructions. **A recommendation here is not a decision** — the owning pass takes it, refuses it, or improves it, and records which.*

***Route `C` for every recommendation** — each is addressed to a pass that has not run, and it closes when that pass takes or refuses it. The three placements that need direction rather than a pass are route `E` and are in this pass's question batch. The three items at the foot carry their own tags.*

*The register exists for one reason. `DECISIONS.md` and this file both record that an unused Bestiary entry is a tracked defect: three entries once sat unplaced until the steps 1–8 sweep found them. **Sixteen new entries could not be written without saying where each one goes**, so each has a named home below.*

**Bestiary placements — recommended, per owning pass.**

- **`Giant Rat`** → `FB`. Thirty years of spoiled stores is the reason the entry exists; the granaries are the reason the party is there.
- **`Cave Bear`** → `FA`. Came in through the broken doors, denned in a side chamber, and is a hazard of the threshold rather than of the hall. One entrance is the whole encounter.
- **`Giant Bat`** → `I` and `HA`. The Skybridge's high vaults and `HA.32`'s vent gallery. **Flame-killing in a place where light is the resource** — this is the entry's real function and it should be placed where a party is carrying open flame.
- **`Sootwing`** → `FD`. The forge flues are warm and the entry needs warm flues.
- **`Bugbear`** → `FB` or `J`. The far post of a warren, behind the smaller things.
- **`Ostmor`** → `J`, with `FB.12` as the shallower instance. The flooded workings after the pumps stopped is the fiction the entry was written from.
- **`Brynkar`** → `I`. Parapet and cornice work on the span, indistinguishable from the roof-work until it moves, and it does not follow anything indoors — which makes the span itself the trap.
- **`Sigkar`** → `FC`. The region already teaches the tiles and the rods; a post that challenges three times before it strikes teaches that a dwarven guardian is a condition rather than a monster.
- **`Drowned`** → `FB`. Whatever went under when the stores flooded.
- **`Unnamed Dead`** → `HB`, with `HA.6` as its clue site. **This is the strongest of the sixteen and the one most worth getting right.** Every other wraith in the module is levered with a name; this one has had its name taken off every surface and cannot be reached at all. The struck names at `HA.6` are the evidence and the crypts are where it is met. **`HA` and `HB` own it jointly and neither should place it alone.**
- **`Grave-Crawler`** → `HB`. Worked up into the tiers through whatever the flooding opened.
- **`Glass Ooze`** → `J`. A corridor-filling mass whose contents are still worth carrying is an Encumbrance problem wearing a monster, which is `J`'s whole register.
- **`Rust-Eater`** → `FD`. A hold built on iron, and a creature that destroys what a party carried in rather than what it came for.

**Bestiary placements that need direction rather than a pass.**

- ~~**`Orc`.**~~ *Routed by direction to **the `A`–`E` audit**, which is the pass that opens those regions anyway and is already booked ahead of `FA`/`GA`/`HA`. Written as the Hobgoblins' hired spears, natural home `B` or `D`, both closed — and the audit is the one pass entitled to revise a closed Creatures field, because that is what it is for. **The entry is not cut and is not left unplaced**; it is the audit's to site.*
- ~~**`Ghoul`.**~~ *Routed by direction to **the `A`–`E` audit**, the third of the alternatives as written. Its natural home is `E`, which is closed; the audit opens it. **The Girkel-is-quiet-at-night line is kept** — moving the fiction to `HB` was the option that cost it, and that option is not taken.*
- ~~**`Wearer`.**~~ *Answered by direction, and answered at the rumour rather than at the placement: **rumour 10 is re-marked `(P)`**, and the `Wearer` is placed in `HA`/`HC`'s service warrens by those passes — route `C` from here. The reasoning given: it is one fact that applies in two directions, which is what the partial marker is for and is the rumour table working as designed. Expanding the partial set is free; only the true set is constrained. Ratified in `DECISIONS.md`; the marker is changed in `outlines/02_RUMOURS.md`.* The collision as it stood. Rumour 10 was marked **`(F)`** — *"Every dwarf in Drakenhold is dead. Whatever you hear moving in there is wearing them."* Placing a shape-taking creature anywhere makes the second sentence of a false rumour true, and `DECISIONS.md` holds that the true set is the one constrained. **The marker may be correct as it stands** — the rumour's false half is *every dwarf is dead*, which survives — but that is a call about the rumour scheme and belongs to whoever owns it, not to a placement. *Alternatives: place it in `HA`/`HC`'s service warrens and leave rumour 10 at `(F)`; place it and re-mark the rumour `(P)`; or cut the entry.*

**Trap placements — recommended.** The catalogue is in the setting outline and every entry is `MEDIUM` or above by construction.

- `HB` — the counterweight grave-trap is already named at `HB.9` and the catalogue entry is written to it.
- `FE` — the rod-locked strongbox is already named at `FE.6`, likewise.
- `GD` — the proximity ward is already named at `GD.9`, likewise. **These three are descriptions of what the region files already say and are not new content.**
- `FC`, `FD` — the false floor over the works, where the vents still run.
- `GB`, `J` — the flooded step, and the alarm that is not a trap.
- `GD`, `FE` — the lock that records. **A trap whose whole effect is that the attempt is written down, in a module about ledgers.**
- `HB`, `GD` — the covered pit, the dart volley, the falling block, the cascading sand, the poison needle. Placed where a level was secured against robbers, which is what these levels are.

**Treasure-type placements — recommended.** Each region's existing prose `Treasure:` field stays authoritative and is not replaced by a type number; this maps the field onto the tables so a Referee improvising in that region rolls on the right one.

- Type I everywhere, and it is the default. Type I is what a body carries.
- Type II — `FC`, `FD`, `GB`, `FA`. Workshops, forge, barracks, trade hall.
- Type III — `E`, `FA`, `GD`, `HA`. Note `E.4` and `E.5` already teach the heavy end of this table on the way in and should be left as the teaching site.
- Type IV — `GD`, `FE`, `HB`, `GB`, `C`. Every one gated, every one with a stated reason for surviving.
- Type V — sparingly, and `HC`/`HE` first. **The lance is not on this table and is not reachable from it.**

**Procedural tables — recommended, at region level.** The five setting-level tables are written. Each below is offered to its region's pass and none is written.

- `A` — the two inn tables are setting-level and sited here; `A` may take them by reference rather than restating them.
- `B` and `C` — the clearing forage table, which is **locked to these two regions** and is the whole of foraging in the module.
- `C` — the midden table, which extends the existing negative-find bullet rather than replacing it.
- `J` — the dark forage table, **locked to `J`**. Its glowing-fungus result is written to be refused by the light rule rather than to weaken it.
- `J` — additionally, a table of what the dark has done to a stretch of gallery since it was last crossed. **Colour only. The moment it counts anything it is the depth crawl below and is not written.**

**Open items.**

- **The treasure taxonomy diverges from the Notes.** *Owner: the rules project.* `Rules_Light_TTRPG_Design_Notes.md` reads II Foraged Goods, III Caches, IV Hoards, V Unique Treasures. The setting is written to II Equipment and Armaments, III Luxury and Trade Goods, IV Caches, V Magical Baubles, ratified by direction and recorded in `DECISIONS.md`. **The Notes are read-only here and this repo does not amend them.** Raised so the next upload closes the gap; until it does, the divergence is deliberate and documented. ~~*Foraged Goods have no table in the setting under the new taxonomy — whether foraging keeps a treasure type or becomes a procedure is part of the same question.*~~ *Answered by direction: **foraging is a procedure, not a treasure type**, and it is region-locked to `B`, `C` and `J`. Two d6 tables are written into the outline's Procedural Tables section and nothing a party forages is worth a slot on the way home. The rules-project question narrows accordingly — it is now only whether the Notes keep a Type II slot for Foraged Goods at all.*
- **The Horror depth crawl.** *Owner: the rules project. Proposal only, and it is not written.* A short procedure for how the Drakmorith reshapes and closes the ground behind a party — a corridor that has gained a turn, a door opening from a side the room does not have, and the way back going progressively wrong. The fiction is fully built in the Bestiary entry and in `HE`. **It fails the test in the section above as things stand**: it would ask the players to hold state that nothing currently asks them to hold, which is the definition of bloat given there. *It is recorded because the alternative reading is arguable — a party in a Horror's reach is already keeping score of the way out, and the procedure would only make that scoring visible, which is exactly the ground the light rule was ratified on.* Answering it either way is a rules-project call and not a region's.
- **`LORE_INDEX.md` into the checker corpus.** *Owner: a pass of its own, after one full region has been closed against it.* The file is outside `scripts/check.py`'s `_CORPUS_FILES` on purpose while its rows are still settling; adding it puts every pointer under M1 reference integrity, which is where it should end up. **The risk to watch is the one `HANDOFF.md` names** — an index that grows into a fifth place the truth lives. If a later pass finds rows carrying content rather than pointers, the file is cut back before it is wired in.

---

## OPEN — RAISED BY THE EDITORIAL MARKUP AND OUTLINE SPLIT PASS

*The pass that added the `(SECTION, key)` and `[[ ... ]]` marks and split the setting outline into `outlines/` also asked what shape the deliverable is in. It decided the notation and it did not decide the shape. **Nothing here is answered by the pass that raised it.***

***Route `E` throughout, and this is the section most in need of it.** None of these is a content gap; every one is a call about the shape of the deliverable, and each will stay open indefinitely until it is made — no pass will arrive that answers them by side effect. Two are in this pass's question batch.*

**Open items.**

- ~~**Is the setting relational diagram one document or three tiers?**~~ *Answered by direction, and answered past the three options as written: **(c)**, consolidated into `diagrams/`, one file per diagram — and **five tiers, not three**.* Tier 1 is the setting and shows the region blocks; tier 2 is a block and shows its regions; tier 3 is a region and shows its location groups; tier 4 is a location group and shows its locations; tier 5 is the location itself and has no diagram. Each tier draws **only the tier below it**, and **connection type is drawn at tier 4 and nowhere else** — above it, two connected children get one plain untyped edge however many typed routes run between them. A tier-4 edge that leaves its group draws the destination location outside the frame, which is the only duplication the layer permits. **Tier 4 is authored and tiers 1 to 3 are derived from it** by `scripts/diagrams.py --write`; `M11` re-derives them and fails on drift, so every fact about the graph is written down once. Host documents carry a marker line and the PDF and web builds splice the file back into place, which is what defeats (c)'s stated cost: no argument is split across two files, because the drawing arrives inside the prose that explains it. **The thirty-two inline diagrams are now 107 files and no diagram is drawn twice anywhere in the corpus.** `S`, the deep cells, the observation rooms and the niche are gone as nodes — they were abstractions the old overview needed because it had nothing below it to resolve into.
- ~~**Do the blocks become published parts, or stay authoring instruments?**~~ *Route `E`, **answered by direction: (c)** — the blocks publish as they stand, under thematic names. The three-tier hierarchy is a reading structure as well as an authoring one. **The cost was named when the option was written and is now paid rather than accepted**: the twelve pass-shaped headings lose their `PASS N — ` prefix at step 12, which leaves `MAJOR ROUTES` and `LANDMARKS AND ROUTES` in front of a reader and is removal rather than rewriting. See `DECISIONS.md`.* The original three options, kept for provenance. *Owner: the same pass.* `PROCEDURES_AND_RULES.md` item 14 defines a block as a connective document holding what belongs to no single region, and its headings are pass-shaped — `PASS 1 — MAJOR ROUTES`, `PASS 3 — LOCATIONS`. They are published to the web view today under file-name labels. Three answers: **(a)** blocks stay authoring instruments and come out of the published site, which is the cleanest reading of what they are; **(b)** blocks become named parts of the deliverable — `BOOK I: THE APPROACH`, `BOOK II: PEAK 1`, and so on — which requires giving each one reader-facing structure and a register, and is a real writing job, not a rename; **(c)** blocks publish as they stand under thematic names, which is (b)'s label without (b)'s work and leaves pass-shaped headings in front of a reader. **The three-tier hierarchy — setting, block, region — is sound as an authoring structure; the question is whether it is also a reading structure.**
- **What fits in none of the three tiers?** *Owner: the same pass.* Named candidates, each of which is currently a file with no tier: `LORE_INDEX.md`, which spans regions and is a register rather than content; `Setting_Playbook_Template.md`; `DESIGN_PATTERNS.md` and `patterns/`; `RECONCILIATION.md`. The first is the only one that carries play-adjacent material, and it has its own open item above.
- **Should `[[ already: ... ]]` be a checked reference instead of an editorial note?** *Owner: whichever pass first needs it.* As an editorial note it is struck at step 12 and nothing ever verifies the claim it makes. The alternative is a checked token so `M9` can confirm the thing it says already exists actually does. **The note form is what is ratified now**, on the ground that the claim's far end is usually a section or a diagram rather than a nameable entry — but the first pass that writes several of these should say whether that held.
- **`LORE_INDEX.md` rows have no stable ids.** *Owner: the same pass as the item above about wiring the file into the corpus.* `(LORE, key)` resolves on the item's name, because names are what the register carries. Names are also what gets edited. If the file is wired into the checker corpus, giving each row a stable number — and referencing `(LORE, #37)` — is the cheaper form. **Not done now**, because numbering a register whose rows are still settling invites renumbering.

---

## OPEN — RAISED AT THE TABLE

*Step-11 intake. **Empty, and correctly so — no session has been run against this material yet.** The section exists ahead of the first playtest so that the first one has somewhere to put what it finds, rather than inventing a place under pressure.*

*What lands here: an observation with no place in the corpus to attach a `[[ playtest: ... ]]` note to, and any note `J13` has promoted. Each item names **which region and which session**, records **what happened rather than what to do about it**, and carries a route like every other item. **One table is not a finding** — an item here is a fact about a session until a second table or a failing judgement check makes it a fact about the module, and the item says which it currently is.*

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
