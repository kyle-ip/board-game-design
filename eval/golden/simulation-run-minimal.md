# Simulation Run — Golden Minimal

```markdown
## Meta
| ID | SIM-001 |
| Game version | v0.4 |
| Rules version | R-012 |
| Simulation version | bgd-runtime-0.1.0 |
| Agent version | params-schema-1 |
| Seed | 482193 |
| Players | 4 |
| Runs | 1000 |
| Agent profiles | random, greedy |
| Population | mixed |
| Linked hypothesis | HYP-017 |
| Fidelity | P1 |
| Status | complete |

## Configuration
| Runner | runtime/bgd-sim |
| Simulation profile | first-player-advantage |

## Objective
Estimate first-player win rate under heuristic / population agents.

## Metrics
| Metric | Value |
| first_player_win_rate | 0.318 |
| average_game_length | 47.2 rounds |
| strategy_distribution | (from JSON) |

## Conclusion
Supports elevated P1 win rate vs 25% fair share — system evidence only.
Does not validate fun or table experience.

## Confidence
Medium — 1000 runs, population mix, single seed family; limitations noted.
```

Required for structural checks when present: **Seed**, **Runs**, **SIM-###** ID, **Fidelity** / P1, hypothesis link, Population or Agent profiles, and explicit non-claim of fun when concluding.
