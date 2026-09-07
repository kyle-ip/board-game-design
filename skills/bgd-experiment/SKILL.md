---
name: bgd-experiment
description: >-
  Design a single-variable human playtest experiment for a tabletop game. Use when the user wants to test one rule change, draft experiment.md / playtest-log, or rank which hypothesis to run next.
metadata:
  package: board-game-design
  companion: true
---

# Design a playtest experiment

Standalone companion skill for the **board-game-design** package. Hosts may surface it as `/bgd-experiment` in the slash menu; agents should also **auto-load** it from this description when relevant.

**Package root:** parent of `skills/` (`board-game-design/`). Resolve companion paths from that root.

1. Enter **Experiment** mode. Load `experiments/framework.md` + `prototype/selection.md`.
2. Write `experiment.md` and prepare `playtest-log.md` (EXP/HYP IDs). One variable only.
3. If multiple hypotheses compete, also load `reasoning/experiment-priority.md`.
