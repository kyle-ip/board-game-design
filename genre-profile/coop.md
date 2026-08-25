# Genre Profile — Cooperative

Players share a win/loss against the system. Balance and diagnostics **do not** equal competitive euro balance.

## Core Experience

- **Aesthetics:** Challenge, fellowship, submission (to scenario), sometimes narrative
- **Player fantasy:** Survive / complete mission together; roles matter
- **Session:** 45–120 min typical; teach often longer than euro of same weight

## Typical Dynamics

- Shared goal; individual information or powers
- Difficulty curve / scenario scaling
- Communication rules shape the game as much as board rules
- Risk of **optimal solution convergence** (puzzle solved once)

## Mechanism Vocabulary (start here)

Structure (STR-02) → Uncertainty / hidden info → Actions (asymmetric powers) → Victory (group lose conditions). See Ch 1, Ch 6.

## Common Failure Modes

| Symptom | Diagnostic | Not usually |
|---|---|---|
| One player dictates all turns | Alpha-player / quarterbacking — see below | Add more solo puzzles |
| Too easy after one win | Difficulty curve / scenario — Open + EXP | Nerf all enemies blindly |
| Always same optimal line | `dominant-strategy.md` + ED005 | More random events only |
| Feels unfair to roles | Asymmetry audit; genre kill overrides | First-player win-rate metrics |
| Flat / forgettable mission | ED003, ED004, ED007 | Competitive runaway fixes |
| No one knows who decides | Information / communication rules | More VP tracks |

### Alpha-player / quarterbacking

Primary co-op pathology: experienced player issues orders; others execute.

**Counters (pick one, test one):** communication limits, real-time pressure, hidden info per player, complex personal powers that outsiders cannot fully optimize.

Route via Stage 0 in `cheatsheet.md` + this profile — not `first-player-advantage.md`.

## Playtest Frameworks by Stage

| Stage | Framework |
|---|---|
| Early | Scenario smoke — can the team lose and win? |
| Mid | Good-Bad-Meh + role agency check ("did you decide anything?") |
| Late | Blind teach; mixed-skill table (alpha risk) |

## Kill Criteria Overrides (recommended defaults)

| Signal | Yellow | Red | Enabled |
|---|---|---|---|
| first_player_win_rate_4p | — | — | **no** (N/A) |
| alpha_player_flag | 1 player decides ≥70% actions | same across 2 sessions | yes |
| win_rate_at_intended_difficulty | >80% or <20% over 5 plays | same after one EXP | yes |
| avg_fun_restructure | ≤3/5 × 2 sessions | — | yes |
| playtime_vs_target | >30% over 2× | >50% over | yes |
| rules_questions_mid | >3 per player | same Q 3× | yes |
| winner_score_spread | — | — | **no** (shared victory) |

## Prototype Constraints

- Difficulty / scenario sheet is a first-class component
- Test mixed experience tables early for quarterbacking
- P1 simulation of "win rate vs AI scenario" is valid **system** evidence; fun/fellowship needs P2–P4
- Optional runtime: cooperative adapters may differ from competitive `micro-scavenger`

## Cross-References

- Alpha-player: `cheatsheet.md` Stage 0; Ch 1, Ch 6
- Experience: ED001–ED008 in `diagnostics/`
- Kill gate: `kill-criteria.md`
