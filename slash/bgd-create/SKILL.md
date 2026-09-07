---
name: bgd-create
description: >-
  Explicit Create mode for board-game-design. New game from scratch: concept-brief, design-state (Target Player Model), mechanism-skeleton. Invoke as /bgd-create <description>.
disable-model-invocation: true
metadata:
  package: board-game-design
  slash: /bgd-create
---

# /bgd-create

**Package root:** parent of `slash/` (`board-game-design/`).

1. Treat all text after `/bgd-create` as the **description** (game idea / constraints).
2. Enter **Create** mode per package `SKILL.md` (Hard Invariants apply).
3. Load Create required files from `routing/context-budget.md`.
4. Write `concept-brief.md`, `design-state.md`, `mechanism-skeleton.md` from `templates/` into the project folder (ask where if unclear).
5. Compare 2–4 mechanism candidates in the skeleton; set genre via `genre-profile/` when known.
