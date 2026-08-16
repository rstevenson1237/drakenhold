# SETTING PLAYBOOK TEMPLATE

---

## SETTING

`[Setting Name] — [Three, Thematic, Tags]`

Tags are the three words a Referee would reach for to find this setting on a shelf.

---

## STYLE

*How the Playbook is written. Binds every section below it. Not player-facing and not struck at any pass.*

**Two registers, and they do not mix.**

The **player register** is lyrical and carries the arrival. Tolkien for landscape, weather, scale and elegy — the long sentence that goes somewhere. Gygax for the thing in the room — the specific noun, the flat clause, the dimension stated without ornament. A location may use either or both; the module should not settle into one.

The **referee register** is Hemingway. Say what it is. Dimensions, materials, orientation, condition, and stop. The Referee is holding twenty-two regions in a head with room for none of it, and every word competes with every other word.

**Vocabulary is precise before it is accessible.** *Machicolation*, not "holes for dropping things through." *Corbel*, *ashlar*, *revetment*, *quern*, *garderobe*. *Hauberk* against *brigandine* where the difference is period and purse. *Attainder*, *wergild*, *manumission* where the social fact is the content. One word carrying a historical fact is the compression this Playbook exists to make. Historical literacy is assumed and content is never gated to a hypothetical reader.

**The one constraint on obscurity: the word must be reconstructible from its sentence.** *The rebate where a grating used to sit* survives a Referee who does not know the word. *The rebate was empty* does not. A term that fails this test is either given its context or replaced.

**Variety, held loosely and countable.** Scoped to `MEDIUM` and `HIGH` entries only; the `LOW` form has no sentences to vary.

- At least one sentence under eight words per Player's Overview.
- No three consecutive sentences within four words of each other in length.
- Feature entries within a location vary in length by at least a factor of two between shortest and longest.
- Within a region, no more than two consecutive locations share a weight class.

**It must survive paraphrase.** The Referee does not recite; they describe in their own words. A detail that lands only because of its phrasing will not reach the table. Load-bearing facts must be facts, not effects.

---

## OVERVIEW

A referee-facing account of the setting entire: where it sits in the world, what shape it takes, why a party comes here, and what the campaign is fundamentally about. Everything overarching or not yet distributed into a later section lives here. As the Playbook develops, material migrates out of this section into Truths, History and the Gazetteer, and material too broad for any of those migrates back in.

---

## TRUTHS

Facts, behaviors and mechanisms stated up front to hold the regions consistent with one another.

**Entry Format:** `[Truth, stated as a flat fact] — [1-2 sentences on how it shows up in play: what it gates, explains, or changes, and any mechanical interplay] — Tags: [regions, factions, or creatures it touches]`

---

## RUMOURS

A d20 table serving the Gather Information move. Rumours are the setting's advertising: each one names something a party could go and do, and points at a region or a faction without resolving it. A mix of true, distorted and false is expected, and nothing on the table announces which it is *to the players*.

**The Referee needs to know, and needs to know at a glance.** Each entry carries a truth marker in the source, stripped by the renderer from any player-facing output:

- **`(T)`** — true as stated.
- **`(P)`** — partially true. Something real, misremembered, exaggerated, or attached to the wrong place. This is what hearsay actually looks like and it should be the largest of the three.
- **`(F)`** — false.

Expanding the false and partial sets is free. **Expanding the true set devalues every clue in the module** — a party that finds rumour and fact reliably identical stops investigating and starts obeying.

The Referee refreshes or replaces entries as the campaign consumes them.

**Entry Format:** `[N] (T/P/F) — [One or two sentences, in the voice of whoever passes it along]`

---

## HISTORY

An outline of the setting's past, kept as a consistent backdrop rather than a narrative to be told. The goal is never to recite the history but to leave traces that reveal it.

**Entry Format:** `[Time Anchor, relative to present day] — [Event Name] — [1-3 sentences: what happened, and what physical or cultural trace it left behind for players to actually discover]`

*One entry explicitly anchors "present day" so every other Time Anchor reads relative to a fixed point.*

---

## FACTIONS

The powers a party may treat with, oppose or ignore. Each carries an Action Dice pool used to resolve Faction Turns.

- **AD (Xd6):** overall strength and capability pool — same scaling logic as Creatures.
- **Resources:** material assets, territory, coin, or manpower they can spend or leverage.
- **Knowledge:** what they know that others don't — secrets, locations, or rivals' intentions.
- **Tactics:** their characteristic move when contested — how they typically act on a Faction Turn.
- **Reactions:** how they respond when players or rival factions interfere with them.
- **Goals:** one or more concrete objectives currently driving their turns.

*A creature that is also a power in its own right carries both a Faction entry and a Bestiary entry. The Faction pool measures what it can accomplish in the world; the Bestiary pool measures what it is to fight.*

*Factions need not know one another exist. Ignorance is its own relation, and discovery should be worth something.*

---

## BESTIARY

A quick-reference index of every creature type named across the Gazetteer, Factions and Truths, so one canonical stat block exists no matter how many places point back to it. Entries stay single-line and general-purpose. Anything tied to a particular location or encounter — specific loot, specific knowledge, the job a given group is doing — belongs in that location's entry instead.

**Standing Rules** *(apply to every entry — not restated per creature)*

- A single Action Dice type per creature, rather than separate Combat/Skill/Magic pools.
- No Wounds or Madness.
- When their last AD is spent, **Morale breaks where Morale applies** — the Referee rules whether they flee, surrender, or land one dying blow. `Undead` and `Construct` have no Morale; when their last AD is spent they are destroyed.
- They don't roll for Forced Danger automatically; the Referee triggers it only when it serves the moment.

**Creature Types** *(every entry's `(Type)` is one of the following, stated singular)*

- **Man** — ordinary mortal humans: bandits, soldiers, cultists, mundane human threats.
- **Humanoid** — non-human, human-shaped peoples with their own culture and society.
- **Beast** — natural animals, however large or dangerous, with no magical or supernatural nature.
- **Fantasy Creature** — catch-all for setting-flavor creatures that aren't natural animals and don't fit a sharper category below.
- **Undead** — anything animated by death-tainted or necrotic energy.
- **Construct** — artificial, non-living bodies, usually magically animated.
- **Horror** — alien or sanity-bending things that sit outside normal nature and magic entirely.
- **Wyrm** — dragons and their draconic kin specifically.
- **Fey** — otherworldly, fae-touched beings bound by strange rules or bargains.
- **Fiend** — extraplanar, malevolent entities of infernal or abyssal origin.
- **Giant** — oversized humanoid-adjacent brutes: giants, ogres, trolls.

**Entry Format:** `[Creature Name] (Type) – AD: Xd6 [+/-N] [MA: Y] Description: [1-3 sentences covering whatever mix of appearance, behavior, and default motivation best brings the creature to life]`

- **Xd6** — total Action Dice, scaled to the creature's overall power.
- **+/-N** — flavor modifier from -2 to +6; roughly X÷3 as a starting reference, hand-tuned from there.
- **MA: Y** *(optional)* — Multiple Attack: up to X÷4 (rounded up) of the total dice may be drawn out and rolled as separate Encounter Initiative attacks, each with its own chance to strike. Omit for creatures without the feature.

*Unique NPCs and one-off variants are stated inline within their location entry. The Bestiary holds only reusable templates.*

---

## STANDING MYSTERIES

*Formerly Unanswered Questions. Open authoring questions and deferred decisions now live in the tracking file and are struck there as passes resolve them. **Nothing in this section is ever struck.***

The things the Playbook raises and does not answer, **on purpose**. A megadungeon needs atmosphere whose far end does not exist, and it needs it to be distinguishable six months later from a thread whose far end has not been written yet. That distinction is impossible to recover from the prose alone, so it is recorded here.

Each entry carries a scope:

- **`[local]`** — belongs to one location or one small cluster, and to nothing else. A Referee may answer it freely at their own table; nothing elsewhere in the Playbook depends on the answer.
- **`[setting]`** — reaches across regions, and the Playbook's position is that no answer exists. The correct Referee response to a party pressing on it is that they are holding everything anybody knows.

**Entry Format:** `[Scope] [Mystery, stated as the question a player would ask] — [What the party can actually find] — [What the Playbook's position is, and why it holds]`

*A mystery that later acquires an answer stops being a mystery and moves into the section that answers it. It is not struck here; it is moved, and the move is recorded.*

---

## REGIONAL GAZETTEER

Regions are broad geographic or stylistic groupings. Each carries a header, a Referee Overview, and the fields below. As locations are developed, field content migrates down into them; what remains is what applies to the region entire.

### `[Code] [Region Name]` — `[SAFE/WILD/DANGEROUS]`, `[d4-d12]`, `[Three, Thematic, Tags]`

**Overview:** A referee-facing paragraph. What this region is, how it is run, and what it is for within the module. Together with the tags, this is the Referee's "how do I find this" and "how do I run this" at a glance.

**Ambiance:** What the players see, smell and hear. Architectural style and materials. Condition, and how layers of history have marked it.

**Layout:** The region's overall shape, the kinds of places it holds and how they connect. How a party moves through it, and how large it is.

**Features:** The main elements a party will interact with. Challenges and rewards — environmental hazards, tricks, traps and puzzles that reward both character and player skill.

**Dangers:** How the region answers intrusion. Not every region is antagonistic; some sleep and some are alive to the presence of intruders.

**Creatures:** Who lives here, what they are doing, how they move, and how they meet the party. *Reference the Bestiary by name rather than restating stats, then add what is specific to this group — what they guard, carry or know.*

**Secrets:** What may be revealed about the setting's past or the party's immediate problems. What hidden ways exist, where, and how they are concealed.

**Treasure:** What rewards exploration here. Gems, jewelry, precious goods, magical items, artifacts, trade goods, armament and coin.

**Tables:** Authored once the region's locations are stubbed.
- SAFE regions carry a d6 **Events** table, rolled on entry and each week thereafter.
- WILD regions carry a d6 **Encounter** table, rolled on each failed Difficulty roll.
- DANGEROUS regions carry a d6 **Danger** table, counting down from 6 with each failed Difficulty roll.

**Inter-region edges are not a field.** They are a `## CONNECTIONS` section of their own, following the fields, opening with the edge types in use — open, gated by tile, gated by rod, hidden, secret, vertical, one-way, conditional on restored mechanism, conditional on faction relation — and then one bullet per edge, naming the far region by code and stating the nature of the route. Within-region edges that matter before the locations exist are held there too, and settled at the diagram pass. The section form is what the mechanical checks parse.

---

## RELATIONAL DIAGRAMS

One diagram for the setting, showing regions and their connections. One diagram per region, showing its locations. One block diagram per set of regions too interconnected to draw separately.

**The diagrams are authoritative.** The `->` pointers inside location Features are checked against them, never the reverse.

Edges carry a type where it matters — open passage, gated, hidden, secret, one-way, vertical, or conditional on a key, restored mechanism or faction relation.

---

## LOCATIONS

Locations are numbered within their parent region code (`FA.1`, `FA.2`). A complex feature substantial enough to warrant its own full listing may take a sub-code (`FA.1a`), which should be rare.

**Every location takes one of three forms.** The forms share their fields and differ in how much of each is written. **The form a location is written in declares its weight class** — there is no separate weight tag, and the checker reads weight off the structure rather than trusting a label.

*The three forms bind from the first-level block (`FA`, `GA`, `HA`) forward. `A` through `E` were written before the forms existed and are not read against them until the retrofit pass booked in `OPEN_QUESTIONS.md` runs.*

**No secret is gated on a search roll.** Secret detail surfaces on a named physical action — standing somewhere, clearing something, opening something, speaking a name, looking back — and never on a granted Difficulty roll. See `DECISIONS.md`; the earlier revision of this template allowed the roll and the allowance was withdrawn deliberately.

**Connection pointers are written `->`.** Plain ASCII, two characters, typeable in any editor without a character palette — the source stays human-writable and that is the point. The renderers substitute a single typographic arrow for the web and PDF targets, so `->` is what is authored and never what is read at the table. A feature that is also an exit carries the pointer at the end of its own entry, so that the way out is found where the thing itself is described rather than in a list underneath.

Never use `->` for anything but a connection. Prose relationships between things — a name leading to a place, a clue leading to an answer — are written in words.

*During the iterative passes a location may also carry a **Connections:** bullet list and a working note. Both are scaffolding. **Both are struck at the final write.*** The pointers are what survives.

---

### THE `HIGH` FORM — the region's landmarks

Five to seven features. All three tiers present, and the secret tier earns the weight rather than decorating it. **One per ten locations, capped at two in any region** — a twenty-stub region carries two, a ten-stub region carries one, and a third is evidence the region has no landmark rather than three of them. This cap is on the form, and it is a different measure from the negative-space thirds in `PROCEDURES_AND_RULES.md` rule 7, which govern how detail is distributed.

```
### `[Code] [Location Name]` — `[Three, Thematic, Tags]`

*Player's Overview: the read-aloud paragraph. Obvious detail only — what is
apparent on entering, in the lyrical register. It should raise questions the
Referee's material can answer.*

**Referee Overview:** Shape, size, dimensions and cardinal orientation.
Materials, smell, sound, light, condition. Everything needed to answer general
player questions not covered by a feature. Written plainly.

**Features:**

* **[Feature Name]:** the opening line is the hidden tier, surfaced when a
  player asks a general question about the thing. Secret detail — what is
  behind, beneath or inside it — is written into the same entry and surfaces
  only on a named physical action.
* **[Feature that is also an exit]:** described as a thing first -> `[Code]`
```

---

### THE `MEDIUM` FORM — the working body of the module

Three to four features. Player's Overview and Referee Overview both present; the secret tier optional. Structurally identical to `HIGH` and distinguished by feature count and by whether any feature carries a secret.

---

### THE `LOW` FORM — passage, transition, and rest between demands

**One or two features, and they are usually the exits.** Landmark tier only, or landmark plus one hidden. Purely additive: the same fields, each cut to a sentence.

- **Player's Overview** — one sentence. The one thing that is here.
- **Referee Overview** — one sentence, **dimension-first**. Thin locations are where a party gets lost, and the dimensions are the only thing that prevents it.
- **Features** — one or two, ordinarily the ways out, each carrying its pointer.

```
### `[Code] [Location Name]` — `[Three, Thematic, Tags]`

*Fallen stone fills the run from floor to roof, and the cold air still comes
through it from somewhere none of you can reach.*

**Referee Overview:** Forty feet of collapsed passage running north-west, the
fall dressed blocks among raw stone, impassable and not worth clearing.

* **Back Down the Run:** the way you came, and the only way -> `[Code]`
```

**A `LOW` location may not contain a find.** Not a small one, not a hidden one. A thin location with treasure in it teaches a party to search every thin location in the module, and the pacing function of every honest one is destroyed. If it has something in it, it is `MEDIUM` and should be written as `MEDIUM`.
