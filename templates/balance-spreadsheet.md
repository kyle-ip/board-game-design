# Balance Spreadsheet

Copy into project folder. Expand as CSV. See `balance/balance-model.md` and `balance/value-budget.md`.

## Build

| Field | Value |
|---|---|
| Game | |
| Version | |
| VP anchor | e.g. 1 VP = 1 VP; 1 Scrap ≈ 0.5 VP |

## Resource Conversion Baseline

| Action / cost | Yields | ≈ VP-equiv | Notes |
|---|---|---|---|
| Standard gather | 1 resource | | |
| Standard convert | 2 → 1 higher | | |
| Standard score | spend X → Y VP | | |

## Income Curve (solo simulation)

Expected resources **per turn** for average play:

| Turn | Early game | Mid game | Late game |
|---|---|---|---|
| Player A (even) | | | |
| Leader (+1 engine) | | | |
| Trailer | | | |

**Snowball check:** leader income − trailer income at midgame should not exceed ~30% without catch-up.

## Card / Action Value Budget

| id | name | cost | imm VP | delayed VP | resource | tempo | info | risk | total est | target | OK? |
|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | |

## Set Collection Curve (if applicable)

| Set size n | VP reward | Marginal VP (n − (n-1)) |
|---|---|---|
| 1 | 1 | 1 |
| 2 | 3 | 2 |
| 3 | 6 | 3 |
| 4 | 10 | 4 |

Prefer triangular default unless design calls for squaring (small sets).

## Probability Quick Reference

| Setup | Rough success |
|---|---|
| d6 ≤ N | N/6 |
| 2d6 sum ≥ T | use spreadsheet or McDie |
| Draw 1 of N good | 1/N |

Dice pools → McDie (`probability-and-balance.md`).

## Change Log

| Version | Change | Expected effect | Measured |
|---|---|---|---|
| | | | |

One change per row — match experiment framework.

## Cross-References

- Playtest tells: `templates/balance-notes.md`
- Experiments: `templates/experiment.md`
