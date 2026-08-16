<!-- Tier 4 · HE · The centre · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph HE_CENTRE["HE · The centre"]
    HE4["HE.4 · Sigmor, the Rift"]
    HE5["HE.5 · The Broken Geometry"]
    HE6["HE.6 · The Drakmorith"]
  end

  HE2["HE.2 · The Halls"]
  HE8["HE.8 · The Workrooms"]
  HE7["HE.7 · The Libraries"]
  HE9["HE.9 · Ulgrin Thurvak"]
  HE10["HE.10 · The Register"]

  HE2 --- HE5
  HE4 --- HE5
  HE4 --- HE6
  HE4 --- HE8
  HE5 --- HE6
  HE5 --- HE7
  HE5 --- HE8
  HE5 --- HE9
  HE5 --- HE10
```
