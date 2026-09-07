---
name: bgd-tts
description: >-
  Guide Tabletop Simulator import for a board-game digital smoke test after paper works. Use when the user mentions TTS decks, custom boards, or remote digital playtests.
metadata:
  package: board-game-design
  companion: true
---

# Import a game into Tabletop Simulator

Standalone companion skill for the **board-game-design** package. Hosts may surface it as `/bgd-tts` in the slash menu; agents should also **auto-load** it from this description when relevant.

**Package root:** parent of `skills/` (`board-game-design/`). Resolve companion paths from that root.

1. Load `tools/TTS-guide.md`. Remind paper-first Hard Invariant when physical_dependency is true.
2. For free 3D/2D bits, optionally load `tools/digital-assets.md` (2–4 picks) or skill `bgd-assets`.
