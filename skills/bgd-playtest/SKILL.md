---
name: bgd-playtest
description: >-
  Apply playtest frameworks and logging for tabletop games. Use when the user wants playtest scripts, frameworks, or session logs.
metadata:
  package: board-game-design
  companion: true
---

# Plan board-game playtests

Standalone companion skill for the **board-game-design** package. Hosts may surface it as `/bgd-playtest` in the slash menu; agents should also **auto-load** it from this description when relevant.

**Package root:** parent of `skills/` (`board-game-design/`). Resolve companion paths from that root.

1. Load `playtesting.md`; for a single-variable test also use Experiment mode (`experiments/framework.md`, templates).
