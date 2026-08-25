# Simulation & Digital Runtime (Optional)

**This skill remains Markdown-only.** No simulator, web server, or package install is required to use Create / Diagnose / Experiment / Balance / Prototype / Simulate modes.

Simulate mode defines **what to plan, record, and claim** — not a built-in game engine.

Optional companion: [`runtime/`](../runtime/README.md) (`bgd-sim`) executes seeded Monte Carlo for supported adapters (first: Micro-Scavenger). Skill decides *what* to test; runtime decides *how* to execute.

## What the skill provides

| Provided | Location |
|---|---|
| Fidelity ladder & selection | `prototype/fidelity-ladder.md`, `prototype/selection.md` |
| Simulation run artifact shape | `templates/simulation-run.md` |
| Metrics / agent / population vocabulary | below |
| Evidence → Claim integration | `lint/rules.md`, `templates/design-state.md` |
| Component JSON schema + optional validator | `tools/component-schema.json`, `eval/validators/validate_components.py` |
| Optional executable runner | `runtime/` (pip install -e) |

## What is out of skill runtime

Do **not** treat these as skill dependencies:

- General-purpose Monte Carlo engine or rules engine (companion is adapter-based)
- Browser multiplayer / TTS automation / WebRTC
- LLM-as-player default for thousands of games
- CI gates that require simulation binaries for skill Markdown use

If a project needs executable sims, use **`runtime/`** (this repo) or project-local scripts and point `simulation-run.md` at their outputs. The skill only requires reproducible metadata.

## Skill ↔ Runtime contract

| Skill owns | Runtime owns |
|---|---|
| Hypothesis, fidelity choice, claims | Seeded game steps, agent policy |
| `simulation-run.md` narrative + confidence | Metrics JSON |
| Never auto-fix from anomaly | Deterministic replay / regress CLI |
| Experience evidence (P2–P4) | System metrics only |

### Required metadata (every executable run)

| Field | Meaning |
|---|---|
| `seed` | RNG seed |
| `rules_version` | Rules id (e.g. R-012) |
| `prototype_version` | Prototype id |
| `simulation_version` | Runner / config version |
| `agent_version` | Agent param schema version |

Map CLI JSON → `templates/simulation-run.md` fields (see runtime README).

## Agent profiles (vocabulary)

Named profiles are **parameter vectors**, not empty labels:

| Profile | Role | Default params (illustrative) |
|---|---|---|
| Random | Legal-move baseline | exploration=1.0, mistake_rate=0 |
| Greedy | Immediate utility | planning_horizon=1, risk=0.7 |
| Conservative | Safety / low risk | risk_tolerance=0.2, horizon=2 |
| Opportunistic | Combos / tactical spikes | exploration=0.3, aggression=0.6 |
| Strategic | Multi-turn value | planning_horizon=3, opponent_awareness=0.7 |
| Adversarial | Seeks exploits | aggression=0.9, opponent_awareness=1.0 |

### Parametric player model schema

```yaml
player:
  planning_horizon: 1–5      # turns of lookahead heuristic
  risk_tolerance: 0.0–1.0
  aggression: 0.0–1.0
  exploration: 0.0–1.0       # ε random legal move
  opponent_awareness: 0.0–1.0
  mistake_rate: 0.0–1.0      # play suboptimal with this prob
```

Prefer **code / heuristic agents** for large run counts. Use LLM play only for small qualitative samples.

## Population simulation

Do not only ask “can this strategy win?” — ask whether the mechanism holds under a **population mix**.

| Preset | Mix (weights) |
|---|---|
| `experienced` | Strategic 40%, Opportunistic 30%, Greedy 20%, Adversarial 10% |
| `casual` | Random 20%, Greedy 30%, Conservative 30%, Opportunistic 20% |
| `mixed` | Greedy 20%, Conservative 20%, Opportunistic 20%, Strategic 20%, Random 10%, Adversarial 10% |
| `adversarial_meta` | Adversarial 40%, Strategic 30%, Greedy 20%, Opportunistic 10% |

Custom weights allowed if they sum to 1.0. Report `strategy_distribution` and per-seat metrics.

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
| 1000+ with seed robustness + agent / population diversity | High eligible |

Also require: question fit (system vs experience), multiple agent profiles or a population for "dominant strategy" claims, and documented limitations.

## Digital P2 (thin)

Companion `bgd-sim play` provides CLI human-vs-heuristic for supported games. Escalation to P3 still uses TTS / Tabletopia (`tools/TTS-guide.md`). No browser runtime ships with the skill.

## Cross-References

- Simulate mode: `SKILL.md`
- Artifact: `templates/simulation-run.md`
- Companion: `runtime/README.md`
- Release notes: `CHANGELOG.md`
