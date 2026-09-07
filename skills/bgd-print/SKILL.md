---
name: bgd-print
description: >-
  Advise on POD vs mass-production print specs for board games (TGC, Panda, file requirements). Use when preparing print files or choosing a manufacturer.
metadata:
  package: board-game-design
  companion: true
---

# Board-game print and manufacturing specs

Standalone companion skill for the **board-game-design** package. Hosts may surface it as `/bgd-print` in the slash menu; agents should also **auto-load** it from this description when relevant.

**Package root:** parent of `skills/` (`board-game-design/`). Resolve companion paths from that root.

1. Load `print-specs.md`. For prototype PnP prefer `templates/pnp-checklist.md` first.
