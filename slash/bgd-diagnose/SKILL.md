---
name: bgd-diagnose
description: >-
  Explicit Diagnose mode for board-game-design. Route symptoms (boring, unfair, forgettable, broken) to BG*/ED* diagnostics. Invoke as /bgd-diagnose <description>.
disable-model-invocation: true
metadata:
  package: board-game-design
  slash: /bgd-diagnose
---

# /bgd-diagnose

**Package root:** parent of `slash/` (`board-game-design/`).

1. Treat text after `/bgd-diagnose` as the **symptom / observation**.
2. Enter **Diagnose** mode. Read project `design-state.md` first if it exists.
3. Load `routing/symptom-index.md` → `cheatsheet.md` → matching `diagnostics/*`.
4. Do **not** change rules before a falsifiable hypothesis. Write/update design-state; `decision.md` if intervening.
