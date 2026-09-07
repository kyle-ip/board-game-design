---
name: bgd-assets
description: >-
  Recommend free/CC0 board-game art, icons, fonts, SFX, and digital tabletops (TTS, Screentop, PlayingCards.io, Tabletopia). Use whenever the user asks for assets, sprites, meeples, card faces, fonts, music, or digitization art sources — recommend 2–4 picks, not a full dump.
metadata:
  package: board-game-design
  companion: true
---

# Recommend free board-game digital assets

Standalone companion skill for the **board-game-design** package. Hosts may surface it as `/bgd-assets` in the slash menu; agents should also **auto-load** it from this description when relevant.

**Package root:** parent of `skills/` (`board-game-design/`). Resolve companion paths from that root.

1. Load `tools/digital-assets.md`. Follow Quick pick — recommend **2–4** sources max; state license caveats.
2. Do **not** dump the full catalog unless the user asks for a survey.
3. Cross-ref `tools/TTS-guide.md` / `tools/export-pipeline.md` when digitizing.
