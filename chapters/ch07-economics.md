# Chapter 7: Economics

## Core Idea
Games are about gaining and using assets to achieve victory; economic mechanisms govern how scarce resources are allocated, transformed, valued, and exchanged between players and the bank.

## Frameworks Introduced
- **Exchanging (ECO-01)**: Players swap a set of assets for a different set with the bank (covers both resource conversion and purchasing).
  - When to use: Any time players convert one asset into another via fixed or formulaic rates.
  - How: Define fixed cost formulas (e.g., Road = Brick + Grain) or hierarchical/non-hierarchical conversion chains.
- **Trading (ECO-02)**: Players exchange assets with each other on player-determined terms.
  - When to use: To add interaction and self-balancing; requires value to differ between players.
  - How: Use Sets to obscure precise value; constrain to timed phases or like-for-like rules.
- **Market (ECO-03)**: Players buy/sell to a market where prices and quantities vary.
  - When to use: When prices should self-balance based on player behavior.
  - How: Track price on a 1-D track, 2-D grid (18xx), or via commodity tokens placed on the track itself.
- **Delayed Purchase (ECO-04)**: Purchased items arrive on a future turn.
  - When to use: To force planning ahead and model production time.
  - How: Place items on a turn track, training facility, production spiral, or discard pile (deck-builders).
- **Income (ECO-05)**: Players gain resources at defined times.
  - When to use: To foster growth and forward progress.
  - How: Choose timing (scheduled, player-controlled, random) and economy type (Open vs Closed).
- **Automatic Resource Growth (ECO-06)**: Held resources grow by a set amount each turn.
  - When to use: To gradually ramp player power simply and intuitively.
  - How: +1 per turn (Hearthstone Mana) or "unused resources breed" (Agricola animals).
- **Loans (ECO-07)**: Players borrow from the bank for more money.
  - When to use: To punish poor money management OR enable engine jump-starting.
  - How: Choose payback model (never, interest-only, repayable); frame carefully to incentivize correctly.
- **Always Available Purchases (ECO-08)**: Certain resources are always purchasable while others are limited.
  - When to use: As a safety valve for weak hands or unaffordable markets (common in deck-builders).
  - How: Offer baseline cards that are weaker but always available (Ascension's Mystics/Heavy Infantry).
- **I Cut, You Choose (ECO-09)**: One player divides a set; others choose first.
  - When to use: When value differs per player but must be obscured (typically 2 players).
  - How: Divider creates stacks; chooser picks; divider gets remainder. Extend to N players with the divider going last.
- **Discounts (ECO-10)**: Future purchases cost less; discounts persist and stack.
  - When to use: For engine-building effects and implicit tech trees.
  - How: Cards reduce future costs (Splendor gems) or grant free acquisition of specified buildings (7 Wonders).
- **Upgrades (ECO-11)**: Assets improve to better versions, often by replacement.
  - When to use: To nudge specialization and implement tech trees.
  - How: Replace card/tile, flip/rotate, or add a component (Monopoly houses); use obsolescence to force upgrades (18xx trains).
- **Random Production (ECO-12)**: Resources generated from a random process and distributed to qualifying players.
  - When to use: To keep all players engaged on others' turns.
  - How: Dice activate tiles (Catan); cards may have own-turn vs opponent-turn triggers (Space Base red/blue sides).
- **Investment (ECO-13)**: Players own shares of an entity and accrue dividends or majority bonuses.
  - When to use: For stock-holding dynamics paralleling Area Majority.
  - How: Pay dividends per share, or reward top shareholders (Acquire); limited shares enable locked majorities.
- **Ownership (ECO-14)**: Players own entities; others pay fees to use them.
  - When to use: To create multilevel value calculations and player interaction.
  - How: Owner uses free; others pay fee (Le Havre, Caylus); or majority shareholder controls entity actions (1830, Imperial).
- **Contracts (ECO-15)**: Players fulfill specific good combinations for rewards.
  - When to use: To give immediate direction, especially for new players.
  - How: Public (raced) or private; obtain via draw, tableau, draft, or auction.
- **Bribery (ECO-16)**: Players offer money to influence another player's action.
  - When to use: For structured, themed influence over an active player's decision.
  - How: Bribes placed on options; active player may accept or ignore (Santiago); or one-on-one negotiation (Sheriff of Nottingham).
- **Increase Value of Unchosen Resources (ECO-17)**: Unselected actions/resources grow in value.
  - When to use: To let players price options whose values vary or change over time (a Dutch Auction variant).
  - How: Add a coin/resource to unchosen roles (Puerto Rico), factions (Small World), or worker spaces (Agricola).
- **Negotiation (ECO-18)**: Players make agreements about courses of action (often non-binding).
  - When to use: To raise emotional stakes via honesty/loyalty tension.
  - How: Dedicated discussion phase; specify whether deals are binding and immediate-resolve only.
- **Alliances (ECO-19)**: Formal relationships that may change during the game.
  - When to use: When cooperation should be rule-bound and time-bound rather than informal.
  - How: Formal enter/exit steps with defined benefits (Dune worm-card windows; Cosmic Encounter per-battle alliances).

## Key Concepts
- **Asset**: Any source of value — money, goods, properties, turn order, board position, hand size.
- **Resource**: Money and goods specifically (not structures or intangibles).
- **Open economy**: A bank pumps new resources into the system; fosters progress, easier to balance.
- **Closed economy**: All resources already exist and only move between players; creates zero-sum timing dynamics.
- **Hierarchical resources**: Conversion chains where value is ordered (e.g., yellow < red < green < brown in Century).
- **Non-hierarchical (lateral) resources**: Resources transform sideways, enabling specialization (Catan sheep port).
- **Set Collection**: Cross-referenced mechanism (Ch 12) that makes the same good worth different amounts to different players — essential for Trading.
- **Strong left-right binding**: Games heavily impacted by turn order adjacency.
- **Catch-the-Leader (VIC-18)**: Self-balancing dynamic where players refuse to trade with or penalize the leader.

## Mental Models
- Use **Markets** when you want prices to self-balance resource production; use **Exchange** when you want predictable, fixed costs.
- Think of **Loans** as either punishment (poor money management) or leverage (engine jump-start) — the framing changes optimal strategy.
- Use **I Cut, You Choose** when value must be obscured and you want one player to self-police fairness.
- Think of **Increase Value of Unchosen Resources** as a Dutch Auction where the price is fixed but the reward rises until a buyer accepts.

## Anti-patterns
- **Forced mortgaging (Monopoly)**: Removes player choice and extends a trailing player's slow death spiral — designers should avoid mandatory mortgaging when players can't pay.
- **Fungible hierarchical resources without obstruction**: If conversion value is too clear and frictionless, resources behave like coins of different denominations — introduce efficiency constraints or time pressure.
- **Open Trading without time limits**: Lengthens games, excludes uninvolved or less assertive players, and creates rules ambiguities about timing.
- **Non-binding future promises in Trading**: Hard to police and requires failure-handling rules — restrict Trades to immediate execution; reserve promises for Negotiation.

## Reference Tables

### Income Timing and Economy Types
| Income Timing | Description | Example |
|---|---|---|
| Scheduled | Income phase at a fixed point in the sequence | Brass, Eclipse |
| Player-controlled | Triggered by a player's chosen action | Global Mogul, Market sales |
| Other-player-dependent | Income when opponents use your buildings | Le Havre, Caylus |
| Random | Driven by dice or card events | Monopoly (passing Go), Catan |

### Loan Payback Models Across Games
| Game | Loan Terms | End-Game Penalty |
|---|---|---|
| Railways of the World | Interest paid per bond each turn; never repaid | -1 VP per bond |
| Brass | Never repaid; immediately reduces ongoing income | None (opportunity cost) |
| Wealth of Nations | Declining cash increments; repayable for $25 | -3 VP per loan |
| Monopoly | Mortgage property; repay +10% to unmortgage | None (but property unusable) |

### Market Price-Track Implementations
| Implementation | Mechanism | Example |
|---|---|---|
| 1-D marker track | Marker moves on buy/sell | Supremacy |
| 2-D grid | Sell moves down column; dividends move columns | 18xx series |
| Commodity tokens on track | Tokens cover/reveal price spaces | Crude, Power Grid |
| One-way ratchet | Price only ever rises | Acquire |
| Declining within turn | Price drops as players buy | Rococo |

## Worked Example
**Century: Spice Road — hierarchical resource valuation.**
Cubes have fixed point values: yellow = 1, red = 2, green = 3, brown = 4. Victory cards pay points strictly equal to the cubes surrendered, so the 1-4 valuation also prices converter cards:
- A card converting green (3) into brown + yellow (4 + 1 = 5) yields net +2 value.
- A card converting red (2) into green (3) yields net +1 value.
Because card values are known, the design challenge becomes time efficiency: players must collect converter cards that assemble the specific cube sets their victory cards demand. Time becomes a second resource layered on top of the nominal cube values, preventing the resources from being trivially fungible.

## Key Takeaways
1. Distinguish **Market** (prices change, self-balancing) from **Exchange** (fixed prices, predictable) — the choice drives whether the system self-corrects.
2. **Trading** requires value to differ between players; use **Sets** to obscure precise value and enable deals.
3. **Increase Value of Unchosen Resources** lets players price options themselves — a flexible Dutch Auction variant for variable-value choices.
4. Frame **Loans** deliberately: as punishment they constrain; as leverage they enable aggressive engine-building (Railroad Tycoon essentially requires them).
5. **Ownership (ECO-14)** creates multilevel play when entity assets are separate from player assets — the core of 18xx and worker-placement building fees.
6. **Bribery** (resource for action) vs **Negotiation** (action for action, often non-binding) — the dividing line is fuzzy but useful for design intent.
7. **Closed economies** create zero-sum timing dynamics; be wealthy at the right time, poor at the right time.

## Connects To
- **Ch 8 Auctions**: Many economic mechanisms are auction-isomorphic — Increase Value of Unchosen Resources is a Dutch Auction (AUC-08); I Cut, You Choose relates to selection-order bidding.
- **Ch 9 Worker Placement**: Ownership (ECO-14) creates the building-fee dynamic central to Caylus and Le Havre; Increase Value of Unchosen Resources powers Agricola's accumulation spaces.
- **Ch 12 Set Collection**: Enables Trading by making the same good worth different amounts to different players.
- **VIC-18 Catch-the-Leader**: Trading and Negotiation serve as soft catch-the-leader mechanisms — players can refuse to trade with or penalize the leader.
