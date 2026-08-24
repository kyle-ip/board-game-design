# Changelog

All notable changes to the board-game-design skill follow [Semantic Versioning](https://semver.org/).

## [2.0.0] — 2026-08-24

### Added

- **Design state** — `templates/design-state.md` as single source of truth for Locked / Open / Rejected decisions
- **Agent modes** — Create, Diagnose, Experiment, Balance, Prototype routing in `SKILL.md`
- **Hard invariants** — read design-state first; diagnose before changing; minimal intervention
- **Reasoning** — `reasoning/design-reasoning.md`, `decision-matrix.md`, `hypothesis-rules.md`
- **Experiments** — `experiments/framework.md`; templates `hypothesis.md`, `experiment.md`, `decision.md`, `iteration.md`
- **Diagnostics** — eight symptom guides in `diagnostics/` with unified schema
- **Kill criteria** — `kill-criteria.md` three-way decision gate (Continue / Restructure / Pause or Kill)
- **Design linter** — `lint/rules.md` (BG001–BG014), `lint/checklist.md`
- **Balance tools** — `balance/balance-model.md`, `value-budget.md`; `templates/balance-spreadsheet.md`
- **Theme & experience** — `theme-and-experience.md` companion (MDA depth, theme-mechanism matrix, emotion curve)
- **Tool guides** — `tools/nanDECK-guide.md`, `tools/TTS-guide.md`
- **Example project** — `templates/examples/micro-scavenger/` format reference

### Changed

- `SKILL.md` — v2.0.0; extended Default Project Outputs; companion index
- `workflow.md` — milestones with allowed stage regression; kill-criteria gate at Stage 3
- `cheatsheet.md` — mixed-demand priority tree; Diagnose mode routing; lint reference
- `playtesting.md` — experiment framework and kill-criteria cross-refs
- `probability-and-balance.md` — links to balance/ and diagnostics/
- All project templates — cross-refs to design-state, experiments, tools, examples

### Not changed (by design)

- 13 mechanism chapters — no expansion; patterns.md unchanged in scope
- `probability-and-balance.md` location — soft-linked via `balance/README.md` to preserve existing URLs

## [1.0.0] — initial release

- 13 Building Blocks mechanism chapters, patterns, cheatsheet, glossary
- Workflow stages 0–5, playtesting frameworks, probability & balance rules
- PnP templates: concept brief through balance notes
