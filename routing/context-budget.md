# Context Budget

Quantified progressive disclosure per **Agent Mode**. Load only what the mode allows. Eval Case J checks forbidden loads.

Principle: **Always load the smallest file that answers the question** (`SKILL.md`).

## How to use

1. Pick one Mode from `SKILL.md`.
2. Load **required** first (plus project `design-state.md` when ongoing).
3. Load **optional** only if the question needs them.
4. Do **not** load **forbidden** in that mode unless the user explicitly asks for a survey / full dump.

Efficiency self-check (maintainer / eval):

```text
Context Efficiency = required_files_used / total_files_loaded
Target: prefer ≥ 0.6 on focused Diagnose / Simulate / Balance turns
```

---

## Create

```yaml
mode: Create
required:
  - genre-profile/  # one profile
  - workflow.md
  - theme-and-experience.md
  - templates/concept-brief.md
  - templates/design-state.md
  - templates/mechanism-skeleton.md
optional:
  - reasoning/design-reasoning.md
  - reasoning/decision-matrix.md
  - cheatsheet.md
  - patterns.md  # selected entries only
forbidden:
  - chapters/          # bulk — jump by code only if comparing a named mechanism
  - tools/nanDECK-guide.md
  - tools/TTS-guide.md
  - print-specs.md
  - prototype/runtime.md  # unless also planning Simulate
  - eval/
```

---

## Diagnose

```yaml
mode: Diagnose
required:
  - templates/design-state.md  # or project copy
  - routing/symptom-index.md
  - cheatsheet.md              # symptom table as needed
  - diagnostics/               # one primary file
optional:
  - reasoning/experiment-priority.md  # if ≥2 candidate fixes
  - genre-profile/                    # one, if genre mismatch suspected
  - theme-and-experience.md           # if ED* / theme path
  - balance/value-budget.md           # if cost/curve suspected
  - kill-criteria.md
forbidden:
  - all chapters (bulk)
  - tools/export-pipeline.md
  - tools/nanDECK-guide.md
  - print-specs.md
  - prototype/runtime.md
```

---

## Experiment

```yaml
mode: Experiment
required:
  - experiments/framework.md
  - prototype/selection.md
  - templates/experiment.md
  - templates/playtest-log.md
optional:
  - reasoning/experiment-priority.md
  - reasoning/hypothesis-rules.md
  - templates/hypothesis.md
  - diagnostics/   # linked symptom only
forbidden:
  - all chapters (bulk)
  - tools/nanDECK-guide.md
  - print-specs.md
  - eval/
```

---

## Simulate

```yaml
mode: Simulate
required:
  - prototype/fidelity-ladder.md
  - prototype/selection.md
  - prototype/runtime.md
  - templates/simulation-run.md
optional:
  - templates/design-state.md
  - diagnostics/   # if anomaly routing
  - runtime/README.md  # if using companion CLI
forbidden:
  - tools/nanDECK-guide.md
  - print-specs.md
  - all chapters (bulk)
  - theme-and-experience.md  # do not use sim to "prove" fun
```

---

## Balance

```yaml
mode: Balance
required:
  - balance/README.md
  - balance/value-budget.md
optional:
  - balance/balance-model.md
  - templates/balance-spreadsheet.md
  - templates/balance-notes.md
  - probability-and-balance.md
  - templates/design-state.md
forbidden:
  - tools/TTS-guide.md
  - print-specs.md
  - all chapters (bulk)  # jump to one chapter if mechanism-specific
```

---

## Prototype

```yaml
mode: Prototype
required:
  - prototype/selection.md
optional:
  - prototype/fidelity-ladder.md
  - templates/rulebook-draft.md      # P4
  - templates/components-sheet.md    # P4
  - templates/pnp-checklist.md       # P4
  - tools/export-pipeline.md         # P4 export
  - lint/checklist.md
  - runtime/README.md                # P1/P2 companion
forbidden:
  - all chapters (bulk)
  - eval/
  - print-specs.md   # until P5 / production path
```

---

## Cross-References

- Modes: `SKILL.md`
- Fidelity: `prototype/selection.md`
- Eval Case J: `eval/benchmark-prompts.md`
