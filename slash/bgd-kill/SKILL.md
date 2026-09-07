---
name: bgd-kill
description: >-
  Continue / Restructure / Pause-or-Kill gate after playtests for board-game-design. Invoke as /bgd-kill <description>.
disable-model-invocation: true
metadata:
  package: board-game-design
  slash: /bgd-kill
---

# /bgd-kill

**Package root:** parent of `slash/` (`board-game-design/`).

1. Treat text after `/bgd-kill` as **evidence summary** or project pointer.
2. Load `kill-criteria.md`. Read design-state + recent playtest/experiment artifacts.
3. Output a clear Continue / Restructure / Pause-or-Kill recommendation with reasons.
