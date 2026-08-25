# Component Export Pipeline

Structured path from design artifacts to printable PnP. Optional — paper hand-drawn prototypes remain valid.

## Pipeline

```text
mechanism-skeleton.md
        ↓
components-sheet.md  (human-editable source of truth)
        ↓
cards.csv / cards.json  (machine export)
        ↓
cards.nde (nanDECK)
        ↓
card_front.png / PDF
        ↓
pnp-checklist.md → print
```

## Step 1 — Components Sheet

Copy `templates/components-sheet.md`. One row per card/tile. Required columns for export:

`id`, `type`, `name`, `qty`, `cost`, `effect`, `tags`, `vp`, `notes`

## Step 2 — Export CSV

Minimum CSV columns for nanDECK (see `tools/examples/cards.csv`):

```csv
id,name,cost,effect,vp,tags
CARD-001,Scrap Hook,0,Take 1 Scrap from discard,0,tool
```

**Convention:**

- Save as `cards.csv` in project root
- `id` must match components-sheet stable codes
- `effect` — plain text; escape commas with quotes in CSV
- Optional JSON export: validate against `tools/component-schema.json`

## Step 3 — nanDECK Script

Copy `tools/examples/cards.nde` to project folder. Adjust:

- `size=63,88` — poker (63×88 mm) or `57,89` tarot
- CSV path in `{(cards.csv)}` references

Run: open nanDECK → load script → F6

Full guide: `tools/nanDECK-guide.md`

## Step 4 — PnP Package

- Generated PNGs/PDF in `print/` subfolder
- `rulebook-draft.md` — run `lint/checklist.md` before print
- `pnp-checklist.md` — verify counts vs components-sheet

## Schema Validation (maintainer)

```bash
python eval/validators/validate_components.py project/cards.json
python eval/validators/validate_components.py tools/examples/cards.json
```

Schema: `tools/component-schema.json`. Example JSON: `tools/examples/cards.json`.

Optional — not required for Markdown agent workflow.

## Cross-References

- nanDECK guide: `tools/nanDECK-guide.md`
- TTS (after paper): `tools/TTS-guide.md`
- Components template: `templates/components-sheet.md`
- Prototype mode: `SKILL.md` Agent Modes
