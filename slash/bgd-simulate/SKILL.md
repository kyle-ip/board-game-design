---
name: bgd-simulate
description: >-
  Explicit Simulate mode for board-game-design. System questions: balance, win rate, length, dominant strategy, populations. Invoke as /bgd-simulate <description>.
disable-model-invocation: true
metadata:
  package: board-game-design
  slash: /bgd-simulate
---

# /bgd-simulate

**Package root:** parent of `slash/` (`board-game-design/`).

1. Treat text after `/bgd-simulate` as the **system question**.
2. Enter **Simulate** mode. Load `prototype/fidelity-ladder.md`, `prototype/selection.md`, `prototype/runtime.md`.
3. Write `simulation-run.md` (SIM ID, seed, sample size). Do **not** claim fun validated. Optional `runtime/` (`bgd-sim`) if available.
