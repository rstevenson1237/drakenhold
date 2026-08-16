<!-- Tier 4 · FD · The school and the residence · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph FD_SCHOOL["FD · The school and the residence"]
    FD11["FD.11 · The Training Halls"]
    FD12["FD.12 · The Student Dorms"]
    FD13["FD.13 · Durnek Balvak's Rooms"]
    FD14["FD.14 · The Private Work"]
  end

  FD2["FD.2 · The Forge Floor"]

  FD2 --- FD11
  FD2 --- FD13
  FD11 --- FD12
  FD13 -.- FD14
```
