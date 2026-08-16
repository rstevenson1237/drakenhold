<!-- Tier 4 · A · Ketter's Farmstead · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph A_FARM["A · Ketter's Farmstead"]
    A14["A.14 · The Farmyard"]
    A15["A.15 · The Farmhouse"]
    A16["A.16 · The Cellar Stair"]
    A17["A.17 · The Cold Store"]
    A18["A.18 · The First Gallery"]
    A19["A.19 · The Lower Niches"]
    A20["A.20 · The Grave of Brannek Kelmor"]
  end

  A1["A.1 · The Landing Gate"]
  A12["A.12 · The Cutting Ground"]

  A1 --- A14
  A12 --- A14
  A14 --- A15
  A14 --- A17
  A15 --- A16
  A16 --- A17
  A17 --- A18
  A18 --- A19
  A18 -.- A20
  A19 --- A20
```
