<!-- Tier 3 · region E · the location groups and how they interconnect. Derived from the tier-4 diagrams by `scripts/diagrams.py --write`. Do not hand-edit: `check.py` M11 re-derives it and fails on drift. One untyped edge per connected pair — connection type is drawn at tier 4 only. -->

```mermaid
graph TD
  E_AXIS["The processional axis"]
  E_HILL1["The first hill — beneath Peak 1"]
  E_HILL2["The second hill — beneath Peak 2"]
  E_HILL3["The third hill — beneath Peak 3"]

  E_AXIS --- E_HILL1
  E_AXIS --- E_HILL2
  E_AXIS --- E_HILL3
```
