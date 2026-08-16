<!-- Tier 4 · E · The processional axis · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph E_AXIS["E · The processional axis"]
    E1["E.1 · The Guard Wall"]
    E2["E.2 · The Town Square"]
    E12["E.12 · The Great Doors"]
  end

  D11["D.11 · The Climbing Road"]
  C5["C.5 · The Scavenger Track"]
  E3["E.3 · The Merchant Halls"]
  E6["E.6 · The Government Quarter"]
  E9["E.9 · The Fine Houses"]
  FA1["FA.1 · The Threshold"]

  D11 --- E1
  C5 --- E1
  E1 --- E2
  E2 --- E3
  E2 --- E6
  E2 --- E9
  E2 --- E12
  E12 === FA1
```
