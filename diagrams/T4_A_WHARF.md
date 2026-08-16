<!-- Tier 4 · A · Wharf quarter · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph A_WHARF["A · Wharf quarter"]
    A8["A.8 · The Boat Landing"]
    A9["A.9 · Skeed's Wharf Office"]
    A10["A.10 · The Idle Warehouses"]
    A11["A.11 · The Sunken Oar"]
  end

  A5["A.5 · The Riverside Temple"]
  A7["A.7 · The Shuttered Trade Houses"]

  A5 --- A8
  A7 --- A10
  A8 --- A9
  A8 --- A10
  A8 --- A11
  A9 --- A10
  A10 --- A11
```
