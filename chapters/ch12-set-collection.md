# Chapter 12: Set Collection

## Core Idea
Set collection leverages the human love of patterns: the value or power of a set is greater than the sum of its parts, and this non-linear valuation causes players to diverge in what they value, producing indirect, non-zero-sum conflict.

## Frameworks Introduced
- **Set Valuation (SET-01)**: The logic or mathematical model by which designers assign values to sets of elements.
  - When to use: Any time sets are scored, spent, or converted to rewards.
  - How: Choose a valuation curve shape (linear, triangular, squaring, terminating, non-monotonic). Decide whether singletons have base value, whether sets have a max size, and whether sets terminate on completion.
- **Tile-Laying (SET-02)**: Set-collection mechanisms with spatial elements, where adjacency and placement rules define or modify set validity.
  - When to use: When spatial relationships should constrain or buff set value.
  - How: Require matching edges/colors/shapes for valid placement (Kingdomino, Latice); score sets based on adjacency, region completion, or global presence regardless of position.
- **Grid Coverage (SET-03)**: Players cover a grid or fill a space using a variety of shapes.
  - When to use: When tessellating shapes into a defined space is the core puzzle.
  - How: Players acquire differently-shaped tiles and place them on their grid. Value comes from coverage efficiency, special icons under tiles, and declining rewards for later completion.
- **Network Building (SET-04)**: A specialized set collection where the collected elements are ties between nodes, often routes between destinations.
  - When to use: When the "set" is a connected graph and its value comes from reaching specific nodes or super-sets of routes.
  - How: Players build connections via Point-to-Point (drawn lines), Tile Placement (edges must match), or Existing Network (claim pre-printed routes). Routes can be exclusive or reusable as sub-sets of larger sets.
- **Combo Abilities (SET-05)**: A collection of abilities acquired separately that synergize together as game verbs (actions) and adverbs (buffs).
  - When to use: When you want emergent gameplay from modular, black-box abilities players assemble themselves.
  - How: Use direct, non-contingent actions; a few resource types; multiple domains where elements can exist (deck, hand, in play); open turn structures. Combos emerge rather than being declared.

## Key Concepts
- **Synergy**: The defining property of sets — value exceeds the sum of parts; this is what makes non-linear valuation possible.
- **Triangular Numbers**: The sequence 1, 3, 6, 10, 15, 21... (each term = previous + n). Near-mantra status among designers because it escalates rewards without over-incentivizing specialization. The marginal value of the nth card is exactly n.
- **Squaring (n²)**: A sharply accelerating curve (1, 4, 9, 16...) useful for small sets or push-your-luck/shoot-the-moon dynamics.
- **Terminating Sets**: Sets with a fixed required size after which no more elements fit (Catan: 1 wood + 1 clay = 1 road).
- **Escalating Sets**: Sets with minimum and maximum valid size, with payouts varying by size; capped sets incentivize diversification.
- **Orthogonal Sets**: A second set dimension that counterbalances a primary one (7 Wonders: monotype science scored n², but one-of-each-type scored 10, beating three of a kind until n=4).
- **Super-set / Set of Sets**: A set whose elements are themselves sets (Ticket to Ride tickets satisfied by any route combination connecting two cities).
- **Set Element Exclusivity**: Whether an element can belong to only one set (SET the game) or be reused across multiple sets (route-building networks).
- **Global Presence Mechanism**: Sets that score regardless of spatial relationships (Suburbia, Alhambra same-color tiles).
- **Enclosing Set**: A set that scores based on enclosing and completing a shape (Rome: City of Marble hexagons).
- **Drafting Verbs vs Nouns vs Adjectives**: Pool-building distinction — deck builders draft verbs (actions, Dominion); Orléans drafts nouns (workers triggering actions); Assault of the Giants drafts adjectives (modifiers on existing cards).
- **Push-Your-Luck in Sets**: Holding cards to grow a set vs cashing in now, knowing unused cards may count against you (Rummy, Ticket to Ride's wasting assets).

## Mental Models
- Use **triangular numbers** as the default escalating curve; it is the most balanced way to reward larger sets without breaking the game.
- Think of set collection as the engine that makes conflict **non-zero-sum** — players value the same components differently, so they can all win by specializing.
- Use **orthogonal sets** (a second scoring dimension) to counterbalance a sharply accelerating primary set and keep specialization vs diversification in tension.
- Think of **Network Building** as a telescoping set of sets — a ticket is a super-set satisfied by many possible route sub-sets.
- Use **Combo Abilities** when you want discovery rather than declaration — Magic: The Gathering's combos are engaging precisely because the designers did not pre-declare them as sets.

## Anti-patterns
- **Pure linear valuation**: Sets worth exactly the sum of their parts remove the synergy that makes set collection interesting; always curve the value.
- **Uncapped squaring on large sets**: n² grows explosively; reserve for small sets or shoot-the-moon strategies, or it will dominate all other scoring.
- **Forgetting the non-monotonic option**: A declining-then-rising curve (Cacao: -10, -4, -1, 0, 2, 4, 7, 11, 16) forces players to either commit lightly or fully, eliminating middling play and adding texture.
- **Pre-declaring all combos**: If you explicitly label every synergistic combination as a "set," you steal the joy of discovery from players; leave some emergent.
- **Requiring strict element exclusivity in networks**: Route-building games usually allow routes to be reused as sub-sets; forcing exclusivity breaks the super-set concept.

## Reference Tables
### Set Valuation Curve Shapes
| Curve | Sequence example | Effect | Example |
|-------|-------------------|--------|---------|
| Linear | 1, 2, 3, 4... | Boring; removes synergy | Avoid as primary |
| Triangular | 1, 3, 6, 10, 15, 21 | Balanced escalation; marginal value of nth = n | Default choice |
| Squaring | 1, 4, 9, 16, 25 | Sharp acceleration; for small sets or shoot-the-moon | 7 Wonders monotype science |
| Terminating | Fixed size, then closed | Incentivizes diversification | Catan (wood+clay=road) |
| Capped/escalating | Min-max size with payout curve | Larger = better, but diminishing returns | Ethnos (6+ all score same) |
| Non-monotonic | -10, -4, -1, 0, 2, 4, 7, 11, 16 | Penalizes middling commitment | Cacao water track |
| Singleton base | Cards worth something alone, more in set | Less punishing | Sushi Go! nigiri + wasabi |
| Worthless singletons | 0 alone, value only in completed set | Pure push-your-luck | Ticket to Ride, Rummy |

### Network Building Approaches
| Method | How connections form | Ownership | Example |
|--------|---------------------|-----------|---------|
| Point-to-Point | Players draw/connect adjacent dots | Owned or neutral | Empire Builder, Transamerica |
| Tile Placement | Place square/hex tiles; edges must match | Owned | 1830, Age of Steam, Tsuro |
| Existing Network | Pre-printed routes claimed/activated | Claimed | Ticket to Ride, Power Grid, Brass |

## Worked Example
**7 Wonders — Science Scoring with Orthogonal Sets.** Three science card types exist: Tablets (T), Compasses (C), Gears (G).
- **Primary (monotype) set**: Cards of the same type score n² (number of matching cards squared).
- **Orthogonal (diversity) set**: One of each type scores 1 point per card + a 7-point set bonus.

Comparing three-card holdings:
- **3 Compasses**: 3² = 9 points (monotype).
- **1 Tablet + 1 Compass + 1 Gear**: 1+1+1 + 7 bonus = 10 points (diversity).

The diversity set actually outscores the monotype set at size 3. Only at size 4 does monotype pull ahead: 4² = 16 vs a 3-diversity + 1 extra = 13. Players leaning into science must decide whether to specialize (high ceiling) or diversify (efficient floor), and the tension is shaped entirely by the choice of curve and its orthogonal counterbalance.

## Key Takeaways
1. Sets are worth more than the sum of their parts; this non-linear valuation is what makes set collection engaging.
2. Triangular numbers (1, 3, 6, 10, 15...) are the designer's default escalating curve — balanced, intuitive (marginal value of nth card = n), and overwhelmingly common.
3. Use orthogonal sets to counterbalance sharply accelerating primary sets, keeping specialization and diversification in productive tension.
4. Terminating/capped sets incentivize diversification; uncapped sets incentivize specialization.
5. Non-monotonic curves (declining then rising) force all-or-nothing commitment and eliminate safe middling play.
6. Network Building is a telescoping set of sets — a ticket is a super-set satisfied by many possible route sub-sets; routes are typically reusable, not exclusive.
7. Combo Abilities are emergent sets: leave synergies undeclared to preserve the joy of discovery.

## Connects To
- **Ch 7 (Economics)**: Set valuation answers "what is a resource worth," complementing economic acquisition mechanisms.
- **Ch 8 (Auctions)**: Auctions are one method of acquiring set elements; set valuation determines what those elements are worth once acquired.
- **Ch 11 (Area Control)**: Territories-within-Regions is a spatial set collection; Area Majority scoring is itself set-like.
- **Ch 13 (Card Mechanisms)**: Melds (CAR-03) are set collection in card form; Deck Building (CAR-05) is pool building of set elements.
- **Ch 3 (Actions)**: Tile-Laying (SeT-02) overlaps with Action Placement; Combo Abilities are modular action systems.
