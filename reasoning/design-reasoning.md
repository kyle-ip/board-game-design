# Design Reasoning

Use in **Create** mode when choosing mechanisms. Do not recommend a single mechanism without comparing alternatives when trade-offs exist.

Load with: `reasoning/decision-matrix.md`, `reasoning/hypothesis-rules.md`.

## Reasoning Chain

Work through in order; write results into `mechanism-skeleton.md` (Candidate Comparison) and `design-state.md`.

```
Design goal
    ↓
Constraints (players, time, complexity, interaction level)
    ↓
Candidate mechanisms (2–4 options)
    ↓
Trade-offs (decision matrix)
    ↓
Expected dynamics (what happens at the table)
    ↓
Failure risks (what could go wrong)
    ↓
Provisional choice + hypothesis to test
```

## Output Template

When the user asks for a mechanism recommendation, produce:

### Design goal
One sentence: what player experience or table dynamic you need.

### Constraints
| Constraint | Value |
|---|---|
| Players | |
| Playtime | |
| Complexity | |
| Interaction target | low / medium / high |
| Other | |

### Candidates
List 2–4 mechanism architectures (with codes where applicable).

### Comparison
Use the matrix in `decision-matrix.md`. Score High / Medium / Low per row.

### Recommendation
Pick one **provisionally** — not locked until playtest evidence supports it.

### Why
2–3 bullets tied to design goal, not generic praise.

### Risks
What could fail; link to `diagnostics/` if known failure mode.

### Test
One minimal experiment (paper tweak or solo run) before locking. Write to `experiment.md`.

## Anti-Patterns

| Do not | Do instead |
|---|---|
| "Use worker placement because it's popular" | Compare WP vs drafting vs market for *this* goal |
| Lock mechanism before core loop sketch | Skeleton loop first, then fit mechanisms |
| Add mechanisms to fix boredom without diagnosis | Diagnose mode → symptom → hypothesis |
| Stack three mechanisms to satisfy every aesthetic | Pick primary dynamic; secondary mechanisms support it |

## Cross-References

- Candidate table format: `templates/mechanism-skeleton.md`
- Symptom-driven changes: `diagnostics/`, `cheatsheet.md`
- Record provisional choice: `design-state.md` (Open until tested; Locked after evidence)
