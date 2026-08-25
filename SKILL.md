---
name: board-game-design
description: "Design and iterate tabletop games with an evidence-driven workflow: genre profiles, Building Blocks mechanisms (13 chapters), falsifiable hypotheses with confidence, fidelity-aware prototyping (simulation → digital → paper PnP), playtest experiments, design-state, symptom routing, diagnosis, balance, automated eval validators, and export pipeline. Invoke when designing or iterating board/card games; diagnosing symptoms (snowball, boredom, unfairness); simulating system hypotheses; running experiments with pass/fail criteria; evaluating continue/restructure/kill; maintaining design-state across sessions; balancing cards and economy; or building print-and-play prototypes."
version: "4.0.0"
license: MIT
compatibility: "Agent Skills hosts (Cursor, Claude Code, and other SKILL.md-compatible runtimes). Markdown-only; no required network or packages."
metadata:
  open-standard: "https://agentskills.io/specification"
  primary-source: "Building Blocks of Tabletop Game Design (Engelstein & Shalev)"
---

# Board Game Design

Knowledge base from *Building Blocks of Tabletop Game Design* by Geoffrey Engelstein & Isaac Shalev (CRC Press, ~517 pages, 13 chapters), plus workflow, playtesting, balance, print guidance, and **project templates** that turn advice into files you can playtest.

**Core loop:** Intent → Model → Claim / Hypothesis → **Select minimum valid fidelity** → Prototype (sim / digital / physical) → Experiment → Evidence → Diagnosis → Decision → update `design-state` → repeat.

**Core objects** (underlying all Modes): **State** (`design-state.md`) · **Claim** (hypothesis with confidence) · **Experiment** (single variable) · **Prototype** (fidelity + version) · **Artifact** (templates output).

Pipeline shorthand: **concept → mechanism skeleton → cheapest valid prototype → playtest/balance → (optional) POD/digital polish**.

## Hard Invariants

Apply on every design or iteration session:

1. **Read design-state first** — for an existing project, load `templates/design-state.md` (or project copy) before proposing changes. Do not reopen **Locked** decisions unless new evidence contradicts them.
2. **Diagnose before changing** — do not change a mechanism before identifying an observed symptom and a plausible causal hypothesis. Load `diagnostics/` or `cheatsheet.md` in Diagnose mode.
3. **Minimal intervention** — change the smallest design variable that can test the hypothesis. One variable per experiment; do not stack three unrelated fixes.
4. **Cheapest valid test first** — pick the lowest fidelity that can answer the hypothesis (`prototype/fidelity-ladder.md`). Do not build higher fidelity than required.
5. **System evidence ≠ experience evidence** — simulation metrics do not prove fun, tension, or clarity; digital play does not replace physical validation when `physical_dependency` is true.
6. **Never auto-fix from a simulation anomaly** — Observation → Diagnostic → Hypothesis → Experiment. Do not silently change costs or rules from a metric spike.

## Agent Modes

Pick one mode per session. Load the smallest file set that mode requires.

| Mode | Trigger | Load first | Write / update |
|---|---|---|---|
| **Create** | New game from scratch | `genre-profile/` (one) + `workflow.md`, `theme-and-experience.md` | concept-brief, design-state, mechanism-skeleton |
| **Diagnose** | Symptom (boring, broken, unfair) | `routing/symptom-index.md` → `cheatsheet.md` → `diagnostics/*`; if ≥2 candidate fixes, also `reasoning/experiment-priority.md` | design-state, decision |
| **Experiment** | Test a specific hypothesis (human playtest) | `experiments/framework.md` + `prototype/selection.md`; if ≥2 hypotheses, also `reasoning/experiment-priority.md` | experiment, playtest-log |
| **Simulate** | System question (balance, win rate, length, dominant strategy) | `prototype/fidelity-ladder.md`, `prototype/selection.md`, `prototype/runtime.md` | simulation-run, design-state Evidence |
| **Balance** | Numbers, cards, economy | `balance/README.md` | balance-spreadsheet, balance-notes |
| **Prototype** | Build at chosen fidelity (often PnP) | `prototype/selection.md`; then P4 → `templates/*`, `tools/export-pipeline.md` | rulebook/components/pnp **or** sim/digital plan per fidelity |

Mixed requests (e.g. "design + PnP + balance"): run **Diagnose/Balance before Create/Prototype** if symptoms exist; system questions → **Simulate** before large physical builds; else **Create → Prototype → Balance**. See `cheatsheet.md` priority tree.

## Mode → Required Artifacts

Every session on an **ongoing project** must read and update `design-state.md`. Prose-only advice is not enough when templates apply.

| Mode | Required writes (project folder) | Also update when… |
|---|---|---|
| **Create** | `concept-brief.md`, `design-state.md`, `mechanism-skeleton.md` | Locked/Rejected land in design-state; compare 2–4 candidates in skeleton |
| **Diagnose** | `design-state.md`, `decision.md` (if intervention chosen) | Symptom routed via `diagnostics/*`; no rule change before hypothesis; note preferred fidelity |
| **Experiment** | `experiment.md`, `playtest-log.md` (linked by EXP/HYP IDs) | Update **Experiment Backlog**; Evidence Plan fidelity; conclusion → design-state Evidence |
| **Simulate** | `simulation-run.md` (SIM ID); update design-state Simulation Evidence | Seed, sample size, agent profiles, confidence; do not claim fun validated |
| **Balance** | `balance-notes.md`; `balance-spreadsheet.md` when numeric | One fix per pass; link to experiment/sim if testing one variable |
| **Prototype** | Per fidelity: P4 → rulebook, components-sheet, pnp-checklist; else fidelity plan + Prototype State row | Run `lint/checklist.md` before P4 delivery |

**After any consequential decision:** update `design-state.md`; write `decision.md`; on version bump write `iteration.md`. After 3+ playtests run `kill-criteria.md` gate.

Format reference for all project files: `templates/examples/micro-scavenger/`.

## How to Use This Skill

**Invocation patterns:**

- **No argument** — return this file (overview + indexes).
- **Mechanism code** (e.g., `WPL-03`, `CAR-05`) — jump directly to the matching `chapters/chNN-*.md` from the Chapter Index below; skip cheatsheet unless trade-offs are unclear.
- **Topic** (e.g., "auctions", "worker placement") — load matching chapter + relevant `patterns.md` entry.
- **Chapter number** (e.g., "ch07") — load that chapter file.
- **Decision needed** — load `cheatsheet.md`; cross-ref `patterns.md` and `reasoning/decision-matrix.md`.
- **Term lookup** — load `glossary.md`.
- **Design / iterate a game** — follow **Default Project Outputs**; load `genre-profile/` + `workflow.md` + needed templates. Output format: `templates/examples/micro-scavenger/`.
- **Genre** (euro, party, social-deduction, solo) — load matching `genre-profile/*.md`; set in design-state Project Status.
- **Vague symptom** — load `routing/symptom-index.md` before diagnostics.
- **System / balance simulation** — load `prototype/selection.md` → Simulate mode; write `simulation-run.md`.
- **After playtests** — load `kill-criteria.md` for Continue / Restructure / Pause-or-Kill gate.
- **Before shipping artifacts** — run `lint/checklist.md`.
- **External links** (tools, publishing, further reading) — load `external-resources.md` only. **Never** load `references/web-resources.md` unless maintaining the skill.

**Always load the smallest file that answers the question.** Do not bulk-load chapters unless the user asks for a survey.

## Default Project Outputs

When the user asks to design, iterate, prototype, or develop a tabletop game, **write project files** (copy from `templates/`; do not only give prose). Prefer the user's project directory; if none, ask where to put them.

| When | Write | From template |
|---|---|---|
| Any ongoing project | design state (maintain) | `templates/design-state.md` |
| 0 Concept | concept brief | `templates/concept-brief.md` |
| 1–2 Mechanisms | mechanism skeleton (+ candidate comparison) | `templates/mechanism-skeleton.md` |
| System hypothesis | simulation run (+ Formal Model notes) | `templates/simulation-run.md` |
| 1 Playable MVP | fidelity-selected prototype (often paper PnP) | `rulebook-draft.md`, `components-sheet.md`, `pnp-checklist.md` for P4 |
| 3 Playtest | playtest log; experiment if testing one variable | `playtest-log.md`, `experiment.md` |
| 3+ Decision | decision record | `templates/decision.md` |
| 4 Balance | balance notes + spreadsheet | `balance-notes.md`, `balance-spreadsheet.md` |
| Iteration pass | iteration summary | `templates/iteration.md` |

**Default fidelity:** cheapest valid for the hypothesis — not automatically paper. For experience / physical questions, P4 paper PnP remains the usual first human-playable build. TTS / Tabletopia when P3 is required or after paper works. Runtime simulators are **optional** (`prototype/runtime.md`). See `tools/` for P4 export.

## Core Frameworks & Mental Models

### MDA alignment
Mechanics → Dynamics → Aesthetics. Choose Aesthetics first, then design Mechanics that produce Dynamics that evoke them. Depth: `theme-and-experience.md`. ([MDA paper](https://www.cs.northwestern.edu/~hunicke/MDA.pdf))

### Prototype fidelity
P0 Model → P1 Simulation → P2 Digital UI → P3 Digital tabletop → P4 Physical PnP → P5 Production. Detail: `prototype/fidelity-ladder.md`.

### Mechanism categories (13 chapters)
Structure → Turn Order → Actions → Resolution → Victory → Uncertainty → Economics → Auctions → Worker Placement → Movement → Area Control → Set Collection → Card Mechanisms. Pick **structure first**. Compare 2–4 candidates: `reasoning/design-reasoning.md`.

### Input vs Output randomness
- **Input** — random result informs decision *before* commitment → agency.
- **Output** — random outcome resolves a committed decision → drama.

### Action economy
Action Points (flexibility) vs Action Retrieval (strictness) vs Action Drafting (denial).

### Resolution curve
Stat Check (unit quality), High Number (force quantity), RPS (no unit always best), Force Commitment (intent), Critical Hits (jackpot).

### Uncertainty types
Match uncertainty type to aesthetic; mismatch causes "feels random" complaints.

### Victory currency separation
Keep victory currency separate from working currency or you get snowball (Monopoly cash).

### Catch-the-leader
Prefer subtle assistance (e.g. Stat Turn Order). Overt catch-up feels punishing.

### Economy openness
Open (easier balance) / Closed (zero-sum timing) / One-in-One-Out (modern card default).

### Auction purpose
English (max value), Dutch (speed), Vickrey (truthful sealed), Constrained (finite token budget).

### Turn-order binding
Strong left-right binding (auctions, worker placement) needs catch-up or asymmetry compensation.

### Print paths
POD (TGC) vs mass (Panda) — see `print-specs.md`. Prototype-first uses `templates/pnp-checklist.md`, not vendor PDFs.

## Chapter Index

Single-code or narrow mechanism questions: jump **directly** to the chapter file below. Use `cheatsheet.md` only for symptoms, trade-offs, or multi-mechanism design.

`patterns.md` holds **selected** high-leverage patterns; full definitions live in the chapter files.

| # | File | Title (mechanism codes) |
|---|---|---|
| 1 | [ch01](chapters/ch01-game-structure.md) | Game Structure (STR-01 to STR-10) |
| 2 | [ch02](chapters/ch02-turn-order.md) | Turn Order and Structure (TRN-01 to TRN-17) |
| 3 | [ch03](chapters/ch03-actions.md) | Actions (ACT-01 to ACT-18) |
| 4 | [ch04](chapters/ch04-resolution.md) | Resolution (RES-01 to RES-22) |
| 5 | [ch05](chapters/ch05-victory.md) | Game End and Victory (VIC-01 to VIC-20) |
| 6 | [ch06](chapters/ch06-uncertainty.md) | Uncertainty (UNC-01 to UNC-11) |
| 7 | [ch07](chapters/ch07-economics.md) | Economics (ECO-01 to ECO-19) |
| 8 | [ch08](chapters/ch08-auctions.md) | Auctions (AUC-01 to AUC-16) |
| 9 | [ch09](chapters/ch09-worker-placement.md) | Worker Placement (WPL-01 to WPL-08) |
| 10 | [ch10](chapters/ch10-movement.md) | Movement (MOV-01 to MOV-24) |
| 11 | [ch11](chapters/ch11-area-control.md) | Area Control (ARC-01 to ARC-08) |
| 12 | [ch12](chapters/ch12-set-collection.md) | Set Collection (SET-01 to SET-05) |
| 13 | [ch13](chapters/ch13-card-mechanisms.md) | Card Mechanisms (CAR-01 to CAR-06) |

## Topic Index

| If you're asking... | See |
|---|---|
| Genre fit (party, social deduction, solo, euro) | `genre-profile/` |
| Vague symptom routing | `routing/symptom-index.md` |
| Which prototype fidelity? | `prototype/selection.md` |
| Run / plan a simulation | `prototype/runtime.md`, `templates/simulation-run.md` |
| Theme, emotion curve, theme-mechanism fit | `theme-and-experience.md` |
| Design reasoning, compare mechanisms | `reasoning/design-reasoning.md` |
| Symptom → diagnosis | `routing/symptom-index.md` → `cheatsheet.md` → `diagnostics/` |
| Falsifiable hypotheses | `reasoning/hypothesis-rules.md` |
| Rank next experiment | `reasoning/experiment-priority.md` |
| Run experiment | `experiments/framework.md` |
| Continue or kill project | `kill-criteria.md` |
| Output quality check | `lint/checklist.md` |
| Co-op alpha-player problem | Ch 1, Ch 6 |
| Solo mode / Automa design | Ch 1, Ch 3 |
| Legacy & campaign structure | Ch 1, Ch 5 |
| First-player advantage / catch-up | Ch 2, `diagnostics/first-player-advantage.md` |
| Real-time vs turn-based | Ch 2 |
| Action selection (drafting, points, retrieval) | Ch 3 |
| Tech trees / gating / progression | Ch 3 |
| Combat resolution / dice pools | Ch 4 |
| Randomness: input vs output | Ch 4, Ch 6 |
| Snowball / runaway leader | Ch 5, Ch 7, `diagnostics/runaway-leader.md` |
| Hidden vs exposed victory points | Ch 5 |
| End-game triggers | Ch 5 |
| Hidden information, hidden roles | Ch 6 |
| Push-your-luck design | Ch 6 |
| Open vs closed economy | Ch 7 |
| Trading & negotiation | Ch 7 |
| Bidding forms & auction selection | Ch 8 |
| Worker placement | Ch 9 |
| Movement / roll-and-move mitigation | Ch 10 |
| Hidden movement | Ch 6, Ch 10 |
| Area majority / force projection | Ch 11 |
| Set collection curves | Ch 12 |
| Deck building / drafting / trick-taking | Ch 13 |
| Concept → prototype pipeline | `workflow.md`, `prototype/`, `templates/` |
| Playtest frameworks | `playtesting.md` |
| Balance failure modes & McDie | `balance/README.md` |
| PnP then POD/mass print | `templates/pnp-checklist.md`, `print-specs.md` |
| Card generation / TTS | `tools/export-pipeline.md`, `tools/` |
| External resources | `external-resources.md` |

## Companion Files

| Path | Purpose |
|---|---|
| [eval/](eval/) | Benchmarks + `validators/validate.py` + component validator + `golden/` schemas |
| [eval/README.md](eval/README.md) | Structural + behavior eval workflow |
| [prototype/](prototype/) | Fidelity ladder, selection, optional-runtime boundary |
| [genre-profile/](genre-profile/) | Euro, party, social-deduction, solo design lenses |
| [routing/symptom-index.md](routing/symptom-index.md) | Symptom → diagnostic routing ontology |
| [CHANGELOG.md](CHANGELOG.md) | Semver release history (matches `version` in frontmatter) |
| [workflow.md](workflow.md) | Milestones 0–5 with template outputs; stage regression allowed |
| [kill-criteria.md](kill-criteria.md) | Continue / Restructure / Pause-or-Kill gate |
| [theme-and-experience.md](theme-and-experience.md) | MDA depth, theme-mechanism matrix, emotion curve |
| [playtesting.md](playtesting.md) | Five playtest frameworks + experiment tie-in |
| [probability-and-balance.md](probability-and-balance.md) | Failure modes, dice intuition, McDie (also indexed in `balance/`) |
| [print-specs.md](print-specs.md) | POD vs mass production specs |
| [cheatsheet.md](cheatsheet.md) | Decision rules + symptom routing + mixed-demand priority |
| [patterns.md](patterns.md) | Selected mechanism patterns |
| [glossary.md](glossary.md) | Term definitions |
| [external-resources.md](external-resources.md) | Agent-facing links by Mode (~25); maintainer index in `references/web-resources.md` |
| [reasoning/](reasoning/) | Design reasoning, decision matrix, hypothesis rules, experiment priority |
| [diagnostics/](diagnostics/) | Symptom guides (8 core failure modes) |
| [experiments/](experiments/) | Experiment framework |
| [balance/](balance/) | Balance model, value budget; index to probability doc |
| [lint/](lint/) | Design lint rules BG001–BG020 + Design Confidence Model |
| [tools/](tools/) | Export pipeline, component schema, nanDECK, TTS |
| [templates/](templates/) | Copy-out project files; see `examples/micro-scavenger/` |
| [docs/solution-design.md](docs/solution-design.md) | v4 architecture roadmap (maintainer) |

## Scope & Limits

- **Book is mechanisms-focused** — trade-offs and catalogues; project process lives in companions + templates.
- **Synthesized, not verbatim** — not a substitute for the original book.
- **Language** — in Chinese context, prefer each game's official/mainstream Chinese name when one exists; otherwise keep English (optional short gloss on first mention).
- **Single-designer focus** — multi-agent design collaboration is out of scope.
- **Fidelity, not medium dogma** — cheapest valid prototype for the hypothesis; paper PnP remains the usual P4 human build. Digital/sim when they fit the question.
- **No CLI required for design** — lint and diagnostics are Markdown instructions for the agent. Maintainer validators under `eval/validators/` are optional.
- **No required simulation runtime** — Simulate mode is procedure + artifacts; runners are project-local / companion only (`prototype/runtime.md`).
