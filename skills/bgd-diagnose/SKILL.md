---
name: bgd-diagnose
description: >-
  Diagnose board-game problems (boring, unfair, snowball, forgettable, broken). Route symptoms to BG* / ED* diagnostics before changing rules. Use whenever the user reports playtest pain, balance complaints, or "something feels wrong".
metadata:
  package: board-game-design
  companion: true
---

# Diagnose tabletop game symptoms

Standalone companion skill for the **board-game-design** package. Hosts may surface it as `/bgd-diagnose` in the slash menu; agents should also **auto-load** it from this description when relevant.

**Package root:** parent of `skills/` (`board-game-design/`). Resolve companion paths from that root.

1. Enter **Diagnose** mode. Read project `design-state.md` first if it exists.
2. Load `routing/symptom-index.md` → `cheatsheet.md` → matching `diagnostics/*`.
3. Do **not** change rules before a falsifiable hypothesis. Write/update design-state; `decision.md` if intervening.
