<!-- Tier 4 · HE · The approach · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph HE_APPROACH["HE · The approach"]
    HE1["HE.1 · The Ramp Head"]
    HE2["HE.2 · The Halls"]
    HE3["HE.3 · The Way Down From Observation"]
  end

  HD1["HD.1 · The Ramp Head"]
  HE5["HE.5 · The Broken Geometry"]
  HE7["HE.7 · The Libraries"]
  HD16["HD.16 · The Way Up"]

  HE1 --- HD1
  HE1 --- HE2
  HE2 --- HE3
  HE2 --- HE5
  HE2 --- HE7
  HE3 -.- HD16
```
