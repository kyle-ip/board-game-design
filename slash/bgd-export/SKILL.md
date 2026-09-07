---
name: bgd-export
description: >-
  Card/component export pipeline (CSV → nanDECK → PnP) for board-game-design. Invoke as /bgd-export <description>.
disable-model-invocation: true
metadata:
  package: board-game-design
  slash: /bgd-export
---

# /bgd-export

**Package root:** parent of `slash/` (`board-game-design/`).

1. Treat text after `/bgd-export` as **what to export** (deck, components path).
2. Load `tools/export-pipeline.md` and `tools/nanDECK-guide.md` as needed.
3. Prefer `components-sheet.md` → CSV/JSON → nanDECK. Point to `tools/digital-assets.md` only if art sources are missing.
