<!-- Tier 4 · FB · The vertical · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph FB_VERT["FB · The vertical"]
    FB4["FB.4 · Khorven, the Vent Chimney"]
    FB15["FB.15 · The Chimney Ledges"]
    FB14["FB.14 · The Marked Descent"]
  end

  FB2["FB.2 · The Granary Floor"]
  FB3["FB.3 · The Water Tanks"]
  FA33["FA.33 · The Vent Gallery"]
  J3["J.3 · The Hidden Descents"]
  FB20["FB.20 · The Wet Dark"]
  J2["J.2 · The Marked Descents"]
  FD9["FD.9 · The Chimney Head"]

  FB2 --- FB4
  FB3 --- FB4
  FB4 --- FB15
  FB4 -.- FA33
  FB4 -.- J3
  FB14 --- FB20
  FB14 -.- J2
  FB15 -.- FD9
```
