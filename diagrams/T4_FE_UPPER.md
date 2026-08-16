<!-- Tier 4 · FE · The upper gallery · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph FE_UPPER["FE · The upper gallery"]
    FE7["FE.7 · The Scorched Gallery"]
  end

  FE1["FE.1 · The Central Antechamber"]
  I13["I.13 · The FE Run"]

  FE1 --- FE7
  FE7 -.- I13
```
