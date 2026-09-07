---
name: bgd-genre
description: >-
  Load a genre profile (euro, party, social-deduction, solo, coop) for board-game-design. Invoke as /bgd-genre <description>.
disable-model-invocation: true
metadata:
  package: board-game-design
  slash: /bgd-genre
---

# /bgd-genre

**Package root:** parent of `slash/` (`board-game-design/`).

1. Treat text after `/bgd-genre` as the **genre** (or description to classify).
2. Load matching `genre-profile/*.md` (one file). Update design-state Project Status when a project exists.
