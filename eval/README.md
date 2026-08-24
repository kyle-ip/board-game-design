# Skill Evaluation — Maintainer Guide

Manual verification that the **board-game-design** skill changes agent behavior. Not automated — run in Cursor or Claude Code with the skill installed.

## When to Run

- Before bumping `version` in `SKILL.md` (especially minor releases)
- After changes to `SKILL.md`, `workflow.md`, templates, or mode routing
- After adding companions under `reasoning/`, `diagnostics/`, `experiments/`, `lint/`, `balance/`

## How to Run

1. Open a **fresh chat** with the skill active (project or `~/.cursor/skills/board-game-design/`).
2. For each case in [`benchmark-prompts.md`](benchmark-prompts.md), paste the prompt verbatim.
3. Use fixture paths below for Cases B–F (Cases A and C create new files).
4. Mark pass criteria checkboxes in a copy of the scoring sheet (bottom of this file).
5. Record skill version and date.

### Fixture paths

| Case | Mode | Input path | Agent may write to |
|---|---|---|---|
| A | Create | *(none — agent creates)* | `./eval-case-a/` or temp folder |
| B | Diagnose | `eval/fixtures/case-b/` | `./eval-case-b/` or in-place update |
| C | Experiment | *(prompt only)* | user-specified path |
| D | Regression | `eval/fixtures/case-d/` | `./eval-case-d/` — must **preserve** existing logs |
| E | Balance | `eval/fixtures/case-e/` | analysis output (no required write) |
| F | Lint | `eval/fixtures/case-f/` | lint report in chat |

Fixtures are **read-only inputs**. Copy to a working directory if the agent should mutate files (especially Case D).

## Scoring

| Cases passed | Action |
|---|---|
| **6/6** | Safe to ship skill version |
| **4–5/6** | Fix failing mode in `SKILL.md` / companions; re-run failed cases only |
| **≤3/6** | Stop release — re-read Mode → Required Artifacts; reduce context loading |

Minimum for minor release (**2.3+**): **5/6** with Case B or D (Diagnose/Regression) mandatory pass.

## If a Case Fails

| Case | Likely fix location |
|---|---|
| A | `SKILL.md` Create mode, `workflow.md`, `reasoning/design-reasoning.md` |
| B | `cheatsheet.md`, `diagnostics/*`, Hard Invariants |
| C | `experiments/framework.md`, `reasoning/hypothesis-rules.md` |
| D | `kill-criteria.md`, `workflow.md` Regression Protocol |
| E | `balance/value-budget.md`, calibration metadata |
| F | `lint/rules.md`, confidence template |

## Scoring Sheet (copy per run)

```
Skill version: ___
Date: ___
Host: Cursor / Claude Code / other

[ ] Case A — Create
[ ] Case B — Diagnose
[ ] Case C — Experiment
[ ] Case D — Regression
[ ] Case E — Balance
[ ] Case F — Lint

Total: ___/6
Notes:
```

## Cross-References

- Prompts + pass criteria: [`benchmark-prompts.md`](benchmark-prompts.md)
- Format reference: `templates/examples/micro-scavenger/`
- Release history: [`CHANGELOG.md`](../CHANGELOG.md)
