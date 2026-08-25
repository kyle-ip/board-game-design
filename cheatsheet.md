# Cheatsheet

Decision rules, trade-off matrices, and tells distilled from *Building Blocks of Tabletop Game Design*. This is the "what would Engelstein & Shalev do?" layer — every line helps you decide something. For term definitions, see `glossary.md`.

## Mixed-Demand Priority

When the user asks for multiple things in one message, run in this order:

1. **Diagnose / Balance** — if symptoms, unfairness, or numbers are mentioned (`diagnostics/`, `balance/`, `design-state.md` first)
2. **Create / Mechanism** — concept, skeleton, reasoning (`workflow.md`, `reasoning/`)
3. **Prototype** — rulebook, components, PnP (`templates/`, `tools/`)
4. **Polish / Publish** — art-adjacent, print specs (last)

Principle: fix the **core loop skeleton** before packaging. Do not generate full PnP for a broken loop unless user explicitly wants a throwaway mockup.

Existing project: always read `templates/design-state.md` (project copy) before any step.

## Symptom → File Routing

Load the smallest file first. Write project templates when designing/prototyping.

| Symptom / ask | Load first | Then |
|---|---|---|
| Existing project / iteration N | `templates/design-state.md` | mode-specific files below |
| "Help me design a game" / new concept | `genre-profile/` (pick one) + `workflow.md` + `theme-and-experience.md` | concept-brief → mechanism-skeleton |
| Vague symptom ("boring", "unfair") | `routing/symptom-index.md` | one `diagnostics/*.md` |
| Boring / flat / no tension | `routing/symptom-index.md` → `diagnostics/endgame-drag.md` or `low-agency.md` | experiment; do not add mechanisms blindly |
| Snowball / runaway leader | `diagnostics/runaway-leader.md` | `balance/value-budget.md` |
| First player always wins | `diagnostics/first-player-advantage.md` | Ch 2 |
| One strategy always wins | `diagnostics/dominant-strategy.md` | balance-spreadsheet |
| Feels too random | `diagnostics/randomness-dominates-skill.md` | Ch 4, Ch 6 |
| Analysis paralysis | `diagnostics/analysis-paralysis.md` | cut branching; Ch 2 simultaneous |
| Kingmaking / spite | `diagnostics/kingmaking.md` | Ch 5 |
| Test a hypothesis | `experiments/framework.md` | `templates/experiment.md` |
| Multiple hypotheses — what to test next? | `reasoning/experiment-priority.md` | update **Experiment Backlog** in `design-state.md` |
| Continue or kill project | `kill-criteria.md` | `decision.md` |
| Output quality before delivery | `lint/checklist.md` | fix or flag TBD |
| Need a playable prototype soon | `templates/pnp-checklist.md` | rulebook + components-sheet + `tools/` |
| Open vs closed economy? | this file Stage 6 | `chapters/ch07-economics.md` |
| Alpha player in co-op | Stage 0 below | Ch 1, Ch 6 |
| Which auction form? | Stage 7 | Ch 8 |
| Worker placement blocking pain | Stage 8 | Ch 9 |
| Deck builder / market row | Stage 11 | Ch 13 |
| Dice pool math unsure | `balance/README.md` | McDie |
| Playtest structure | `playtesting.md` | `templates/playtest-log.md` |
| Print for friends vs factory | `templates/pnp-checklist.md` then `print-specs.md` | — |
| Theme feels pasted on | `theme-and-experience.md` | revisit mechanism skeleton |

## Stage 0 — Structure & Scope

| Question | Decision rule |
|---|---|
| What's the game's basic structure? | Pick first — it's the chassis everything bolts onto. STR-01 (competitive) is the default; choose STR-02 (co-op) for new players, STR-10 (legacy) for long-form commitment. |
| Solo mode? | Use Automa (representational, not procedural) — mimic outputs, don't simulate a full player. |
| Co-op alpha-player problem? | Counter with: communication limits (Hanabi), real-time pressure (Space Cadets), hidden info per player (Sentinels), or complex personal powers (Spirit Island). |
| Semi-coop? | All players must agree on whether group-win + individual-loss beats total group loss — mismatched incentives break the game. |
| Tie-breaker needed? | Treat as a design surface, not afterthought. Positional rewards turn-order play; resource rewards economy; random adds excitement but feels unsatisfying for final victory. |

## Stage 1 — Turn Order & Pacing

| Situation | Do this |
|---|---|
| Default turn order | Use Interleaved phases; only use Sequential when you want epic momentum swings. |
| Catch-the-leader needed | Use Stat Turn Order (TRN-02); be subtle — overt mechanisms feel punishing. |
| Real-time game | Use only if <20 min; use Punctuated Real-Time if you need intensity + complexity. |
| High player count (5+) | Avoid Progressive Turn Order (TRN-04) — 9-turn gaps create unacceptable downtime. |
| Simultaneous selection | Think of it as a "Yomi enabler" — gameplay is in anticipating others. |
| First-player advantage | Compensate via bidding, asymmetric starts, or catch-up mechanisms. |
| Anti-pattern: Lose a Turn | Deprecated in modern design; removes agency (Monopoly Jail, Snakes & Ladders exact-count). |

## Stage 2 — Actions & Player Powers

| Need | Mechanism | Why |
|---|---|---|
| Flexibility | Action Points (ACT-01) | Currency model; budget per turn. |
| Strictness | Action Retrieval (ACT-03) | Spent tokens return to pool. |
| Marketplace feel | Action Drafting (ACT-02) | Denial as valuable as acquisition. |
| Specialization | Tech Trees (ACT-16) | Player-driven via prerequisite chains. |
| Controlled pacing | Gating (ACT-15) | Designer-controlled via prerequisites. |
| Everyone engaged | Follow (ACT-08) | Everyone plays on everyone's turn; engagement up, pace down. |
| Variable powers | Use on simple frameworks only (Cosmic Encounter combat = highest number wins). | Cognitive load overwhelms on complex frameworks. |

## Stage 3 — Resolution

| If you want... | Use | Because |
|---|---|---|
| Unit quality to matter | Stat Check (RES-02) | Hold one target number constant across die types. |
| Force quantity to dominate | High Number (RES-01) | Highest total wins. |
| No unit always best | Rock, Paper, Scissors (RES-07) | Antidote to transitive strength ladders. |
| Guessing opponent intent | Force Commitment (RES-14) | Battle about intent, not army sizes. |
| Jackpot excitement | Critical Hits/Failures (RES-03) | Exploding dice can produce unbounded hits. |

**Resolution tells (smells):**
- Long modifier stacks → prefer intrinsic strengths, card play, or dice pools that model desired probabilities directly.
- Winner-takes-all in realistic settings → a 10-strength fleet eliminating a 1-strength at no cost strains theme.
- Sophisticated card-based combat at >2 players → slows dramatically.

## Stage 4 — Uncertainty

| If you want... | Use | Tell |
|---|---|---|
| Player agency | Input Randomness | Random result informs decision *before* commitment. |
| Drama/tension | Output Randomness | Random outcome resolves a committed decision. |
| Social, conversational uncertainty | Hidden Roles (UNC-04) | Players have secret identities. |
| Systemic, replayable uncertainty | Unknown Information (UNC-07) | Information no player has. |
| Push-your-luck | UNC-02 | Two levers: sunk-cost attachment + uncalculable odds. If EV always computable, tension evaporates. |

**Anti-patterns:**
- Constantly changing hidden info → reduces bluffing to random guessing; players need stable info to build a history.
- Memory/HTI without aids in competitive settings → sharply reduces accessibility; provide tracking components (Clue's pad).
- Hidden end-game bonuses with large ratio to in-game points → makes standing hard to judge; offer intermediate scoring (Concordia).

## Stage 5 — Victory & End-Game

| Failure mode | Tell | Fix |
|---|---|---|
| Snowball / runaway leader | Victory currency also fuels growth (Monopoly cash) | Split victory currency from working currency. |
| All-temporary VPs + threshold end | Perpetual leader-bashing (Munchkin, Dune) | Mix in permanent VPs. |
| Exposed VPs + fixed turns + deterministic scoring | Final turn becomes over-optimized calc exercise (Vinci) | Hide scores or add randomness. |
| Random end-game elimination | Players feel they lost to luck (Hunger Games: District 12) | Use deterministic elimination (High Society: least money cannot win). |
| Turtling | Players avoid conflict | King of the Hill (VIC-17) forces conflict; Highest Lowest (VIC-20) forces breadth. |

**End-game trigger rule:** Prefer natural tracking (depleting card stacks) over a round marker to reduce rules burden.

## Stage 6 — Economy

| Decision | Rule |
|---|---|
| Open vs. closed economy | Open: bank pumps new resources, fosters progress, easier to balance. Closed: zero-sum timing dynamics. |
| Fixed prices vs. self-balancing | Use Exchange (ECO-01) for predictable fixed costs; use Market (ECO-03) for self-balancing prices. |
| Obscure value, self-policing fairness | Use I Cut, You Choose (ECO-09). |
| Loans as punishment vs. leverage | Framing changes optimal strategy — be explicit which you intend. |
| Trading without Set Collection | Won't work — Set Collection makes the same good worth different amounts to different players, enabling trades. |

**Anti-patterns:**
- Forced mortgaging (Monopoly) → removes choice, extends trailing player's slow death spiral.
- Fungible hierarchical resources without obstruction → behave like coins of different denominations; introduce efficiency constraints or time pressure.
- Open Trading without time limits → lengthens games, excludes less assertive players.
- Non-binding future promises → hard to police; restrict Trades to immediate execution.

## Stage 7 — Auctions

| Need | Use | Trade-off |
|---|---|---|
| Quick sub-system auction | Sealed-Bid (AUC-04) | No iterative info reveal. |
| Iterative info reveal matters | Turn Order Until Pass (AUC-03) | Slow with $1 increments. |
| Solve length + small-value distinctions | Constrained Bidding (AUC-06) | Fixed tokens can't make change — plan redistribution. |
| Ergonomic, durable resource allocation | Dutch Auction (AUC-08) market row | Quick, decisive, board-space efficient. |
| Mathematically identical to Area Majority | Multiple-Lot (AUC-11) | Troops/influence cubes are bidding tokens. |

**Auction tells:**
- Too-precise valuation (a $10 bill) → bidding collapses; obscure value via hidden goals, future-dependent value, or set collection.
- Vickrey in practice → players don't intuitively understand truthful bidding is dominant; rarely worth rules overhead.
- Reverse Auction as central mechanism → inherently negative experience; use as seasoning only.
- Open Auction → messy, noisy, confusing without an auctioneer.

## Stage 8 — Worker Placement

| Decision | Rule |
|---|---|
| Hard vs. soft blocking | Hard (one worker, one space) frustrates; consider bumping (Euphoria) or cost-increase (Coal Baron). |
| Worker acquisition | Think of it as a declining-price auction — early workers pay off across more turns; late workers must be cheap. |
| Immediate vs. delayed resolution | Delayed (Caylus) enables combos, placement-order independence, and space for an intervening mechanism like the Provost. |
| Turn Order building with strong left-right binding | Avoid (Lords of Waterdeep); player to the left of new start player gets unearned windfall. |
| Unmetered worker growth | Becomes dominant strategy (Stone Age reproduction hut); require housing, feeding costs, or hard caps. |
| Toothless feeding costs | Makes starvation viable (Stone Age), removing the tension worker upkeep is meant to create. |

## Stage 9 — Movement

| Situation | Rule |
|---|---|
| Grid choice | Hexagons > squares when diagonal realism matters (50%-shifted square "brick" grid is isomorphic to hex). |
| Diagonal moves on square grids | Disallow, charge more, or switch to hex — diagonal is ~50% further than orthogonal. |
| Bare Roll-and-Move | Mitigate via choice (Backgammon), wagering (Camel Up), or push-your-luck wraps. |
| Movement Points | Think of as currency spent on terrain; wargame infantry 3 MP vs armor 6 MP. |
| Hidden movement | Rules must be *simpler* than open-movement rules — errors are uncatchable mid-game. |
| Programmed movement | Label turns "Clockwise/Counter-Clockwise," not "Right/Left" — visualization errors otherwise. |

## Stage 10 — Set Collection

| Curve | When | Why |
|---|---|---|
| Triangular (1, 3, 6, 10, 15) | Default escalating curve | Most balanced; marginal value of nth card = n. |
| Squaring (1, 4, 9, 16) | Small sets or shoot-the-moon | Grows explosively; reserve for small sets. |
| Linear (1, 2, 3, 4) | Never | Removes synergy; always curve the value. |
| Non-monotonic (declining then rising) | Force commitment | Eliminates middling play; adds texture (Cacao). |

**Set-collection tells:**
- Orthogonal sets (second scoring dimension) counterbalance sharply accelerating primary sets — keeps specialization vs. diversification in tension (7 Wonders science).
- Pre-declaring all combos steals joy of discovery — leave some emergent (Magic: The Gathering).
- Forgetting non-monotonic option → misses a chance to add texture via commitment dynamics.

## Stage 11 — Cards

| Need | Use | Why |
|---|---|---|
| Card-by-card comparison tied to contract | Trick Taking (CAR-01) | Specialized auction where lot = bids. |
| Shedding + set-comparison hybrid | Ladder Climbing (CAR-02) | East Asian traditions (President, Tichu). |
| Self-improving engine | Deck Building (CAR-05) | Past acquisitions shape future draws. |
| Quick, less-mathy distribution | Drafting (CAR-06) | "What do I want most?" rather than precise valuation. |
| Refilling market | Market Row (Ascension, Star Realms) | Replaces Dominion's static market. |
| Preserve deck order | No-Shuffle (Aeon's End) | Removing shuffle variance changes strategic landscape. |

**Card tells:**
- Dealing the whole deck in trick-taking → rewards memory and card-counting; deal a subset (Diamonds) to lower impact.
- Bare pick-and-pass drafts → first picker advantaged; use snake or Kingdomino-style "pick valuable = go last next round."
- Deck builders with only one viable strategy → synergies too tightly coupled; include orthogonal paths (Dominion's Cornucopia).
- Hand limits in co-op → difficulty dial; loosening them is the easiest way to make a card game easier (Forbidden Island).
- Wheeling / hate-drafting → emergent behaviors, not rules; evaluate prototypes for them, don't legislate them.

## Universal Tells & Smells

| Smell | Likely cause | Fix |
|---|---|---|
| Players bored mid-game | Pacing issue; one phase dominates | Interleave phases; add punctuated real-time |
| One player dominates co-op | Alpha-player problem | Communication limits, real-time pressure, hidden info |
| Trailing player has no hope | Snowball without catch-up | Split victory currency from working currency; add King of the Hill |
| Players avoid conflict | Turtling | Force interaction; escalating stakes; Highest Lowest scoring |
| Game length varies wildly | Open trading without time limits; or unconstrained negotiation | Time-box trading; restrict to immediate execution |
| Analysis paralysis | Too much hidden info; or too-precise valuation | Reduce hidden info; obscure value via set collection |
| Replayability low | Single dominant strategy; no orthogonal sets | Add variable setup; orthogonal scoring dimensions |

## Cross-Chapter Equivalences (mental shortcuts)

| If you're using... | Think of it as... |
|---|---|
| Trick Taking (CAR-01) | A specialized auction where the lot = the bids. |
| Multiple-Lot Auction (AUC-11) | Area Majority (ARC-02) with bidding tokens. |
| Worker Placement (WPL-01) | Action Drafting (ACT-02) with the worker-in-building metaphor. |
| Deck Building (CAR-05) | Drafting verbs; Orléans drafts nouns; Assault of the Giants drafts adjectives. |
| Catch the Leader (VIC-18) | Self-balancing dynamic where players refuse to trade with the leader. |
| Variable Setup (UNC-10) | The "last page of the rules" — defines the game as much as base rules. |
