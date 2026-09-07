---
name: bgd-create
description: >-
  Start a new board or card game from scratch: write concept-brief, design-state (Target Player Model), and mechanism-skeleton. Use whenever the user wants a new tabletop game concept, chassis comparison, or Create-mode artifacts — even if they do not name the skill.
metadata:
  package: board-game-design
  companion: true
---

# Create a new tabletop game

Standalone companion skill for the **board-game-design** package. Hosts may surface it as `/bgd-create` in the slash menu; agents should also **auto-load** it from this description when relevant.

**Package root:** parent of `skills/` (`board-game-design/`). Resolve companion paths from that root.

1. Enter **Create** mode per package hub `SKILL.md` (Hard Invariants apply).
2. Load Create required files from `routing/context-budget.md`.
3. Write `concept-brief.md`, `design-state.md`, `mechanism-skeleton.md` from `templates/` into the project folder (ask where if unclear).
4. Compare 2–4 mechanism candidates in the skeleton; set genre via `genre-profile/` when known.
