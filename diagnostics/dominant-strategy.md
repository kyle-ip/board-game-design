# Diagnostic: Dominant Strategy

Lint: **BG002**. Related: Ch 3, Ch 4, `probability-and-balance.md`.

## Symptom

One path wins regardless of opponents; repeated play converges on same opener; "always do X."

## Evidence to Collect

- Opening moves across 5+ playtests
- Win rate of strategy X vs alternatives
- Whether counters exist on board/cards
- Player statements: "There's no reason to do Y"

## Diagnostic Questions

1. Is one action strictly better in cost/effect?
2. Are alternatives orthogonal or strictly dominated?
3. Does randomness mask dominance until N is large enough?
4. Is dominance a **tempo** issue (first to engine) not a single card?

## Likely Causes

| Cause | Tell |
|---|---|
| Broken cost curve | 2 cost → 5 VP, 3 cost → 2 VP |
| Missing counter | No answer to rush strategy |
| Negative interaction too weak | Solitaire optimal |
| Scoring track linear | One resource always best |

## Candidate Interventions

| Fix | Risk |
|---|---|
| Nerf dominant card/action | May over-correct |
| Add counter card/space | Arms race complexity |
| RPS loop in scoring | Opacity |
| Increase cost of dominant path | Slows game |
| Hidden information | AP; new player pain |

## Minimal Experiment

**Variable:** single cost or effect on dominant option.

**Metric:** ≥2 distinct winning strategies appear in 5 playtests.

**Success:** Dominant path wins ≤60% over 5 sessions after tweak.

## Success Criteria

No strategy wins >50% over 10 playtests at skilled table; players describe trade-offs not a script.

## Cross-References

- `balance/value-budget.md`
- `diagnostics/runaway-leader.md`
