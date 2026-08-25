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

| ID | Claim | Confidence | Evidence refs | Contradictions | Pref. fidelity | Status |
|---|---|---|---|---|---|---|
| HYP-001 | One-line falsifiable claim | Low/Med/High | PT-001, EXP-002, SIM-001 | — | P1 | testing |

### Recent Evidence (extended)

| Date | Source | Source type | Key finding | Confidence |
|---|---|---|---|---|
| | PT-001 / SIM-001 | physical_playtest / simulation | | Medium |

### Kill Criteria Overrides

Project-specific thresholds. Copy defaults from `kill-criteria.md`; override per genre profile.

| Signal | Yellow | Red | Enabled |
|---|---|---|---|
| first_player_win_rate_4p | 35% | 45% | yes |
| avg_fun_restructure | ≤3/5 × 2 sessions | — | yes |

## v4 Recommended Sections

### Prototype State

| ID | Fidelity | Version | Status | Purpose |
|---|---|---|---|---|
| PRT-001 | P1 | v0.3 | active | first-player test |

### Simulation Evidence

| ID | Runs | Seed | Metric | Finding | Confidence |
|---|---:|---|---|---|---|
| SIM-001 | 1000 | 482193 | first_player_win_rate | 31.8% | Medium |

## ID Conventions

- Hypotheses: `HYP-###`
- Experiments: `EXP-###`
- Playtests: `PT-###`
- Simulations: `SIM-###`
- Prototypes: `PRT-###`
- Decisions: `DEC-###`
- Iterations: `ITER-###`
