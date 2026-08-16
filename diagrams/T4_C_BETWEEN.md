<!-- Tier 4 · C · The ground between · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph C_BETWEEN["C · The ground between"]
    C4["C.4 · The Contested Hollow"]
    C5["C.5 · The Scavenger Track"]
    C6["C.6 · The Bone Midden"]
  end

  C1["C.1 · Ashfoot Camp"]
  C2["C.2 · Wetreed Camp"]
  C3["C.3 · Longmire Camp"]
  E1["E.1 · The Guard Wall"]
  C7["C.7 · The Deadwood Fringe"]

  C1 --- C4
  C2 --- C4
  C3 --- C4
  C1 --- C5
  C2 --- C5
  C2 --- C6
  C5 --- C6
  C5 --- E1
  C4 --- C7
```
