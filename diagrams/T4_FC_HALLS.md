<!-- Tier 4 · FC · The four halls · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph FC_HALLS["FC · The four halls"]
    FC6["FC.6 · The Stonecraft Hall"]
    FC7["FC.7 · The Ledger Hall"]
    FC8["FC.8 · The Metalwork Hall"]
    FC9["FC.9 · The Fine Goods Hall"]
    FC10["FC.10 · The Frozen Scales"]
    FC11["FC.11 · The Lamp Brackets"]
    FC12["FC.12 · The Practice Bench"]
    FC13["FC.13 · The Wrong Room"]
  end

  FC2["FC.2 · Mekgir, the Dispatch Floor"]

  FC2 --- FC6
  FC2 --- FC7
  FC2 --- FC8
  FC2 --- FC9
  FC6 --- FC11
  FC6 --- FC13
  FC7 --- FC10
  FC7 --- FC11
  FC8 --- FC11
  FC8 --- FC12
  FC9 --- FC11
```
