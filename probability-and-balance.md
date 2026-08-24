# Probability & Balance Decision Rules

Use after playtests show a repeated tell, or before locking dice/economy numbers. Log changes in `templates/balance-notes.md`.

**Extended balance tools:** `balance/README.md` (model, value budget, spreadsheet template).

**Structured diagnosis:** failure tells below → detailed guides in `diagnostics/`; run `lint/rules.md` after 3+ playtests.

## When to Use McDie (Monte Carlo Dice Simulator)

**Use [McDie](https://pmc.ncbi.nlm.nih.gov/articles/PMC8134935/) when the mechanism involves dice pools, rerolls, multi-die distributions, or success-threshold curves where intuition fails.**

Trigger questions:
- Does adding one die meaningfully change success %?
- Is reroll average close enough to expected value that it matters?
- Are outcomes bimodal (e.g. "great or nothing")?

If any "yes" → run McDie before locking the number. Do not eyeball dice-pool balance.

## Quick Probability Intuition (no simulator yet)

| Setup | Rough takeaway |
|---|---|
| Single d6 target ≤N | Success ≈ N/6 (e.g. ≤3 → 50%) |
| 2d6 sum | Bell curve; 7 most common; extremes rare — players feel this |
| Highest of 2d6 vs 1d6 | Advantage is large; do not treat as "+3.5 average" casually |
| Dice pool "count successes on 5+" | Adding one die is roughly +1/3 success expected — diminishing drama unless thresholds stack |
| Exploding / critical faces | Lengthens the right tail; jackpot feel, harder to balance caps |
| Reroll once | Helps bad rolls more than it boosts already-good rolls; can still worsen if "must take second" |

**Decision rule:** if you cannot sketch the distribution on a napkin, table it or simulate before shipping the number.

## Spreadsheet Before Simulation

For card costs, VP curves, and engine timing:
1. One row per card/action with cost, effect, VP, frequency.
2. Solo-run expected resource income per turn at early/mid/late game.
3. Check whether the leader's income compounds (snowball) without a sink or catch-up.

Use McDie for dice; use `templates/balance-spreadsheet.md` for economies and set-collection curves (triangular default: 1, 3, 6, 10, 15). Card-level checks: `balance/value-budget.md`.

## Common Balance Failure Modes

Structured diagnosis: `diagnostics/` (one file per mode). Lint IDs: `lint/rules.md`.

| Failure | Tell | Fix | Diagnostic |
|---|---|---|---|
| Snowball / runaway leader | Early advantage compounds each turn | Split victory vs working currency; catch-up; declining returns | `runaway-leader.md` |
| Kingmaking | Eliminated / hopeless player decides winner | Avoid elimination; hide scores; shared-victory options | `kingmaking.md` |
| Dominant strategy | One path wins across N playtests | Asymmetric costs; counters; RPS loops; orthogonal scoring | `dominant-strategy.md` |
| Turtling | Players avoid conflict, stalemate | Forced interaction; King of the Hill; escalating stakes; timer | cheatsheet Stage 5 |
| Lucky runaway | One early random event swings game | Bound RNG; input randomness; deterministic early turns | `randomness-dominates-skill.md` |
| Analysis paralysis | Turns take 5+ min | Cut branching; simultaneous selection; hide some info | `analysis-paralysis.md` |
| First-player advantage | Seat 1 wins disproportionately | Bid for start; asymmetric starts; Stat Turn Order | `first-player-advantage.md` |
| Dead last / no agency | Trailing player cannot affect outcome | Catch-the-leader; temporary VP grabs; interaction that scales | `low-agency.md` |

**Decision rule:** spot the tell in 2+ playtests → apply **one** fix → measure next session. Do not stack three balance changes at once.

## Currency & Curve Checklist

- [ ] Victory currency ≠ working currency (unless snowball is intentional)
- [ ] Set collection uses a curve (not linear 1, 2, 3, 4)
- [ ] Engine games have a pivot from building to scoring
- [ ] Catch-up is subtle (Stat Turn Order) rather than overt punishment
- [ ] Open economies are easier to tune than closed zero-sum ones

## Loss Aversion (Engelstein — Achievement Relocked)

Players feel a loss ~2× as much as an equal gain. Frame stakes carefully; do not weaponize against player trust.

## Recommended Tools

| Tool | Use case |
|---|---|
| [McDie](https://pmc.ncbi.nlm.nih.gov/articles/PMC8134935/) | Dice probability / Monte Carlo, visual, no code |
| Spreadsheet | Card economies, VP curves, income per turn |
| Component.Studio | Data-driven card/board generation from spreadsheet |
| NanDeck | Scripted card generation — see `tools/nanDECK-guide.md` |

## Deep Dives
- GameTek (Engelstein): https://gametek.substack.com/
- Building Blocks PDF — mechanism encyclopedia
- Ludology Game Design Checklist — self-review template

## Cross-References
- Balance index: `balance/README.md`
- Workflow: `workflow.md` Milestones 1 & 4
- Playtest triage: `playtesting.md` Framework 4
- Project log: `templates/balance-notes.md`, `templates/balance-spreadsheet.md`
- Symptom routing: `cheatsheet.md`
- Experiments: `experiments/framework.md` — one fix per pass
