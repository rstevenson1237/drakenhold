<!-- Tier 4 · GB · The prison half · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph GB_PRISON["GB · The prison half"]
    GB11["GB.11 · The Prison Gate"]
    GB12["GB.12 · The Cell Corridors"]
    GB13["GB.13 · The Confiscation Store"]
    GB14["GB.14 · The Register"]
    GB15["GB.15 · The Jailer's Rod"]
  end

  GB2["GB.2 · The Arena"]
  GB16["GB.16 · The Descent"]
  GC13["GC.13 · The Steward's Rooms"]

  GB2 --- GB11
  GB11 --- GB12
  GB12 --- GB13
  GB12 --- GB14
  GB12 --- GB15
  GB12 --- GB16
  GB12 -.- GC13
```
