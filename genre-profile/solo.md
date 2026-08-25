# Genre Profile — Solo / Automa

Single-player or primarily solo: puzzle, campaign episode, or AI opponent. Player competes against system or personal best.

## Core Experience

- **Aesthetics:** Challenge, discovery, submission
- **Player fantasy:** Beat the puzzle; optimize; survive escalation
- **Session:** 20–90 min; teach via solo learn-as-you-play

## Typical Dynamics

- **Automa** (representational, not full AI simulation) — mimic player outputs
- Difficulty scaling via deck/order/timers, not "smarter AI"
- Downtime irrelevant; pacing is player-controlled
- Score variance = difficulty tuning signal

## Mechanism Vocabulary

- Automa / bot player (Ch 1, Ch 3)
- Escalation decks, scenario goals
- Action retrieval / AP for solo pacing
- Hidden information from deck, not opponents

## Common Failure Modes

| Symptom | Diagnostic | Not usually |
|---|---|---|
| Automa too complex | Cognitive load — simplify bot rules | Simulate full player |
| Puzzle solved | `dominant-strategy.md` | Add randomness only |
| Too easy / too hard | Difficulty curve — scenario tiers | Buff all enemies |
| Feels multiplayer pasted on | Solo wasn't design target — Restructure | Add PvP |
| Boring repetition | `low-agency.md`, `endgame-drag.md` | More chrome |

## Playtest Frameworks by Stage

| Stage | Framework |
|---|---|
| Early | Designer solo plays (5× gate in `workflow.md`) |
| Mid | Good-Bad-Meh — log difficulty feel per scenario |
| Late | Blind setup — can you play without reference after 1 game? |

## Kill Criteria Overrides (recommended defaults)

| Signal | Yellow | Red | Enabled |
|---|---|---|---|
| first_player_win_rate_4p | — | — | **no** |
| avg_fun_restructure | designer urge to redesign by play 3 | by play 5 | yes |
| playtime_vs_target | >30% over 2× | >50% over | yes |
| rules_questions_mid | >2 per session | same confusion 3× | yes |
| winner_score_spread | — | — | **no** |

**Solo-specific:** Designer cannot finish 5 solo plays without redesign urge → Pause or Kill (`kill-criteria.md`).

## Prototype Constraints

- Automa reference card on table — one page max
- Scenario book or deck; paper PnP sufficient
- Log win rate / score per difficulty tier for tuning

## Cross-References

- Automa design: Ch 1, Ch 3
- Co-op alpha-player (if hybrid): `cheatsheet.md` Stage 0
