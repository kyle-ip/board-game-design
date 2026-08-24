# Experiment Framework

Upgrade playtests from **logging** to **experiment management**. Use in **Experiment** mode.

Prerequisite: read `reasoning/hypothesis-rules.md`. Every experiment links to one falsifiable hypothesis. When multiple hypotheses compete, rank first via `reasoning/experiment-priority.md` and update **Experiment Backlog** in `design-state.md`.

## When to Write an Experiment

| Situation | Write experiment? |
|---|---|
| Scattershot early playtest | No — log only in `playtest-log.md` |
| Testing one rule change | Yes |
| Comparing two mechanism variants | Yes — two variants, one metric |
| Balance number tweak | Yes — single variable |
| "Let's see how it feels" | No — use hypothesis or defer |

## Experiment Lifecycle

```
Objective → Hypothesis → Design variable (one) → Baseline vs Variant
    → Success criteria → Run playtest(s) → Observed data → Conclusion → Decision
    → Update design-state → Next experiment
```

## Fields (see `templates/experiment.md`)

| Field | Purpose |
|---|---|
| **Experiment ID** | EXP-001, EXP-002, … |
| **Objective** | What design question you are answering |
| **Hypothesis** | Falsifiable claim |
| **Design variable** | The **one** thing that differs |
| **Baseline** | Current build behavior / metric |
| **Variant** | Changed build |
| **Success criteria** | Observable pass threshold |
| **Observed data** | Facts from playtest(s) |
| **Conclusion** | Supported / refuted / inconclusive |
| **Decision** | Keep / revert / iterate |
| **Next experiment** | Follow-up if needed |

## Link to Playtest Log

- One experiment may span 1–3 playtest sessions.
- Each session still gets a `playtest-log.md` entry.
- Playtest log **Hypothesis Under Test** must match the experiment ID.

## Minimal Experiment Examples

| Problem | Variable | Baseline → Variant | Metric |
|---|---|---|---|
| First-player advantage | Start player selection | fixed → bid 0–3 for seat | P1 win rate |
| Resource competition too low | Income | 4/round → 3/round | contested spaces per round |
| Endgame drag | End trigger | fixed rounds → VP threshold | median turn count last 3 games |
| Blocking frustration | Worker spaces | 5 → 3 spaces | negative blocking comments + win rate spread |

## Anti-Patterns

- Changing three rules "while we're at it"
- No baseline metric recorded
- Concluding "players liked it" without a pre-defined criterion
- Skipping `design-state.md` update after conclusion

## Cross-References

- Hypothesis rules: `reasoning/hypothesis-rules.md`
- Playtest frameworks: `playtesting.md`
- Kill gate after repeated failure: `kill-criteria.md`
- Template: `templates/experiment.md`
