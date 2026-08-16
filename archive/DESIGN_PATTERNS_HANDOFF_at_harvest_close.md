> **ARCHIVED — frozen, never edited, never cited as current.**
>
> This is the handoff written at the close of the design-pattern harvest conversation.
> Its content has been distributed and now lives in the working files: the decisions in
> `DECISIONS.md`, the assumptions, hanging items and side threads in `OPEN_QUESTIONS.md`,
> the checker predicates in `RECONCILIATION.md`, and the catalogue itself in
> `DESIGN_PATTERNS.md` and `patterns/`. It is kept only so the reasoning behind those
> entries can be read back. **Where it disagrees with a working file, the working file is
> right** — several of its positions were amended by ruling when the catalogue was wired in.

---

# HANDOFF — DESIGN PATTERN CATALOGUE

*Written at the close of the harvest conversation. Everything below is either a decision that was made, an assumption that was made silently and may want revisiting, or a thread left open. The raw sources died with that conversation; this is what survives besides the ten files.*

---

## 1. DECISIONS MADE

### Structure

- **Tier one is `DESIGN_PATTERNS.md`. Tier two is nine files**, one per `mode × weight` cell, plus the Playbook template as a shared spine. Ten documents total.
- **The retrieval key is `mode × weight`, both known before writing.** Mode is declared at the Gazetteer pass; weight is decided at the stub pass by which locations are named and which are unnamed fill. Pattern is *not* a retrieval key — it is applied after writing.
- **Weight is declared by the form the location is written in.** No weight tag. The checker reads weight off structure.
- **The cells are deliberately unequal.** `DANGEROUS LOW` is the largest by room count; `SAFE LOW` and `WILD LOW` are near-empty and are written short on purpose. Do not pad them to match.

### Pattern changes from the previous revision

- **`THRESHOLD` and `SET PIECE` merged.** One pattern at two weights. Mode-crossing thresholds are the ones that earn `HIGH`.
- **Patterns compose.** A location carries as many tags as it earns; weight tracks elaboration, never tag count.
- **Eleven patterns retained otherwise:** `CONNECTIVE`, `EMPTY`, `THRESHOLD`, `READING`, `TRACE`, `HIDDEN CLUE`, `STANDING HAZARD`, `OCCUPIED`, `CACHE`, `PUZZLE`, `SET PIECE` (merged out — the list is now ten in practice).

### Template amendments

Eight, listed in the template's own changelog. The load-bearing ones:

- **`STYLE` section added** — two registers, vocabulary rule, variety floors scoped to `MEDIUM`+.
- **`UNANSWERED QUESTIONS` became `STANDING MYSTERIES`** and inverted: open authoring questions move to the separate tracking file; this section holds only what is never answered, scoped `[local]` or `[setting]`, and nothing in it is ever struck.
- **Three location forms** — `HIGH`, `MEDIUM`, `LOW` — sharing all fields, differing in how much of each is written. `LOW` is purely additive: one sentence player, one dimension-first sentence referee, one or two features that are usually exits.
- **`LOW` may not contain a find.** Stated in both the template and tier one.
- **Rumours gain `(T)` / `(P)` / `(F)`** in source, stripped by renderer.
- **Bestiary gains `Ooze`**; Morale standing rule scoped to creatures that have Morale.
- **Gazetteer gains a `Connections` field** for inter-region edges and held threads.

### Format decisions confirmed by the user

- `Connections:` bullet lists and working notes are **scaffolding, struck at the final write**. The `->` pointers survive and are the authored source of truth.
- The relational diagrams are authoritative; pointers are checked against them, never the reverse.
- Setting-level and block-level diagrams already exist and cover the inter-region case.

---

## 2. ASSUMPTIONS MADE — WORTH A SECOND LOOK

These were decided without explicit confirmation and are the most likely places to disagree.

1. **The nine cells assume mode is a property of the *region*, not the location.** One exception is already live: a boundary location may belong to two regions of different modes, with identical edges at both ends. If more of these appear, mode may need to become a per-location field with the region carrying a default.

2. **`WILD LOW` was written as "this cell does not exist as locations."** That conclusion rests on one worked WILD region. If a later WILD region — a marsh, a broken-ground crossing, a hex-crawl — turns out to want keyed thin locations, this file needs revisiting rather than following.

3. **The variety floors were scoped to `MEDIUM` and above** on the grounds that the `LOW` form has too few sentences to vary. The adjacency floor (*no more than two consecutive locations sharing a weight class*) was kept binding at `LOW` because runs of thin rooms are the failure it exists to catch.

4. **Extent and shared-node were named as needed fields but not added to the template.** They are described in tier one and in the relevant cell files. If the checker needs them structured, they need a home in the location header or the Referee Overview by convention.

5. **Excerpts are characterisations with citations, not quotations.** This was flagged early and held throughout. Every excerpt names its source and area so the original can be opened. If the intent was ever a quotation anthology, none of these files supply one.

6. **Worked examples are set nowhere**, using `X.n` codes and no Drakenhold place names, specifically so they cannot be quarried into canon by accident. They are illustrations of form, not draft content.

---

## 3. HANGING ITEMS

### The checker is specified but not built

Predicates are distributed across the nine files as the rules that generate them. **Section 5 below collects them.** What does not exist: a field grammar for the Markdown, a parse strategy, severity levels, or the script itself.

### Six modules were read; the mine and quarry material was never supplied

The `CONNECTIVE` gap was closed by *The Hole in the Oak* instead — the noun-phrase headline form and the directional sense-cue rule. The original request for real mine workings, haulage ways and underground industrial architecture was withdrawn as unnecessary. **If the deep levels want an industrial texture the current files do not supply, that source request is still open.**

### The trope pass is deliberately unfilled

Each cell file ends with a `FOR THE TROPE PASS` section noting where classic furniture will land and what the constraints are. Nothing was inserted. Two cautions recorded there are worth carrying forward:

- A `HIGH` location can carry only **one** central mechanism. Puzzle plus hazard plus hoard is three `MEDIUM` locations stacked, and it plays as none of them.
- A `WILD` region should carry exactly **one** lethal off-road site. Three means leaving the road is forbidden rather than chosen.

### Sources mined, so a later pass does not re-derive

Arden Vul (Level 3), Rappan Athuk (DL3), Highfell, Winter's Daughter — from the earlier pass. This pass added: B4 *The Lost City*, B2 *The Keep on the Borderlands*, X1 *Isle of Dread*, *Fourtower Bridge*, *The Hole in the Oak*.

---

## 4. SIDE THREADS SURFACED

Things noticed in passing that belong to some other pass.

- **The Danger / Encounter / Events tables are state machines, not draw tables.** The `DANGEROUS` countdown from 6 escalating to *the way back is gone* is better than anything in the corpus. My original harvest predicates assumed random-draw tables and were re-expressed against the countdown; **anything written about table composition elsewhere should be re-read against this.**
- **Ambient-to-actionable ratio on event and encounter tables** looks like roughly 15–35% actionable across two independent sources. Recorded as a soft target, not enforced.
- **The single-character sighting** — one player sees the thing, the others do not — is a one-clause technique that produces table behaviour nothing else does. Not used anywhere in Drakenhold yet.
- **An unreliable informant must be right once**, or the players simply discount them. Fourtower's fisherman is the model. Drakenhold has unreliable sources; check that at least one has a verified truth attached.
- **The bypass priced in deprivation** — faster, and the cost is what the party arrives *without* — appears nowhere in the corpus and is a Drakenhold invention. It constrains every gate written above the first level and is recorded in tier one's house rules.
- **Sub-lettering** (`FA.1a`, `B.4a`) is in use and the template calls it rare. Both live instances are load-bearing. No action; noted so nobody prunes them for tidiness.

---

## 5. CHECKER PREDICATES, COLLECTED

*Gathered from the nine cell files and tier one. Severities suggested, not fixed.*

### Structural — all modes

| Check | Severity |
|---|---|
| Location parses into exactly one Player's Overview, one Referee Overview, and a Features block | error |
| Every bolded noun in the Player's Overview appears as a feature below | error |
| Weight inferred from form; `LOW` = ≤2 features and one-sentence Overviews | — |
| No more than two consecutive locations in a region share a weight class | warning |
| Variety floors (sentence under eight words; no three consecutive within four words; feature lengths varying ×2) apply to `MEDIUM` and `HIGH` only | warning |
| `->` appears only in connection pointers | error |
| Every `->` target resolves to an existing location code | error |
| Pointer set matches the region diagram's edges, both directions | error |
| A location shared between two regions carries identical edges at both ends | error |
| Obscure term reconstructible from its sentence | manual |

### Mode-conditional field sets

| Mode | Required | Forbidden |
|---|---|---|
| `SAFE` | ≥1 service with a stated cost (coin / standing / obligation / risk); ≥1 refusal; region-level ceiling; any find carries a social consequence in the same location; named occupants carry ≥1 relation to another occupant | combat statistics; encounter table |
| `WILD` | keyed sites declare a non-visual approach cue with a distance; occupants declare a trigger condition; terrain declares a rate | encounter table drawn on a clock rather than on failure |
| `DANGEROUS` | reactions branch on named player actions; gates declare an answer that is not the gate; exits carry sensory cues | search-roll gates on any secret |

### Weight-conditional

| Weight | Check | Severity |
|---|---|---|
| `LOW` | contains no treasure, no inhabitant, no gated find | error |
| `LOW` `CONNECTIVE` | declares a sensory cue per significant exit, **or** declares a traversal cost | error |
| `LOW` | exit cues resolve to something present at the destination | error |
| `MEDIUM` | secret tier present in roughly half of a region's `MEDIUM` locations | warning |
| `HIGH` | ≤2 per region | error |
| `HIGH` `PUZZLE` | solution string present in Referee Overview; ≥1 clue reference resolving to an existing location; **zero** attribute-check or search-roll tokens in the solution chain | error |
| `HIGH` | declares one central mechanism, not several | warning |

### Pattern-conditional

| Pattern | Check |
|---|---|
| `EMPTY` | no find of any kind; load-bearing variant carries exactly one remnant and no other feature |
| `TRACE` | present-tense remnant noun precedes any past-tense verb; past tense attaches to something currently touchable |
| `HIDDEN CLUE` | both ends exist; far end does not explain itself; unplaced far ends recorded in the tracking file |
| `CACHE` | states a reason it survived; reason is not solely a guardian |
| `OCCUPIED` | want stateable in one clause; ≥2 reaction branches keyed to named player actions; zero reaction-roll tokens |
| `STANDING HAZARD` | announcement distance stated, with the condition that changes it |
| `THRESHOLD` | mode-crossing instances carry no roll, no cost, no encounter |

### Document-level

| Check | Severity |
|---|---|
| Every rumour carries `(T)` / `(P)` / `(F)`; count of `(T)` ≤ count of existing clue destinations | error |
| Every ordered faction pair declares a relation; *unaware of* is legal | warning |
| Every Standing Mystery carries `[local]` or `[setting]` | error |
| Every declared field resolves to a value or the literal `None` | error |
| Region declares scale; check cadence consistent with it | warning |
| Bestiary entries referenced by the Gazetteer exist | error |
| Ambient-to-actionable ratio on event and encounter tables, 15–35% | report only |
| No combat statistics anywhere in a `SAFE` region | error |

---

## 6. WHAT TO BUILD NEXT

In order of dependency:

1. **A field grammar for the location Markdown** — what the parser recognises as a header, an Overview, a feature, a pointer, a tag. Nothing formal exists; the files describe the shapes in prose.
2. **The parse-and-check script**, against the table above. Start with the structural and pointer-resolution checks — they are exact, they catch the most common real failure, and they need no judgement.
3. **Mode-conditional checks**, which need the region header parsed and the classification read.
4. **Pattern-conditional checks**, which need pattern tags to be authored during step 10 — and those tags are scaffolding struck at the final write, so **the checker must run before the final write, or on the pre-strike source.** This is a real sequencing constraint and it is not recorded anywhere else.
