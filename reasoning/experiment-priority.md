# Experiment Priority

Choose **which hypothesis to test next** when multiple options exist. Use in **Diagnose** and **Experiment** modes after reading `design-state.md`.

This is **heuristic ranking**, not mathematical optimization. Scores guide judgment; they do not replace designer intuition.

Prerequisite: every candidate hypothesis must pass `reasoning/hypothesis-rules.md` (falsifiable, one variable).

## When to Run

| Trigger | Action |
|---|---|
| Active Hypotheses ≥ 2 | Rank all testing/draft hypotheses before writing a new `experiment.md` |
| Open Questions with observed symptom | Convert to candidate hypotheses, then rank |
| User asks "what should I test next?" | Load this file + current `design-state.md` |
| Single clear next experiment already in backlog rank 1 | Skip re-ranking; proceed to `experiments/framework.md` |

## Priority Formula (heuristic)

```
Priority ≈ Impact × Uncertainty × (1 / Test Cost)
```

Use **High / Medium / Low** for each factor (do not use decimals).

| Factor | High | Medium | Low |
|---|---|---|---|
| **Impact** | Could invalidate core loop or fix top player complaint | Meaningful but localized (one card type, one phase) | Cosmetic or edge-case |
| **Uncertainty** | No data; conflicting player reports | Some playtest signal but inconclusive | Mostly settled; confirm only |
| **Test Cost** | Full reprint, new components, >3 sessions | One rule tweak + 2 playtests | Table talk / thought experiment only |

**Test Cost inverse:** High cost → treat as Low in formula; Low cost → treat as High.

### Quick score (optional)

Assign 3 / 2 / 1 per factor, multiply: `Impact × Uncertainty × CostInverse`. Higher = test sooner.

Example: Impact High (3) × Uncertainty High (3) × Cost Low → CostInverse High (3) = **27** (top priority).

## Ranking Workflow

1. List candidate hypotheses from **Active Hypotheses** + symptom-linked **Open Questions**.
2. Score each row (Impact, Uncertainty, Test Cost).
3. Sort descending; tie-break by **fewer dependencies** (test the variable that blocks others).
4. Write rank 1 to **Experiment Backlog** in `design-state.md` and draft `experiment.md` for that ID only.
5. After conclusion, re-rank remaining items.

## Example Backlog

| Rank | ID | Impact | Uncertainty | Cost | Score | Rationale |
|---|---|---|---|---|---|---|
| 1 | HYP-002 | High | High | Low | 27 | P1 won 4/7 — cheap seat-order test |
| 2 | HYP-001 | Medium | Medium | Low | 12 | Interaction weak — add one blocking space |
| 3 | HYP-003 | High | Medium | High | 6 | Faction rewrite — only if HYP-002 refuted |

## Anti-Patterns

- Testing the most **interesting** change instead of the most **informative** one
- Stacking rank-1 and rank-2 in one experiment (violates Hard Invariant #3)
- Re-ranking after every chat without new evidence
- Pretending scores are precise ("priority 27.4")

## Cross-References

- Falsifiable hypotheses: `reasoning/hypothesis-rules.md`
- Experiment record: `experiments/framework.md`, `templates/experiment.md`
- State sync: `templates/design-state.md` (Experiment Backlog)
- Symptom routing: `cheatsheet.md` → `diagnostics/*`
