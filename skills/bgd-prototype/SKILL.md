---
name: bgd-prototype
description: >-
  Build a board-game prototype at the cheapest valid fidelity (simulation, digital tabletop, or paper PnP). Use when the user wants rulebook/components/pnp artifacts or a digital smoke-test plan.
metadata:
  package: board-game-design
  companion: true
---

# Build a tabletop prototype

Standalone companion skill for the **board-game-design** package. Hosts may surface it as `/bgd-prototype` in the slash menu; agents should also **auto-load** it from this description when relevant.

**Package root:** parent of `skills/` (`board-game-design/`). Resolve companion paths from that root.

1. Enter **Prototype** mode. Load `prototype/selection.md` first; then fidelity-appropriate templates/`tools/`.
2. Prefer cheapest valid fidelity. For P4 write rulebook, components-sheet, pnp-checklist; run `lint/checklist.md` before delivery.
