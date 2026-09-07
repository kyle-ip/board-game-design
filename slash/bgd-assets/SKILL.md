---
name: bgd-assets
description: >-
  Recommend free/CC0 board-game art, icons, fonts, SFX, and digital tabletops (TTS/Screentop). Invoke as /bgd-assets <description>.
disable-model-invocation: true
metadata:
  package: board-game-design
  slash: /bgd-assets
---

# /bgd-assets

**Package root:** parent of `slash/` (`board-game-design/`).

1. Treat text after `/bgd-assets` as the **asset need** (icons, meeples, fonts, SFX, platform…).
2. Load `tools/digital-assets.md`. Follow Quick pick — recommend **2–4** sources max; state license caveats.
3. Do **not** dump the full catalog unless the user asks for a survey. Cross-ref `tools/TTS-guide.md` / `tools/export-pipeline.md` when digitizing.
