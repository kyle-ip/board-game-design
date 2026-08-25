# Components Sheet

Data before art. One row per unique component or card. Copy into the project folder; expand as CSV/spreadsheet when the set grows.

Format reference: `templates/examples/micro-scavenger/components-sheet.md`

Before delivery: `lint/checklist.md` components section.

## Legend
| Column | Meaning |
|---|---|
| id | Stable code (e.g. CARD-012, TILE-A3) |
| type | card / tile / board / token / die / other |
| name | Prototype label (plain text OK) |
| qty | How many in the box |
| cost | Buy/build cost if any |
| effect | Rules text or shorthand |
| tags | Set / color / type for collection |
| vp | Victory points if scored from this |
| notes | Balance or print notes |

## Cards / Tiles
| id | type | name | qty | cost | effect | tags | vp | notes |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |

## Boards / Maps
| id | name | size / folds | spaces / regions | notes |
|---|---|---|---|---|
| | | | | |

## Tokens / Meeples / Dice
| id | name | qty | purpose | notes |
|---|---|---|---|---|
| | | | | |

## Counts Check
- [ ] Every id appears in the rulebook or is marked "unused / cut"
- [ ] Starting hands / setup quantities sum correctly for min and max player counts
- [ ] No art yet — placeholders only
- [ ] Cross-checked against `rulebook-draft.md` setup

## Tools Reference

Convert this sheet to printable or digital assets:

- **Cards (batch PNG/PDF):** `tools/export-pipeline.md` → `tools/nanDECK-guide.md` — export table to CSV
- **Digital table (optional, after paper works):** `tools/TTS-guide.md`
- **Spreadsheet-driven art:** Component.Studio — see `probability-and-balance.md`

## Next
→ `templates/pnp-checklist.md`
