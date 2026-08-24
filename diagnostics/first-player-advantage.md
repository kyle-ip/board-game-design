# Diagnostic: First Player Advantage

Lint: **BG001**. Related: Ch 2 (`TRN-*`), `cheatsheet.md` Stage 1.

## Symptom

Seat 1 (or fixed start player) wins disproportionately; later seats feel scripted or inferior.

## Evidence to Collect

- Win count by seat over ≥7 games (4p) or ≥10 (2–3p)
- First-round resource/action advantage magnitude
- Whether turn order binds strongly (auctions, worker placement)

## Diagnostic Questions

1. Does seat 1 get strictly better first pick?
2. Is turn order fixed all game?
3. Are scoring opportunities exhaustible left-to-right?
4. Does the game end before seat 4 has equal turns?

## Likely Causes

| Cause | Tell |
|---|---|
| Fixed sequential turn order + scarce first spots | Seat 1 always takes best action |
| Auction without catch-up | Seat 1 sets prices |
| End trigger on round count | Last player one turn short |
| Asymmetric setup favoring seat 1 | Documented in setup |

## Candidate Interventions

| Fix | Risk |
|---|---|
| Bid for start player | Downtime; complexity |
| Stat Turn Order (catch-up) | Feels punitive if overt |
| Rotate start player each round | May not fix within-round binding |
| Asymmetric compensating resources | Hard to tune |
| Simultaneous selection phases | Reduces binding |

## Minimal Experiment

**Variable:** start player selection (fixed → bid 0–3 influence for seat).

**Metric:** Seat 1 win rate.

**Success:** Below 35% over 10 plays (adjust fair share for player count).

## Success Criteria

Win rate by seat within ±10% of equal share after fix, confirmed over N≥10.

## Cross-References

- `diagnostics/runaway-leader.md` if seat 1 also snowballs
- Ch 2 turn order patterns
