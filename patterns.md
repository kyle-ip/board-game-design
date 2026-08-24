# Patterns

Named mechanisms from *Building Blocks of Tabletop Game Design*, grouped by chapter/category. Each pattern preserves the book's exact name and code. Use this as a mechanism-selection lookup when designing.

**Coverage:** this file lists **high-leverage patterns**, not every code in a range. Section titles show the book's full code span; missing codes are defined in the matching `chapters/chNN-*.md`. Prefer this file for quick trade-offs; open the chapter for the complete catalogue.

## Game Structure (Ch 1) — STR-01 to STR-10 (complete in this file)

### Competitive Games (STR-01)
**When to use**: Default symmetric "fair fight" experience.
**How**: Equal starting positions, or balance asymmetries via meta-structures (bidding in bridge, alliances in Diplomacy); break ties decisively.
**Trade-offs**: Players remember endings — invest in tie-breakers.

### Cooperative Games (STR-02)
**When to use**: Gateway for new players, lower pressure, shared experience.
**How**: AI deck (Sentinels) or pure puzzle (Hanabi); counter the alpha-player problem via communication limits, real-time pressure, hidden info per player, or complex personal powers.
**Trade-offs**: Alpha player can dominate if not actively countered.

### Team-Based Games (STR-03)
**When to use**: Bilateral conflicts, supporting more players, role separation.
**How**: Assign openly or secretly; asymmetric factions in One vs. All need distinct victory conditions.
**Trade-offs**: Role rotation disorients new players.

### Solo Games (STR-04)
**When to use**: Solo market or add-on mode.
**How**: Goal-based (VP target), record-based (high score), or AI-based (Automa). Automa is representational, not procedural.
**Trade-offs**: Automa mimics outputs without simulating a full player.

### Semi-Cooperative Games (STR-05)
**When to use**: Blending co-op survival with personal ambition.
**How**: Ensure all players agree on whether group win + individual loss beats total group loss.
**Trade-offs**: Mismatched incentives cause sabotage.

### Single Loser Games (STR-06)
**When to use**: Light/party games, stacking/dexterity.
**How**: Avoid bash-the-loser runaway; encourage lighter confrontation.

### Traitor Games (STR-07)
**When to use**: Suspense and betrayal narrative.
**How**: Obfuscate (shuffle crisis card contributions); design post-reveal gameplay; provide reference materials.
**Trade-offs**: Players can't ask questions without revealing loyalty.

### Scenario/Mission/Campaign Games (STR-08)
**When to use**: Extending replayability; storytelling.
**How**: Reuse core rules across maps/missions; link sessions in campaign structure.

### Score-and-Reset Games (STR-09)
**When to use**: Card games, dexterity, games with strong turn-order advantage.
**How**: Cumulative scoring across rounds; partial resets possible (Amun-Re pyramids persist).

### Legacy Games (STR-10)
**When to use**: Long-form narrative commitment, visceral permanent change.
**How**: Combine irreversible destruction (tearing cards, writing on boards) with unlocks (gated content revealed at session end).
**Trade-offs**: Novel unrepeatable experience vs. replayability.

## Turn Order (Ch 2) — TRN-01 to TRN-17 (selected; full list in ch02)

### Fixed Turn Order (TRN-01)
**When to use**: Default; low complexity.
**How**: Player order never changes.
**Trade-offs**: First-player advantage must be compensated.

### Stat Turn Order (TRN-02)
**When to use**: Catch-the-leader; reward high investment.
**How**: Player order set by a stat (e.g., highest bid).
**Trade-offs**: Predictable; can be scripted.

### Progressive Turn Order (TRN-04)
**When to use**: Fluid turn passing.
**How**: Pass token; next passer goes next.
**Trade-offs**: Large gaps between turns at high player counts (9-turn gap in 5p).

### Real-Time (TRN-07)
**When to use**: Intensity under 20 minutes.
**How**: No turn order; all act simultaneously under clock.
**Trade-offs**: Manufacturing variation in sand timers; complexity mistakes cascade.

### Simultaneous Action Selection (TRN-09)
**When to use**: Yomi-enabling gameplay.
**How**: All choose at once; reveal simultaneously.
**Trade-offs**: Requires resolution phase to adjudicate.

### Time Track (TRN-13)
**When to use**: Action cost as waiting time.
**How**: Pay more time = wait longer to act again; "price tag" on each action.

### Interrupts (TRN-17)
**When to use**: Out-of-turn reactions.
**How**: LIFO stack resolution (Magic: The Gathering).

## Actions (Ch 3) — ACT-01 to ACT-18 (selected; full list in ch03)

### Action Points (ACT-01)
**When to use**: Flexibility > strictness.
**How**: Currency spent on actions; budget per turn.

### Action Drafting (ACT-02)
**When to use**: Marketplace metaphor; denial as valuable as acquisition.
**How**: Select from a dwindling set of actions.

### Action Retrieval (ACT-03)
**When to use**: Strictness > flexibility; readable turn budgets.
**How**: Spent actions go to a spent pool until a retrieve action returns them.
**Trade-offs**: Less flexible than Action Points; easier to teach and balance.

### Follow (ACT-08)
**When to use**: Keep all players engaged on every turn.
**How**: Non-active players may perform a version of the active player's action.
**Trade-offs**: Raises engagement; slows pace; watch for free-rider strength.

### Rondel (ACT-10)
**When to use**: Circular action selection with cost curve.
**How**: Movement costs increase with distance around the rondel.

### Variable Player Powers (ACT-12)
**When to use**: Asymmetric factions; best on simple frameworks.
**How**: Distinct abilities per faction.
**Trade-offs**: Cognitive load on complex frameworks; one correct strategy per faction limits replayability.

### Gating and Unlocking (ACT-15)
**When to use**: Designer-controlled pacing of new verbs.
**How**: New actions appear at scripted game points or thresholds.
**Trade-offs**: Predictable arc; less player-driven than Tech Trees.

### Tech Trees / Tech Tracks (ACT-16)
**When to use**: Player-driven specialization.
**How**: Prerequisite chains unlock new abilities.

## Resolution (Ch 4) — RES-01 to RES-22 (selected; full list in ch04)

### High Number (RES-01)
**When to use**: Force quantity should dominate.
**How**: Highest total wins.

### Stat Check (RES-02)
**When to use**: Unit quality should matter; hold one target number constant.
**How**: Roll + modifier vs. target number.

### Critical Hits and Failures (RES-03)
**When to use**: Add jackpot excitement.
**How**: Extreme die faces generate bonus success / catastrophic failure; exploding dice possible.

### Card Play (RES-06)
**When to use**: Tactical counter-play; Yomi through card-exhaustion tracking.
**How**: Cards modify base conflict outcomes (Kemet's strength/shield/damage).

### Rock, Paper, Scissors (RES-07)
**When to use**: Antidote to transitive strength ladders.
**How**: No single unit type always best.

### Force Commitment (RES-14)
**When to use**: Battle about guessing intent, not comparing sizes.
**How**: Players commit forces before revealing.

### Enclosure (RES-12)
**When to use**: Surround capture (Go, Reversi).
**How**: Corner/edge spaces more valuable (harder to enclose).

### Rerolling and Locking (RES-21)
**When to use**: Push-your-luck in dice resolution.
**How**: Dice may be rerolled or locked; rerolling averages ~+0.75 but can worsen result (Yahtzee).

## Game End and Victory (Ch 5) — VIC-01 to VIC-20 (selected; full list in ch05)

### Victory Points from Game State (VIC-01)
**When to use**: Default VP scoring.
**How**: Score from board state at game end.

### Temporary and Permanent Victory Points (VIC-03)
**When to use**: Mix for ideal tension.
**How**: Permanent VPs drive conclusion; temporary VPs allow sudden grabs.
**Trade-offs**: All-temporary with threshold end encourages perpetual leader-bashing.

### End-Game Bonuses (VIC-06)
**When to use**: Roadmap for new players.
**How**: Personal goals tell players what to pursue from turn one.

### Race (VIC-07)
**When to use**: First-to-target.
**How**: Many VP-threshold games are races in disguise (Catan's 10 points).

### Player Elimination (VIC-08)
**When to use**: Short/light games or thematically consonant designs.
**Trade-offs**: Anti-pattern except in those cases.

### Fixed Number of Rounds (VIC-09)
**When to use**: Predictable length.
**How**: Prefer natural tracking (depleting card stacks) over round marker.

### King of the Hill (VIC-17)
**When to use**: Force conflict, prevent turtling.
**How**: Points earned by occupying a special board position; naturally creates catch-the-leader dynamics.

### Highest Lowest (VIC-20)
**When to use**: Force breadth, anti-specialization.
**How**: Player with highest *lowest* score wins.

## Uncertainty (Ch 6) — UNC-01 to UNC-11 (selected; full list in ch06)

### Betting and Bluffing (UNC-01)
**When to use**: Social, conversational uncertainty.
**How**: Players wager on hidden information.

### Push-Your-Luck (UNC-02)
**When to use**: Sunk-cost attachment + uncalculable odds.
**How**: Risk current gains for more; if EV always computable, tension evaporates.

### Memory (UNC-03)
**When to use**: Hidden, trackable information (HTI).
**Trade-offs**: Sharply reduces accessibility; provide tracking components.

### Hidden Roles (UNC-04)
**When to use**: Social, conversational uncertainty.
**How**: Players have secret identities with different win conditions.

### Communication Limits (UNC-06)
**When to use**: Cooperative games (Hanabi, The Mind), party games (Charades).
**How**: Restrict what/how players communicate.

### Unknown Information (UNC-07)
**When to use**: Systemic, replayable uncertainty shared by all.
**How**: State aspects unknown to everyone but within a known range (draw decks, face-down tiles).

### Hidden Information (UNC-08)
**When to use**: Deductive / secret-goal play.
**How**: Some players know what others do not (hands, secret objectives).
**Trade-offs**: Distinct from Unknown Information — at least one player has the secret.

### Variable Setup (UNC-10)
**When to use**: "Last page of the rules."
**How**: Different starting configurations (Dominion's 10 kingdom cards define the game as much as base rules).

## Economics (Ch 7) — ECO-01 to ECO-19 (selected; full list in ch07)

### Exchanging (ECO-01)
**When to use**: Fixed-ratio conversion.
**How**: Direct resource conversion.

### Market (ECO-03)
**When to use**: Self-balancing prices.
**How**: Prices respond to production.

### I Cut, You Choose (ECO-09)
**When to use**: Obscure value; self-policing fairness.
**How**: One player divides, the other selects.

### Loans (ECO-07)
**When to use**: Either punishment (poor money management) or leverage (engine jump-start).
**How**: Borrowed resources; framing changes optimal strategy.

## Auctions (Ch 8) — AUC-01 to AUC-16 (selected; full list in ch08)

### Open Auction (AUC-01)
**When to use**: Free-form; rare.
**Trade-offs**: Messy, noisy, confusing without auctioneer.

### English Auction (AUC-02)
**When to use**: Standard ascending-bid.
**How**: Bids increase until no one bids higher.

### Sealed-Bid Auction (AUC-04)
**When to use**: Auctions as sub-system; must be quick.
**How**: All bid simultaneously.

### Constrained Bidding (AUC-06)
**When to use**: Solve auction length + small-value distinctions.
**How**: Fixed budget of bidding tokens.

### Dutch Auction (AUC-08)
**When to use**: Most ergonomic, durable resource-allocation tool.
**How**: Price drops until a buyer accepts; market-row implementation is quick, decisive, board-space efficient.

### Vickrey / Second-Bid Auction (AUC-09)
**When to use**: Rarely; rules overhead rarely worth it.
**How**: Winner pays second-highest bid; truthful bidding dominant but unintuitive.

### Multiple-Lot Auction (AUC-11)
**When to use**: Mathematically identical to Area Majority.
**How**: Simultaneous auction of multiple lots; troops/influence cubes are bidding tokens.

### Reverse Auction (AUC-13)
**When to use**: Seasoning only.
**How**: Price to avoid a penalty; everyone loses.

## Worker Placement (Ch 9) — WPL-01 to WPL-08 (selected; full list in ch09)

### Standard Worker Placement (WPL-01)
**When to use**: Intuitive action drafting; worker-in-building metaphor.
**How**: Workers claim exclusive action spaces; hard blocking by default.

### Workers of Differing Types (WPL-02)
**When to use**: Asymmetric worker abilities.
**How**: Different workers unlock different actions.

### Acquiring and Losing Workers (WPL-03)
**When to use**: Worker acquisition as declining-price auction.
**How**: Early workers pay off across more turns; late workers must be cheap.
**Trade-offs**: Unmetered worker growth = dominant strategy.

### Workers-As-Dice (WPL-04)
**When to use**: Pool-building crossover.
**How**: Dice drafted into a worker pool.

### Adding and Blocking Buildings (WPL-05)
**When to use**: Evolving action market.
**How**: Players add buildings to the board, blocking others.

### Single Workers (WPL-06)
**When to use**: Focused worker games; no worker-economy side game.
**How**: Each player has one primary worker and cannot acquire more.

### Building Actions and Rewards (WPL-07)
**When to use**: Ownership and timing matter on spaces.
**How**: Rewards vary by owner, turn order, or upgrades.

### Turn Order and Resolution Order (WPL-08)
**When to use**: When placement order vs resolution order is a design lever.
**How**: Separate who places when from when actions fire (e.g. delayed resolution).
**Trade-offs**: Strong left-right binding — compensate adjacent-seat windfalls.

## Movement (Ch 10) — MOV-01 to MOV-24 (selected; full list in ch10)

### Tessellation (MOV-01)
**When to use**: Regulate movement on a grid.
**How**: Hexagons preferred over squares when diagonal realism matters (50%-shifted square "brick" grid is isomorphic to hex).

### Roll and Move (MOV-02)
**When to use**: Anti-pattern without mitigation.
**How**: Mitigate via choice in applying roll (Backgammon), wagering (Camel Up), or push-your-luck wraps.

### Movement Points (MOV-04)
**When to use**: Movement as currency.
**How**: Spend points on terrain; wargame infantry 3 MP vs armor 6 MP.

### Movement Template (MOV-20)
**When to use**: Miniatures games.
**How**: Defined templates (Short Straight, Sharp Right) determine movement (X-Wing Miniatures).

### Pieces as Map (MOV-21)
**When to use**: No separate board.
**How**: Units themselves compose the map (Hive).

### Hidden Movement
**When to use**: Suspense; simpler rules than open movement.
**How**: Anchor/distance technique — track last known position + distance counter.
**Trade-offs**: Any error invalidates the entire experience; uncatchable mid-game.

## Area Control (Ch 11) — ARC-01 to ARC-08 (selected; full list in ch11)

### Absolute Control (ARC-01)
**When to use**: Entry should trigger combat.
**How**: One player's forces exclusive in an area.

### Area Majority / Influence (ARC-02)
**When to use**: Opposing forces co-exist peacefully.
**How**: Most forces in an area control it.
**Trade-offs**: Specify friendly vs unfriendly ties explicitly.

### Force Projection (ARC-06)
**When to use**: Spatial equivalent of remaining money in an auction.
**How**: A unit's potential to act in adjacent spaces threatens every opponent decision.

### Zone of Control (ARC-07)
**When to use**: Hard (wargame must-attack friction) vs. Soft (costly but possible movement).
**How**: Restrict ZOC to identifiable unit types.

### Line of Sight (ARC-08)
**When to use**: Visibility/attack determination.
**How**: Use cylinder proxies (Warmachine) or lookup tables to avoid thread-laying disputes.

## Set Collection (Ch 12) — SET-01 to SET-05 (selected; full list in ch12)

### Set Valuation (SET-01)
**When to use**: Default escalating curve.
**How**: Triangular numbers (1, 3, 6, 10, 15...); marginal value of nth card = n.
**Trade-offs**: Pure linear valuation removes synergy; always curve the value.

### Tile-Laying (SET-02)
**When to use**: Spatial set collection.
**How**: Tiles placed to form scoring sets.

### Network Building (SET-04)
**When to use**: Telescoping set of sets.
**How**: A ticket is a super-set satisfied by many possible route sub-sets (Ticket to Ride).

### Combo Abilities (SET-05)
**When to use**: Discovery rather than declaration.
**How**: Magic: The Gathering's combos are engaging because designers didn't pre-declare them.
**Trade-offs**: Pre-declaring all combos steals joy of discovery.

## Card Mechanisms (Ch 13) — CAR-01 to CAR-06 (complete in this file)

### Trick Taking (CAR-01)
**When to use**: Card-by-card comparison tied to contract/bid.
**How**: Deal cards; follow lead suit if able; highest of lead suit wins unless trump; winner leads next.
**Mental model**: Highly specialized auction where lot = bids.

### Ladder Climbing (CAR-02)
**When to use**: Shedding + set-comparison hybrid (East Asian traditions).
**How**: Lead with single/pair/triple/quad/run; followers must match set shape + equal-or-exceed rank; bombs override.

### Melding and Splaying (CAR-03)
**When to use**: Rummy-style sets/runs; cards whose physical overlap matters (Innovation).
**How**: Assemble melds; lay on table; others may lay off; splay left/right/up to reveal/conceal icon rows.

### Card Draw Limits and Deck Exhaustion (CAR-04)
**When to use**: Card economy shapes difficulty.
**How**: Set hand limit (static or government-dependent); draw limit (Ticket to Ride: 2 cards, 1 if wild); define deck-exhaustion triggers.
**Trade-offs**: Hand limits are difficulty dials in co-op games (Forbidden Island).

### Deck Building (CAR-05)
**When to use**: Self-improving engine; past acquisitions shape future draws.
**How**: Thin starter deck; play up to N action cards; spend money to buy from market (static Dominion / refilling row Ascension); draw back to hand size; cycle as deck exhausts.

### Drafting (CAR-06)
**When to use**: Quick, less-mathy distribution than auctions.
**How**: Rochester (full info), pick-and-pass (simplicity), snake (balance), parallel (speed).
**Trade-offs**: First picker advantaged; mitigate with snake or Kingdomino-style cost.
