# Experiment Priority

Choose **which hypothesis to test next** when multiple options exist. Use in **Diagnose**, **Experiment**, and **Simulate** modes after reading `design-state.md`.

This is **heuristic ranking**, not mathematical optimization. Scores guide judgment; they do not replace designer intuition.

Prerequisite: every candidate hypothesis must pass `reasoning/hypothesis-rules.md` (falsifiable, one variable). Assign fidelity via `prototype/selection.md` before scoring cost.

## When to Run

| Trigger | Action |
|---|---|
| Active Hypotheses ≥ 2 | Rank all testing/draft hypotheses before writing a new `experiment.md` |
| Open Questions with observed symptom | Convert to candidate hypotheses, then rank |
| User asks "what should I test next?" | Load this file + current `design-state.md` |
| System question (balance, win rate, length) | Prefer P1 Simulate path if Formal Model exists — see matrix in `prototype/selection.md` |
| Single clear next experiment already in backlog rank 1 | Skip re-ranking; proceed to `experiments/framework.md` or Simulate |

## Priority Formula (heuristic)

```
Priority ≈ Impact × Uncertainty × Evidence Gap × Decision Relevance × (1 / Test Cost)
```

Use **High / Medium / Low** for each factor (do not use decimals).

| Factor | High | Medium | Low |
|---|---|---|---|
| **Impact** | Could invalidate core loop or fix top player complaint | Meaningful but localized (one card type, one phase) | Cosmetic or edge-case |
| **Uncertainty** | No data; conflicting player reports | Some playtest/sim signal but inconclusive | Mostly settled; confirm only |
| **Evidence Gap** | No appropriate evidence type yet for this claim | Partial / wrong-fidelity evidence only | Adequate evidence of matching type |
| **Decision Relevance** | Blocks Locked decision, prototype gate, or kill gate | Affects near-term backlog | Nice-to-know |
| **Test Cost** | Full reprint, new components, >3 sessions, or heavy digital build | One rule tweak + 2 playtests, or 1k seeded sims | Table talk / thought experiment / smoke sim |

**Test Cost inverse:** High cost → treat as Low in formula; Low cost → treat as High.

**Fidelity lowers cost:** Prefer P1 simulation over P4 reprint when the question is system-only and a Formal Model exists.

### Quick score (optional)

Assign 3 / 2 / 1 per factor, multiply:
`Impact × Uncertainty × EvidenceGap × DecisionRelevance × CostInverse`. Higher = test sooner.

Example: Impact High (3) × Uncertainty High (3) × Evidence Gap High (3) × Decision Med (2) × Cost Low → CostInverse High (3) = **162** (top priority).

## Ranking Workflow

1. List candidate hypotheses from **Active Hypotheses** + symptom-linked **Open Questions**.
2. Assign **preferred fidelity** and **evidence type** (`prototype/selection.md`).
3. Score each row (Impact, Uncertainty, Evidence Gap, Decision Relevance, Test Cost).
4. Sort descending; tie-break by **fewer dependencies** and **lower fidelity**.
5. Write rank 1 to **Experiment Backlog** in `design-state.md`.
6. If fidelity is P1 → Simulate mode + `templates/simulation-run.md`; else Experiment / Prototype path.
7. After conclusion, re-rank remaining items.

## Example Backlog

| Rank | ID | Impact | Uncertainty | Evidence Gap | Cost | Fidelity | Score | Rationale |
|---|---|---|---|---|---|---|---|---|
| 1 | HYP-002 | High | High | High | Low | P1 | — | Seat win rate — cheap seeded sim before reprint |
| 2 | HYP-001 | Medium | Medium | Medium | Low | P4 | — | Interaction weak — needs table feel |
| 3 | HYP-003 | High | Medium | Low | High | P4 | — | Faction rewrite — only if HYP-002 refuted |

## Anti-Patterns

- Testing the most **interesting** change instead of the most **informative** one
- Stacking rank-1 and rank-2 in one experiment (violates Hard Invariant #3)
- Choosing P4 paper when P1 simulation can answer a system question (BG015)
- Claiming High confidence from simulation on an experience question (BG019)
- Re-ranking after every chat without new evidence
- Pretending scores are precise ("priority 27.4")

## Cross-References

- Falsifiable hypotheses: `reasoning/hypothesis-rules.md`
- Fidelity selection: `prototype/selection.md`
- Experiment record: `experiments/framework.md`, `templates/experiment.md`
- Simulation record: `templates/simulation-run.md`
- State sync: `templates/design-state.md` (Experiment Backlog)
- Symptom routing: `cheatsheet.md` → `diagnostics/*`
