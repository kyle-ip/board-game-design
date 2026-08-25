# Genre Profile — Euro / Strategy

Mechanism-driven games: worker placement, engine building, resource conversion, area control. Aligns with Building Blocks chapters.

## Core Experience

- **Aesthetics:** Challenge, discovery, submission (to system)
- **Player fantasy:** Build an efficient machine; optimize under scarcity
- **Session:** 45–120 min typical; teach 10–20 min

## Typical Dynamics

- Action economy tension (AP, placement, drafting)
- Engine snowball risk (watch BG003, BG007)
- Turn-order binding (auctions, WPL) → catch-up needed
- Score opacity vs transparency trade-off

## Mechanism Vocabulary (start here)

Structure → Turn Order → Actions → Economics → Worker Placement → Victory. See `chapters/` index.

## Common Failure Modes

| Symptom | Diagnostic | Not usually |
|---|---|---|
| Snowball / runaway | `runaway-leader.md` | Add more randomness |
| Flat midgame | `low-agency.md`, `endgame-drag.md` | Add unrelated mini-game |
| One strategy wins | `dominant-strategy.md` | Buff everything |
| First player wins | `first-player-advantage.md` | Shuffle turn order only |
| AP / slow turns | `analysis-paralysis.md` | More options |
| Forgettable / generic | ED004, ED005 | More mechanisms |

## Playtest Frameworks by Stage

| Stage | Framework |
|---|---|
| Early (loop untested) | Scattershot — not for shipping |
| Mid (loop works) | Good-Bad-Meh + Three-Bucket Triage |
| Late (rules stable) | Blind Rulebook Test |

## Kill Criteria Overrides (recommended defaults)

Copy to design-state **Kill Criteria Overrides**:

| Signal | Yellow | Red | Enabled |
|---|---|---|---|
| first_player_win_rate_4p | 35% | 45% | yes |
| avg_fun_restructure | ≤3/5 × 2 sessions | — | yes |
| playtime_vs_target | >30% over 2× | >50% over | yes |
| rules_questions_mid | >3 per player | same Q 3× | yes |
| winner_score_spread | leader +50% | last cannot affect winner | yes |

## Prototype Constraints

- Paper PnP default; components-sheet before art
- Balance pass via `balance/value-budget.md` when cards/actions exist
- Value budget useful; watch pseudo-precision on engine cards

## Cross-References

- Compare mechanisms: `reasoning/design-reasoning.md`
- Balance: `balance/README.md`
- Examples: `templates/examples/micro-scavenger/`
