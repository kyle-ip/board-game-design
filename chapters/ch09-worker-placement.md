# Chapter 9: Worker Placement

## Core Idea
Worker Placement is action drafting where players select actions by placing workers on buildings; its enduring popularity comes from tight theme-mechanism correspondence — placing a worker in a sawmill to generate wood is intuitive and memorable, making the underlying auction/drafting structure accessible.

## Frameworks Introduced
- **Standard Worker Placement (WPL-01)**: Players place a worker on a building in turn order and execute the action immediately; round ends when all workers are placed.
  - When to use: The baseline — intuitive action drafting with blocking (Agricola, Lords of Waterdeep).
  - How: One worker per turn per building; immediate resolution (improvement over Caylus's end-of-round resolution).
- **Workers of Differing Types (WPL-02)**: Workers vary in ability, tier, or building access.
  - When to use: To add specialization and majority contests among worker types.
  - How: Improved workers count as multiple basics (Belfort); specialists access restricted buildings (Manhattan Project scientists/engineers); dice workers show capability via pips (Praetor, Euphoria).
- **Acquiring and Losing Workers (WPL-03)**: Workers beyond the starting complement may be gained (temporarily or permanently) or lost.
  - When to use: To create a growth arc — but meter it, or acquisition becomes dominant strategy.
  - How: Purchase with housing (Caverna); fixed mid-game grant (Lords of Waterdeep); temporary hire (Snowdonia); feeding/upkeep cost (Agricola); attrition via aging/retirement (Village, Praetor).
- **Workers-As-Dice (WPL-04)**: Workers are dice whose pip values impact placement or effectiveness.
  - When to use: To introduce probability management into worker placement.
  - How: Allocate dice to buildings matching pip combinations (Alien Frontiers); pip value = resource yield (Artemis Project); warrior dice = combat strength (Champions of Midgard).
- **Adding and Blocking Buildings (WPL-05)**: Buildings (and their actions) are added to the pool; buildings may be occupied to block or hinder others.
  - When to use: To manage action availability and scarcity across the game arc.
  - How: Static set (Stone Age), revealed pattern (Agricola), or player-built with ownership rewards (Caylus, Lords of Waterdeep). Blocking can be hard (one worker) or soft (cost increase, dueling, bumping).
- **Single Workers (WPL-06)**: Players control only one primary worker and cannot acquire more.
  - When to use: To blur into role-selection, rondel, and time-track games while retaining blocking.
  - How: Block along multiple axes (Kanban: occupied space, same-department rule, neutral boss); or leave assistants that gain bonuses when bumped (The Gallerist, Istanbul).
- **Building Actions and Rewards (WPL-07)**: Buildings offer varying rewards based on ownership, turn order, or upgrades.
  - When to use: To create declining-reward dynamics and combo opportunities.
  - How: First-claimer gets more (role-selection flavor); choice among rewards (Caylus, Yedo districts); accumulation spaces grow richer over time (Agricola); buildings replaceable mid-play (Fabled Fruit).
- **Turn Order and Resolution Order (WPL-08)**: The order of action selection and resolution is a design variable.
  - When to use: To fold turn order into the worker placement engine and separate placement from resolution.
  - How: Turn Order building (Lords of Waterdeep — has strong left-right binding); draft turn order + workers together (Last Will); random master-builder pull with descending price (Pillars of the Earth = Dutch Auction); delayed resolution enables combos and the Provost (Caylus).

## Key Concepts
- **Action Drafting (ACT-02)**: The mathematical parent mechanism of Worker Placement — selecting from a dwindling set of actions.
- **Blocking (hard)**: An occupied building cannot be used by others — the standard scarcity mechanic.
- **Blocking (soft)**: Occupied buildings cost more (Coal Baron), require a duel (Carson City), or trigger bumping.
- **Bumping**: An occupied building is reused; the original worker is displaced and the owner gains a bonus (Euphoria, The Gallerist, Istanbul).
- **Worker upkeep / feeding**: A recurring cost for permanent workers that throttles worker acquisition (Agricola's feeding is famously unforgiving; Stone Age's is toothless).
- **Immediate vs delayed resolution**: Whether a building's reward pays on placement (Agricola) or at end of round (Caylus) — delayed enables combos and placement-order independence.
- **Private vs public actions**: Private actions are owner-only or owner-cheap (The Manhattan Project); public actions are always available to all (Stone Age resource spaces).
- **Master builder**: A special worker type or token-pull mechanism governing placement priority (Pillars of the Earth).
- **Strong left-right binding**: Turn Order decisions disproportionately affect adjacent players — a key design challenge in WPL-08.

## Mental Models
- Use **Worker Placement** when you want intuitive action drafting — the worker-in-building metaphor makes rules and incentives memorable without requiring players to understand the underlying auction math.
- Use **soft blocking (bumping)** when you want fluidity without removing scarcity — bumped players gain a bonus, turning blocking into a feature rather than a frustration.
- Think of **worker acquisition as a declining-price auction** — early workers pay off across more turns, so they're worth more; late workers must be cheap to be worth buying.
- Use **delayed resolution (Caylus)** when you want placement-order independence, combos, and space for an intervening mechanism like the Provost.

## Anti-patterns
- **Turn Order building with strong left-right binding (Lords of Waterdeep)**: The player to the left of the new start player gets an unearned windfall; the player to the right is penalized through no fault of their own — design around it with multiple slots or by folding turn order into other choices.
- **Unmetered worker growth**: If workers are too easy to acquire, it becomes the dominant strategy (Stone Age's reproduction hut is picked first or second every round) — require housing, feeding costs, or hard caps.
- **Toothless feeding costs (Stone Age)**: Makes a starvation strategy viable, removing the tension that worker upkeep is meant to create.
- **Thematic dissonance (Dungeon Petz)**: When the rule "largest worker group goes first" has no real-world analogue, players struggle to remember and internalize the mechanism.
- **Single-Worker games without blocking**: If players can't interfere with each other, it's an Action Point game (ACT-01), not Worker Placement — the blocking element is definitional.
- **Excluding the worker metaphor**: Games like Orleans and Through the Ages place workers on private tableaus without drafting or blocking — these fall outside the chapter's narrower definition.

## Reference Tables

### Blocking Types
| Type | Mechanism | Example |
|---|---|---|
| Hard blocking | One worker per building; occupied = blocked | Agricola, Lords of Waterdeep |
| Cost increase | Occupied building costs more for others | Coal Baron |
| Duel | Workers in same space duel for reward | Carson City |
| Bumping | Reuse occupied building; original worker displaced + bonus to owner | Euphoria, The Gallerist |
| Payment to blocker | Placing player pays the blocker to use the space | Istanbul |

### Worker Acquisition Models
| Model | Mechanism | Trade-off |
|---|---|---|
| Housing purchase | Build housing to gain worker | Up-front resource investment (Caverna) |
| Fixed mid-game grant | All players gain a worker on a set turn | No cost, balanced (Lords of Waterdeep) |
| Temporary hire | Worker returns after use | Must re-hire each time (Snowdonia) |
| Feeding cost | Recurring upkeep per worker | Throttles acquisition (Agricola) |
| Hard cap | Total pip value capped | Limits incentive (Euphoria) |
| Turn-order trade-off | More workers = later turn order | Reduces worker EV (Last Will) |

### Resolution Timing Models
| Model | When Resolved | Enables |
|---|---|---|
| Immediate | On placement | Faster play, less memory load (Agricola) |
| End-of-round | After all placement complete | Combos, Provost, placement-order independence (Caylus) |
| On recall | When owner retrieves worker | Escalating rewards, timing decisions (Tzolk'in, Manhattan Project) |

## Worked Example
**Pillars of the Earth — master-builder pull as a Dutch Auction.**
Each round, all players' master builders are placed in a bag and drawn one at a time:
1. When a player's builder is drawn, they may pay the current gold price to take an action immediately, or pass and accept a later turn-order position.
2. The price of actions decreases by one gold with each successive draw.
3. This is structurally a **Dutch Auction (AUC-08)**: the price descends until a buyer accepts, but the "buyer" is determined randomly rather than by who calls out first.
4. The randomness drew critique, but the core idea — a variable, descending price for placement priority — survived in **Lords of Waterdeep's Waterdeep Harbor**: placing a worker there yields an Intrigue card (the reward) at the cost of waiting for all other workers to be placed before reassigning that worker to a real action space. The implied cost (lost priority) decreases with each passing turn, mirroring the explicit gold-price decrease in Pillars of the Earth.

## Key Takeaways
1. Worker Placement's power is **theme-mechanism correspondence** — the worker-in-building metaphor makes rules intuitive and incentives legible without exposing the auction math.
2. **Meter worker growth** (housing costs, feeding costs, hard caps) or acquisition becomes the dominant strategy.
3. **Hard blocking** creates scarcity; **soft blocking** (bumping, cost increases, dueling) maintains fluidity and reduces frustration.
4. **Separate placement from resolution** when you want combos, escalating rewards, or an intervening mechanism like Caylus's Provost.
5. **Turn Order buildings create strong left-right binding** — design around it with multiple slots, descending-price mechanisms, or by folding turn order into other draft choices.
6. **Worker acquisition is a declining-price auction** — early workers pay off across more turns, so they're worth a higher purchase price than late ones.
7. **Single-Worker games** blur into Action Point (ACT-01), Action Drafting (ACT-02), Rondel (ACT-10), and Time Track (TRN-13) games; the worker metaphor and blocking element are what distinguish them.
8. The chapter's narrower definition (action drafting + blocking + worker theme) excludes tableau-only games (Orleans, Through the Ages) and bid-marker games (Jórvík, Spyrium, Keyflower).

## Connects To
- **Ch 8 Auctions**: Worker Placement is a specialized auction — workers are bid tokens, blocking is allocation, and Pillars of the Earth explicitly uses a Dutch Auction (AUC-08) for placement priority.
- **Ch 7 Economics**: Ownership (ECO-14) creates the building-fee dynamic in Caylus and Le Havre; Increase Value of Unchosen Resources (ECO-17) powers Agricola's accumulation spaces; Contracts (ECO-15) often intersect with worker actions.
- **Ch 3 Actions**: Worker Placement is a form of Action Drafting (ACT-02); Single-Worker games border on Action Point (ACT-01) and Rondel (ACT-10) mechanisms.
- **Ch 2 Turn Order**: Turn Order and Resolution Order (WPL-08) connects to Claim Turn Order Action (TRN-05) and Random Turn Order (TRN-11).
- **AUC-08 Dutch Auction**: Pillars of the Earth's master-builder pull and Agricola's accumulation spaces are both Dutch Auction variants expressed through worker placement.
