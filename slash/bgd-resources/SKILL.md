---
name: bgd-resources
description: >-
  Agent-facing external links by Mode (tools, publishing, further reading) for board-game-design. Invoke as /bgd-resources <description>.
disable-model-invocation: true
metadata:
  package: board-game-design
  slash: /bgd-resources
---

# /bgd-resources

**Package root:** parent of `slash/` (`board-game-design/`).

1. Treat text after `/bgd-resources` as the **topic** (publish, playtest tools, comps…).
2. Load `external-resources.md` only — **not** `references/web-resources.md` unless maintaining the skill.
3. For art/CC0/digital tabletops, prefer `/bgd-assets` → `tools/digital-assets.md`.
