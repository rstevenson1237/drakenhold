<!-- Tier 4 · HA · The hall and the gathering area · the locations in the group and how they connect. Authored, and the one place edge type is drawn. A destination outside the group is drawn outside the frame. -->

```mermaid
graph TD
  subgraph HA_HALLG["HA · The hall and the gathering area"]
    HA1["HA.1 · The Celebration Hall"]
    HA2["HA.2 · The Scrubbed Floor"]
    HA3["HA.3 · The Singers' Gallery"]
    HA4["HA.4 · The Gathering Area"]
    HA5["HA.5 · The Black Obelisk"]
    HA6["HA.6 · The Struck Names"]
    HA7["HA.7 · The Uncut Spaces"]
    HA10["HA.10 · The Domed Antechamber"]
  end

  HA8["HA.8 · The Processional of the Dead"]
  HB1["HB.1 · The Stairwell Foot"]
  HC1["HC.1 · The Ramp Head"]
  HA11["HA.11 · The Vestry Approaches"]
  HA15["HA.15 · The Funerary Preparation Rooms"]
  HA18["HA.18 · The Runemasters' Service Warren"]

  HA1 --- HA2
  HA1 --- HA3
  HA1 --- HA4
  HA4 --- HA5
  HA4 --- HA10
  HA4 === HA8
  HA5 --- HA6
  HA5 --- HA7
  HA10 --- HB1
  HA10 --- HC1
  HA10 --- HA11
  HA10 --- HA15
  HA10 --- HA18
```
