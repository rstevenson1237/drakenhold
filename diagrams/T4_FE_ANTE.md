<!-- Tier 4 · FE · The antechamber · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph FE_ANTE["FE · The antechamber"]
    FE1["FE.1 · The Central Antechamber"]
    FE10["FE.10 · The Scion's Room"]
  end

  FD1["FD.1 · The Ramp Head"]
  FE2["FE.2 · The Mining Chamber"]
  FE3["FE.3 · The Smithing Chamber"]
  FE4["FE.4 · The Masonry Chamber"]
  FE5["FE.5 · The Trade Chamber"]
  FE7["FE.7 · The Scorched Gallery"]

  FE1 --- FD1
  FE1 --- FE2
  FE1 --- FE3
  FE1 --- FE4
  FE1 --- FE5
  FE1 --- FE7
  FE1 --- FE10
```
