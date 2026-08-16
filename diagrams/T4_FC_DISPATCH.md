<!-- Tier 4 · FC · The dispatch floor · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph FC_DISPATCH["FC · The dispatch floor"]
    FC1["FC.1 · The Ramp Landing"]
    FC2["FC.2 · Mekgir, the Dispatch Floor"]
    FC3["FC.3 · The Sequence Board"]
    FC4["FC.4 · The Chute Heads"]
    FC5["FC.5 · The Rising Chutes"]
    FC21["FC.21 · The Hidden Access"]
  end

  FA9["FA.9 · The Domed Antechamber"]
  FB16["FB.16 · The Collectors' Landing"]
  FD1["FD.1 · The Ramp Head"]
  FC14["FC.14 · The Craftsmen's Gate"]
  FC6["FC.6 · The Stonecraft Hall"]
  FC7["FC.7 · The Ledger Hall"]
  FC8["FC.8 · The Metalwork Hall"]
  FC9["FC.9 · The Fine Goods Hall"]
  FB8["FB.8 · The Chute Mouths"]
  FD8["FD.8 · The Stock Rooms"]

  FC1 --- FA9
  FC1 --- FB16
  FC1 --- FD1
  FC1 --- FC2
  FC1 --- FC14
  FC2 --- FC3
  FC2 --- FC4
  FC2 --- FC5
  FC2 --- FC6
  FC2 --- FC7
  FC2 --- FC8
  FC2 --- FC9
  FC2 -.- FC21
  FC4 -.- FB8
  FC5 -.- FD8
  FC21 -.- FD8
```
