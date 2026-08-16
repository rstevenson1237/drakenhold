<!-- Tier 4 · HE · The Sanctuary itself · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph HE_SANCTUARY["HE · The Sanctuary itself"]
    HE7["HE.7 · The Libraries"]
    HE8["HE.8 · The Workrooms"]
    HE9["HE.9 · Ulgrin Thurvak"]
    HE10["HE.10 · The Register"]
  end

  HE2["HE.2 · The Halls"]
  HE4["HE.4 · Sigmor, the Rift"]
  HE5["HE.5 · The Broken Geometry"]

  HE2 --- HE7
  HE4 --- HE8
  HE5 --- HE7
  HE5 --- HE8
  HE5 --- HE9
  HE5 --- HE10
  HE7 --- HE9
  HE9 --- HE10
```
