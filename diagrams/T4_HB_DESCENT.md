<!-- Tier 4 · HB · The descent · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph HB_DESCENT["HB · The descent"]
    HB1["HB.1 · The Stairwell Foot"]
    HB2["HB.2 · The Tiering"]
    HB3["HB.3 · The Crypt Access"]
    HB10["HB.10 · The Interment Record"]
  end

  HA10["HA.10 · The Domed Antechamber"]
  HB4["HB.4 · The Royal Gallery"]
  HA29["HA.29 · The Crypt Access"]
  HB12["HB.12 · The Late Burials"]

  HB1 --- HA10
  HB1 --- HB2
  HB2 --- HB4
  HB2 --- HB10
  HB3 -.- HA29
  HB3 --- HB12
  HB4 --- HB10
```
