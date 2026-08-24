# Chapter 4: Resolution

## Core Idea
Resolution mechanisms determine the outcome of actions with uncertain results—especially conflicts—ranging from purely deterministic comparison to heavily random dice resolution. Each mechanism trades off player agency, tension, cognitive load, and thematic fidelity differently.

## Frameworks Introduced
- **High Number (RES-01)**: Each side has a numeric strength; higher wins.
  - When to use: Simple, fast conflict resolution; the baseline for combat.
  - How: Total each side's strength (fixed piece values, board position, or random sources), apply modifiers, compare. Ties typically go to the defender. Ordered High Number (Risk) pairs dice highest-to-highest for lower variance.

- **Stat Check (RES-02)**: Generate a random number and compare to a target; meet or exceed to succeed.
  - When to use: RPG-style task resolution; combat where unit quality matters more than quantity.
  - How: Assign each unit a target number; roll dice; each die meeting the target is a hit. Keep one target number constant and vary die type (d6/d8/d10) for easier cognition (Fortress America). Can be combined with High Number (Infinity: roll under your stat but higher than opponent).

- **Ratio/Combat Results Table (RES-04)**: Index the attacker-to-defender strength ratio into a table column, then roll a die to read the result.
  - When to use: Wargames needing fine-grained control over outcome distributions.
  - How: Compute strength ratio (rounded toward defender), find the column, roll, read result (elimination/damage/retreat). Modifiers can shift the column or the die roll. Differentials (attacker minus defender) are simpler but less realistic.

- **Rock, Paper, Scissors (RES-07)**: Three cyclically superior options (A beats B, B beats C, C beats A).
  - When to use: When you want intransitive relationships that prevent any single dominant strategy.
  - How: Players secretly select one of three options, reveal, and compare. Can be implemented as direct selection, modifiers to a High Number system, varying dice counts, or unit-type matchups (infantry/cavalry/artillery). Intransitive dice (A>B, B>C, C>A, ~55-45) extend this over many rolls.

- **Prisoner's Dilemma (RES-08)**: Each player chooses Cooperate or Defect; mutual cooperation maximizes total payoff, but unilateral defection yields the highest individual payoff.
  - When to use: To inject trust, betrayal, and Yomi dynamics—especially in multi-player games.
  - How: Both players secretly choose, reveal, consult a payoff matrix. Requires 3+ players (or nested sub-dilemmas) to function; with only two players, Defect always dominates.

- **Force Commitment (RES-14)**: Players secretly allocate forces to battle categories, reveal, and resolve.
  - When to use: When you want simultaneous, guessing-driven combat with multiple objectives per battle.
  - How: Players assign forces to categories (in-battle, casualties, prisoners, etc.), reveal simultaneously, resolve each category by High Number. Secret assignment emphasizes Yomi; sequential (attacker then defender) removes luck but may advantage the last placer.

- **Tie-Breakers (RES-18)**: When a resolution ties, use an alternate method to break it.
  - When to use: Whenever ties are possible in any resolution, auction, or victory check.
  - How: Choose among Resource (most/least of a resource), Positional (turn order or track position), Random (roll-off), or Secondary Values (unique sub-numbers on components). Friendly ties give all tied players the full benefit; unfriendly ties give reduced or no benefit.

- **Dice Selection (RES-19)**: Roll multiple dice and select one based on a rule (highest, lowest, or median).
  - When to use: To skew single-die distributions toward high or low without modifiers.
  - How: Roll 2 take highest ("advantage"), 2 take lowest ("disadvantage"), or 3 take median. High selection nearly doubles the chance of a 6; median selection halves extreme results.

## Key Concepts
- **Output Randomness**: Uncertainty introduced after a player commits to an action (e.g., rolling to resolve an attack), creating drama; contrasted with input randomness where the random result informs the decision before commitment.
- **Critical Hits and Failures (RES-03)**: Extreme die faces generate bonus success or catastrophic failure; lengthens the distribution tail and adds jackpot excitement. Exploding dice (6 = double success + reroll) can theoretically produce unbounded hits.
- **Die Icons (RES-05)**: Custom die faces with symbols instead of numbers; counting matching icons is cognitively simpler than comparing numbers, especially when the target icon matches the unit type being attacked (Memoir '44).
- **Card Play (RES-06)**: Players play cards to modify base conflict outcomes; enables tactical counter-play (Kemet's strength/shield/damage values) and Yomi through card-exhaustion tracking.
- **Static Capture (RES-11)**: Pieces are captured when another occupies or passes their space—among the oldest mechanisms (Chess, Checkers, Backgammon).
- **Enclosure (RES-12)**: Capture by surrounding pieces or key areas (Go, Reversi); corner/edge spaces become more valuable because they are harder to enclose.
- **Voting (RES-15)**: Players vote on whether a proposed action occurs; an Area Majority variant with Yay/Nay coalitions that encourages negotiation (can be time-consuming).
- **Player Judge (RES-16)**: One player subjectively selects the winner of a task; best with anonymous submissions to avoid meta-gaming against the leader.
- **Targeted Clues (RES-17)**: The clue-giver scores best when some but not all players guess correctly—rewarding ambiguity calibration (Dixit, Decrypto).
- **Yomi**: The ability to read and out-guess opponents; central to simultaneous-reveal resolution systems like Force Commitment and Card Play.

Additional mechanisms in this chapter: **Minimap (RES-13)** (conflicts move to a separate battle board for tactical resolution—Titan, Bismarck); **Action Speed (RES-20)** (actions have initiative ratings; faster actions execute first in simultaneous systems—Libertalia); **Rerolling and Locking (RES-21)** (dice may be rerolled or locked; rerolling averages ~+0.75 but can worsen the result—Yahtzee, Zombie Dice); **Kill Steal (RES-22)** (only the player completing a task gets the reward regardless of prior contributions—Cutthroat Caverns).

## Mental Models
- Use **Stat Check** when unit quality should matter and you can hold one target number constant across die types; use **High Number** when force quantity should dominate.
- Think of **Rock, Paper, Scissors** as the antidote to transitive strength ladders—it guarantees no single unit type is always best.
- Use **Force Commitment** when a battle should be about guessing your opponent's intent, not just comparing army sizes.
- Treat **Tie-Breakers** as a design surface, not an afterthought: positional tie-breakers reward turn-order play; resource tie-breakers reward economy; random tie-breakers add excitement but feel unsatisfying for final victory.

## Anti-patterns
- **Long modifier stacks**: Stacking many +/− modifiers from multiple sources burdens cognition; prefer intrinsic strengths, card play, or dice pools that model desired probabilities directly.
- **Winner Takes All in realistic settings**: A 10-strength fleet eliminating a 1-strength fleet at no cost strains theme and immersion.
- **Sophisticated card-based combat at high player counts**: Multi-round card resolution (We the People, Starcraft) slows play dramatically beyond two players.
- **Random final-victory tie-breakers**: Breaking an end-game tie randomly is unsatisfying; prefer tie-breakers that reward a harder route to victory (going last, using fewer resources).

## Reference Tables

### Dice Selection Probabilities (RES-19)
| Result | 1 Die (%) | 2 Dice, High (%) | 2 Dice, Low (%) | 3 Dice, Median (%) |
|--------|----------|-------------------|------------------|---------------------|
| 1      | 16       | 3                 | 31               | 7                   |
| 2      | 16       | 8                 | 8                | 19                  |
| 3      | 16       | 14                | 19               | 24                  |
| 4      | 16       | 19                | 14               | 24                  |
| 5      | 16       | 25                | 8                | 19                  |
| 6      | 16       | 31                | 3                | 7                   |

### Tie-Breaker Categories (RES-18)
| Category       | Method                                      | Example                                              |
|----------------|---------------------------------------------|------------------------------------------------------|
| Resource       | Most or least of a particular resource      | Trade on the Tigris: fewest Barbarian tokens         |
| Positional     | Turn-order or track position                | Rising Sun: higher on Honor track wins ties         |
| Random         | Roll-off or randomizer                      | Risk: ties go to the defender                        |
| Secondary Values | Unique sub-number on a component          | Libertalia: unique Flag number on each card          |
| Friendly       | All tied players gain the full benefit      | Leader scores 10 pts; all tied leaders score 10     |
| Unfriendly     | Tied players get reduced or no award       | No tied player scores                                |

## Worked Example
**Prisoner's Dilemma in Diplomacy (RES-08):** Austria and Italy begin adjacent, with Venice and Trieste touching—the only such starting pair among seven players. After negotiation, both write secret orders simultaneously. If both **Cooperate** (move away from the border), each gets a reasonable start and preserves trust. If both **Defect** (invade), neither loses a home center but both fall behind the other five players and distrust festers. If one Cooperates and the other Defects, the defector captures a home center—a devastating blow. With only two players, Defect would always dominate (neither gains ground if both pick the same option). But because five other players exist, the long-term cost of broken trust makes Cooperation viable, turning a pure PD into a repeated-game trust problem with emotional weight.

## Key Takeaways
1. Match the resolution mechanism to the desired feel: deterministic (Alternate Removal, RES-09) for strategy, random (Stat Check, RES-02) for tension, simultaneous (Force Commitment, RES-14) for Yomi.
2. Prefer intrinsic strengths and dice pools over long modifier lists to reduce cognitive load.
3. Use intransitive (RPS) relationships to prevent any single dominant unit type or strategy.
4. Dice Selection (advantage/disadvantage) shifts distributions significantly without rules overhead—use it to skew outcomes toward or away from extremes.
5. Tie-breakers shape behavior near boundaries: choose deliberately based on what your game should reward.
6. Physical Action (RES-10) resolution adds performative uncertainty but risks alienating players who lack dexterity skills.

## Connects To
- **Ch 6 Uncertainty**: Output randomness is the core of most resolution mechanisms; Yomi (UNC-01) drives simultaneous-reveal systems like Force Commitment and Card Play.
- **Ch 3 Actions**: Resolution determines the outcome of Actions chosen via the mechanisms in Chapter 3.
- **Ch 5 Victory**: Resolution feeds directly into victory—battle wins often yield Victory Points (VIC-02) or enable Race (VIC-07) progress.
