<!-- Tier 4 · A · Upper town · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph A_UPPER["A · Upper town"]
    A1["A.1 · The Landing Gate"]
    A2["A.2 · The Well Square"]
    A3["A.3 · The Old Toll-House"]
    A4["A.4 · The Reeve's Hall"]
    A5["A.5 · The Riverside Temple"]
    A6["A.6 · The Kingfisher"]
    A7["A.7 · The Shuttered Trade Houses"]
  end

  B1["B.1 · The Road Out"]
  A12["A.12 · The Cutting Ground"]
  A14["A.14 · The Farmyard"]
  A8["A.8 · The Boat Landing"]
  A10["A.10 · The Idle Warehouses"]

  A1 --- B1
  A1 --- A2
  A1 --- A3
  A1 --- A12
  A1 --- A14
  A2 --- A3
  A2 --- A4
  A2 --- A5
  A2 --- A6
  A2 --- A7
  A3 --- A4
  A5 --- A8
  A7 --- A10
```
