# DRAKENHOLD

A complete tabletop RPG adventure module, delivered as a Setting Playbook. A ruined dwarven mountain hold in three peaks, occupied by a red dragon, robbed by whoever dares. Touchstones: *The Hobbit* for the road, Conan and sword-and-sorcery for the halls, pulp treasure-hunter fiction throughout, OSR design philosophy for structure. **The spine is extraction and survival, not a boss fight.** Dragonslaying is achievable and optional.

---

## THE DELIVERABLE

**Working form:** this repository. Region files are authoritative for region content; nothing is assembled by hand.

**Final form:** one Setting Playbook, assembled by script from the files in this repo, in the order and shape defined by `Setting_Playbook_Template.md`. Assembly is mechanical and repeatable. It is not an authoring step and no content originates in it.

Because assembly is scripted, **every file must be structurally predictable**. Headings, field names and entry formats follow the template exactly. Formatting drift is a build failure, not a style opinion.

Two further outputs are built from the same source: a paginated **PDF** for the table, and a browsable **web version** for reference during play. Both are built in CI on every push and pull request; the web version is published to GitHub Pages from `main`.

**Read it here: <https://rstevenson1237.github.io/drakenhold/>** — every location code in the text (`FA.17`, `A.20`) is a link to the stub it names, and the PDF is linked from the contents page. The site publishes play content only: the setting outline, the regions, the block documents and the setting diagram. `HANDOFF.md` and the process documents are authoring instruments and stay out of it.

---

## STRUCTURE

```
├── CLAUDE.md                     instructions loaded every turn — kept short on purpose
├── README.md                     this file
├── PROCEDURES_AND_RULES.md       the build sequence and the authorial rules
├── RECONCILIATION.md             the checklist every closing pass runs
├── HANDOFF.md                    current phase, position, open items, live threads
│
├── Setting_Playbook_Template.md  the deliverable's shape. Illustrative content never enters the setting.
├── Drakenhold_Setting_Outline.md steps 1–2. Truths, Rumours, History, Factions, Bestiary, Unanswered Questions.
│
├── diagrams/                     mermaid + prose, one pair per level of zoom
│   ├── 00_setting.md             the whole map, region to region
│   ├── blocks/                   one per block: A–E, first level, peak 1, peak 2, peak 3, I/J
│   ├── regions/                  one per region, resolving to individual locations
│   └── locations/                where a single location's internal shape needs one
│
├── blocks/                       connective documents — systems, budgets, shared routes
│   ├── FIRST_LEVEL_BLOCK.md
│   ├── PEAK_1_BLOCK.md
│   ├── PEAK_2_BLOCK.md
│   ├── PEAK_3_BLOCK.md
│   └── I_AND_J_BLOCK.md
│
├── regions/                      22 region files + 00_INDEX.md — authoritative
├── archive/
│   └── Drakenhold_Gazetteer.md   frozen. Superseded by regions/. Never edited, never cited.
└── scripts/
    ├── check.sh                  runs every mechanical check; must pass before commit
    ├── build.sh                  assembles the Playbook markdown from the sources
    ├── render_pdf.sh             assembled markdown -> paginated PDF
    ├── build_web.sh              sources -> browsable site in build/web/
    └── pdf/                      the shared Node render toolchain (mermaid-cli,
                                  marked, puppeteer) and both renderers.
                                  Named for the PDF, used by both targets.
```

---

## PHASE POSITION

Architect (steps 1–6) complete. Engineer step 7 — location stubs and region tables — **complete for all 22 regions**.

Current: **step 8, region relational diagrams**, drawn from the stubs before the outlines are written. Then step 9, location outlines, with the diagrams reconciled against them. Then the full 1–9 reconciliation, then the builder phase.

`HANDOFF.md` carries the live detail and is updated at the close of every region.

---

## THE REGIONS

| Code | Name | Class | Die |
|---|---|---|---|
| A | Thornhaven | SAFE | — |
| B | Ironwood Trail | WILD | d6 |
| C | Goblin Camps | WILD | d6 |
| D | River Crossing | WILD | d6 |
| E | Girkel, the Outer City | WILD | d6 |
| FA–FE | Peak 1 — Takdun, Brankel, Mekdun, Khorvak, Aztak | | |
| GA–GE | Peak 2 — Grathdun, Karmor, Azdun, Valdmor, Azith | | |
| HA–HE | Peak 3 — Thaldun, Nurmor, Sigdun, Zarkel, Sigaz | | |
| I | Brynaz, the Skybridge | WILD | d6 |
| J | Mordrak, the Lost Caverns | WILD | d8 |

Classifications and difficulty dice per region are in `regions/00_INDEX.md`.

---

## WORKING ON THIS PROJECT

One region per conversation. Read `CLAUDE.md`, then `PROCEDURES_AND_RULES.md`, then the region's own file and its block document. Run `scripts/check.sh` before committing. Close with an updated `HANDOFF.md`.
