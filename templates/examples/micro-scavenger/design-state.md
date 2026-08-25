# Design State — Micro Scavenger (Example)

## Project Status

| Field | Value |
|---|---|
| Working title | Micro Scavenger |
| Build / version | v0.2 (example) |
| Genre profile | euro |
| Current milestone | 3 Playtest |
| Last updated | 2026-08-24 |

## Version Lineage

| Field | Value |
|---|---|
| Previous version | v0.1 |
| Supersedes | DEC-001 (hand size locked at 3 in v0.1) |
| Reason for bump | VP-from-sets rule + end trigger locked after PT-002 |
| Evidence | PT-002, DEC-002 |

## Locked

| Decision | Rationale | Locked on |
|---|---|---|
| 2 players only | Tension in 2p market; 3p untested | 2026-08-20 |
| 24-card deck + discard market | Fits 10 min; teach in 2 min | 2026-08-20 |
| VP from converted sets, not raw cards | Prevents hoarding without combo | 2026-08-22 |
| Game ends when deck empty | Natural clock | 2026-08-22 |

## Open Questions

| Question | Blocks | Priority |
|---|---|---|
| Is 3-card hand too swingy? | balance | medium |
| Need tie-breaker rule? | rulebook | low |

## Rejected

| Rejected | Why not | Rejected on | Superseded by | Revivable if |
|---|---|---|---|---|
| Auction for first pick | Too heavy for 10 min family | 2026-08-21 | — | never for this audience |
| Dice combat for scraps | Output randomness; wrong feel | 2026-08-21 | — | — |

## Active Hypotheses

| ID | Claim | Confidence | Evidence refs | Contradictions | Status |
|---|---|---|---|---|---|
| HYP-001 | Limiting hand to 2 cards increases discard pile tension without AP | Medium | PT-002 | — | testing |

## Recent Evidence

| Date | Source | Key finding |
|---|---|---|
| 2026-08-23 | PT-002 | Winner had 3-card hand all game — swing felt high |

## Current Risks

1. First-player advantage if best card always top of deck
2. Dominant "convert early" strategy untested at 2p skill gap

## Experiment Backlog

| Rank | ID | Impact | Uncertainty | Cost | Score | Rationale |
|---|---|---|---|---|---|---|
| 1 | HYP-001 | Medium | Medium | Low | 12 | Directly tests swing complaint from PT-002 |
| 2 | (HYP-002 draft) | High | High | Low | 27 | First-player fix — rank after hand-size test unless seat data worsens |

### Next Experiment (rank 1)

| Field | Value |
|---|---|
| ID | EXP-001 |
| Objective | Test hand size 3 vs 2 |
| Single variable | max hand size |
| Success criteria | Both players reach discard fight in 4/5 games; fun ≥3.5/5 |

## Kill Criteria Overrides

| Signal | Yellow | Red | Enabled |
|---|---|---|---|
| first_player_win_rate_4p | 35% | 45% | yes |
| avg_fun_restructure | ≤3/5 × 2 | — | yes |
| playtime_vs_target | >30% over 2× | >50% over | yes |
