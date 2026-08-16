<!-- Tier 4 · FB · The stores · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph FB_STORES["FB · The stores"]
    FB8["FB.8 · The Chute Mouths"]
    FB9["FB.9 · The Kitchen Chute Bottom"]
    FB13["FB.13 · The Tally Gallery"]
    FB11["FB.11 · The Sealed Bins"]
    FB17["FB.17 · The Skimmed Count"]
    FB12["FB.12 · The Drowned Rank"]
    FB19["FB.19 · The Undeclared Cache"]
    FB20["FB.20 · The Wet Dark"]
  end

  FB2["FB.2 · The Granary Floor"]
  FC4["FC.4 · The Chute Heads"]
  FA8["FA.8 · The Service Chute Head"]
  FB14["FB.14 · The Marked Descent"]

  FB2 --- FB8
  FB2 --- FB13
  FB8 --- FB9
  FB8 -.- FC4
  FB9 -.- FA8
  FB11 --- FB13
  FB12 --- FB13
  FB12 --- FB20
  FB12 -.- FB19
  FB13 -.- FB17
  FB14 --- FB20
```
