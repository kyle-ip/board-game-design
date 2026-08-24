# Balance Model

Relative value framework for internal consistency. Not a substitute for playtesting — a sanity check before and after tests.

Use with `value-budget.md` and `templates/balance-spreadsheet.md`. Every VP-equivalent estimate needs **confidence**, **calibration source**, and **use scope** (comparison within this game only) — see `value-budget.md` Calibration Metadata.

## Value Dimensions

Express values in **VP-equivalents** (arbitrary unit) for comparison only.

| Dimension | What it measures | Example proxy |
|---|---|---|
| **Resource value** | Working currency | 1 Wood ≈ 0.7 VP if buyable |
| **Action value** | One standard action | 1 Action ≈ 2.5 VP opportunity cost |
| **Tempo value** | Acting before opponent | First pick ≈ +0.5 VP |
| **VP value** | Direct points | 1 VP = 1 VP |
| **Information value** | Hidden knowledge edge | Peek 2 cards ≈ +0.3 VP |
| **Position value** | Board/seat advantage | Best space ≈ +1 VP |
| **Risk value** | Variance exposure | Push-your-luck slot ≈ −0.2 to +0.8 VP |

Calibrate anchors from your game's **baseline action** (e.g. "spend 2 resources → 3 VP" sets resource ≈ 1.5 VP each).

## Conversion Table (project)

Fill for your game; leave blank in template until first balance pass.

| Unit | ≈ VP | ≈ Actions | Notes |
|---|---|---|---|
| 1 [resource A] | | | |
| 1 [resource B] | | | |
| 1 standard action | | 1 | |
| 1 card draw | | | |

## Consistency Checks

| Check | Rule |
|---|---|
| Transitive costs | If A→B and B→C, A→C should not strictly dominate printed costs |
| Engine compounding | Income per turn should not grow unbounded without pivot |
| Early vs late | Late-game actions may worth more VP — document intentionally |
| Catch-up | Behind-player action worth more? Note in model, don't hide |

## Tempo Curve

Sketch expected VP per round for a "average" player:

| Round | Expected VP accumulated | Expected resources |
|---|---|---|
| 1 | | |
| 2 | | |
| 3 | | |
| End | | |

Flat or accelerating — both OK if intentional. **Decelerating trailing players** across 3+ rounds → runaway risk.

## Cross-References

- Failure tells: `probability-and-balance.md`
- Per-card budget: `value-budget.md`
- Experiment one variable: `experiments/framework.md`
