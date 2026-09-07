---
name: bgd-experiment
description: >-
  Explicit Experiment mode for board-game-design. Design a single-variable human playtest. Invoke as /bgd-experiment <description>.
disable-model-invocation: true
metadata:
  package: board-game-design
  slash: /bgd-experiment
---

# /bgd-experiment

**Package root:** parent of `slash/` (`board-game-design/`).

1. Treat text after `/bgd-experiment` as the **hypothesis or question to test**.
2. Enter **Experiment** mode. Load `experiments/framework.md` + `prototype/selection.md`.
3. Write `experiment.md` and prepare `playtest-log.md` (EXP/HYP IDs). One variable only.
