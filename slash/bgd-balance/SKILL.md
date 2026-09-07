---
name: bgd-balance
description: >-
  Explicit Balance mode for board-game-design. Numbers, cards, economy, Effective Value Range. Invoke as /bgd-balance <description>.
disable-model-invocation: true
metadata:
  package: board-game-design
  slash: /bgd-balance
---

# /bgd-balance

**Package root:** parent of `slash/` (`board-game-design/`).

1. Treat text after `/bgd-balance` as the **balance target** (card, economy, curve).
2. Enter **Balance** mode. Load `balance/README.md` (+ `balance/value-budget.md` as needed).
3. One fix per pass. Write `balance-notes.md`; `balance-spreadsheet.md` when numeric.
