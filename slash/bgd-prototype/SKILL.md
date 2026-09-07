---
name: bgd-prototype
description: >-
  Explicit Prototype mode for board-game-design. Build at chosen fidelity (sim / digital / PnP). Invoke as /bgd-prototype <description>.
disable-model-invocation: true
metadata:
  package: board-game-design
  slash: /bgd-prototype
---

# /bgd-prototype

**Package root:** parent of `slash/` (`board-game-design/`).

1. Treat text after `/bgd-prototype` as the **prototype goal** (fidelity, components, platform).
2. Enter **Prototype** mode. Load `prototype/selection.md` first; then fidelity-appropriate templates/`tools/`.
3. Prefer cheapest valid fidelity. For P4 write rulebook, components-sheet, pnp-checklist; run `lint/checklist.md` before delivery.
