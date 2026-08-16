<!-- Tier 4 · GA · Where the Processionals meet · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph GA_JOIN["GA · Where the Processionals meet"]
    GA5["GA.5 · The Monument of the Driving Down"]
  end

  GA1["GA.1 · The Judgement Chamber"]
  FA10["FA.10 · The Processional of the Living"]
  HA8["HA.8 · The Processional of the Dead"]
  GA27["GA.27 · The Wrong Mouth"]

  GA1 --- GA5
  GA5 === FA10
  GA5 === HA8
  GA27 --> GA5
```
