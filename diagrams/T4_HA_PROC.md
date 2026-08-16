<!-- Tier 4 · HA · The Processional of the Dead · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph HA_PROC["HA · The Processional of the Dead"]
    HA8["HA.8 · The Processional of the Dead"]
    HA9["HA.9 · The Wedge"]
  end

  HA4["HA.4 · The Gathering Area"]
  HA33["HA.33 · The Wrong Mouth"]
  GA5["GA.5 · The Monument of the Driving Down"]

  HA4 === HA8
  HA8 --- HA9
  HA8 --- HA33
  HA8 === GA5
```
