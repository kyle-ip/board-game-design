# Design State — Orchard Run (Eval Case B)

Fixture for **Case B — Diagnose**. Symptom: "fine but nothing exciting happens" after 3 playtests.

## Project Status

| Field | Value |
|---|---|
| Working title | Orchard Run |
| Build / version | v0.4 |
| Current milestone | 3 Playtest |
| Last updated | 2026-08-20 |

## Version Lineage

| Field | Value |
|---|---|
| Previous version | v0.3 |
| Supersedes | — |
| Reason for bump | Added market row after PT-002 feedback |
| Evidence | PT-003 |

## Locked

| Decision | Rationale | Locked on |
|---|---|---|
| 3–4 players, 60 min | Target family weight | 2026-08-10 |
| Pick-and-deliver core loop | Teach in 5 min | 2026-08-10 |
| Closed economy (no trading) | Faster turns | 2026-08-12 |

## Open Questions

| Question | Blocks | Priority |
|---|---|---|
| Why does midgame feel flat? | next iteration | high |
| Is apple VP curve too linear? | balance | medium |

## Rejected

| Rejected | Why not | Rejected on | Superseded by | Revivable if |
|---|---|---|---|---|
| Real-time harvest phase | Too chaotic for audience | 2026-08-11 | — | never for this audience |

## Active Hypotheses

| ID | Hypothesis | Status |
|---|---|---|
| HYP-001 | Adding a contested market row increases midgame tension without AP | draft |
| HYP-002 | End trigger at 12 VP instead of 15 shortens drag | draft |

## Recent Evidence

| Date | Source | Key finding |
|---|---|---|
| 2026-08-18 | PT-001 | All players finished; avg fun 3.2/5 |
| 2026-08-19 | PT-002 | "Fine but nothing exciting happens" (3/4 players) |
| 2026-08-20 | PT-003 | Turns 4–7 identical: pick orchard → deliver → repeat |

## Current Risks

1. Low agency in midgame — optimal path obvious after turn 3
2. No interaction on deliveries
3. Endgame drag untested at 4p

## Experiment Backlog

| Rank | ID | Impact | Uncertainty | Cost | Score | Rationale |
|---|---|---|---|---|---|---|
| 1 | HYP-001 | High | High | Low | 27 | Addresses flat midgame symptom directly |
| 2 | HYP-002 | Medium | Medium | Low | 12 | May help but doesn't add interaction |

### Next Experiment (rank 1)

| Field | Value |
|---|---|
| ID | EXP-001 |
| Objective | Test if contested market row fixes midgame flatness |
| Single variable | add shared market row (3 slots) |
| Success criteria | ≥3/4 players change plan midgame in 2/3 playtests; fun ≥3.5/5 |
