# Design State

**Single source of truth** for the current game project. Copy into the project folder. Agent rule: read this first on every session for an existing project; update after every consequential decision.

Format reference: `templates/examples/micro-scavenger/design-state.md`

## Project Status

| Field | Value |
|---|---|
| Working title | |
| Build / version | e.g. v0.3 |
| Genre profile | euro / party / social-deduction / solo / … — see `genre-profile/` |
| Current milestone | 0 Concept / 1 Core MVP / 2 Structure / 3 Playtest / 4 Polish / 5 Publish |
| Last updated | |

## Version Lineage

Track why this build exists and what it replaced. Detail in `iterations/ITER-*.md` and `decisions/DEC-*.md`.

| Field | Value |
|---|---|
| Previous version | e.g. v0.2 |
| Supersedes | DEC-003, ITER-007 (if any) |
| Reason for bump | One line — why this version |
| Evidence | EXP-012 / PT-005 (links) |

## Locked (do not reopen without new contradicting evidence)

Decisions that are settled. Link to `decisions/DEC-*.md` when formalized.

| Decision | Rationale | Locked on |
|---|---|---|
| | | |

## Open Questions

Unresolved design questions. Do not guess — mark Open until evidence closes them.

| Question | Blocks | Priority |
|---|---|---|
| | | |

## Rejected

Ideas explicitly cut. Prevents re-litigating dead paths. Not all rejected ideas are permanent — note revival conditions.

| Rejected | Why not | Rejected on | Superseded by | Revivable if |
|---|---|---|---|---|
| | | | DEC-xxx / v0.x | new evidence shows… |

## Active Hypotheses

Link to `hypotheses/HYP-*.md` or `experiments/EXP-*.md`. Each row is a **Claim** — falsifiable, with explicit confidence.

| ID | Claim (one line) | Confidence | Evidence refs | Contradictions | Status |
|---|---|---|---|---|---|
| | | Low / Med / High | PT-00X, EXP-00X | — | testing / supported / refuted |

**Confidence rules:** Low = 1–2 plays or intuition; Medium = 3+ partial metrics; High = reproducible metric breach. See `lint/rules.md` Design Confidence Model.

## Recent Evidence

Summaries only — detail lives in playtest logs and experiments.

| Date | Source | Key finding | Confidence |
|---|---|---|---|
| | PT-00X / EXP-00X | | Low / Med / High |

## Current Risks

Top design risks right now (max 5).

1.
2.

## Experiment Backlog

Rank candidates before writing `experiment.md`. Method: `reasoning/experiment-priority.md`. When ≥2 active hypotheses, rank all; otherwise rank 1 is the next test.

| Rank | ID | Impact | Uncertainty | Cost | Score | Rationale |
|---|---|---|---|---|---|---|
| 1 | HYP-00X | H/M/L | H/M/L | H/M/L | | |
| 2 | | | | | | |

### Next Experiment (rank 1)

| Field | Value |
|---|---|
| ID | EXP-00X |
| Objective | |
| Single variable to change | |
| Success criteria (observable) | |

## Kill Criteria Overrides

Project-specific thresholds. Copy defaults from `kill-criteria.md`; override when genre or player count differs. Genre profiles suggest starting values.

| Signal | Yellow | Red | Enabled |
|---|---|---|---|
| first_player_win_rate_4p | 35% | 45% | yes / no |
| avg_fun_restructure | ≤3/5 × 2 sessions | — | yes / no |
| playtime_vs_target | >30% over 2× | >50% over | yes / no |
| rules_questions_mid | >3 per player | same Q 3× | yes / no |
| winner_score_spread | leader +50% | last cannot affect winner | yes / no |

## Sync Rules

After updating this file, also sync when applicable:

- **Locked / Rejected** → `mechanism-skeleton.md` (Rejected Alternatives), `decision.md`
- **Hypotheses / Evidence / Backlog** → `experiment.md`, `playtest-log.md`
- **Version Lineage** → `iteration.md` on bump; link superseded decisions
- **Risks / balance tells** → `balance-notes.md`
