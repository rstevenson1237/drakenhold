<!-- Tier 3 · region HA · the location groups and how they interconnect. Derived from the tier-4 diagrams by `scripts/diagrams.py --write`. Do not hand-edit: `check.py` M11 re-derives it and fails on drift. One untyped edge per connected pair — connection type is drawn at tier 4 only. -->

```mermaid
graph TD
  HA_ART["The arteries"]
  HA_HALLG["The hall and the gathering area"]
  HA_POCKET["The Peak 3 pocket"]
  HA_PROC["The Processional of the Dead"]
  HA_SUPPORT["Hall support"]
  HA_WARREN["The Peak 3 warren"]

  HA_ART --- HA_WARREN
  HA_HALLG --- HA_PROC
  HA_HALLG --- HA_SUPPORT
  HA_HALLG --- HA_WARREN
  HA_WARREN --- HA_POCKET
  HA_PROC --- HA_WARREN
  HA_SUPPORT --- HA_WARREN
```
