# Chapter 8: Auctions

## Core Idea
Auctions allocate resources fairly while providing agency, drama, and skill-testing; they are the "skeletal system" of games, with many other mechanisms (worker placement, area majority, trick-taking) being mathematically isomorphic to auction types.

## Frameworks Introduced
- **Open Auction (AUC-01)**: Players shout bids freely with no turn order; seller may accept any bid at any time. Rarely used — messy and noisy; mainly a theoretical basis. No auctioneer; high bidder usually wins but no rule requires it.
- **English Auction (AUC-02)**: Auctioneer requests bids; players signal willingness; price ascends until no raises. Use when dynamic, dramatic bidding is desired; needs an auctioneer (or auctioneer-player as in Modern Art, where the seller rarely buys their own lot).
- **Turn Order Until Pass Auction (AUC-03)**: Players raise or pass in turn order; last remaining bidder wins. Simple, intuitive allocation without an auctioneer (Power Grid, Through the Ages). Pass = out (usually); re-entry variant allows returning but lengthens play.
- **Sealed-Bid Auction (AUC-04)**: All players secretly bid; high bid wins on simultaneous reveal. Use when auctions must be quick and decisive (sub-systems, sequential auctions like A Game of Thrones). Closed-fist currency, dials, or screens; requires a tie-breaker.
- **Sealed Bid with Cancellation (AUC-05)**: Tied high bids cancel and become the lowest bids. Use in lighter, chaotic games with constrained bid markers and high Yomi; pair with limited token sets so ties are likely, letting a weak bid win when two strong bidders cancel.
- **Constrained Bidding (AUC-06)**: Meta-mechanism limiting valid bids to specific increments or token combinations. Use to speed auctions and force larger value distinctions (Knizia's Ra, Amun-Re, High Society). Fixed bid tokens can't make change — balance initial apportionment and redistribution carefully.
- **Once-Around Auction (AUC-07)**: Each player gets one bid opportunity (pass or raise); high bidder wins after one round. Use when tight coupling to turn order is desirable (Medici, Modern Art). Strong left-right binding — first bidder sets market blind, last bidder has perfect info.
- **Dutch Auction (AUC-08)**: Price starts high and descends until first bidder accepts; no ties possible. Use to maximize seller price and pressure buyers to act fast; the market-row implementation (cards slide to cheaper positions) is the most durable allocation solution. Clock countdown (rare) or row/river of cards; last card often free.
- **Second-Bid Auction / Vickrey (AUC-09)**: Highest bidder pays the second-highest bid amount. Theoretically encourages truthful bidding (dominant strategy), but rare in practice (Das letzte Paradies) — players don't intuit the strategy, and the efficiency reduces strategic interest.
- **Selection Order Bid (AUC-10)**: Players bid for draft order, not the lots themselves; passers take later picks. Use for elegant multi-lot allocation (For Sale, Age of Steam). Pay-half-when-pass variant acts like a simultaneous two-lot bid.
- **Multiple-Lot Auction (AUC-11)**: Players bid on multiple lots simultaneously in parallel. Compresses allocation time; isomorphic to Area Majority. Players manage which lots to bid on AND how to divide money across them; compatible with sealed, fixed-placement, and Dutch Priority variants.
- **Closed-Economy Auction (AUC-12)**: Meta-mechanism where all spent money is paid to participants; total money never changes. Use for zero-sum timing dynamics — be wealthy at the right moment (Ra, Dream Factory, No Thanks!). Handle remainder by leaving it in the center for the next bid.
- **Reverse Auction (AUC-13)**: Players bid to AVOID taking a lot with negative effects; non-claimants usually pay. Use as seasoning, not central mechanism — inherently negative experience (No Thanks!, High Society misfortune cards). Claimant takes the lot plus all bid tokens placed.
- **Dexterity Auction (AUC-14)**: A dexterity act is required to submit a valid bid. Use for real-time, physical bidding drama (Going, Going, GONE!); potentially inaccessible. Drop bid tokens into cups; only tokens landing inside count.
- **Fixed-Placement Auction (AUC-15)**: Meta-mechanism using a board track to visually represent bids on multiple lots; often with constrained values. Use to govern multi-lot bidding, prevent rebidding on just-outbid lots, and integrate bidding with other actions (Amun-Re, Cyclades, Vegas Showdown). Triangular bid increments prevent $1-at-a-time grinding.
- **Dutch Priority Auction (AUC-16)**: Multiple-lot auction where price = number of bid tokens on a lot; priority player chooses to pay or pass (removing a token, dropping price by one). Use when players must declare interest in lots separately from pricing (Die Speicherstadt/Jórvík, Spyrium). Passing may yield money (Spyrium).

## Key Concepts
- **Lot**: The item or group of items up for auction.
- **All-pay auction**: All bidders pay their bids regardless of winning (common in combat/battle themes).
- **Winner-pay**: Only the winner pays (standard purchase auctions).
- **Vickrey auction**: Synonym for Second-Bid Auction; winner pays second-highest bid.
- **Strong left-right binding**: Games heavily impacted by turn order and seating adjacency (Once-Around, Turn Order buildings).
- **Market row / river of lots**: Dutch Auction implementation where cards slide to cheaper positions as the turn progresses.
- **Penny auction**: Players pay a fee per bid even if they don't win (analogous to Selection Order Bid's pay-half-when-pass).
- **Lighthouse bidding**: Leaving a paddle up to signal long-haul commitment (English Auction psychology).

## Mental Models
- Use **Sealed-Bid** when auctions are a sub-system and must be quick; use **Turn Order Until Pass** when iterative information reveal matters.
- Use **Constrained Bidding** to solve two problems at once: auction length and the difficulty of making small value distinctions.
- Think of **Multiple-Lot Auctions** as mathematically identical to **Area Majority** — troops/influence cubes are bidding tokens.
- Use **Reverse Auctions** only as seasoning — everyone loses, so they flavor a game rather than anchor it.
- Think of **Dutch Auction market rows** as the most ergonomic, durable resource-allocation tool — they're quick, decisive, and board-space efficient.

## Anti-patterns
- **Too-precise valuation**: If a lot's value is exactly knowable (a $10 bill), bidding collapses — obscure value via hidden goals, future-dependent value, or set collection.
- **Turn Order Until Pass with $1 increments**: Slow and tedious; the dominant strategy is to increment minimally, so designers must incentivize larger increments.
- **Vickrey Auctions in practice**: Players don't intuitively understand that truthful bidding is dominant, and the efficiency makes outcomes less interesting — rarely worth the rules overhead.
- **Reverse Auctions as the central mechanism**: The experience is inherently negative (the "winner" gets a penalty, losers pay) — No Thanks! is the rare exception that works.
- **Open Auctions**: Messy, noisy, confusing — multiple bidders bid the same amounts, increments are inconsistent, and governance is difficult without an auctioneer.
- **Constrained Bidding without redistribution planning**: Fixed tokens can't make change — designers must carefully balance initial apportionment and how tokens return to owners.

## Reference Tables

### Auction Type Comparison
| Type | Speed | Info Revealed | Turn-Order Sensitivity | Tie Handling |
|---|---|---|---|---|
| Open | Slow | High | Low | Messy / ungoverned |
| English | Slow | High | Low | Auctioneer decides |
| Turn Order Until Pass | Medium | Medium | Medium | First to bid wins |
| Sealed-Bid | Fast | Low | None | Tie-breaker needed |
| Sealed w/ Cancellation | Fast | Low | None | Ties cancel (become lowest) |
| Once-Around | Fast | Medium | High | Last bidder wins |
| Dutch (clock) | Fast | None | None | First to accept wins |
| Selection Order Bid | Medium | Medium | High | Last remaining pays full |
| Fixed-Placement | Medium | High | Turn-governed | Top bidder per lot |

### Dutch Auction Market-Row Variants
| Variant | Example |
|---|---|
| Cards slide to cheaper positions when purchased | Suburbia, Through the Ages |
| Bypassing a card adds a coin; purchaser collects coins | Small World |
| Lowest card removed each turn; new card enters pricey side | Pax series |
| Prices on a rotating wheel adjust tile costs | Vikings |

### Payment Model Variants
| Model | Who Pays | Thematically Fits |
|---|---|---|
| Winner-pay | Winner only | Purchasing goods |
| All-pay | All bidders | Battles, political contests |
| Loser-pays-half | Passers pay half their bid | For Sale (Selection Order Bid) |
| Closed-economy | Winner pays other participants | Ra, Dream Factory |

## Worked Example
**For Sale — Selection Order Bid (AUC-10) with pay-half-when-pass.**
A flop of property cards is revealed with widely varying values (e.g., a $2 card and a $30 card in the same round). Players bid in turn order for the right to draft first:
1. Players raise or pass in turn order. Passing means taking the **lowest-value card remaining** and paying **half** the previous bid.
2. The last player remaining takes the **highest-value card** and pays the **full** bid.
3. Reinterpreting the structure: each player is simultaneously bidding **full price** on the most valuable card AND placing a **half-price ante** on the least valuable card they'd accept. The half-price payment functions like a penny-auction bid fee.
4. The design's elegance: it compresses allocation into one round, creates strong turn-order dynamics (early bidders set the market blind; late bidders have full information), and the pay-half-when-pass mechanic incentivizes higher opening bids because passing recovers value.

## Key Takeaways
1. Auctions require **obscured value** — if players can value lots too precisely, bidding collapses to a single rational price.
2. **Constrained Bidding** solves two auction defects at once: excessive length and the difficulty of making small value distinctions.
3. **Dutch Auctions as market rows** are the most durable, ergonomic resource-allocation tool — quick, decisive, and board-space efficient.
4. **Multiple-Lot Auctions are isomorphic to Area Majority** — troops and influence cubes are bidding tokens in disguise.
5. **Vickrey Auctions** are theoretically elegant (bid your true value) but rarely used — players don't intuit the dominant strategy, and the efficiency reduces strategic interest.
6. **Reverse Auctions** are inherently negative experiences; use them as seasoning, not as the core mechanism (No Thanks! is the rare exception).
7. **Closed-Economy Auctions** create zero-sum timing dynamics — the core challenge is being wealthy at the right time and poor at the right time.
8. Auctions declined in popularity as **Worker Placement (Ch 9)** and **Drafting (CAR-06)** offered alternative allocation methods requiring less precise valuation.

## Connects To
- **Ch 7 Economics**: Increase Value of Unchosen Resources (ECO-17) is a Dutch Auction variant; I Cut, You Choose (ECO-09) relates to Selection Order Bid.
- **Ch 9 Worker Placement**: Worker Placement is a specialized auction where workers are bid tokens and blocking is the allocation mechanism; Pillars of the Earth uses a Dutch Auction for placement priority.
- **Ch 11 Area Control**: Multiple-Lot Auctions (AUC-11) are mathematically similar to Area Majority (ARC-02) — nested multi-lot auctions model multiple influence regions.
- **Ch 13 Card Mechanisms**: Trick-taking (CAR-01) is like a Once-Around Auction with multiple currencies; Hearts is a Reverse-Auction variant of trick-taking.
- **UNC-01 Yomi**: Sealed Bid with Cancellation and Constrained Bidding increase the Yomi/read-the-opponent element.
