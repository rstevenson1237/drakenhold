<!-- Tier 3 · region J · the location groups and how they interconnect. Derived from the tier-4 diagrams by `scripts/diagrams.py --write`. Do not hand-edit: `check.py` M11 re-derives it and fails on drift. One untyped edge per connected pair — connection type is drawn at tier 4 only. -->

```mermaid
graph TD
  J_CAVERN["The natural cavern and the vents"]
  J_DEEP["The deep dark"]
  J_FLOOD["The flooded galleries"]
  J_TUNNEL["The tunnel"]
  J_VEIN["The vein"]
  J_WORKINGS["The exhausted workings"]

  J_TUNNEL --- J_CAVERN
  J_CAVERN --- J_DEEP
  J_TUNNEL --- J_DEEP
  J_TUNNEL --- J_FLOOD
  J_TUNNEL --- J_WORKINGS
  J_WORKINGS --- J_VEIN
```
