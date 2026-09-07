---
name: bgd-playtest
description: >-
  Playtest frameworks and logging for board-game-design. Invoke as /bgd-playtest <description>.
disable-model-invocation: true
metadata:
  package: board-game-design
  slash: /bgd-playtest
---

# /bgd-playtest

**Package root:** parent of `slash/` (`board-game-design/`).

1. Treat text after `/bgd-playtest` as the **playtest goal** (script, framework, log).
2. Load `playtesting.md`; for a single-variable test also use Experiment mode (`experiments/framework.md`, `templates/experiment.md`, `templates/playtest-log.md`).
