# Diagnostic: Insufficient Escalation

Lint: **ED008**. Related: ED003; endgame-drag (BG012); victory / economy chapters.

**Evidence type:** experience + tempo logs. P1 game_length alone ≠ escalation quality.

## Symptom

Power/stakes/options do not grow; endgame feels like early game with more VP; no sense of building toward a climax; "why am I still doing turn-1 actions?"

## Evidence to Collect

- Action quality / options count early vs late
- Score velocity by round
- Player ratings of "did the game escalate?"
- Engine maturity timing vs end trigger

## Diagnostic Questions

1. Is escalation missing in power, stakes, information, or interaction?
2. Does the end trigger fire before engines matter?
3. Is catch-up flattening escalation into mush?
4. Does Target Player `experience.mastery` / `challenge` expect escalation?

## Likely Causes

| Cause | Tell |
|---|---|
| Flat action set | Same menu all game |
| Soft economy | Income never accelerates |
| Early end | Engines unfinished |
| Over-dampening | Catch-up removes peaks |

## Candidate Interventions

| Fix | Risk |
|---|---|
| Mid-game unlock / tech tier | Complexity / runaway |
| Escalating stakes (costs, VP multipliers) | Snowball |
| Phase shift (new actions late) | Teach burden |
| Better end trigger timing | Length variance |

## Minimal Experiment

**Variable:** one escalation lever (unlock, multiplier, or phase).

**Metric:** ≥4/5 players report higher stakes or stronger options in final third.

**Success:** Late-game turns are not identical to opening turns in decision quality.

## Success Criteria

Clear escalation curve without mandatory runaway-leader pathology (check BG003).

## Cross-References

- `diagnostics/flat-emotional-curve.md` (ED003)
- `diagnostics/endgame-drag.md`
- `diagnostics/runaway-leader.md`
