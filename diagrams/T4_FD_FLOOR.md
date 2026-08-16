<!-- Tier 4 · FD · The forge floor · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph FD_FLOOR["FD · The forge floor"]
    FD1["FD.1 · The Ramp Head"]
    FD2["FD.2 · The Forge Floor"]
    FD3["FD.3 · The Banked Channels"]
    FD4["FD.4 · The Soot Frieze"]
    FD5["FD.5 · The Order Post"]
    FD15["FD.15 · The Skybridge Terminus"]
  end

  FC1["FC.1 · The Ramp Landing"]
  FE1["FE.1 · The Central Antechamber"]
  FD6["FD.6 · The Production Galleries"]
  FD9["FD.9 · The Chimney Head"]
  FD11["FD.11 · The Training Halls"]
  FD13["FD.13 · Durnek Balvak's Rooms"]
  FD10["FD.10 · The Flow Gate"]
  FD16["FD.16 · The Slag Channel"]
  I1["I.1 · The Western Terminus"]

  FD1 --- FC1
  FD1 --- FE1
  FD1 --- FD2
  FD1 --- FD15
  FD2 --- FD3
  FD2 --- FD4
  FD2 --- FD5
  FD2 --- FD6
  FD2 --- FD9
  FD2 --- FD11
  FD2 --- FD13
  FD3 --- FD10
  FD3 --- FD16
  FD5 --- FD6
  FD15 --- I1
```
