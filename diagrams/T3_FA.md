<!-- Tier 3 · region FA · the location groups and how they interconnect. Derived from the tier-4 diagrams by `scripts/diagrams.py --write`. Do not hand-edit: `check.py` M11 re-derives it and fails on drift. One untyped edge per connected pair — connection type is drawn at tier 4 only. -->

```mermaid
graph TD
  FA_ART["The arteries"]
  FA_HALL["The hall and the kitchens"]
  FA_POCKET["The Peak 1 pocket"]
  FA_PROC["The Processional of the Living"]
  FA_WARREN["The warren"]

  FA_HALL --- FA_ART
  FA_WARREN --- FA_ART
  FA_ART --- FA_POCKET
  FA_HALL --- FA_PROC
  FA_HALL --- FA_WARREN
  FA_WARREN --- FA_POCKET
```
