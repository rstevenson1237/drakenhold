<!-- Tier 4 · FE · The four chambers · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph FE_CHAMBERS["FE · The four chambers"]
    FE2["FE.2 · The Mining Chamber"]
    FE3["FE.3 · The Smithing Chamber"]
    FE9["FE.9 · What Dovrek Did After the Vote"]
    FE4["FE.4 · The Masonry Chamber"]
    FE5["FE.5 · The Trade Chamber"]
    FE8["FE.8 · The Hung Panel"]
    FE6["FE.6 · The Rod-Locked Strongrooms"]
  end

  FE1["FE.1 · The Central Antechamber"]

  FE1 --- FE2
  FE1 --- FE3
  FE1 --- FE4
  FE1 --- FE5
  FE2 --- FE6
  FE3 --- FE6
  FE3 --- FE9
  FE4 --- FE6
  FE5 --- FE6
  FE5 --- FE8
```
