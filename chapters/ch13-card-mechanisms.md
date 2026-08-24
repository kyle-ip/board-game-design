# Chapter 13: Card Mechanisms

## Core Idea
Cards are flexible game elements that function as portable rulebook additions — each card carries a small payload of additional rules — and the major card mechanisms (trick-taking, climbing, melding, drawing, deck building, drafting) span a millennium of design from classic suits to modern engines.

## Frameworks Introduced
- **Trick Taking (CAR-01)**: Players play cards from their hand to the table in a series of rounds ("tricks") each evaluated separately to determine a winner and apply effects.
  - When to use: When you want card-by-card comparison tied to a contract or bid.
  - How: Deal cards (often the whole deck); players in turn play one card, typically following the lead suit if able. Highest card of the lead suit wins, unless a trump suit outranks. Winner leads next trick. Score by tricks won vs a bid.
- **Ladder Climbing (CAR-02)**: Players play one card or a set of related cards; subsequent plays must be an equal-or-higher value of the same set; the last to successfully play wins the right to start a new round.
  - When to use: When you want shedding + set-comparison hybrid popular in East Asian card traditions.
  - How: Lead with a single, pair, triple, quad, or run. Followers must match the set shape and equal-or-exceed rank. Bombs (unbeatable combinations) can override any preceding set. Going out is the goal or scores points.
- **Melding and Splaying (CAR-03)**: A meld is a set of cards in a specific relationship that allows them to be played or scored; splaying is how overlapping cards reveal or conceal abilities.
  - When to use: For Rummy-style sets/runs and for cards whose physical overlap matters (Innovation).
  - How: Assemble melds in hand (sets of identical cards, or runs of consecutive cards), then lay them on the table. Other players may "lay off" onto existing melds. Splay melds left/right/up to reveal or conceal icon rows.
- **Card Draw, Limits and Deck Exhaustion (CAR-04)**: Games limit cards held in a container (hand, deck) and trigger effects when a deck, pile, or hand becomes exhausted.
  - When to use: Whenever card economy (hand size, draw rate, discard) should shape difficulty and player power.
  - How: Set a hand limit (static or government-dependent in Through the Ages), a draw limit (Ticket to Ride: 2 cards, 1 if a wild is taken), and define deck-exhaustion triggers (reshuffle, game-end, escalating threat).
- **Deck Building (CAR-05)**: Players play cards out of individual decks, iteratively acquiring new cards to improve the deck over the course of the game.
  - When to use: When you want a self-improving engine where past acquisitions shape future draws.
  - How: Start with a thin starter deck. Each turn: play up to N action cards, spend money cards to buy from a market (static like Dominion or a refilling row like Ascension/Star Realms), draw back to hand size (usually 5). Cycle the deck as it exhausts.
- **Drafting (CAR-06)**: A means of distributing cards or other game elements to players through an ordered selection process.
  - When to use: When you want agential card distribution without the math/intimidation of auctions, and when variety of selection matters.
  - How: Choose a draft format — Rochester (all visible, take one per turn), pick-and-pass (draw N, keep 1, pass the rest), snake (invert order each round to balance), or parallel pick-and-pass (all players choose simultaneously, then pass hands).

## Key Concepts
- **Draw deck / Hand / Table / Tableau / Discard pile**: The core card-game containers; the tableau is private but visible, the discard pile has varying interaction rules.
- **Trump**: A suit that outranks the lead suit regardless of numerical value; can be fixed, bid-determined (Bridge), or single-card-and-shifting (The Bottle Imp).
- **Follow Suit**: Requirement to play a card of the lead suit if possible; the defining constraint of classic trick-taking.
- **Over-tricking**: Taking more tricks than the contract called for; may be more valuable, equal, or penalized depending on the game.
- **Bombs**: Unbeatable combinations in ladder-climbing games that can override any preceding set.
- **Pyramidal Deck**: A deck where the quantity of cards in each rank equals the rank's value (eight 8s, nine 9s...) — used in The Great Dalmuti.
- **Laying Off**: Adding cards from your hand to existing melds on the table (Rummy), usually only after playing your own meld.
- **Splaying**: The physical overlapping of cards in a meld to reveal or conceal icon rows — left, right, up, or no splay (Innovation).
- **One-in-One-Out Economy**: Symmetric, metered card flow (most trick-taking and Rummy games) where each turn adds one and removes one card.
- **Agential Card Draw**: Modern games overturn one-in-one-out; players choose when/how to draw, discard, and convert cards (Deus, Race for the Galaxy).
- **Market Row**: A refilling display of purchasable cards drawn from a randomized deck (Ascension, Star Realms), replacing Dominion's static market.
- **Pool Building**: The larger category containing deck building; pools can be chips (Puzzle Strike), workers from a bag (Orléans), or dice (Roll for the Galaxy).
- **Drafting Verbs / Nouns / Adjectives**: Deck builders draft verbs (actions per card, Dominion); Orléans drafts nouns (workers that trigger actions via set collection); Assault of the Giants drafts adjectives (modifiers attached to existing cards).
- **Chit-Pull System**: A pool-building resolution mechanism using drawn tokens/chips instead of cards.
- **Wheeling**: A drafting behavior where a player passes a desired card, betting it will return unused; emerges from drafting, not a rule.
- **Hate-Drafting**: Taking a card useless to you to deny it to an opponent; an emergent behavior in synergy-heavy drafts.
- **No-Shuffle Deck Builder**: A variant that preserves deck order (Aeon's End), removing shuffle variance.

## Mental Models
- Think of **Trick Taking** as a highly specialized auction — players bid with cards to win the trick, and the lot up for bid is composed of the bids themselves.
- Use **Drafting** instead of **Auctions** when you want quick, less-mathy distribution; the player asks "what do I want most?" rather than precisely valuing each lot.
- Think of **Deck Building** as drafting verbs — each card is an action you will re-encounter as the deck cycles; contrast with Orléans drafting nouns that must be combined into sets to trigger actions.
- Use **parallel pick-and-pass** to accelerate a draft (all choose simultaneously) at the cost of card visibility (each player sees only a fraction of the pool).
- Think of **Splaying** as a physical state machine — how cards overlap determines which icons are active, and re-splaying is a meaningful action.

## Anti-patterns
- **Dealing the whole deck without uncertainty mitigation**: Classic trick-taking with full deals rewards memory and card-counting; deal a subset (Diamonds) to lower the impact.
- **Bare pick-and-pass drafts without turn-order mitigation**: The first picker is advantaged; use snake drafts or Kingdomino-style "pick valuable = go last next round" to balance.
- **Deck builders with only one viable strategy**: If synergies are too tightly coupled, the game solves itself; include orthogonal paths and variety rewards (Dominion's Cornucopia).
- **Hand limits that make co-op games too easy**: Forbidden Island without an artifact-card hand limit is substantially easier; co-op difficulty is tightly coupled to card economy.
- **Confusing wheeling/hate-drafting with rules**: These are emergent behaviors; evaluate prototypes for them, but do not legislate them.
- **No-shuffle decks without compensating design**: Removing shuffle variance (Aeon's End) changes the strategic landscape; design for deliberate sequencing.

## Reference Tables
### Broad Card Game Categories
| Category | Goal | Examples |
|----------|------|----------|
| Trick-taking | Win tricks vs a contract/bid | Bridge, Spades, Wizard, Diamonds |
| Shedding | Get rid of cards first | Rummy family |
| Ladder climbing (hybrid) | Shed by playing equal-or-higher sets | President, Tichu, The Great Dalmuti, Haggis |
| Hand-comparison | Acquire the best hand by ranking | Poker, Blackjack |

### Drafting Formats
| Format | How it works | Tradeoff |
|--------|--------------|----------|
| Rochester | All cards visible; take one per turn in turn order | Full info but analysis paralysis; tests recall |
| Pick-and-pass | Draw N cards, keep 1, pass the rest | Tightly coupled to turn order; first picker advantaged |
| Snake | Invert draft order each round | Mitigates but does not resolve turn-order imbalance |
| Parallel pick-and-pass | All players choose simultaneously, then pass | Fast, but each player sees only a fraction of cards |
| Booster (CCG) | Draft from sealed packs of unknown contents | Extreme valuation disparity; enables wheeling/hate-drafting |

### Deck Building Market Types
| Market | How it works | Example |
|--------|--------------|---------|
| Static open | Fixed piles always available at fixed cost | Dominion |
| Refilling row | Cards drawn from a randomized deck to fill slots | Ascension, Star Realms |
| Pyramidal | Buy only base cards; higher tiers drop down as pyramid crumbles | Valley of the Kings |
| Tech-tiered | Acquire by demonstrating requisite icon counts | Eminent Domain |

## Worked Example
**Kingdomino — Drafting with Embedded Turn-Order Cost.** Each round, domino tiles (each with two terrain squares, some with crowns) are laid out in a vertical display, sorted by number — lowest-numbered (least valuable) on top, highest-numbered (most valuable) on bottom.
1. The player who picked the most valuable tile last round goes **last** this round.
2. The player who picks the least valuable tile this round goes **first** next round.
3. Players choose based on both tile value and turn-order position: a tile that fits your kingdom poorly but grants first pick next round may be worth taking.
4. Crowns on a tile make all connected same-terrain squares score 1 VP per crown in the combined region, so tile value is relative to each player's existing tableau.

The draft format encodes a self-balancing cost: power (valuable tile) is paid for with tempo (late next-round pick). No snake draft or external balancing is needed because the valuation curve of the tiles does the work, and players whose needs differ will naturally select different positions.

## Key Takeaways
1. Modern cards are portable rulebook additions — each card carries a small payload of rules, plus shared characteristics like suits, costs, and prerequisites.
2. Trick-taking, shedding, and hand-comparison are the three broad classical categories, with ladder-climbing as a shedding-plus-comparison hybrid.
3. Trick-taking is mathematically a specialized auction where the lot is composed of the bids, but experientially emphasizes hand-management over valuation.
4. Splaying exploits card physicality — how cards overlap determines which icons are active, turning layout into a game state.
5. Hand and draw limits are difficulty dials, especially in co-op games; loosening them is the easiest way to make a card game easier.
6. Deck Building is one form of pool building; distinguish drafting verbs (Dominion), nouns (Orléans), and adjectives (Assault of the Giants).
7. Drafting replaces auctions for less-mathy distribution; choose Rochester (full info), pick-and-pass (simplicity), or parallel (speed) based on desired visibility and pace.
8. Wheeling and hate-drafting are emergent behaviors, not rules — design for them by evaluating prototypes, not by legislating them.

## Connects To
- **Ch 8 (Auctions)**: Trick-taking is a specialized auction; Drafting is a quicker alternative to auctions for distributing cards.
- **Ch 9 (Worker Placement)**: Drafting is closely related to Action Drafting (ACT-02) and Worker Placement — all are ordered selection for exclusive use.
- **Ch 12 (Set Collection)**: Melds (CAR-03) are set collection in card form; Deck Building acquires set elements iteratively.
- **Ch 3 (Actions)**: Programmed Movement (MOV-10) and Action Queues (ACT-06) share DNA with deck-building turn structures.
- **Ch 6 (Uncertainty)**: Deck exhaustion and card draw are core uncertainty engines; booster drafts add unknown-pool uncertainty.
