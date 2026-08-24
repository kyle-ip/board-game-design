# Value Budget

Per-component value worksheet. One row per card, action, or upgrade. Copy rows into `templates/balance-spreadsheet.md`.

## Row Template

| Field | Meaning |
|---|---|
| id | CARD-012 |
| cost | Resources + actions spent |
| immediate VP | Scored now |
| delayed VP | Expected later (note round) |
| resource gen | +N resource/turn (discounted) |
| tempo | First-mover, extra action |
| information | Draw, peek, steal info |
| risk | Variance / push-your-luck |
| **total est.** | Sum in VP-equiv |
| **target band** | cost × 0.9 – 1.1 typical |
| **confidence** | Low / Medium / High — how sure is this estimate? |
| **calibration source** | heuristic / playtest / data — where anchors came from |
| **use scope** | comparison only — e.g. "within this card set", not cross-game |

## Calibration Metadata (required per row or per pass)

Every VP-equivalent is a **heuristic**, not empirical truth. State explicitly:

```
Wood value: 0.7 VP-equiv
Confidence: Low
Calibration source: heuristic (baseline: 2 wood → 1 VP action)
Use scope: Compare cards within this game only — not portable
```

Do not present spreadsheet totals as proven balance facts. Recommend playtest before shipping numeric changes.

## Example Row

**Card: Iron Mine** — Cost 3, Immediate VP 0, +1 metal/turn for 3 rounds, tempo 0.

```
Immediate VP:     0
Delayed VP:       1 metal/round × 3 rounds × 0.7 VP/metal ≈ 2.1
Tempo:            0
Information:      0
Risk:             0
Total estimated:  2.1 VP-equiv
Cost paid:        3 resources ≈ 2.1 VP if 0.7/resource
Target band:      1.9 – 2.3 → tune cost or yield
Confidence:       Low
Calibration:      heuristic (0.7 VP/metal from baseline convert action)
Use scope:        Compare engine cards within this game only
```

## Discount Rules (defaults)

| Effect type | Discount |
|---|---|
| Delayed VP round N | × 0.85^(N-1) rough |
| Recurring income | Sum discounted turns until pivot |
| Draw 1 card | ≈ 0.4–0.6 VP-equiv (game dependent) |
| Push-your-luck | −0.2 base + upside estimate |

Tune discounts in `balance-model.md` conversion table.

## Red Flags

- Two cards same cost, total est. differs by >40% → dominant strategy risk
- Cheapest card has highest total est. → rush dominates
- Engine card total est. unbounded (no round cap in model) → BG007 lint

## Cross-References

- Model anchors: `balance-model.md`
- Dominant strategy: `diagnostics/dominant-strategy.md`
- Project sheet: `templates/balance-spreadsheet.md`
