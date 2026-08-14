# RECONCILIATION

*Run before a region closes, and again as a full sweep across steps 1–9 before the builder phase begins anywhere. "Reconcile" without a list becomes "reread and feel fine about it," which is why this is a list.*

Two kinds of check. **Mechanical** checks are scripted, run every pass, and take no judgement — a failure is a fact. **Judgement** checks are read by a person and by Claude, per region, and a failure is an argument.

---

## MECHANICAL — `scripts/check.sh`

**M1 · Reference integrity.** Every location code appearing anywhere in the corpus (`FA.17`, `GA.19`, `HE.10`) resolves to a stub that exists. Dangling references fail.

**M2 · Connection symmetry.** Where `X` names an edge to `Y`, `Y` names the edge back — unless the edge is explicitly typed one-way. Asymmetry without a one-way type fails.

**M3 · Diagram agreement.** Every edge in a region's connection bullets appears in its diagram, and every edge in the diagram appears in some entry's bullets. Diagrams are authoritative; the bullets are what gets corrected.

**M4 · Budget and ratio.** Stub count against stated room budget, at roughly half. Region totals against block totals. Flags drift rather than enforcing a number.

**M5 · Table conformance.** Classification matches table type — SAFE→Events, WILD→Encounters, DANGEROUS→Dangers. Danger tables count 6→1; all others ascend. Six entries.

**M6 · Vocabulary.** Every dwarven proper name decomposes into roots recorded in the setting outline. An unrecognised root fails, because roots are proposed rather than coined.

**M7 · Format.** Headings, field names and entry formats match `Setting_Playbook_Template.md`. Required fields present, including those stating "None." This is what makes scripted assembly possible.

**M8 · Struck notes.** No working note survives in a location whose Overviews and Features are written.

---

## JUDGEMENT

**J1 · Open items.** Every item this pass touched, checked against the Unanswered Questions in the setting outline and the open items in the handoff. Items resolved are struck with a note saying where they were resolved. Items newly opened are recorded. **Nothing is resolved silently and nothing is resolved by assumption.**

**J2 · Demotion.** The region's step-5 fields read against its locations. Anything true of one named location is pushed down into that location; what remains is what applies to the region entire. Fields narrow as the region develops — a field still carrying location-specific detail is a defect, not a redundancy.

**J3 · Clue chain.** Rule 10: clues to hidden and secret detail always exist. For every secret in the region, at least one clue exists, and at least one of those clues lives **outside the location holding the secret**. A secret discoverable only by standing in the room it is in is not a secret; it is a search roll.

**J4 · Connections.** Beyond the mechanical check: does every gate still have an answer that is not the gate, and is the answer priced — longer, darker, or watched by something worse? Does the region still have more than one route to most places? Can a party lose the way?

**J5 · Creature placement.** Every creature named resolves to a Bestiary entry, and what is specific to *this* group — what they guard, carry, know, or are currently doing — is stated in the location rather than the Bestiary. Unique NPCs are inline. Check the region is not carrying a monster it does not need, and is not empty of consequence where the tables promise one.

**J6 · Treasure placement.** Distribution across the region and against the module — weight, portability, and what taking it costs socially. Treasure with an owner, a witness or a count attached is doing more work than treasure without. Check the region is not uniformly rich or uniformly bare.

**J7 · Show don't tell.** *The heaviest check, run last, on player-facing text only.*
- No player-facing text states a conclusion the player should reach. Not "the room feels dangerous" — the thing that makes it so.
- Every hidden route exists as a describable object with a mechanism, searchable by a player who does not know it is there.
- Every creature that patrols leaves signs: sound, wear, smell, schedule, something moved.
- Every historical layer is legible from a physical trace, not narrated.
- Anything the player cannot see, touch, hear or ask about is not yet real. Write it or cut it.

**J8 · Register.** Player text lyrical and questioning; Referee text plain, bounded and spatially precise, with measurements and cardinal directions stated. **Architect voice appears nowhere.** Drift here is gradual and invisible from inside a single region, so it is checked against a region closed several passes earlier rather than against itself.

**J9 · Negative space.** Roughly a third low detail, a third medium, a third high — or a third combat and hazard, a third puzzle and conundrum, a third connective tissue. Rooms may be empty. A region where everything is interesting has no landmarks.

---

## THE FULL SWEEP

Before the builder phase begins anywhere, steps 1–9 are read back through as one body of work rather than region by region. The additional checks at that scale:

- **Truths hold.** Every Truth in the setting outline is honoured everywhere it applies, and no region has quietly contradicted one.
- **Rumours point somewhere.** Every rumour resolves to something that now exists, or is deliberately false and marked as such in the author's record.
- **History leaves traces.** Every History entry's stated trace exists in a region or a location.
- **Factions have somewhere to act.** Every faction's Goals are actionable against real locations, and relations are cross-referenced to rumour numbers.
- **The Bestiary is used.** Every entry appears somewhere; every creature named anywhere has an entry.
- **Threads land.** Every cross-region thread in every block document is live at both ends.
