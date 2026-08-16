<!-- Tier 4 · HC · The excavation · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph HC_DIG["HC · The excavation"]
    HC11["HC.11 · The Survey Line"]
    HC12["HC.12 · The Excavation Face"]
    HC13["HC.13 · The Spoil"]
  end

  HC4["HC.4 · Vekkut"]
  HC6["HC.6 · The Loyalists' Camp"]
  HD4["HD.4 · The Circuit"]

  HC4 --- HC12
  HC6 --- HC12
  HC11 --- HC12
  HC11 --- HC13
  HC12 --- HC13
  HC12 -.- HD4
```
