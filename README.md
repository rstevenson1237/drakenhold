# DRAKENHOLD

A complete tabletop RPG adventure module, delivered as a Setting Playbook. A ruined dwarven mountain hold in three peaks, occupied by a red dragon, robbed by whoever dares. Touchstones: *The Hobbit* for the road, Conan and sword-and-sorcery for the halls, pulp treasure-hunter fiction throughout, OSR design philosophy for structure. **The spine is extraction and survival, not a boss fight.** Dragonslaying is achievable and optional.

---

## THE DELIVERABLE

**Working form:** this repository. Region files are authoritative for region content; nothing is assembled by hand.

**Final form:** one Setting Playbook, assembled by script from the files in this repo, in the order and shape defined by `Setting_Playbook_Template.md`. Assembly is mechanical and repeatable. It is not an authoring step and no content originates in it.

Because assembly is scripted, **every file must be structurally predictable**. Headings, field names and entry formats follow the template exactly. Formatting drift is a build failure, not a style opinion.

Two further outputs are built from the same source: a paginated **PDF** for the table, and a browsable **web version** for reference during play. Both are built in CI on every push and pull request; the web version is published to GitHub Pages from `main`.

**Read it here: <https://rstevenson1237.github.io/drakenhold/>** — every location code in the text (`FA.17`, `A.20`) is a link to the stub it names, every setting-outline reference (`(BESTIARY, Goblin)`, `(TREASURE, II)`) is a link to the field it names, and the PDF is linked from the contents page. Editorial notes (`[[ ... ]]`) are stripped by both renderers and never reach a reader. The site publishes play content only: the setting outline, the regions, the block documents and the setting diagram. `HANDOFF.md` and the process documents are authoring instruments and stay out of it.

---

## STRUCTURE

```
├── CLAUDE.md                     instructions loaded every turn — kept short on purpose
├── README.md                     this file
├── PROCEDURES_AND_RULES.md       the build sequence and the authorial rules
├── RECONCILIATION.md             the checklist every closing pass runs, and the backlog
│                                 of checks specified but not yet built
├── DESIGN_PATTERNS.md            tier one of the design pattern catalogue: the three
│                                 layers, the nine mode × weight groupings, the ten
│                                 patterns, and the house rules that bind across them.
├── patterns/                     tier two — one file per grouping. A writer opens
│                                 exactly one, chosen by the region's mode and the
│                                 location's weight, and does not carry the other eight.
│                                 DESIGN_PATTERNS.md and patterns/ are process documents:
│                                 not assembled into the Playbook, not published to the
│                                 web, and outside the corpus check.sh reads — which is
│                                 why their worked examples use X.n codes freely.
├── HANDOFF.md                    what the next conversation does first. Nothing else. Kept to a page.
├── DECISIONS.md                  what has been ratified and is not re-litigated, including
│                                 mechanical rulings received from the rules project.
├── OPEN_QUESTIONS.md             the single register of what is not yet decided, and who
│                                 decides it. Answered items are struck, never deleted.
│                                 DECISIONS and OPEN_QUESTIONS are architect material:
│                                 not assembled into the Playbook, not published to the web.
│
├── Rules_Light_TTRPG_Design_Notes.md  **the source of truth for game mechanics.**
│                                 Authored in a separate project and mirrored here.
│                                 Read-only in this repo: never edited, never extended.
│                                 Replaced wholesale when a new revision is uploaded.
├── Setting_Playbook_Template.md  the deliverable's shape. Illustrative content never enters the setting.
├── Drakenhold_Setting_Outline.md steps 1–2, the index: title, tagline, Overview, and a
│                                 SECTIONS table pointing at outlines/. The build drops
│                                 that table and reads the fields below in numeric order.
├── outlines/                     one file per outline field, in template order —
│                                 01_TRUTHS … 10_STANDING_MYSTERIES. Referee-facing only.
│                                 Standing Mysteries holds what the module leaves open at
│                                 the table on purpose; authors' open items go in
│                                 OPEN_QUESTIONS.md instead.
├── LORE_INDEX.md                 register of documentary items that have a far end —
│                                 engravings, ledgers, maps, notes. An index and not a
│                                 source: the text lives in the region file, which stays
│                                 authoritative. Outside the corpus check.sh reads, for now.
│
├── diagrams/
│   └── Drakenhold_Relational_Diagram.md   step 6 and every level of zoom below it:
│                                 the setting graph, then a graph per block. Region-level
│                                 graphs live in the region files' own diagram sections.
│
├── blocks/                       connective documents — systems, budgets, shared routes
│   ├── FIRST_LEVEL_BLOCK.md
│   ├── PEAK_1_BLOCK.md
│   ├── PEAK_2_BLOCK.md
│   ├── PEAK_3_BLOCK.md
│   └── I_AND_J_BLOCK.md
│
├── regions/                      22 region files + 00_INDEX.md — authoritative
├── archive/                      frozen. Never edited, never cited as current.
│   ├── Drakenhold_Gazetteer.md   superseded by regions/.
│   ├── HANDOFF_at_step_8_close.md  the handoff as it stood before it was cut back.
│   └── DESIGN_PATTERNS_HANDOFF_at_harvest_close.md  the catalogue's reasoning, kept
│                                 after its content was distributed to the working files.
└── scripts/
    ├── check.sh                  runs every mechanical check; must pass before commit.
    │                             check.sh --final also fails on surviving editorial notes
    ├── build.sh                  assembles the Playbook markdown from the sources
    ├── render_pdf.sh             assembled markdown -> paginated PDF
    ├── build_web.sh              sources -> browsable site in build/web/
    └── pdf/                      the shared Node render toolchain (mermaid-cli,
                                  marked, puppeteer) and both renderers.
                                  Named for the PDF, used by both targets.
```

---

## PHASE POSITION

Architect (steps 1–6) complete. Engineer step 7 — location stubs and region tables — **complete for all 22 regions**. Engineer step 8 — region relational diagrams, drawn from the stubs before the outlines — **complete for all 22 regions**.

Current: **step 9, location outlines**, one region per conversation, with each region's diagram reconciled against its finished outlines before the region closes. The reconciled diagram is the deliverable. Procedure 12 requires a reconciliation pass over steps 1–8 before step 9 begins anywhere. Then the full 1–9 sweep, then the builder phase.

`HANDOFF.md` says what the next conversation does. `OPEN_QUESTIONS.md` and `DECISIONS.md` carry the live detail and are updated at the close of every region.

---

## THE REGIONS

| Code | Name | Class | Die |
|---|---|---|---|
| A | Thornhaven | SAFE | d6 |
| B | Ironwood Trail | WILD | d10 |
| C | Goblin Camps | WILD | d6 |
| D | River Crossing | WILD | d8 |
| E | Girkel, the Outer City | WILD | d8 |
| FA–FE | Peak 1 — Takdun, Brankel, Mekdun, Khorvak, Aztak | | |
| GA–GE | Peak 2 — Grathdun, Karmor, Azdun, Valdmor, Azith | | |
| HA–HE | Peak 3 — Thaldun, Nurmor, Sigdun, Zarkel, Sigaz | | |
| I | Brynaz, the Skybridge | WILD | d6 |
| J | Mordrak, the Lost Caverns | WILD | d8 |

Classifications and difficulty dice per region are in `regions/00_INDEX.md`.

---

## WORKING ON THIS PROJECT

One region per conversation. Read `CLAUDE.md`, then `PROCEDURES_AND_RULES.md`, then `DESIGN_PATTERNS.md` and the one `patterns/` file for the cell being written, then the region's own file and its block document. Run `scripts/check.sh` before committing. Close with an updated `HANDOFF.md`.
