# DRAKENHOLD — DESIGN PATTERNS

*Tier one. The classification scheme and the rules that bind across it. **Tier two is nine files, one per grouping**, listed at the foot of this document. Nothing here supplies a sentence, an image or an object.*

---

## HOW THIS DOCUMENT IS USED

**The groupings are prebinnable. The patterns are not.**

A location's grouping is known before a word of it is written: the region declares its mode at the Gazetteer pass, and the stub pass sorts locations into `LOW`, `MEDIUM` and `HIGH` by deciding which are named and which are unnamed fill. So a writer opens exactly one tier-two file — the one for that mode and that weight — and does not carry the other eight.

The **pattern** is applied after writing, as classification, and **it is a reading discipline that reaches no page.** A location is written, then read against the list, and what the reading changes is the location — not a tag on it. If it does not fit a pattern, the pattern list is wrong before the location is. **There is no pattern field, no pattern tag and nothing for a script to read**: the template defines no slot for one, and the pattern-conditional checks in `RECONCILIATION.md` are judgement checks for that reason.

**Weight is declared in a `**Weight:**` field and the form must agree with it**, per the Playbook template. *This supersedes the earlier position that the form alone declares weight and no tag exists; the form proved not to be a readable signal.* The field is struck at step 12.

---

## THE THREE LAYERS

*Stated as a placement rule. This is the spine of the catalogue: a pattern is largely a statement about which layers a location carries and how much of each.*

| Layer | Lives in | Reached by | Register |
|---|---|---|---|
| **Landmark** | The Player's Overview | Arriving and looking | The poetry. May withhold. May never state a conclusion the player should reach. |
| **Hidden** | A feature's name and opening line | Asking about a thing named in the Overview | Plain, direct, complete. The player pushed; answer them. |
| **Secret** | Inside that same feature's entry | A named physical action | Gated on the action, never on a roll. |

The Playbook template nests all three in one place. A Referee scanning at the table reads one bullet and gets both the answer and what is behind it — there is no cross-reference between a hidden list and a secret list, and there is not meant to be.

**Every bolded noun in the Player's Overview appears below as a feature.** This is what makes the landmark layer a promise rather than decoration, it is the module's most common real failure, and it is exactly checkable.

**No secret is gated on a search roll anywhere in this module.** Gates are physical: standing somewhere, clearing something, opening something, speaking a name, looking back. Six published modules were read at the harvest stage and they divide cleanly on this. The division tracks quality exactly.

---

## THE NINE GROUPINGS

*Mode is a property of the region. Weight is a property of the location. Together they determine which fields a location must carry, which it may not, and how much of each is written.*

|  | `LOW` | `MEDIUM` | `HIGH` |
|---|---|---|---|
| **`SAFE`** | thin by nature | the body of a settlement | the people and places worth returning for |
| **`WILD`** | dissolved into procedure | the body of a road | the arrival, and the thing worth leaving it for |
| **`DANGEROUS`** | the bulk of the module | the working body of a level | the region's landmarks |

**The cells are unequal on purpose and are not to be padded to match.**

**`HIGH` is budgeted at one per ten locations, counted per region.** A twenty-stub region carries two; a forty-stub region carries four. **The former maximum of two is withdrawn** — the rate governs. This is the same measure as rule 7's distribution and not a second one: **the weight budget is `HIGH` one in ten, `LOW` three in ten, `MEDIUM` six in ten**, with `LOW` and `MEDIUM` counted per location group. *The two were once written as though they were different things; they are one, and a module cannot hold two standards for the same quantity.*

`SAFE LOW` is thin because an empty shop is a dead town, not a thin location. `WILD LOW` is thin because in a road region the low tier is not written as locations at all — it dissolves into procedure, into watches and Navigate and the Encounter table, and the ground between landmarks is conveyed rather than keyed. `DANGEROUS LOW` is the largest cell in the module by room count and the smallest by content, and it is carried almost entirely by format.

### What each mode requires

**`SAFE`** — every location declares a service and its cost, and the cost may be coin, standing, obligation or risk. Every location declares at least one refusal and the settlement declares a ceiling. Any find requires a stated social consequence in the same location. Occupants carry a named relation to another occupant. **No combat statistics.** A SAFE region that needs them has a mode-tagging error, and the one scenario they would serve ends the campaign.

**`WILD`** — every keyed site declares a non-visual approach cue at a distance the party can still turn back from. Occupants carry a trigger condition, not only a disposition. Terrain carries a rate and, where it applies, a formation constraint. Danger is a field around fixed points and a cost of leaving the road, not a table rolled against the clock.

**`DANGEROUS`** — reactions branch on named player actions rather than on a roll. Gates carry an answer that is not the gate. Exits carry sensory cues. The Danger table counts down rather than draws at random.

### Scale and mode

A region declares its scale, and check cadence is consistent with it within a region. A block that mixes a hundred-foot hall and a three-league reach without changing its cadence is malformed.

**A location may belong to two regions of different modes.** Fenn's boundary is one node on two diagrams. This is legal, the edges must be identical at both ends, and the checker treats an asymmetry as the error rather than the sharing.

---

## THE TEN PATTERNS

*Applied after writing. The matrix against the groupings is sparse, and the sparseness is a finding rather than a gap: each tier-two file opens with the patterns that populate its cell and names the ones that do not.*

`CONNECTIVE` · `EMPTY` · `THRESHOLD` · `READING` · `TRACE` · `HIDDEN CLUE` · `STANDING HAZARD` · `OCCUPIED` · `CACHE` · `PUZZLE`

**`SET PIECE` is not a pattern and is not on the list.** It and `THRESHOLD` were never two patterns; they were one pattern at two weights, and the entry is `THRESHOLD`. A threshold between two locations in the same mode is thin. A threshold between modes carries the module's heaviest landmark writing, because the Referee needs the players' picture to change register and not merely location. **Mode-crossing thresholds are the ones that earn `HIGH`**, and are where the lyrical budget goes. The old name is recorded here only so that a reader who met it elsewhere knows where it went.

**Patterns compose.** A location carries as many tags as it earns. Weight is a function of elaboration — feature count and layer depth — never of tag count. The old tower ruin in a Playbook we read carries `EMPTY`, `TRACE`, `READING` and a quest hook in five sentences and is still `LOW`.

### Two fields the grid does not capture

**Extent.** A location may occupy six rooms, or run under half a region, or surface in a dozen places and belong to none of them. Extent is separate from detail and is stated in the Referee Overview where it is not obvious.

**Shared nodes.** See above. A location on a region boundary belongs to both diagrams and is drawn identically in each.

---

## HOUSE RULES

*These bind across all nine groupings and are not restated in the tier-two files. They are the rules the module already keeps; they are written down here so a later pass does not have to rediscover them.*

**The clue lives outside the location holding the secret.** The rite is performed in public, for free, in a temple, long before the grave that needs it. The name-stones point west into blank wall. A secret whose only evidence is inside itself is not a secret; it is a die roll wearing a costume.

**Every gate has an answer that is not the gate, and the answer is priced.** Not a second door. A longer road, a worse road, a road that arrives in the wrong place. Both branches are costed and the module never says which is the mistake.

**A bypass may be cheaper in time and still expensive.** Where it is, the cost is stated as *what the party arrives without* — unpractised, unmet, burning light they will want later. This is the only shortcut mechanism the harvest did not find in any published source and it is the one that scales to a module whose regions teach in sequence.

**Repetition before explanation.** Show the same stone four times in two regions before anything names it. Recognition is worth more than information and costs less.

**Withholding is content.** The first genuinely rich-looking room contains nothing. The module declines to say what became of the man who did not come out of the wood. A party that opens all fourteen niches learns it the long way, and that is the lesson.

**Trope is free structure; defiance is funded by convention held elsewhere.** Naming a trope imports a whole shape at a cost of three words, and the budget saved goes into the detail that could only be this instance. A module that subverts constantly teaches players that nothing means what it looks like, and then every clue placed anywhere goes unread. **Each deliberate defiance names the straight instances that fund it.**

**A guardian is usually a condition, not a monster.** A beast that will not touch anyone wearing the right mask. A thing that escalates through four refusals before it strikes. A toll-taker who beats you and bans you for life. A `CACHE`'s reason for surviving is the pattern's whole discipline, and violence is the least interesting version of it.

**State the nil.** A field that resolves to nothing says so. An omitted field is ambiguous — did the author decide, or forget? — and a written *None* is a decision on the page.

**Mysteries are scoped.** `[local]` or `[setting]`, recorded in Standing Mysteries, never struck. A thread whose far end is not yet written is a different thing and lives in the tracking file.

---

## WHY ANY OF THIS

*Restated in one line because it is the reason every count above exists: this text is not read, it is reconstructed — through the Referee, into speech, into the players' picture, into decisions — and the Referee's capacity, not the page, is the binding constraint.*

---

## TIER TWO

*One file per grouping. A writer opens one. Each file carries the patterns that populate its cell, the form and its constraints, worked examples at full template, and excerpts from the corpus that illustrate a trope or reinforce a rule.*

| File | Covers |
|---|---|
| `patterns/SAFE_LOW.md` | thin — why the cell is nearly empty, and the few things that belong in it |
| `patterns/SAFE_MEDIUM.md` | shops, halls, offices, wharves — service, cost, refusal, ceiling |
| `patterns/SAFE_HIGH.md` | the people worth returning for, and the places that gate on standing |
| `patterns/WILD_LOW.md` | procedure rather than locations — watches, navigation, the ground between |
| `patterns/WILD_MEDIUM.md` | the body of a road — waystones, crossings, chokepoints, boundaries |
| `patterns/WILD_HIGH.md` | the arrival, the lethal thing worth going to, the mode-crossing threshold |
| `patterns/DANGEROUS_LOW.md` | the bulk of the module — passage, collapse, honest nothing |
| `patterns/DANGEROUS_MEDIUM.md` | the working body of a level — one thing to find, one thing to decide |
| `patterns/DANGEROUS_HIGH.md` | the region's landmarks, and the puzzles that earn their weight |
