<!-- Tier 4 · FA · The hall and the kitchens · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph FA_HALL["FA · The hall and the kitchens"]
    FA1["FA.1 · The Threshold"]
    FA2["FA.2 · The Trade Hall"]
    FA3["FA.3 · The Tapestry Fragments"]
    FA4["FA.4 · The Weighing Floor"]
    FA12["FA.12 · The Cut-Down Panels"]
    FA5["FA.5 · The Great Kitchens"]
    FA6["FA.6 · The Bakehouse Ranks"]
    FA7["FA.7 · The Cold Stores"]
    FA8["FA.8 · The Service Chute Head"]
    FA14["FA.14 · The Kitchen Tally Post"]
    FA13["FA.13 · The Porters' Gate"]
    FA9["FA.9 · The Domed Antechamber"]
  end

  E12["E.12 · The Great Doors"]
  FA10["FA.10 · The Processional of the Living"]
  FB9["FB.9 · The Kitchen Chute Bottom"]
  FB1["FB.1 · The Stairwell Foot"]
  FC1["FC.1 · The Ramp Landing"]
  FA15["FA.15 · The Runners' Ways"]
  FA16["FA.16 · The Long Run — Peak 1 Stretch"]

  E12 === FA1
  FA1 --- FA2
  FA2 --- FA3
  FA2 --- FA4
  FA2 --- FA12
  FA2 --- FA5
  FA2 --- FA13
  FA2 --- FA9
  FA2 === FA10
  FA5 --- FA6
  FA5 --- FA7
  FA5 --- FA8
  FA5 --- FA14
  FA8 -.-> FB9
  FA9 --- FB1
  FA9 --- FC1
  FA9 --- FA15
  FA9 --- FA16
  FA13 --- FA15
```
