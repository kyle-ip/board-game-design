---
name: bgd-simulate
description: >-
  Run or plan board-game system simulations (win rate, length, dominant strategy, economy, populations). Use for Simulate-mode work and simulation-run artifacts; optional bgd-sim runtime when available. Do not claim fun is validated by sims.
metadata:
  package: board-game-design
  companion: true
---

# Simulate tabletop system questions

Standalone companion skill for the **board-game-design** package. Hosts may surface it as `/bgd-simulate` in the slash menu; agents should also **auto-load** it from this description when relevant.

**Package root:** parent of `skills/` (`board-game-design/`). Resolve companion paths from that root.

1. Enter **Simulate** mode. Load `prototype/fidelity-ladder.md`, `prototype/selection.md`, `prototype/runtime.md`.
2. Write `simulation-run.md` (SIM ID, seed, sample size). Do **not** claim fun validated.
3. Optional `runtime/` (`bgd-sim`) if available for supported adapters.
