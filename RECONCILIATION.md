# RECONCILIATION

*Run before a region closes, and again as a full sweep across steps 1–9 before the builder phase begins anywhere. "Reconcile" without a list becomes "reread and feel fine about it," which is why this is a list.*

*The judgement checks are ordered by weight and not by number. **`J13` is new and runs before `J7`**, because a playtest note changes what the show-don't-tell read is looking for; it is numbered last because the earlier numbers are cited elsewhere and renumbering them would break those citations for no gain.*

Two kinds of check. **Mechanical** checks are scripted, run every pass, and take no judgement — a failure is a fact. **Judgement** checks are read by a person and by Claude, per region, and a failure is an argument.

---

## MECHANICAL — `scripts/check.sh`

**M1 · Reference integrity.** Every location code appearing anywhere in the corpus (`FA.17`, `GA.19`, `HE.10`) resolves to a stub that exists. Dangling references fail.

**M2 · Connection symmetry.** Where `X` names an edge to `Y`, `Y` names the edge back — unless the edge is explicitly typed one-way. Asymmetry without a one-way type fails.

**M3 · Diagram agreement.** Every edge in a region's connection bullets appears in one of the region's tier-4 diagrams, and every edge those diagrams draw with an end in the region appears in some entry's bullets. Diagrams are authoritative; the bullets are what gets corrected.

**M4 · Budget and ratio.** Stub count against stated room budget, at roughly half. Region totals against block totals. Flags drift rather than enforcing a number.

**M5 · Table conformance.** Classification matches table type — SAFE→Events, WILD→Encounters, DANGEROUS→Dangers. Danger tables count 6→1; all others ascend. Six entries.

**M6 · Vocabulary.** Every dwarven proper name decomposes into roots recorded in the setting outline. An unrecognised root fails, because roots are proposed rather than coined.

**M7 · Format.** Headings, field names and entry formats match `Setting_Playbook_Template.md`. Required fields present, including those stating "None." This is what makes scripted assembly possible.

**M8 · Struck notes.** No working note survives in a location whose Overviews and Features are written.

**M9 · Editorial references.** Every `(SECTION, key)` token resolves to a field that exists.

**M10 · Editorial notes.** Reports every surviving `[[ ... ]]` during authoring; fails on them under `check.sh --final`, **which is now step 12's acceptance test rather than a mode anyone may pass in the middle of a pass**. It counts notes and does not read them — **`J13` is what reads them**, and a `[[ playtest: ... ]]` note must be routed there before this check is allowed to go quiet.

**M12 · Pointer completeness.** Every code named in a written location's `Connections:` field also appears as an `->` pointer inside one of its features. **This is the precondition for step 12 dropping that field** — `HANDOFF.md` has required it since `A`'s pass and nothing verified it, so a missing pointer would have been an edge deleted silently, on a branch never merged back, in the one step that cannot be re-run. One-directional on purpose: it asks whether the pointers cover the field, not whether the field covers the pointers. Stubs are skipped — they carry the field and no features at all.

**M13 · Location structure.** A written location parses into exactly one Player's Overview, one Referee Overview and a Features block. A location carrying two of the three is malformed rather than written, and `M8`'s test could not say so.

**M14 · Pointer discipline.** `->` appears only in a feature's connection pointer. It matters more since the repoint: the pointer set is what `M3` reads, and after step 12 it is the only record a connection has.

**M15 · Shared-node parity.** A location belonging to two regions carries identical edges at both ends. The sharing is legal by ratified decision; the asymmetry is the error.

**M11 · Diagram tiering.** The five-tier diagram layer resolves end to end. Every stub is a member of exactly one tier-4 group frame in its own region; every location a tier-4 file draws outside its frame is a member of some other frame; a cross-group edge is drawn at both ends, unless it is one-way, which is drawn from the end it leaves; the tier-1 to tier-3 files match what `scripts/diagrams.py` derives from the tier-4 files; and every diagram file is spliced in by exactly one marker, with every marker naming a file that exists.

---

## JUDGEMENT

**J1 · Open items.** Every item this pass touched, checked against **`OPEN_QUESTIONS.md`, which is the single register.** Items resolved are struck there with a note saying where the answer now lives; struck items are never deleted. Items newly opened are recorded there. **Nothing is resolved silently and nothing is resolved by assumption.** The setting outline's Unanswered Questions is *not* a second register — it is referee-facing, it holds only what the module leaves open at the table on purpose, and adding to it is a deliberate act rather than a place to park work. A mechanical gap resolves in the rules project, never in a region file: record it in `OPEN_QUESTIONS.md`, raise it in the batch, and write the answer received into `DECISIONS.md`.

**J2 · Demotion.** The region's step-5 fields read against its locations. Anything true of one named location is pushed down into that location; what remains is what applies to the region entire. Fields narrow as the region develops — a field still carrying location-specific detail is a defect, not a redundancy.

**Demotion is automatic at a region's close and is not batched for direction.** *Ratified after `A`'s step-9 pass.* It is part of closing a region, not a proposal about one. What follows is the procedure that makes it safe, because the risk in demotion is not that it is done — it is that a clause is deleted from a field having never actually arrived anywhere.

**How demotion is run, clause by clause.**

1. **Split the field into clauses before editing anything.** Each sentence or bound phrase is one clause. Work the list, not the paragraph — a paragraph rewritten whole is where detail goes missing, because nothing was ever counted.
2. **Name a destination for every clause: a location code, or `region`.** A clause is location-specific if it is true of one named location and not of the region entire. A clause with no destination **stays in the field** — that is a correct outcome, not an unfinished one, and it is the reason a field may still carry detail after demotion.
3. **Write the destination first, then cut the clause.** Never the reverse. The clause is not removed from the field until its content is readable in the location text, in that location's register — which usually means it is rephrased rather than moved, and rephrasing is where a nuance is quietly dropped.
4. **Re-read the original field against the finished locations, from the pre-pass version in git.** Every clause is found, or it is restored. `A`'s pass ran this and it caught one loss: Wyla Fenn "living as a hedge-witch because she has nowhere else to be" had thinned to a date in `A.13`'s Referee Overview, and was put back.
5. **The ledger goes in the pass's commit message** — clause, destination, one line each. It is not a new file and it does not become a fifth place the truth lives. The commit is the record that step 4 was actually run, and `git show` is how the next pass reads it.

**Not mechanised, and deliberately.** No scripted check can verify this. Demotion rephrases prose between registers, so there is no text to match and a diff proves only that a field got shorter. The procedure above is the safeguard, and step 4 is the part that must not be skipped.

**Demotion runs *after* the destination exists, never before.** A field's detail is pushed down once the location that will carry it has been written, as part of closing that region — not audited out of the fields in advance of the pass that gives it somewhere to go. Moving material between midpoints before the endpoint exists loses it. **Until a location is written, a field carrying its detail is correct**, and the check does not apply.

**J3 · Clue chain.** Rule 10: clues to hidden and secret detail always exist. For every secret in the region, at least one clue exists, and at least one of those clues lives **outside the location holding the secret**. A secret discoverable only by standing in the room it is in is not a secret; it is a search roll. **And no secret is gated on a search roll anywhere in the module** — gates are physical: standing somewhere, clearing something, opening something, speaking a name, looking back. A `PUZZLE`'s solution chain carries no attribute check and no search roll at any link. Ratified; see `DECISIONS.md`.

**J4 · Connections.** Beyond the mechanical check: does every gate still have an answer that is not the gate, and is the answer priced — longer, darker, or watched by something worse? Does the region still have more than one route to most places? Can a party lose the way? **Where a bypass is cheaper in time, is its cost stated as what the party arrives *without*** — unpractised, unmet, burning light they will want later? The module never says which branch is the mistake, and both branches are costed.

**J5 · Creature placement.** Every creature named resolves to a Bestiary entry, and what is specific to *this* group — what they guard, carry, know, or are currently doing — is stated in the location rather than the Bestiary. Unique NPCs are inline. Check the region is not carrying a monster it does not need, and is not empty of consequence where the tables promise one.

**J6 · Treasure placement.** Distribution across the region and against the module — weight, portability, and what taking it costs socially. Treasure with an owner, a witness or a count attached is doing more work than treasure without. Check the region is not uniformly rich or uniformly bare.

**J13 · Playtest notes.** *Runs before J7, because a table observation changes what the show-don't-tell read is looking for. Applies only where step 11 has run; where no session has touched this ground, the check is nil and says so.*

Every `[[ playtest: ... ]]` note in the ground this run covers is read, diagnosed and **routed under the six resolution routes in `OPEN_QUESTIONS.md`**. A note leaves this check in exactly one of three states:

- **Resolved in place** — the fix is local and in scope. The content is edited and the note struck.
- **Promoted** — the note raises something not settled. It becomes an item in `OPEN_QUESTIONS.md` under `OPEN — RAISED AT THE TABLE`, with an owner, and the note is struck against that item.
- **Booked for regeneration** — the note is evidence that the step which produced this ground produced it wrongly. The owning step is re-run over that region or block as its own pass; the note stays where it is until that pass runs, and the register carries the booking.

**A playtest note is never deleted for being stale, and never struck to make `check.sh --final` pass.** M10 is a deletion gate with no judgement in it; this check is the judgement that must run in front of it. A note that survives to **step 12** unrouted is a failure of this check, not of M10 — the strike removes the mark, this check removes the question, and reaching the strike with the question still open means the gate was not satisfied.

**One table is not a finding.** A note that a party missed a clue is a fact about one party. It becomes a defect when the clue chain fails J3 on re-reading, when the far end was never placed, or when the same note arrives from a second table. **The check asks what the corpus already says, not what the players wanted** — a party that hated a gate is not evidence the gate is wrong, and may be evidence it worked.

**J7 · Show don't tell.** *The heaviest check, run last, on player-facing text only.*
- No player-facing text states a conclusion the player should reach. Not "the room feels dangerous" — the thing that makes it so.
- Every hidden route exists as a describable object with a mechanism, searchable by a player who does not know it is there.
- Every creature that patrols leaves signs: sound, wear, smell, schedule, something moved.
- Every historical layer is legible from a physical trace, not narrated.
- Anything the player cannot see, touch, hear or ask about is not yet real. Write it or cut it.

**J8 · Register.** Checked against the template's `STYLE` section, which is the authority. Player text lyrical and questioning; Referee text plain, bounded and spatially precise, with measurements and cardinal directions stated. **Architect voice appears nowhere.** The vocabulary rule and its one constraint apply: a precise term is preferred to an accessible one, and the term must be reconstructible from its own sentence. Load-bearing facts must survive paraphrase, because the Referee describes rather than recites. Drift here is gradual and invisible from inside a single region, so it is checked against a region closed several passes earlier rather than against itself.

**J9 · Negative space.** Roughly a third low detail, a third medium, a third high — or a third combat and hazard, a third puzzle and conundrum, a third connective tissue. Rooms may be empty. A region where everything is interesting has no landmarks. **This is a detail-distribution check and not a count of the `HIGH` form**, which is capped separately at one per ten locations, maximum two.

**J10 · The landmark promise.** *The module's most common real failure, and the cheapest to check.* **Every bolded noun in a Player's Overview appears below as a feature.** A noun given weight in the read-aloud and then absent from the Features block is a promise the Referee cannot keep at the table — the player asks about the thing and there is nothing to answer with. Either the feature is written or the bolding comes off.

**J11 · Pattern conformance.** *Run against `DESIGN_PATTERNS.md` and the region's cell files. These are judgement checks and not mechanical ones, because no pattern tag is authored and there is nothing for a script to read.* Each location is read against the ten patterns, and where one applies its discipline is checked:

- **`EMPTY`** — no find of any kind. The load-bearing variant carries exactly one remnant and no other feature.
- **`TRACE`** — the remnant is named in the present tense before any past-tense verb, and the past tense attaches to something currently touchable.
- **`HIDDEN CLUE`** — both ends exist, and the far end does not explain itself. An unplaced far end is recorded in `OPEN_QUESTIONS.md` rather than assumed.
- **`CACHE`** — states a reason it survived, and the reason is not solely a guardian.
- **`OCCUPIED`** — the want is stateable in one clause, and at least two reaction branches key to named player actions rather than to a reaction roll.
- **`STANDING HAZARD`** — the announcement distance is stated, with the condition that changes it.
- **`THRESHOLD`** — mode-crossing instances carry no roll, no cost and no encounter. Crossing is the event.

**J12 · The house rules.** *Stated in `DESIGN_PATTERNS.md`; checked here because they are the ones a region breaks without noticing.*
- **The clue lives outside the location holding the secret.** Overlaps J3 deliberately; J3 checks existence, this checks placement.
- **A guardian is usually a condition, not a monster.** A beast that will not touch anyone wearing the right mask, a thing that escalates through four refusals, a toll-taker who bans you for life. Violence is the least interesting version.
- **Repetition before explanation.** The same stone shown several times across regions before anything names it.
- **Withholding is content.** The first genuinely rich-looking room contains nothing, and the module declines to say what became of some of what it raises.
- **Trope defiance is funded.** Each deliberate defiance names the straight instances that pay for it. A module that subverts constantly teaches players that no clue means what it looks like.
- **State the nil.** A field that resolves to nothing says `None` with a brief reason. An omitted field is ambiguous — did the author decide, or forget?
- **One central mechanism per `HIGH`.** Puzzle plus hazard plus hoard is three `MEDIUM` locations stacked and plays as none of them.

---

## MECHANICAL — NOT YET BUILT

*The predicate backlog from the design-pattern harvest, held here because this file is where checks live. **None of these is implemented; `scripts/check.sh` runs M1–M11 and none of them is one of these.*** Building them is its own pass and it needs a field grammar for the location Markdown first — what the parser recognises as a header, an Overview, a feature, a pointer. That does not exist; the catalogue describes the shapes in prose.

**This list is a block and not a backlog.** *Ratified at the strike pass.* **No further step-9 region is opened while it is non-empty.** A predicate that will exist shapes what an author writes — a `LOW` that may hold no find, a `HIGH` that declares one mechanism — so seventeen regions written ahead of the checks are seventeen regions to regenerate afterward, and that is the same mistake the six routes were written to stop. **Expect these to fail on `A`–`E`**, which were written before the three location forms existed: that failure is evidence for the retrofit already booked in `OPEN_QUESTIONS.md` and is not grounds to weaken a predicate. **The severities stated below are now real.** `scripts/check.py` carries three — `ERROR` fails the build, `WARN` and `REPORT` print and leave the exit code alone — and a check declares one in the registry, which may be a callable where the weight depends on the run: `M10` is `REPORT` during authoring and `ERROR` under `--final`.

Predicates that duplicate an existing check are **not** listed: pointer-set-against-diagram is M3, `->` target resolution is M1, every-field-resolves-or-says-`None` is M7, and `SAFE` carries no encounter table by rule 15 and M5 already. The backlog is what is genuinely new.

**Structural, all modes.**

| Check | Severity |
|---|---|
| ~~Location parses into exactly one Player's Overview, one Referee Overview and a Features block~~ **built, `M13`** | error |
| Every bolded noun in the Player's Overview appears as a feature below (**J10**, mechanised) — **blocked, see below** | error |
| Weight inferred from form: `LOW` = ≤2 features and one-sentence Overviews — **blocked, see below** | — |
| No more than two consecutive locations in a region share a weight class — *blocked on weight* | warning |
| Variety floors — a sentence under eight words; no three consecutive sentences within four words; feature lengths varying by ×2 — applied to `MEDIUM` and `HIGH` only — *blocked on weight* | warning |
| ~~`->` appears only in connection pointers~~ **built, `M14`** | error |
| ~~A location shared between two regions carries identical edges at both ends~~ **built, `M15`** | error |

**Two of the structural predicates cannot be built as specified, and the reason is the same in both: the backlog assumed a convention the corpus does not use.** Recorded here rather than worked around, because a predicate written to a convention that does not exist is worse than an absent one — it passes, and the pass means nothing.

- **`J10` has nothing to mechanise. No Player's Overview in the corpus contains bold — none of the 66.** The judgement check reads *"every bolded noun in a Player's Overview appears below as a feature"* and calls it the module's most common real failure and the cheapest to check; the mechanised form would report zero findings on every run, for ever, because the input set is empty. **Either the bolding convention was intended and never adopted, or `J10` describes a different check than the one it states.** It stays a judgement check and it stays honest — a human reading a Player's Overview against the Features below is doing real work — but it is not mechanisable in this form.
- **Weight cannot be inferred, so four predicates fall with it.** The backlog defines only `LOW` — *≤2 features and one-sentence Overviews* — and **no written location has fewer than three features**, so the rule identifies nothing. Above `LOW` there is no signal at all: the template puts `HIGH` at five to seven features, which would make 33 of the 66 written locations `HIGH` against a cap of one per ten and two per region, and that is a measurement artefact rather than 33 defects. **`HIGH` is a form an author chooses and there is no tag by ratified decision**, which is exactly the sequencing problem the catalogue recorded and then left in the backlog anyway.

**Mode-conditional.**

| Mode | Required | Forbidden |
|---|---|---|
| `SAFE` | ≥1 service with a stated cost in coin, standing, obligation or risk; ≥1 refusal; a region-level ceiling; any find carrying a social consequence in the same location; named occupants carrying ≥1 relation to another occupant | combat statistics anywhere in the region |
| `WILD` | keyed sites declaring a non-visual approach cue with a distance the party can still turn back from; occupants declaring a trigger condition, not only a disposition; terrain declaring a rate | — |
| `DANGEROUS` | reactions branching on named player actions; gates declaring an answer that is not the gate; exits carrying sensory cues | search-roll gates on any secret |

**Weight-conditional.**

| Weight | Check | Severity |
|---|---|---|
| `LOW` | contains no treasure, no inhabitant and no gated find | error |
| `LOW` `CONNECTIVE` | declares a sensory cue per significant exit, **or** declares a traversal cost | error |
| `LOW` | exit cues resolve to something actually present at the destination | error |
| `MEDIUM` | a secret tier present in roughly half of a region's `MEDIUM` locations | warning |
| `HIGH` | ≤1 per ten locations, ≤2 per region | error |
| `HIGH` `PUZZLE` | solution string present in the Referee Overview; ≥1 clue reference resolving to an existing location; **zero** attribute-check or search-roll tokens in the solution chain | error |
| `HIGH` | declares one central mechanism, not several | warning |

**Document-level.**

| Check | Severity |
|---|---|
| A rumour carries no `(T)` / `(P)` / `(F)` marker — **named, never failed.** An unmarked rumour rests on a question the module has not answered, and marking it would settle that question by side effect. The register says which pass owns each one. | **warning** |
| The count of `(T)` exceeds the count of existing clue destinations | error |
| Every Standing Mystery carries `[local]` or `[setting]` | error |
| Region declares its scale, and check cadence is consistent with it | warning |
| Ambient-to-actionable ratio on event and encounter tables, 15–35% | report only |

*The pattern-conditional predicates are deliberately absent from this backlog. They live at **J11** and stay there: no pattern tag is authored anywhere, so there is nothing for a parser to read, and the sequencing problem they would otherwise create — a checker that must run before the scaffolding is struck — does not arise.*

---

## THE FULL SWEEP

Before the builder phase begins anywhere, steps 1–9 are read back through as one body of work rather than region by region.

**A sweep that precedes a step checks that the ground still says what it said. It does not do the next step's work early.** J2 in particular is a closing check and belongs to a region's own pass; the sweep may note that a field is carrying location-specific detail, and must leave it where it is. The additional checks at that scale:

- **Truths hold.** Every Truth in the setting outline is honoured everywhere it applies, and no region has quietly contradicted one.
- **Rumours point somewhere.** Every rumour resolves to something that now exists, or is deliberately false and marked as such in the author's record.
- **History leaves traces.** Every History entry's stated trace exists in a region or a location.
- **Factions have somewhere to act.** Every faction's Goals are actionable against real locations, and relations are cross-referenced to rumour numbers.
- **The Bestiary is used.** Every entry appears somewhere; every creature named anywhere has an entry.
- **Threads land.** Every cross-region thread in every block document is live at both ends.
