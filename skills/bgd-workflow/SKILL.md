---
name: bgd-workflow
description: >-
  Map a tabletop project to workflow milestones 0–5 (concept through polish). Use when the user asks what stage they are in or what to do next.
metadata:
  package: board-game-design
  companion: true
---

# Board-game design workflow milestones

Standalone companion skill for the **board-game-design** package. Hosts may surface it as `/bgd-workflow` in the slash menu; agents should also **auto-load** it from this description when relevant.

**Package root:** parent of `skills/` (`board-game-design/`). Resolve companion paths from that root.

1. Load `workflow.md`. Map to templates and next milestone; allow stage regression when evidence requires it.
