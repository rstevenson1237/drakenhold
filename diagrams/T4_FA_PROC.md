<!-- Tier 4 · FA · The Processional of the Living · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph FA_PROC["FA · The Processional of the Living"]
    FA10["FA.10 · The Processional of the Living"]
    FA11["FA.11 · The Founding Panel"]
  end

  FA2["FA.2 · The Trade Hall"]
  GA5["GA.5 · The Monument of the Driving Down"]

  FA2 === FA10
  FA10 --- FA11
  FA10 === GA5
```
