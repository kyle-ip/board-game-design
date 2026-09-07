---
name: bgd-kill
description: >-
  Apply Continue / Restructure / Pause-or-Kill criteria after playtests. Use when the user asks whether to keep iterating, pivot, or stop a tabletop project.
metadata:
  package: board-game-design
  companion: true
---

# Continue or kill a board-game project

Standalone companion skill for the **board-game-design** package. Hosts may surface it as `/bgd-kill` in the slash menu; agents should also **auto-load** it from this description when relevant.

**Package root:** parent of `skills/` (`board-game-design/`). Resolve companion paths from that root.

1. Load `kill-criteria.md`. Read design-state + recent playtest/experiment artifacts.
2. Output a clear Continue / Restructure / Pause-or-Kill recommendation with reasons.
