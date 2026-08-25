# Skill Evaluation — Maintainer Guide

Manual **behavior** verification plus automated **structural** validation for the **board-game-design** skill.

## When to Run

- Before bumping `version` in `SKILL.md` (especially minor/major releases)
- After changes to `SKILL.md`, `workflow.md`, `prototype/`, templates, or mode routing
- After adding companions under `reasoning/`, `diagnostics/`, `experiments/`, `lint/`, `balance/`, `genre-profile/`, `routing/`, `prototype/`

## Two-Layer Evaluation

| Layer | What | How |
|---|---|---|
| **Structural** | Required sections, IDs, single-variable, sim meta | `python eval/validators/validate.py` |
| **Behavior** | Mode routing, diagnosis, fidelity selection | Manual Cases A–F, G, J below |

Structural checks catch artifact discipline regressions. Behavior checks catch agent reasoning regressions. Both are required for a release.

## Structural Validation (automated)

```bash
# Single project output
python eval/validators/validate.py ./eval-case-a/

# All fixture inputs (smoke test)
python eval/validators/validate.py --fixture-all

# Regression: ensure playtest history preserved
python eval/validators/validate.py ./eval-case-d/ --baseline eval/fixtures/case-d/

# Component JSON against schema (optional)
python eval/validators/validate_components.py tools/examples/cards.json
```

Golden schemas: `eval/golden/`. Validator source: `eval/validators/`.

## Manual Behavior Benchmarks

1. Open a **fresh chat** with the skill active (project or `~/.cursor/skills/board-game-design/`).
2. For each case in [`benchmark-prompts.md`](benchmark-prompts.md), paste the prompt verbatim.
3. Use fixture paths below for Cases B–F (Cases A, C, G, J create new files or analysis).
4. Run structural validator on agent output directory.
5. Mark pass criteria checkboxes in scoring sheet below.
6. Record skill version and date.

### Fixture paths

| Case | Mode | Input path | Agent may write to |
|---|---|---|---|
| A | Create | *(none — agent creates)* | `./eval-case-a/` or temp folder |
| B | Diagnose | `eval/fixtures/case-b/` | `./eval-case-b/` or in-place update |
| C | Experiment | *(prompt only)* | user-specified path |
| D | Regression | `eval/fixtures/case-d/` | `./eval-case-d/` — must **preserve** existing logs |
| E | Balance | `eval/fixtures/case-e/` | analysis output (no required write) |
| F | Lint | `eval/fixtures/case-f/` | lint report in chat |
| G | Simulate | *(prompt only)* | `simulations/SIM-001.md` |
| J | Fidelity | *(prompt only)* | chat analysis |

Fixtures are **read-only inputs**. Copy to a working directory if the agent should mutate files (especially Case D).

## Scoring

| Cases passed | Structural | Action |
|---|---|---|
| **8/8** + all structural | Pass | Safe to ship skill version |
| **6–7/8** | Pass | Fix failing mode; re-run failed cases |
| **≤5/8** or structural fail | Fail | Stop release — re-read Mode → Required Artifacts |

Minimum for **5.0+**: **6/8** behavior with Case B or D mandatory pass, plus Case G or J pass; **all fixtures pass** `--fixture-all`. Cases H/K optional.

## If a Case Fails

| Case | Likely fix location |
|---|---|
| A | `SKILL.md` Create mode, `workflow.md`, `genre-profile/`, `reasoning/design-reasoning.md` |
| B | `routing/symptom-index.md`, `cheatsheet.md`, `diagnostics/*`, Hard Invariants |
| C | `experiments/framework.md`, `reasoning/hypothesis-rules.md` |
| D | `kill-criteria.md`, `workflow.md` Regression Protocol |
| E | `balance/value-budget.md`, calibration + dependency metadata |
| F | `lint/rules.md`, Design Confidence Model |
| G | `prototype/*`, `templates/simulation-run.md`, Simulate mode in `SKILL.md` |
| H | `runtime/` CLI determinism / regress |
| J | `prototype/selection.md`, BG015/BG019, `routing/context-budget.md` |
| K | Diagnosis quality — `diagnostics/`, `reasoning/hypothesis-rules.md` |

## Scoring Sheet (copy per run)

```
Skill version: ___
Date: ___
Host: Cursor / Claude Code / other

Structural (--fixture-all): ___/___

[ ] Case A — Create
[ ] Case B — Diagnose
[ ] Case C — Experiment
[ ] Case D — Regression
[ ] Case E — Balance
[ ] Case F — Lint
[ ] Case G — Simulate
[ ] Case J — Fidelity Selection

Total behavior: ___/8

Optional:
[ ] Case H — Runtime Regression
[ ] Case K — Design Quality (mean rubric ___/5)

Notes:
```

## Cross-References

- Prompts + pass criteria: [`benchmark-prompts.md`](benchmark-prompts.md)
- Golden artifacts: [`golden/README.md`](golden/README.md)
- Format reference: `templates/examples/micro-scavenger/`
- Optional runtime: [`runtime/README.md`](../runtime/README.md)
- Release history: [`CHANGELOG.md`](../CHANGELOG.md)
