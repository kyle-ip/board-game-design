---
name: bgd-balance
description: >-
  Balance tabletop game numbers, cards, and economies using Effective Value Range / value-budget. Use when the user asks to cost cards, fix economy, or build a balance spreadsheet.
metadata:
  package: board-game-design
  companion: true
---

# Balance cards and economy

Standalone companion skill for the **board-game-design** package. Hosts may surface it as `/bgd-balance` in the slash menu; agents should also **auto-load** it from this description when relevant.

**Package root:** parent of `skills/` (`board-game-design/`). Resolve companion paths from that root.

1. Enter **Balance** mode. Load `balance/README.md` (+ `balance/value-budget.md` as needed).
2. One fix per pass. Write `balance-notes.md`; `balance-spreadsheet.md` when numeric.
