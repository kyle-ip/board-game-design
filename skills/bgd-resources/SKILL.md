---
name: bgd-resources
description: >-
  Provide agent-facing external links for board-game design by Mode (tools, publishing, comps, further reading). Use when the user asks for websites, publishing guides, or further reading — not for CC0 art (use bgd-assets).
metadata:
  package: board-game-design
  companion: true
---

# Board-game design external resources

Standalone companion skill for the **board-game-design** package. Hosts may surface it as `/bgd-resources` in the slash menu; agents should also **auto-load** it from this description when relevant.

**Package root:** parent of `skills/` (`board-game-design/`). Resolve companion paths from that root.

1. Load `external-resources.md` only — **not** `references/web-resources.md` unless maintaining the skill.
2. For art/CC0/digital tabletops, prefer skill `bgd-assets` → `tools/digital-assets.md`.
