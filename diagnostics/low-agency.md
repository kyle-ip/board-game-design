# Diagnostic: Low Agency / Dead Last

Lint: **BG004**, **BG005**. Related: Ch 2, Ch 5, `probability-and-balance.md`.

## Symptom

Trailing player cannot affect winner; turns feel pointless; "I'm already out"; dead turns with no decision.

## Evidence to Collect

- Whether trailer's actions change leader outcome (kingmaking test)
- Decisions available when losing by X VP
- Elimination or effective elimination timing
- Catch-up mechanism usage rate

## Diagnostic Questions

1. Can a player in last place steal a win in one round?
2. Are there dead turns (nothing useful to do)?
3. Does interaction scale with losing (more tools when behind)?
4. Is scoring opaque so players don't know they're out?

## Likely Causes

| Cause | Tell |
|---|---|
| No catch-up or interaction for trailers | Multiplayer solitaire |
| Elimination without catch-up | Player sits out |
| Runaway leader + no midgame scoring | Gap too large |
| All-or-nothing end scoring | Only final round matters |

## Candidate Interventions

| Fix | Risk |
|---|---|
| Temporary VP grabs / missions | Swingy |
| Catch-up resources (subtle) | Leader frustration |
| Avoid elimination | Longer game with hopeless states |
| Hidden VP | Opacity |
| Kingmaking checks on all interaction | Design audit needed |

## Minimal Experiment

**Variable:** add one midgame scoring opportunity for trailers only (e.g. underdog bonus once).

**Metric:** in 4/5 games, trailer affects who wins (not just kingmaker).

## Success Criteria

No player reports "nothing to do" in 3 consecutive external playtests; dead turns absent at max players.

## Cross-References

- `diagnostics/kingmaking.md`
- `diagnostics/runaway-leader.md`
