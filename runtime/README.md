# Optional simulation companion for board-game-design
# Skill decides What to test; this package executes How.

**Install (optional):**

```bash
pip install -e ./runtime
# or with tests:
pip install -e "./runtime[dev]"
```

**Not required** for Create / Diagnose / Experiment / Balance / Prototype / Simulate artifact planning. See `../prototype/runtime.md`.

## CLI

```bash
bgd-sim run --game micro-scavenger --runs 1000 --seed 42 --population mixed --out sim.json
bgd-sim regress --baseline base.json --candidate cand.json
bgd-sim check-determinism --runs 50 --seed 42 --population mixed
bgd-sim play --game micro-scavenger --seed 42 --opponent greedy
```

Or: `python -m bgd_runtime.cli …`

## Contract

| Output field | → `templates/simulation-run.md` |
|---|---|
| `seed` | Seed |
| `runs` / `metrics.runs` | Runs |
| `population` | Population |
| `simulation_version` | Simulation version |
| `agent_version` | Agent version |
| `rules_version` | Rules version |
| `metrics.*` | Metrics table |

Never auto-fix game rules from anomalies — update design-state via HYP/EXP only.

## Population presets

`experienced` · `casual` · `mixed` · `adversarial_meta` — see `prototype/runtime.md`.

## Digital P2

`bgd-sim play` is a thin CLI human-vs-heuristic loop. For P3 use TTS/Tabletopia (`../tools/TTS-guide.md`). No browser UI ships here.

## Tests

```bash
cd runtime && pip install -e ".[dev]" && pytest -q
```
