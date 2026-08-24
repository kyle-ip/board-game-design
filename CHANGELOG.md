# Changelog

All notable changes to the **board-game-design** skill follow [Semantic Versioning](https://semver.org/).

Format based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).  
Current skill version: declared in [`SKILL.md`](SKILL.md) YAML frontmatter (`version`).

## [2.0.1] — 2026-08-24

### Removed

- `docs/report 1.md`, `docs/report 2.md`, `docs/report 3.md` — internal improvement analysis; not part of the skill package

### Changed

- `SKILL.md` — link to this changelog from Companion Files index
- `CHANGELOG.md` — complete semver history from initial release through v2

## [2.0.0] — 2026-08-24

Major release: evidence-driven design workflow (state, experiments, diagnostics).

### Added

- **Version field** — `version: "2.0.0"` in `SKILL.md` YAML frontmatter
- **Design state** — `templates/design-state.md` as single source of truth (Locked / Open / Rejected)
- **Agent modes** — Create, Diagnose, Experiment, Balance, Prototype in `SKILL.md`
- **Hard invariants** — read design-state first; diagnose before changing; minimal intervention
- **Reasoning** — `reasoning/design-reasoning.md`, `decision-matrix.md`, `hypothesis-rules.md`
- **Experiments** — `experiments/framework.md`; templates `hypothesis.md`, `experiment.md`, `decision.md`, `iteration.md`
- **Diagnostics** — eight guides in `diagnostics/` (runaway leader, FPA, dominant strategy, AP, low agency, kingmaking, endgame drag, randomness)
- **Kill criteria** — `kill-criteria.md` (Continue / Restructure / Pause or Kill)
- **Design linter** — `lint/rules.md` (BG001–BG014), `lint/checklist.md`
- **Balance tools** — `balance/README.md`, `balance-model.md`, `value-budget.md`; `templates/balance-spreadsheet.md`
- **Theme & experience** — `theme-and-experience.md` companion (MDA, theme-mechanism matrix, emotion curve)
- **Tool guides** — `tools/nanDECK-guide.md`, `tools/TTS-guide.md`
- **Example project** — `templates/examples/micro-scavenger/` format reference
- **Changelog** — this file

### Changed

- `SKILL.md` — core loop, modes, extended Default Project Outputs, companion index, chapter-code direct routing
- `workflow.md` — milestones with allowed regression; kill-criteria gate at Milestone 3
- `cheatsheet.md` — mixed-demand priority tree; Diagnose routing; lint reference
- `playtesting.md` — experiment framework and kill-criteria cross-refs
- `probability-and-balance.md` — links to `balance/` and `diagnostics/`
- `README.md` — v2 layout, **How to prompt** guide with copy-paste examples by mode
- All seven project templates — cross-refs to design-state, experiments, tools, examples

### Not changed (by design)

- 13 mechanism chapters — no expansion; `patterns.md` scope unchanged
- `probability-and-balance.md` path — soft-linked via `balance/README.md` to preserve existing URLs

## [1.0.1] — 2026-08-24

### Changed

- `references/web-resources.md` — curated external link updates

## [1.0.0] — 2026-08-24

Initial public skill package.

### Added

- `SKILL.md` entrypoint with Building Blocks chapter index and mental models
- `chapters/ch01`–`ch13` mechanism distillations (STR / TRN / ACT / RES / VIC / UNC / ECO / AUC / WPL / MOV / ARC / SET / CAR codes)
- `patterns.md`, `cheatsheet.md`, `glossary.md`
- `workflow.md` — stages 0–5
- `playtesting.md` — five playtest frameworks
- `probability-and-balance.md` — failure modes, McDie rule, dice intuition
- `print-specs.md`, `external-resources.md`
- `templates/` — concept brief, mechanism skeleton, rulebook, components sheet, PnP checklist, playtest log, balance notes
- `references/web-resources.md` — extended resource index

[2.0.1]: https://github.com/kyle-ip/board-game-design/compare/v2.0.0...v2.0.1
[2.0.0]: https://github.com/kyle-ip/board-game-design/compare/v1.0.0...v2.0.0
[1.0.1]: https://github.com/kyle-ip/board-game-design/compare/v1.0.0...v1.0.1
[1.0.0]: https://github.com/kyle-ip/board-game-design/releases/tag/v1.0.0
