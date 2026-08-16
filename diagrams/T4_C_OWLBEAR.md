<!-- Tier 4 · C · Owlbear country · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph C_OWLBEAR["C · Owlbear country"]
    C7["C.7 · The Deadwood Fringe"]
    C8["C.8 · The Den Mouth"]
    C9["C.9 · The Nest"]
  end

  C3["C.3 · Longmire Camp"]
  C4["C.4 · The Contested Hollow"]

  C3 --- C7
  C4 --- C7
  C7 --- C8
  C8 --- C9
  C7 -.- C9
```
