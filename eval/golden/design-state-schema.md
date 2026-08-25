# Design State — Golden Schema

Required sections (validator checks `## Section` headers):

1. Project Status
2. Version Lineage
3. Locked
4. Open Questions
5. Rejected
6. Active Hypotheses
7. Recent Evidence
8. Current Risks
9. Experiment Backlog

## v3 Recommended Fields

### Genre (Project Status table)

| Field | Value |
|---|---|
| Genre profile | euro / party / social-deduction / solo / … |

### Active Hypotheses (extended columns)

| ID | Claim | Confidence | Evidence refs | Contradictions | Status |
|---|---|---|---|---|---|
| HYP-001 | One-line falsifiable claim | Low/Med/High | PT-001, EXP-002 | — | testing |

### Recent Evidence (extended)

| Date | Source | Key finding | Confidence |
|---|---|---|---|
| | PT-001 | | Medium |

### Kill Criteria Overrides

Project-specific thresholds. Copy defaults from `kill-criteria.md`; override per genre profile.

| Signal | Yellow | Red | Enabled |
|---|---|---|---|
| first_player_win_rate_4p | 35% | 45% | yes |
| avg_fun_restructure | ≤3/5 × 2 sessions | — | yes |

## ID Conventions

- Hypotheses: `HYP-###`
- Experiments: `EXP-###`
- Playtests: `PT-###`
- Decisions: `DEC-###`
- Iterations: `ITER-###`
