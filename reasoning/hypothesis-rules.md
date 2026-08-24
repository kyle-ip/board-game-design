# Hypothesis Rules

Every design hypothesis must be **falsifiable** with observable evidence. Use in Experiment mode and when writing `hypothesis.md` / `experiment.md`.

## Hard Rule

> **Every hypothesis must state observable evidence and a pass/fail threshold.**

Vague hypotheses are not allowed in project files.

## Bad vs Good

| Bad (reject) | Good (accept) |
|---|---|
| "Players should feel more tension." | "In 4/5 playtests, at least 3 players change their plan in the final two rounds due to resource scarcity." |
| "This mechanism should be more fun." | "In 5 playtests, players voluntarily choose this action ≥3 times when alternatives exist (not only when forced by rules)." |
| "First player advantage should be reduced." | "Player 1 win rate drops below 35% over 10 plays (baseline: 58%)." |
| "The game should be faster." | "Median playtime ≤45 min with ≤10% rules questions after play 3." |

## Hypothesis Template

```
We believe [design change / mechanism choice]
will cause [observable player behavior or metric]
because [causal reasoning].

Success: [metric threshold]
Failure: [what would refute the hypothesis]
```

## Threshold Guidelines

Thresholds need not be universal — tune to project — but must be **written before the test**.

| Signal type | Example threshold |
|---|---|
| Win rate / seat bias | ±15% from fair share |
| Subjective fun | ≥3.5/5 average over N sessions |
| Rules friction | ≤2 clarifying questions per player per game (mid stage) |
| Strategy diversity | ≥2 distinct winning paths in N playtests |
| Downtime | No player idle >2 min without a decision |

## One Variable Rule

Each hypothesis tests **one design variable**. If you change income, turn order, and VP curve simultaneously, you cannot attribute results.

See also: Hard Invariant #3 in `SKILL.md` — minimal intervention.

## Lifecycle

| Status | Meaning |
|---|---|
| **Draft** | Written, not yet tested |
| **Testing** | Experiment in progress |
| **Supported** | Success criteria met → consider Lock in `design-state.md` |
| **Refuted** | Failure criteria met → Reject or revise |
| **Inconclusive** | Run again with clearer metric or larger N |

## Cross-References

- Experiment record: `templates/experiment.md`
- Playtest session: `templates/playtest-log.md`
- Update state: `templates/design-state.md`
