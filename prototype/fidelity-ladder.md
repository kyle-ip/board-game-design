# Prototype Fidelity Ladder

Choose the **cheapest fidelity that can answer the current hypothesis**. Do not default to paper PnP or digital UI when a cheaper test suffices.

Load this file in **Simulate** or **Prototype** mode, or when ranking experiments. Selection matrix: `prototype/selection.md`.

## Levels

| Level | Name | Answers | Typical artifacts |
|---|---|---|---|
| **P0** | Formal Game Model | Can the design be stated as structure? | Structured rules YAML/tables (players, actions, resources, victory) — no UI |
| **P1** | Simulation | Do systems behave as claimed? | `simulation-run.md`, metrics, seeded runs — optional project-local runner |
| **P2** | Interactive Digital | Do humans understand and operate the core loop? | Minimal local web/CLI UI over a rules model |
| **P3** | Digital Tabletop | Do multiplayer / social dynamics hold? | TTS, Tabletopia, lightweight multiplayer |
| **P4** | Physical PnP | Does the table experience work? | Rulebook, components-sheet, nanDECK, `pnp-checklist.md` |
| **P5** | Production Prototype | Does manufacturing / finish work? | Near-final components, print specs |

## Hard rules

1. **System evidence ≠ experience evidence** — win rates and resource curves do not prove fun, tension, or clarity.
2. **Digital ≠ physical** — automation (auto-shuffle, instant counting) must be marked `DIGITAL-ONLY` when it diverges from table reality.
3. **Never auto-fix** from a simulation anomaly — Observation → Diagnostic → Hypothesis → Experiment.
4. **Runtime is optional** — this skill requires no simulator package. See `prototype/runtime.md`.

## Genre caveats

| Genre | Simulation (P1) value | Prefer |
|---|---|---|
| Euro / engine / economy | High for balance, length, first-player | P1 before large physical reprints |
| Party | Low | P2/P4 human playtests |
| Social deduction | Limited (info structure only) | P3/P4 humans; do not claim social tension from bots |
| Solo / Automa | Medium–High for difficulty variance | P1 + human solo sessions |

## Cross-References

- Fidelity selection: `prototype/selection.md`
- Runtime boundary: `prototype/runtime.md`
- Simulate mode: `SKILL.md` Agent Modes
- Simulation artifact: `templates/simulation-run.md`
- Physical export: `tools/export-pipeline.md`
