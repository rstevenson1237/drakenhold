<!-- Tier 4 · GA · The court and its support · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph GA_SUPPORT["GA · The court and its support"]
    GA6["GA.6 · The Domed Antechamber"]
    GA7["GA.7 · The Writ-Rooms"]
    GA8["GA.8 · The Holding Approach"]
  end

  GA1["GA.1 · The Judgement Chamber"]
  GA3["GA.3 · The Standing Floor"]
  GA9["GA.9 · The Clerks' Warrens"]
  GB1["GB.1 · The Stairwell Foot"]
  GC1["GC.1 · The Ramp Head"]
  GA16["GA.16 · The Holding Rooms"]

  GA1 --- GA6
  GA3 --- GA8
  GA6 --- GA7
  GA6 --- GA9
  GA6 --- GB1
  GA6 --- GC1
  GA7 --- GA9
  GA8 --- GA16
```
