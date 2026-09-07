---
name: bgd-genre
description: >-
  Load a tabletop genre design lens (euro, party, social-deduction, solo, coop). Use when the user names a genre or needs genre-specific constraints (e.g. alpha-player in coop).
metadata:
  package: board-game-design
  companion: true
---

# Apply a board-game genre profile

Standalone companion skill for the **board-game-design** package. Hosts may surface it as `/bgd-genre` in the slash menu; agents should also **auto-load** it from this description when relevant.

**Package root:** parent of `skills/` (`board-game-design/`). Resolve companion paths from that root.

1. Load matching `genre-profile/*.md` (one file). Update design-state Project Status when a project exists.
