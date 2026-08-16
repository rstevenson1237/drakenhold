<!-- Tier 4 · HB · The guard gallery · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph HB_GUARD["HB · The guard gallery"]
    HB11["HB.11 · The Guard Gallery"]
    HB12["HB.12 · The Late Burials"]
    HB13["HB.13 · The Watch That Stayed"]
  end

  HB3["HB.3 · The Crypt Access"]
  HB4["HB.4 · The Royal Gallery"]
  HB8["HB.8 · The Guild Gallery"]
  HB9["HB.9 · The Grave-Goods"]
  HB14["HB.14 · The Blank Wall"]
  HB18["HB.18 · The Thickening"]
  HB17["HB.17 · The Survivors' Burials"]

  HB3 --- HB12
  HB4 --- HB13
  HB8 --- HB11
  HB9 --- HB11
  HB11 --- HB12
  HB11 --- HB13
  HB11 --- HB14
  HB11 --- HB18
  HB12 --- HB17
```
