---
name: bgd-lint
description: >-
  Run board-game-design output quality lint (BG001–BG020) before shipping rulebooks, components, or PnP packs. Use when the user asks to check prototype quality or finish a delivery checklist.
metadata:
  package: board-game-design
  companion: true
---

# Lint board-game design artifacts

Standalone companion skill for the **board-game-design** package. Hosts may surface it as `/bgd-lint` in the slash menu; agents should also **auto-load** it from this description when relevant.

**Package root:** parent of `skills/` (`board-game-design/`). Resolve companion paths from that root.

1. Load and apply `lint/checklist.md` (+ `lint/rules.md` when a rule fires).
2. Report findings; do not silently rewrite design without Diagnose/Experiment if rules imply mechanism change.
