# Diagnostic: Randomness Dominates Skill

Lint: **BG008**. Related: Ch 4, Ch 6, input vs output randomness.

## Symptom

Outcomes feel arbitrary; winners attribute luck not decisions; skilled players lose to novices repeatedly; "feels random."

## Evidence to Collect

- Input vs output randomness map on core loop
- Win correlation with early random events
- Player quotes post-game
- Rematch desire from losers

## Diagnostic Questions

1. Is randomness **output** (after commitment) on critical paths?
2. Do early random swings determine resources for whole game?
3. Is there mitigation (reroll, insurance, draft)?
4. Does theme promise skill but dice decide combats?

## Likely Causes

| Cause | Tell |
|---|---|
| Output randomness on combat/scoring | Roll to win after committing troops |
| High variance early, low recovery | Bad opening draw ruins game |
| Dice pool without threshold design | Swingy totals |
| Push-your-luck without opt-out | Forced gambling |

## Candidate Interventions

| Fix | Risk |
|---|---|
| Shift to input randomness | Less drama |
| Rerolls / mitigation tokens | Complexity |
| Bound swing (cap losses) | Thematic strain |
| Deterministic early rounds | Slow start |
| McDie tune thresholds | Still feels bad if output type wrong |

## Minimal Experiment

**Variable:** move one critical roll to **before** player commitment (input) on one subsystem.

**Metric:** losers cite "my mistake" ≥3/5 times vs "bad luck."

## Success Criteria

Over 10 plays, win rate correlates with repeated players' prior wins more than seat order; "feels random" ≤2/10 sessions.

## Cross-References

- `cheatsheet.md` Stage 4 uncertainty
- `probability-and-balance.md` McDie section
