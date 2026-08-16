<!-- Tier 3 · region D · the location groups and how they interconnect. Derived from the tier-4 diagrams by `scripts/diagrams.py --write`. Do not hand-edit: `check.py` M11 re-derives it and fails on drift. One untyped edge per connected pair — connection type is drawn at tier 4 only. -->

```mermaid
graph TD
  D_BELOW["Below the overlook"]
  D_GORGE["The gorge"]
  D_OVER["The overlook"]

  D_OVER --- D_BELOW
  D_BELOW --- D_GORGE
  D_OVER --- D_GORGE
```
