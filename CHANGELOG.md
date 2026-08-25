# Changelog

All notable changes to the **board-game-design** skill follow [Semantic Versioning](https://semver.org/).

Format based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).  
Current skill version: declared in [`SKILL.md`](SKILL.md) YAML frontmatter (`version`).

## [4.0.0] — 2026-08-25

Prototype Architecture 2.0 — fidelity-aware prototyping + Simulate mode (Markdown-compatible). Runtime simulators remain optional companions (`prototype/runtime.md`). Roadmap: `docs/solution-design.md`.

### Added

- **`prototype/`** — `fidelity-ladder.md`, `selection.md`, `runtime.md` (optional-runtime boundary)
- **Simulate mode** in `SKILL.md` — system hypotheses → `templates/simulation-run.md`
- **Core object Prototype** + Hard Invariants: cheapest valid test, system ≠ experience, never auto-fix from sim anomaly
- **Design-state** sections: Prototype State, Simulation Evidence; fidelity / source_type columns
- **Hypothesis / Experiment** fidelity + Evidence Plan fields
- **Lint BG015–BG020** — fidelity mismatch, digital assumption, sim seed/version, unsupported claim, physical required
- **Eval Cases G (Simulate) and J (Fidelity Selection)**; golden `simulation-run-minimal.md`
- **`eval/validators/validate_components.py`** + `tools/examples/cards.json`
- Fidelity-aware **experiment priority** (Evidence Gap × Decision Relevance)

### Changed

- **`SKILL.md`** — v4.0.0; Prototype mode fidelity-routed; default = cheapest valid fidelity (paper still usual P4)
- **`workflow.md`**, **`cheatsheet.md`** — Simulate in priority tree; fidelity selection before PnP
- **`lint/rules.md`** — Evidence types in Design Confidence Model
- **`eval/validators/validate.py`** — optional v4 sections; simulation-run structural checks when present
- **`tools/export-pipeline.md`** — component validator is live

## [3.0.0] — 2026-08-25

Validation & Automation release (v3 roadmap per architecture review).

### Added

- **`eval/validators/validate.py`** — structural artifact validator (design-state sections, EXP/HYP IDs, single-variable experiments)
- **`eval/golden/`** — golden schemas for design-state, experiment, hypothesis, playtest-log
- **`genre-profile/`** — euro, party, social-deduction, solo profiles with kill-criteria defaults
- **`routing/symptom-index.md`** — formal symptom routing ontology
- **`tools/component-schema.json`** — JSON schema for card export
- **`tools/export-pipeline.md`** — components-sheet → CSV → nanDECK → PnP pipeline
- **`tools/examples/cards.csv`** + **`cards.nde`** — working nanDECK example
- **Design Confidence Model** in `lint/rules.md` — Claim → Evidence → Confidence → Contradiction → Decision
- **Kill Criteria Overrides** section in `templates/design-state.md`
- **Dependency dimensions** (interaction, combo, timing) in `balance/value-budget.md`

### Changed

- **`SKILL.md`** — v3.0.0; genre routing; Core Objects; Diagnose loads `routing/symptom-index.md`; Prototype loads export pipeline
- **`eval/README.md`** — two-layer eval (structural + behavior); `--fixture-all` gate
- **`kill-criteria.md`** — default thresholds + override protocol; genre-aware notes
- **`templates/design-state.md`** — Genre profile, Claim/Confidence/Evidence refs/Contradictions columns
- **`templates/hypothesis.md`** — Claim, Evidence refs, Contradictions, Confidence
- **`templates/balance-spreadsheet.md`** — interaction/combo/timing columns
- **`cheatsheet.md`** — genre + symptom-index routing
- **`tools/nanDECK-guide.md`** — links to export pipeline and examples
- **`templates/components-sheet.md`** — export pipeline cross-ref
- **`eval/fixtures/`** — aligned with v3 structural checks (Cases B–F)

## [2.3.1] — 2026-08-24

Branding and README polish (Loop Hex identity + book-to-skill-style layout).

### Added

- **`assets/`** — Loop Hex cover (`banner.svg` / `banner.png`) and shareable logo (`logo.svg` / `logo.png`); PNG for local Markdown preview, SVG as source

### Changed

- **`README.md`** — hero banner, shields badges, table-of-contents nav, Why / How it works sections, collapsible prompt examples; display name **Board Game Design** (skill id unchanged: `board-game-design`)
- **`.gitignore`** — ignore `node_modules/` (asset export tooling)

## [2.3.0] — 2026-08-24

Agent decision + evaluation release (per architecture review P0–P2).

### Added

- **`reasoning/experiment-priority.md`** — heuristic ranking (Impact × Uncertainty × Cost) for next experiment
- **`eval/fixtures/`** — minimal project inputs for Cases B, D, E, F
- **`eval/README.md`** — maintainer manual eval workflow and release scoring discipline
- **Confidence Output Template** in `lint/rules.md` (Confidence, Evidence, Signals, Missing)
- **Calibration metadata** on balance rows (`confidence`, `calibration source`, `use scope`)

### Changed

- **`templates/design-state.md`** — Version Lineage, Experiment Backlog, Rejected revival columns
- **`templates/iteration.md`** — Version Lineage block (supersedes, evidence)
- **`templates/balance-spreadsheet.md`** — anchor confidence + per-row conf/calib columns
- **`balance/value-budget.md`** — calibration metadata requirements
- **`SKILL.md`** — Experiment mode loads experiment-priority when backlog unset; `version: 2.3.0`
- **`experiments/framework.md`** — rank before experiment when multiple hypotheses
- **`eval/benchmark-prompts.md`** — fixture paths under `eval/fixtures/`
- **`templates/examples/micro-scavenger/design-state.md`** — backlog + lineage example
- **`lint/checklist.md`** — backlog, lineage, confidence template refs
- **`cheatsheet.md`** — experiment-priority routing for multi-hypothesis sessions
- **`README.md`** — v2.3.0 overview, what's new, eval workflow, prompt examples

## [2.2.0] — 2026-08-24

External resource quality pass: distill high-value URLs into agent-facing companions; demote maintainer bibliography.

### Added

- TTGDA — Tips for New Game Designers, Break My Game Designer Resources, TTGDA Blog (index + `external-resources.md`)
- `tier` / `used-by` metadata and maintainer checklist in `references/web-resources.md`
- Break My Game playtest log cross-ref in `playtesting.md`; TTGDA stage link in `workflow.md` Milestone 0

### Changed

- **`external-resources.md`** — rewritten by Agent Mode (~25 links); `load-when` via section headers
- **`references/web-resources.md`** — maintainer bibliography; core vs optional vs deprecated tiers
- **`SKILL.md`** — external load rule (agents: `external-resources.md` only); `version: 2.2.0`

### Removed (from agent-facing lists)

- BloomWiki MDA, arXiv Dynamics, indienova/qq repost, ResearchGate MTG paper, redundant blogs, fake local PDF paths, Shapeways, paywalled/low-value index bloat

## [2.1.0] — 2026-08-24

Integration patch: close SKILL → Mode → Artifact → State execution chain (per v2.0.1 review).

### Added

- **Mode → Required Artifacts** — explicit write requirements per Create/Diagnose/Experiment/Balance/Prototype in `SKILL.md`
- **Regression Protocol** — milestone rollback checklist in `workflow.md`
- **Evaluation benchmarks** — `eval/benchmark-prompts.md` (Cases A–F with pass criteria)
- Playtest log fields: **Experiment ID**, **Hypothesis ID**, **Variant** (template + micro-scavenger example)

### Changed

- `SKILL.md` — YAML `description` expanded for activation (hypotheses, kill gate, design-state); `version: 2.1.0`
- `SKILL.md` — Companion index links to `eval/benchmark-prompts.md`

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

[2.1.0]: https://github.com/kyle-ip/board-game-design/compare/v2.0.1...v2.1.0
[2.0.1]: https://github.com/kyle-ip/board-game-design/compare/v2.0.0...v2.0.1
[2.0.0]: https://github.com/kyle-ip/board-game-design/compare/v1.0.0...v2.0.0
[1.0.1]: https://github.com/kyle-ip/board-game-design/compare/v1.0.0...v1.0.1
[1.0.0]: https://github.com/kyle-ip/board-game-design/releases/tag/v1.0.0
