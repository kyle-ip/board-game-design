# Design State

**Single source of truth** for the current game project. Copy into the project folder. Agent rule: read this first on every session for an existing project; update after every consequential decision.

Format reference: `templates/examples/micro-scavenger/design-state.md`

## Project Status

| Field | Value |
|---|---|
| Working title | |
| Build / version | e.g. v0.3 |
| Current milestone | 0 Concept / 1 Core MVP / 2 Structure / 3 Playtest / 4 Polish / 5 Publish |
| Last updated | |

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

Ideas explicitly cut. Prevents re-litigating dead paths.

| Rejected | Why not | Rejected on |
|---|---|---|
| | | |

## Active Hypotheses

Link to `hypotheses/HYP-*.md` or `experiments/EXP-*.md`.

| ID | Hypothesis (one line) | Status |
|---|---|---|
| | testing / supported / refuted | |

## Recent Evidence

Summaries only — detail lives in playtest logs and experiments.

| Date | Source | Key finding |
|---|---|---|
| | PT-00X / EXP-00X | |

## Current Risks

Top design risks right now (max 5).

1.
2.

## Next Experiment

| Field | Value |
|---|---|
| ID | EXP-00X |
| Objective | |
| Single variable to change | |
| Success criteria (observable) | |

## Sync Rules

After updating this file, also sync when applicable:

- **Locked / Rejected** → `mechanism-skeleton.md` (Rejected Alternatives), `decision.md`
- **Hypotheses / Evidence** → `experiment.md`, `playtest-log.md`
- **Risks / balance tells** → `balance-notes.md`
