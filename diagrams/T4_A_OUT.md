<!-- Tier 4 · A · Outskirts · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph A_OUT["A · Outskirts"]
    A12["A.12 · The Cutting Ground"]
    A13["A.13 · Wyla Fenn's Grove"]
  end

  A1["A.1 · The Landing Gate"]
  A14["A.14 · The Farmyard"]
  B13["B.13 · Fenn's Boundary"]

  A1 --- A12
  A12 --- A13
  A12 --- A14
  A12 --- B13
  A13 --- B13
```
