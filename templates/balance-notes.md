# Balance Notes

Drive from failure-mode tells. See `probability-and-balance.md`, `balance/README.md`, `diagnostics/`. Copy into the project folder.

Use `templates/balance-spreadsheet.md` for numeric work. One fix per pass — `experiments/framework.md`.

## Build
| Field | Value |
|---|---|
| Version | |
| Date | |
| Playtests informing this pass | |

## Observed Tells
Mark any that appeared in 2+ playtests. Load matching `diagnostics/*.md` before fixing.

| Failure mode | Seen? | Evidence | Diagnostic |
|---|---|---|---|
| Snowball / runaway leader | | | runaway-leader |
| Kingmaking | | | kingmaking |
| Dominant strategy | | | dominant-strategy |
| Turtling | | | cheatsheet |
| Lucky runaway | | | randomness-dominates-skill |
| Analysis paralysis | | | analysis-paralysis |
| First-player advantage | | | first-player-advantage |
| Dead last with no agency | | | low-agency |

## Currency & Curve Audit
| Check | OK? | Note |
|---|---|---|
| Victory currency ≠ working currency | | |
| Set-collection curve (not linear) | | |
| Engine → pivot timing exists | | |
| Catch-up is subtle, not punitive | | |

## Dice / Probability (if any)
| Question | Answer |
|---|---|
| Dice pools / rerolls / thresholds involved? | |
| Intuition failed? → run McDie before locking numbers | |
| Key % you care about (hit / bust / explode) | |

## Changes This Pass
| Change | Expected effect | Measure next playtest | Experiment ID |
|---|---|---|---|
| | | | |

## Decision Rule
Spot tell in 2+ playtests → apply **one** fix → measure in the next playtest. Do not stack three balance changes at once.

Global rule: `SKILL.md` Hard Invariant #3 — minimal intervention.

## Sync

- [ ] `design-state.md` risks updated
- [ ] `iteration.md` if version bump
