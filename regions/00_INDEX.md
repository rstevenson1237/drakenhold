# DRAKENHOLD — REGION FILE INDEX

*Procedures steps 3–5 are complete in each file. Step 6 lives in `Drakenhold_Relational_Diagram.md` and is mirrored into each file's Connections section.*

*Step 7 — location stubs and region tables — is **closed for all twenty-two regions**. Step 8 — region relational diagrams — is **closed for all twenty-two regions**. Step 9 — location outlines, one region per conversation — is **closed for `A`** and has not begun in the other twenty-one. Connective documents: `FIRST_LEVEL_BLOCK.md` (FA/GA/HA), `PEAK_1_BLOCK.md` (FB/FC/FD/FE) `PEAK_2_BLOCK.md` (GB/GC/GD/GE) `PEAK_3_BLOCK.md` (HB/HC/HD/HE) and `I_AND_J_BLOCK.md` (I/J).*

| Code | Region | Mode | Die | Stubs | Rooms | File |
|---|---|---|---|---|---|---|
| A | Thornhaven | SAFE | d6 | 20 | — | `A_Thornhaven.md` |
| B | Ironwood Trail | WILD | d10 | 13 + 1 sub | — | `B_Ironwood_Trail.md` |
| C | Goblin Camps | WILD | d6 | 9 | — | `C_Goblin_Camps.md` |
| D | River Crossing | WILD | d8 | 11 | — | `D_River_Crossing.md` |
| E | Girkel, the Outer City | WILD | d8 | 12 | — | `E_Girkel_the_Outer_City.md` |
| FA | Takdun, Peak 1 Main Level Trade Hall | DANGEROUS | d10 | 34 | 65 | `FA_Takdun_Peak_1_Main_Level_Trade_Hall.md` |
| FB | Brankel, Peak 1 Under Level Granaries | WILD | d8 | 20 | 40 | `FB_Brankel_Peak_1_Under_Level_Granaries.md` |
| FC | Mekdun, Peak 1 Level 2 Workshop | DANGEROUS | d10 | 21 | 40 | `FC_Mekdun_Peak_1_Level_2_Workshop.md` |
| FD | Khorvak, Peak 1 Level 3 Forge | DANGEROUS | d10 | 16 | 30 | `FD_Khorvak_Peak_1_Level_3_Forge.md` |
| FE | Aztak, Peak 1 Level 4 Guildmaster Manse | DANGEROUS | d8 | 10 | 16 | `FE_Aztak_Peak_1_Level_4_Guildmaster_Manse.md` |
| GA | Grathdun, Peak 2 Main Level Judgement Hall | DANGEROUS | d10 | 27 | 52 | `GA_Grathdun_Peak_2_Main_Level_Judgement_Hall.md` |
| GB | Karmor, Peak 2 Under Level Prison and Barracks | DANGEROUS | d10 | 20 | 40 | `GB_Karmor_Peak_2_Under_Level_Prison_and_Barracks.md` |
| GC | Azdun, Peak 2 Level 2 Throne of the King | DANGEROUS | d8 | 15 | 30 | `GC_Azdun_Peak_2_Level_2_Throne_of_the_King.md` |
| GD | Valdmor, Peak 2 Level 3 Treasure Vaults | DANGEROUS | d8 | 16 | 30 | `GD_Valdmor_Peak_2_Level_3_Treasure_Vaults.md` |
| GE | Azith, Peak 2 Level 4 Dragon's Lair | DANGEROUS | d4 | 9 | 16 | `GE_Azith_Peak_2_Level_4_Dragon_s_Lair.md` |
| HA | Thaldun, Peak 3 Main Level Celebration Hall | DANGEROUS | d8 | 33 | 63 | `HA_Thaldun_Peak_3_Main_Level_Celebration_Hall.md` |
| HB | Nurmor, Peak 3 Under Level Crypts | DANGEROUS | d6 | 20 | 40 | `HB_Nurmor_Peak_3_Under_Level_Crypts.md` |
| HC | Sigdun, Peak 3 Level 2 Chapel of the Runemasters | DANGEROUS | d8 | 20 | 40 | `HC_Sigdun_Peak_3_Level_2_Chapel_of_the_Runemasters.md` |
| HD | Zarkel, Peak 3 Level 3 Temple of Stone | DANGEROUS | d6 | 16 | 30 | `HD_Zarkel_Peak_3_Level_3_Temple_of_Stone.md` |
| HE | Sigaz, Peak 3 Level 4 Runemaster Sanctuary | DANGEROUS | d4 | 10 | 16 | `HE_Sigaz_Peak_3_Level_4_Runemaster_Sanctuary.md` |
| I | Brynaz, the Skybridge | WILD | d6 | 16 | 30 | `I_Brynaz_the_Skybridge.md` |
| J | Mordrak, the Lost Caverns | WILD | d8 | 24 | 50 | `J_Mordrak_the_Lost_Caverns.md` |

**Stubs and Rooms** are the ratified figures from the step-7 close, moved here from `HANDOFF.md` so that one table carries them. `Rooms` is the region's room budget; `Stubs` is the count of named locations, at roughly half that budget, with the balance unnamed fill inside the stated groupings. The approach regions A–E have no room budget by design. `scripts/check.sh` M4 checks this table against the stub headings actually on disk.

**S — the servants' passages** are not a region. They are written into FA, GA and HA as those regions' true body, and they interconnect all three peaks. They appear in the relational diagram as a shared node.
