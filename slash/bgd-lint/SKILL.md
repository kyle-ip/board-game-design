---
name: bgd-lint
description: >-
  Run board-game-design output quality lint (BG001–BG020) before shipping artifacts. Invoke as /bgd-lint <description>.
disable-model-invocation: true
metadata:
  package: board-game-design
  slash: /bgd-lint
---

# /bgd-lint

**Package root:** parent of `slash/` (`board-game-design/`).

1. Treat text after `/bgd-lint` as optional **scope** (which project files).
2. Load and apply `lint/checklist.md` (+ `lint/rules.md` when a rule fires).
3. Report findings; do not silently rewrite design without Diagnose/Experiment if rules imply mechanism change.
