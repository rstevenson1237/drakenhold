<!-- Tier 3 · region GA · the location groups and how they interconnect. Derived from the tier-4 diagrams by `scripts/diagrams.py --write`. Do not hand-edit: `check.py` M11 re-derives it and fails on drift. One untyped edge per connected pair — connection type is drawn at tier 4 only. -->

```mermaid
graph TD
  GA_CHAMBER["The judgement chamber"]
  GA_JOIN["Where the Processionals meet"]
  GA_SEALED["The sealed segment of the Long Run"]
  GA_SUPPORT["The court and its support"]
  GA_WARREN["The Peak 2 warren"]

  GA_CHAMBER --- GA_JOIN
  GA_CHAMBER --- GA_SUPPORT
  GA_WARREN --- GA_JOIN
  GA_SEALED --- GA_WARREN
  GA_SUPPORT --- GA_WARREN
```
