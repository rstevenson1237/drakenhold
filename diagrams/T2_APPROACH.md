<!-- Tier 2 · The approach · the regions in the block and how they interconnect. Derived from the tier-4 diagrams by `scripts/diagrams.py --write`. Do not hand-edit: `check.py` M11 re-derives it and fails on drift. One untyped edge per connected pair — connection type is drawn at tier 4 only. -->

```mermaid
graph TD
  A["A · Thornhaven"]
  B["B · Ironwood Trail"]
  C["C · Goblin Camps"]
  D["D · River Crossing"]
  E["E · Girkel"]

  A --- B
  B --- D
  B --- C
  C --- E
  D --- E
```
