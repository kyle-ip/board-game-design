# Diagnostic: Runaway Leader (Snowball)

Lint: **BG003**. Related: Ch 5, Ch 7, `probability-and-balance.md`.

## Symptom

Early leader stays ahead; trailing players cannot catch up; game feels decided before end.

## Evidence to Collect

- Score or resource lead by round (round 1, 2, 3, final)
- Whether leader's **income** increases each round
- Victory currency vs working currency (same pool?)
- Win rate by who led at midgame

## Diagnostic Questions

1. Does the leader gain **more** resources/actions per turn than trailers?
2. Are VP and spending currency the same?
3. Is there a pivot from engine-building to scoring, or does engine run unbounded?
4. Do catch-up mechanisms trigger only when game is already over?

## Likely Causes

| Cause | Tell |
|---|---|
| Shared victory/working currency | Leader spends and still leads on VP track |
| Compounding engine | +1 income per building with no sink |
| Positive feedback combat | Winner takes more from loser |
| Exposed VP leader board | Table piles on leader too late |

## Candidate Interventions

| Fix | Risk |
|---|---|
| Split victory vs working currency | May add tracking overhead |
| Declining returns on engine | May feel punitive to leader |
| Catch-up (Stat Turn Order) | Overt catch-up feels bad |
| Hidden VP / delayed scoring | Analysis load; opacity complaints |
| End trigger tied to leader action | Can rush game awkwardly |

## Minimal Experiment

**Variable:** income curve only (e.g. flat 3 vs scaling 3+1 per building).

**Metric:** % of games where trailing player reaches within 20% of leader by final round.

**Success:** ≥50% of playtests show recoverable gap by round N-1.

## Success Criteria

Tell absent in 3 consecutive playtests at target player count, or leader win rate ≤ fair share +10%.

## Cross-References

- `diagnostics/low-agency.md` if trailers also cannot act
- `balance/value-budget.md` for income modeling
