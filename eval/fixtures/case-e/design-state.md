# Design State — Forge Duel (Eval Case E)

Fixture for **Case E — Balance**.

## Project Status

| Field | Value |
|---|---|
| Working title | Forge Duel |
| Build / version | v0.6 |
| Current milestone | 4 Polish |
| Last updated | 2026-08-23 |

## Version Lineage

| Field | Value |
|---|---|
| Previous version | v0.5 |
| Supersedes | — |
| Reason for bump | Card set locked for balance pass |
| Evidence | PT-008 |

## Locked

| Decision | Rationale | Locked on |
|---|---|---|
| 2-player only | Duel focus | 2026-08-15 |
| Ore as sole resource | Simple economy | 2026-08-15 |

## Open Questions

| Question | Blocks | Priority |
|---|---|---|
| Is CARD-015 dominant? | balance | high |
| CARD-017 cost fair? | balance | medium |

## Rejected

| Rejected | Why not | Rejected on | Superseded by | Revivable if |
|---|---|---|---|---|
| — | — | — | — | — |

## Active Hypotheses

| ID | Hypothesis | Status |
|---|---|---|
| HYP-003 | CARD-015 total value exceeds cost by >40% vs engine cards | testing |

## Recent Evidence

| Date | Source | Key finding |
|---|---|---|
| 2026-08-23 | PT-008 | Winner bought CARD-015 turn 1 in 4/5 games |

## Current Risks

1. CARD-015 rush may dominate opening
2. Engine cards underpriced relative to rush

## Experiment Backlog

| Rank | ID | Impact | Uncertainty | Cost | Score | Rationale |
|---|---|---|---|---|---|---|
| 1 | HYP-003 | High | Medium | Low | 18 | Dominant rush strategy signal |

### Next Experiment (rank 1)

| Field | Value |
|---|---|
| ID | EXP-003 |
| Objective | Confirm CARD-015 dominance via value audit + 2 playtests |
| Single variable | CARD-015 cost 1 → 2 Ore |
| Success criteria | ≥2 distinct opening buys in 3 playtests |
