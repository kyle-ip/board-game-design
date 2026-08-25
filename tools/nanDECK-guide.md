# nanDECK Quick Guide

Shortest path from `components-sheet.md` to printable card PNGs/PDF. Free tool: [nanDECK](https://www.nand.it/nandeck/).

Full pipeline: `tools/export-pipeline.md` | Schema: `tools/component-schema.json` | Example: `tools/examples/cards.csv` + `cards.nde`

## Prerequisites

- Filled `components-sheet.md` (or export CSV with columns: id, name, effect, cost, vp, tags)
- nanDECK installed (Windows; Wine/macOS possible)

## 1. Export CSV

From components sheet, minimum columns:

```csv
id,name,cost,effect,vp,tags
CARD-001,Scrap Hook,0,Take 1 Scrap from discard,0,tool
CARD-002,Rusty Gears,1,Trade 1 Scrap for 2 VP,2,trade
```

Save as `cards.csv` in project folder. See `tools/export-pipeline.md` for full convention and `tools/examples/cards.csv` for a working sample.

## 2. Minimal Script (`cards.nde`)

Copy from `tools/examples/cards.nde` or use:

```text
[card]
font=Arial,12,,,#000000
size=63,88
dpi=300
recto=card_front.png
versos=none

[card_front.png]
card=1-{(cards.csv),"id"}
text=1,{(cards.csv),"name"},0,5,100,15,C,#
text=2,Cost: {(cards.csv),"cost"},0,25,100,10,L,#
htmltext=3,{(cards.csv),"effect"},5,40,90,35,L,#
text=4,{(cards.csv),"vp"} VP,0,78,100,10,R,#
```

Adjust `size=63,88` for poker (63×88 mm) or `57,89` for tarot.

## 3. Generate

1. Open nanDECK → load `cards.nde`
2. Run script (F6)
3. Output: `card_front.png` per row, or combined PDF via `pdf=1` directive

## 4. Key Directives

| Directive | Use |
|---|---|
| `HTMLTEXT` | Wrapped rules text with basic formatting |
| `FONT` | Global or per-element font |
| `BORDER` | Cut-friendly borders |
| `DPI=300` | Print quality |

## 5. Print

- Print at 100% scale — do not "fit to page"
- Cardstock 250gsm+ for first external playtest
- Mark `(id)` on card face for prototype edits

## Cross-References

- Component columns: `templates/components-sheet.md`
- PnP hygiene: `templates/pnp-checklist.md`
- Alternative: Component.Studio (spreadsheet-driven, see `probability-and-balance.md`)
