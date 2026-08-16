<!-- Tier 3 · region FB · the location groups and how they interconnect. Derived from the tier-4 diagrams by `scripts/diagrams.py --write`. Do not hand-edit: `check.py` M11 re-derives it and fails on drift. One untyped edge per connected pair — connection type is drawn at tier 4 only. -->

```mermaid
graph TD
  FB_HALL["The great under hall"]
  FB_STORES["The stores"]
  FB_VERT["The vertical"]

  FB_HALL --- FB_VERT
  FB_HALL --- FB_STORES
  FB_VERT --- FB_STORES
```
