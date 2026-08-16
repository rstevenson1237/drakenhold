<!-- Tier 4 · HC · The cells and side chambers · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph HC_CELLS["HC · The cells and side chambers"]
    HC8["HC.8 · The Cells"]
    HC9["HC.9 · The Listening Cell"]
    HC10["HC.10 · The Copied Wall"]
    HC15["HC.15 · The Instruction Rooms"]
    HC17["HC.17 · The Chapel Records"]
    HC18["HC.18 · The Sealed Chamber"]
    HC19["HC.19 · The Shaft"]
    HC20["HC.20 · What He Saw Coming Up"]
  end

  HC2["HC.2 · The Chapel Proper"]
  HC3["HC.3 · The Sigil Walls"]
  HC4["HC.4 · Vekkut"]
  HC7["HC.7 · The Bypass Mouth"]
  HA19["HA.19 · The Scholars' Stair"]
  HC16["HC.16 · The Refectory"]

  HC2 --- HC8
  HC3 --- HC10
  HC4 --- HC9
  HC4 --- HC20
  HC7 --- HC8
  HC8 --- HC9
  HC8 --- HC15
  HC8 -.- HC18
  HC9 --- HC10
  HC9 --- HC19
  HC15 --- HA19
  HC15 --- HC17
  HC16 --- HC20
```
