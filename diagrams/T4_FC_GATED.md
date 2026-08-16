<!-- Tier 4 · FC · Behind the craftsmen's gate · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph FC_GATED["FC · Behind the craftsmen's gate"]
    FC14["FC.14 · The Craftsmen's Gate"]
    FC15["FC.15 · The Bypass Mouth"]
    FC16["FC.16 · The Craftsmen's Housing"]
    FC17["FC.17 · The Meeting Rooms"]
    FC18["FC.18 · The Shrine"]
    FC19["FC.19 · The Ledger-Stones"]
    FC20["FC.20 · The Grievance Room"]
  end

  FC1["FC.1 · The Ramp Landing"]
  FA30["FA.30 · The Bypass"]

  FC1 --- FC14
  FC14 --- FC16
  FC15 --- FC16
  FC15 -.- FA30
  FC16 --- FC17
  FC16 --- FC18
  FC17 --- FC20
  FC17 -.- FC19
```
