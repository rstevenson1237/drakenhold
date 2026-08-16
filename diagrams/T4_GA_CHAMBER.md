<!-- Tier 4 · GA · The judgement chamber · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph GA_CHAMBER["GA · The judgement chamber"]
    GA1["GA.1 · The Judgement Chamber"]
    GA2["GA.2 · The Council Table"]
    GA3["GA.3 · The Standing Floor"]
    GA4["GA.4 · The Seven Figures"]
  end

  GA5["GA.5 · The Monument of the Driving Down"]
  GA6["GA.6 · The Domed Antechamber"]
  GA8["GA.8 · The Holding Approach"]

  GA1 --- GA2
  GA1 --- GA3
  GA1 --- GA4
  GA1 --- GA5
  GA1 --- GA6
  GA3 --- GA8
```
