<!-- Tier 4 · FB · The great under hall · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph FB_HALL["FB · The great under hall"]
    FB1["FB.1 · The Stairwell Foot"]
    FB2["FB.2 · The Granary Floor"]
    FB3["FB.3 · The Water Tanks"]
    FB5["FB.5 · The Chieftain's Seat"]
    FB6["FB.6 · Snath's Fires"]
    FB18["FB.18 · Vekkut's Den"]
    FB7["FB.7 · The Tribute Floor"]
    FB16["FB.16 · The Collectors' Landing"]
    FB10["FB.10 · The Brood Warren"]
  end

  FA9["FA.9 · The Domed Antechamber"]
  FB4["FB.4 · Khorven, the Vent Chimney"]
  FB8["FB.8 · The Chute Mouths"]
  FB13["FB.13 · The Tally Gallery"]
  FC1["FC.1 · The Ramp Landing"]

  FA9 --- FB1
  FB1 --- FB2
  FB2 --- FB3
  FB2 --- FB4
  FB2 --- FB5
  FB2 --- FB7
  FB2 --- FB8
  FB2 --- FB10
  FB2 --- FB13
  FB2 --- FB16
  FB3 --- FB4
  FB5 --- FB6
  FB5 --- FB18
  FB7 --- FB16
  FB16 --- FC1
```
