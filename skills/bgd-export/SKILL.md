---
name: bgd-export
description: >-
  Run the board-game card/component export pipeline (components-sheet → CSV/JSON → nanDECK → PnP images). Use when batching card art or preparing printable decks.
metadata:
  package: board-game-design
  companion: true
---

# Export cards for print-and-play

Standalone companion skill for the **board-game-design** package. Hosts may surface it as `/bgd-export` in the slash menu; agents should also **auto-load** it from this description when relevant.

**Package root:** parent of `skills/` (`board-game-design/`). Resolve companion paths from that root.

1. Load `tools/export-pipeline.md` and `tools/nanDECK-guide.md` as needed.
2. Prefer `components-sheet.md` → CSV/JSON → nanDECK.
3. Point to `tools/digital-assets.md` (or skill `bgd-assets`) only if art sources are missing.
