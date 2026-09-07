---
name: bgd-tts
description: >-
  Tabletop Simulator import guide for board-game-design digital smoke tests after paper. Invoke as /bgd-tts <description>.
disable-model-invocation: true
metadata:
  package: board-game-design
  slash: /bgd-tts
---

# /bgd-tts

**Package root:** parent of `slash/` (`board-game-design/`).

1. Treat text after `/bgd-tts` as the **import goal** (deck, board, tokens).
2. Load `tools/TTS-guide.md`. Remind paper-first Hard Invariant when physical_dependency is true.
3. For free 3D/2D bits, optionally load `tools/digital-assets.md` (2–4 picks).
