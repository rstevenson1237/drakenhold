<!-- Tier 3 · region FD · the location groups and how they interconnect. Derived from the tier-4 diagrams by `scripts/diagrams.py --write`. Do not hand-edit: `check.py` M11 re-derives it and fails on drift. One untyped edge per connected pair — connection type is drawn at tier 4 only. -->

```mermaid
graph TD
  FD_FLOOR["The forge floor"]
  FD_GALLERIES["The galleries"]
  FD_SCHOOL["The school and the residence"]
  FD_SHAFT["The chimney and the channels"]

  FD_FLOOR --- FD_GALLERIES
  FD_FLOOR --- FD_SHAFT
  FD_FLOOR --- FD_SCHOOL
```
