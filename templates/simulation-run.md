# Simulation Run

Record one simulation campaign (one hypothesis / one rules version). Copy to project `simulations/SIM-001.md`.

**Runtime optional** — fill metrics from a project-local runner, spreadsheet Monte Carlo, or manual batch of seeded games. See `prototype/runtime.md`.

## Meta

| Field | Value |
|---|---|
| ID | SIM-001 |
| Date | |
| Game version | e.g. v0.4 |
| Rules version | e.g. R-012 |
| Prototype version | e.g. PRT-001 |
| Seed | required for reproducibility |
| Players | |
| Runs | |
| Agent profiles | e.g. random, greedy, adversarial |
| Linked hypothesis | HYP-00X |
| Linked experiment | EXP-00X (if any) |
| Fidelity | P1 |
| Status | planned / complete |

## Objective

One system question this run answers (not "is it fun?").

## Configuration

| Field | Value |
|---|---|
| Simulation profile | first-player-advantage / economy-runaway / dominant-strategy / game-length / custom |
| Runner | none / project-local path / external tool |
| Notes | DIGITAL-ONLY substitutions, if any |

## Metrics

| Metric | Value | Notes |
|---|---|---|
| first_player_win_rate | | |
| average_game_length | | |
| score_spread | | |
| dominant_action_rate | | |
| comeback_rate | | |
| (add rows as needed) | | |

## Anomalies

-

## Conclusion

- [ ] Supports linked hypothesis
- [ ] Refutes linked hypothesis
- [ ] Inconclusive / needs more runs or agent diversity

Summary (system evidence only — do **not** claim fun or physical ergonomics validated):

## Confidence

| Field | Value |
|---|---|
| Confidence | Low / Medium / High |
| Sample size adequate? | yes / no |
| Agent diversity adequate? | yes / no |
| Limitations | |

## Decision

- [ ] Open / update HYP — do not auto-change rules
- [ ] Propose EXP for a single-variable intervention
- [ ] Escalate fidelity (P2/P4) because question is experience/physical

## Sync

- [ ] Updated `design-state.md` — Simulation Evidence + Recent Evidence (`source_type: simulation`)
- [ ] Updated Active Hypotheses confidence / contradictions
