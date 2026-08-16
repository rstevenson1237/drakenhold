<!-- Tier 4 · GB · The deep cells · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph GB_DEEP["GB · The deep cells"]
    GB16["GB.16 · The Descent"]
    GB17["GB.17 · The Jailer"]
    GB18["GB.18 · The Talking Cell"]
    GB19["GB.19 · The Kept Thing"]
    GB20["GB.20 · The Broken Floor"]
  end

  GB12["GB.12 · The Cell Corridors"]
  J3["J.3 · The Hidden Descents"]

  GB12 --- GB16
  GB16 --- GB17
  GB17 --- GB18
  GB17 --- GB19
  GB19 --- GB20
  GB20 -.- J3
```
