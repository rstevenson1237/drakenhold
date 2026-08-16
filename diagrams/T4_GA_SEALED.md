<!-- Tier 4 · GA · The sealed segment of the Long Run · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph GA_SEALED["GA · The sealed segment of the Long Run"]
    GA10["GA.10 · The Long Run — Peak 2 Stretch"]
    GA11["GA.11 · The Second Seal"]
    GA18["GA.18 · The Watchers' Nest"]
    GA19["GA.19 · The Pocket"]
    GA20["GA.20 · Their Buried"]
  end

  FA17["FA.17 · The Seal"]
  HA14["HA.14 · The Long Run — Peak 3 Stretch"]
  GA25["GA.25 · The Older Course"]
  GA22["GA.22 · The Capillary Maze"]

  GA10 -.- FA17
  GA10 --- GA11
  GA10 --- GA18
  GA11 -.- HA14
  GA11 -.- GA25
  GA18 --- GA19
  GA18 -.- GA22
  GA19 --- GA20
```
