# Simulation & Digital Runtime (Optional)

**This skill remains Markdown-only.** No simulator, web server, or package install is required to use Create / Diagnose / Experiment / Balance / Prototype / Simulate modes.

Simulate mode defines **what to plan, record, and claim** — not a built-in game engine.

## What the skill provides

| Provided | Location |
|---|---|
| Fidelity ladder & selection | `prototype/fidelity-ladder.md`, `prototype/selection.md` |
| Simulation run artifact shape | `templates/simulation-run.md` |
| Metrics / agent-profile vocabulary | below |
| Evidence → Claim integration | `lint/rules.md`, `templates/design-state.md` |
| Component JSON schema + optional validator | `tools/component-schema.json`, `eval/validators/validate_components.py` |

## What is out of skill runtime

Do **not** treat these as skill dependencies:

- General-purpose Monte Carlo engine or rules engine
- Browser multiplayer / TTS automation / WebRTC
- LLM-as-player default for thousands of games
- CI gates that require simulation binaries

If a project needs executable sims, place **project-local** scripts (or a separate companion repo) and point `simulation-run.md` at their outputs. The skill only requires reproducible metadata (seed, rules version, metrics, sample size).

## Agent profiles (vocabulary)

When proposing or reporting a simulation, name profiles explicitly:

| Profile | Role |
|---|---|
| Random | Legal-move baseline / rules sanity |
| Greedy | Immediate utility; exposes obvious dominant lines |
| Conservative | Safety / low risk |
| Opportunistic | Combos / tactical spikes |
| Strategic | Multi-turn value |
| Adversarial | Actively seeks exploits (attack the design) |

Prefer **code / heuristic agents** for large run counts. Use LLM play only for small qualitative samples. See Non-Goals in `docs/solution-design.md`.

## Metrics taxonomy (report only what you measured)

- **Outcome:** win_rate, score_mean/median/std, score_spread
- **Tempo:** game_length, round_length
- **Economy:** generation, spend, stock, sinks
- **Action:** frequency, diversity, unused_action_rate
- **Strategy:** dominant_action_rate, strategy_distribution
- **Comeback:** lead_change_count, comeback_rate

## Confidence for simulation

Do not claim High confidence from tiny samples. Defaults (override with real statistics when available):

| Runs (stable result) | Typical ceiling |
|---|---|
| < 100 | Low |
| 100–999 | Medium |
| 1000+ with seed robustness + agent diversity | High eligible |

Also require: question fit (system vs experience), multiple agent profiles for "dominant strategy" claims, and documented limitations.

## Cross-References

- Simulate mode: `SKILL.md`
- Artifact: `templates/simulation-run.md`
- Architecture roadmap: `docs/solution-design.md`
