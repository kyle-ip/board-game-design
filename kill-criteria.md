# Kill Criteria

Decision gate after playtesting. Use when **3+ playtests** exist, or when core loop still fails after **2 weeks** in Stage 1. Load at start of playtest planning too — set expectations early.

Aligns with `templates/playtest-log.md` Decision field and `workflow.md` Stage 3 gate.

## Three-Way Gate

| Path | Meaning | Typical next step |
|---|---|---|
| **Continue** | Core loop validated; hypotheses supported or fixable | Stage 4 polish, or next experiment |
| **Restructure** | Theme or goal has value, but **mechanism chassis** is wrong | Return to Stage 1–2; new mechanism skeleton |
| **Pause or Kill** | Core premise fails; sunk cost not justified | Archive; document learnings in design-state |

## Continue — triggers (need most, not all)

- [ ] Players can state the **goal** and **core loop** in one sentence after play 2+
- [ ] At least one playtester asks to play again unprompted
- [ ] Core fun hypothesis **supported** or minor tuning only (single-variable experiments working)
- [ ] No kill-criteria **Pause** trigger fired

## Restructure — triggers

- [ ] **2 consecutive** sessions: average fun ≤3/5 and feedback points at **same mechanism** (not numbers only)
- [ ] Core loop requires >3 sentences to explain after 5 playtests
- [ ] Dominant strategy or zero agency confirmed in 3+ plays (`diagnostics/dominant-strategy.md`, `low-agency.md`)
- [ ] Theme-audience fit good but mechanism-theme matrix failed (`theme-and-experience.md`)

**Action:** Record in `decision.md`; move failed mechanisms to **Rejected** in `design-state.md`; do not tune numbers on a broken chassis.

## Pause or Kill — triggers

- [ ] **3 consecutive** sessions: no player accurately describes the win condition
- [ ] **3 consecutive** sessions: interest drops to zero before game end (table talk stops, phones out)
- [ ] Solo designer cannot finish 5 solo plays without redesign urge (`workflow.md` Stage 1 gate)
- [ ] After restructure attempt, same Restructure triggers fire again

**Action:** Honest conversation with user; archive artifacts; optional post-mortem in `iteration.md`.

## Default Thresholds (skill-level)

Copy into project `design-state.md` **Kill Criteria Overrides** section. Tune per project; genre profiles suggest starting overrides.

| Signal | Yellow flag | Red flag | Notes |
|---|---|---|---|
| Playtime vs target | >30% over target 2× in a row | >50% over, players complain | |
| Rules questions (mid stage) | >3 per player per game | Same question 3 games in a row | Party: use >2 (see `genre-profile/party.md`) |
| First-player win rate (4p) | >35% for seat 1 | >45% after one fix attempt | Disable for social-deduction / party |
| Winner score spread | Leader +50% over last place routinely | Last place cannot affect winner | Disable for party / hidden-role |
| Avg fun (restructure) | ≤3/5 × 2 consecutive | ≤2.5/5 × 2 (party) | Genre-specific |

## Override Protocol

1. On Create: load genre profile → copy recommended overrides to design-state
2. On gate review: compare evidence against **project overrides**, not skill defaults alone
3. Document changes in `decision.md` when thresholds change

Example in design-state:

```markdown
## Kill Criteria Overrides

| Signal | Yellow | Red | Enabled |
|---|---|---|---|
| first_player_win_rate_4p | 35% | 45% | yes |
| avg_fun_restructure | ≤3/5 × 2 | — | yes |
| playtime_vs_target | >30% over 2× | >50% over | yes |
```

## Decision Log (per gate review)

| Field | Value |
|---|---|
| Date | |
| Playtests reviewed | PT-001 … |
| Gate result | Continue / Restructure / Pause or Kill |
| Evidence summary | |
| Confidence | Low / Medium / High |
| Thresholds used | design-state overrides / skill defaults |
| User confirmed | yes / no |

## Cross-References

- Override templates: `templates/design-state.md` Kill Criteria Overrides
- Genre defaults: `genre-profile/`
- Stage guidance when restructuring: [TTGDA — Tips for New Game Designers](https://www.ttgda.org/get-assistance/newpage)
- Playtest decision line: `templates/playtest-log.md`
- Failure mode detail: `diagnostics/`
- Workflow placement: `workflow.md` Stage 3 end
