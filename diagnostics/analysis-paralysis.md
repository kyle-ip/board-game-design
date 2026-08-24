# Diagnostic: Analysis Paralysis

Lint: **BG009**. Related: Ch 2, Ch 3, `cheatsheet.md` Universal Tells.

## Symptom

Turns take 5+ minutes; players freeze; downtime while one player calculates; game length explodes.

## Evidence to Collect

- Average turn duration (sample 3 players × 2 rounds)
- Branching factor: choices per turn
- Perfect information surface area
- Player count (AP worsens at 4+)

## Diagnostic Questions

1. How many meaningful choices per turn?
2. Is all information public?
3. Are there combinatorial combos (engine × market × combat)?
4. Does simultaneous selection exist anywhere?

## Likely Causes

| Cause | Tell |
|---|---|
| High branching action points | Many optional micro-actions |
| Full open information | Perfect optimization possible |
| Variable powers on complex base | Cosmic Encounter on heavy framework |
| Long modifier stacks in combat | Resolution drag |

## Candidate Interventions

| Fix | Risk |
|---|---|
| Cut branching / cap actions | May reduce depth |
| Simultaneous selection | Different feel |
| Hide some information | Tracking burden |
| Reference aids / defaults | Band-aid if core too heavy |
| Real-time timer | Stress; wrong for all audiences |

## Minimal Experiment

**Variable:** remove or merge one decision layer (e.g. 5 actions → 3).

**Metric:** median turn time drops ≥30% without fun score drop >0.5/5.

## Success Criteria

Target playtime met; ≤1 min median turn at midgame for medium-weight game (adjust for weight class).

## Cross-References

- Ch 3 action economy
- `diagnostics/endgame-drag.md` if slow only late game
