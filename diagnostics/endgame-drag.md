# Diagnostic: Endgame Drag

Lint: **BG012**. Related: Ch 5 (`VIC-*`), `workflow.md` Stage 4.

## Symptom

Final rounds take as long as midgame but add few decisions; players want game to end; anticlimax.

## Evidence to Collect

- Turn count and time in last 2 rounds vs midgame
- Decision count per turn in endgame
- End trigger type (fixed rounds, VP threshold, depletion)
- Whether winner is known before official end

## Diagnostic Questions

1. Does end trigger fire when outcome is already decided?
2. Are endgame turns mostly bookkeeping?
3. Is there a "cleanup phase" every round that grows?
4. Do players stop caring once leader is obvious?

## Likely Causes

| Cause | Tell |
|---|---|
| Fixed round count after winner clear | Padding rounds |
| Engine keeps running post-pivot | No engine shutdown |
| Simultaneous endgame scoring steps | Long resolution |
| High VP threshold with slow accrual | Grind to line |

## Candidate Interventions

| Fix | Risk |
|---|---|
| Earlier or dynamic end trigger | Sudden endings |
| Accelerating VP in final rounds | Swing |
| Leader-triggered end | King runs out clock |
| Cut endgame phases | Less closure |
| Hidden end trigger | Surprise complaints |

## Minimal Experiment

**Variable:** end trigger only (e.g. 10 rounds → first to 15 VP).

**Metric:** last 2 rounds ≤40% of midgame turn time; fun score stable.

## Success Criteria

Median last-round duration ≤ midgame; ≤20% playtests where winner obvious 2+ rounds early without tension.

## Cross-References

- Ch 5 end-game triggers
- `diagnostics/runaway-leader.md`
