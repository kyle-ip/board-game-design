---
name: bgd-print
description: >-
  POD vs mass-production print specs for board-game-design. Invoke as /bgd-print <description>.
disable-model-invocation: true
metadata:
  package: board-game-design
  slash: /bgd-print
---

# /bgd-print

**Package root:** parent of `slash/` (`board-game-design/`).

1. Treat text after `/bgd-print` as the **print path** (TGC, Panda, file specs).
2. Load `print-specs.md`. For prototype PnP prefer `templates/pnp-checklist.md` first.
