# Chapter 6: Uncertainty

## Core Idea
Uncertainty is central to the player experience—its source (dice, cards, opponents, memory, hidden roles) and its framing (input vs. output randomness) shape the emotional tone of a game. Designers have a broad palette of uncertainty sources and mitigation tools; managing uncertainty properly is key to the art of game design. The most commercially successful games typically have more luck than the most highly regarded hobby games, because uncertainty broadens accessibility across skill gaps.

## Frameworks Introduced
- **Betting and Bluffing (UNC-01)**: Players commit a stake to purchase a chance of winning everyone's stake, based on some random outcome. Players have partial information and may bluff (representing a stronger position) or fold (limiting losses).
  - When to use: To add Yomi, social reading, and self-balancing of random deals (trick-taking bets, combat commitment).
  - How: Combine hidden information with information transmission (betting patterns, visible components). Keep hidden information stable enough to give history to choices—constant change reduces bluffing to random guessing. Distinguish wagers (losers pay, all-pay combat) from auctions (only winner pays).

- **Push-Your-Luck (UNC-02)**: Players decide between settling for existing gains or risking them all for further rewards. Also called press-your-luck.
  - When to use: To create drama, tension, and excitement; works as a core mechanism (Can't Stop) or a layer atop another core (Ra's tile-drawing).
  - How: Give players a "bust" condition (Can't Stop: no matching die sum; Zombie Dice: 3 shotgun blasts). Rely on sunk-cost psychology and the difficulty of computing exact probabilities—games where expected values are always calculable feel stale. Vary stake levels to shift risk tolerance as the game progresses.

- **Hidden Roles (UNC-04)**: One or more players are assigned differing roles that are not publicly revealed at the start. Three sub-types: social deduction (Werewolf), traitor (Battlestar Galactica), and competing roles (Coup, Ravenous River).
  - When to use: To put uncertainty at the heart of gameplay and drive unstructured social interaction (lying, bluffing, posturing).
  - How: Usually only one team faces uncertainty (werewolves know everyone; villagers deduce). Traitor games need hidden resolution systems (face-down cards, dice behind screens) so traitors can sabotage anonymously. Modern designs remove the moderator via apps (One Night Ultimate Werewolf) or asymmetric win conditions (Dracula's Feast).

- **Unknown Information (UNC-07)**: Aspects of the game state are unknown to all players but lie within a known range.
  - When to use: To create uncertainty during a play and variety across plays; event decks and exploration tiles.
  - How: Players know the range of possibilities and often the cadence of revelation but not specifics. Pandemic's infection deck generates tension because the discard pile (now on top) is known. Encourage first-play familiarity via card manifests or pre-game deck reviews.

- **Hidden Information (UNC-08)**: Aspects of the game state are hidden from all but one or a few players—secret abilities, secret goals, enemy strength, item locations.
  - When to use: To add layers of strategy for advanced players through deduction and bluffing.
  - How: Use cards (Clue: show disproving card only to accuser), face-down tokens, player screens, or figures with info on the base. Players spend actions/resources to gain knowledge—or don't. Knowing that others watch your guesses creates meta-level bluffing.

- **Probability Management (UNC-09)**: Mechanisms that let players influence outcome probabilities without directly determining them.
  - When to use: To give players agency over randomness—especially in dice and deck-building games.
  - How: Direct modifiers (Kingsburg: +/− tokens), positional play (Backgammon), or deck tuning (Dominion: curate card composition). At high skill, card-denial (Twilight Struggle: trigger opponent's events safely) shifts deck weight over time.

- **Variable Setup (UNC-10)**: The starting game state varies from game to game through changes to shared components (map) and/or player setups (factions, resources, objectives).
  - When to use: To drive replayability—though variable setup and replayability are not identical.
  - How: Randomize the board (Catan), starting powers (Cosmic Encounter), or available card pools (Dominion: ten kingdom cards). Beware balance issues in longer games; use constraints (no more than N same-type tiles in a row) or pre-game response (Catan's snake draft for initial settlements).

## Key Concepts
- **Yomi**: The Japanese term for the ability to read and out-guess opponents; prominent in simultaneous-reveal games (1v1 fighting games, Force Commitment combat, The Mind).
- **Input Randomness**: Players see a random result before deciding—randomness is an input to decision-making; makes randomness something players respond to. Characteristic of European design school.
- **Output Randomness**: Players make a decision contingent on a random outcome they don't yet know; creates drama and tension but can feel punishing.
- **Memory (UNC-03)**: Hidden, trackable information (HTI) whose tracking gives an advantage; spectrum from pure memory tests (Memory) to strategic HTI (Small World's hidden VP totals, El Grande's Castillo). HTI sharply reduces accessibility.
- **Roles with Asymmetric Information (UNC-05)**: Players have different win conditions and different starting information; the "werewolf" may know identities but lack a secret that "villagers" share (Spyfall: spy doesn't know the location).
- **Communication Limits (UNC-06)**: Restrictions on what or how players may communicate; common in cooperative games (Hanabi: limited clues, The Mind: no communication). Party games use non-verbal limits (Charades, Pictionary).
- **Hidden Control (UNC-11)**: Players have hidden influence on locations or characters, revealed to perform actions (Kremlin: secret influence logs, Mythology: secret control-point assignment); uncommon due to tracking burden and fragility to deception.
- **Sunk-Cost Fallacy**: The emotional driver of Push-Your-Luck—players invest more based on past investment rather than expected return, which designers can leverage.
- **Performative Uncertainty**: Uncertainty from a player's own dexterity or physical skill (flicking, stacking), distinct from chance-based randomness.

## Mental Models
- Use **Input Randomness** when you want players to feel agency; use **Output Randomness** when you want drama and tension around a committed decision.
- Think of **Push-Your-Luck** as relying on two levers: sunk-cost attachment and uncalculable odds—if expected value is always computable, the tension evaporates.
- Use **Hidden Roles** when uncertainty should be social and conversational; use **Unknown Information** when it should be systemic and re-playable.
- Treat **Variable Setup** as the last page of the rules—Dominion's ten kingdom cards define the game as much as the base rules.

## Anti-patterns
- **Constantly changing hidden information**: Reduces bluffing to random guessing—players need stable info to build a history of choices to read.
- **Push-Your-Luck with always-calculable expected values**: Feels stale; obfuscate the odds or add sunk-cost emotional pressure.
- **Memory/HTI without aids in competitive settings**: Sharply reduces accessibility and inclusion; provide tracking components (Clue's pad) or design around it.
- **Social deduction without structure**: Unstructured discussion drags; add mechanisms with in-game consequences (Salem 1692's action cards, Shadow Hunters' yes/no cards).
- **Randomized setups creating balance issues**: Especially damaging in longer games; add constraints or pre-game response (Catan's snake draft).
- **Hidden end-game bonuses with a large ratio to in-game points**: Makes standing hard to judge; offer an intermediate scoring step (Concordia).

## Reference Tables

### Sources of Uncertainty
| Mechanism                          | Source                | Agency         | Examples                       |
|------------------------------------|-----------------------|----------------|--------------------------------|
| Betting and Bluffing (UNC-01)      | Opponent + chance     | High (Yomi)    | Poker, Coup, Kemet             |
| Push-Your-Luck (UNC-02)            | Draws/rolls           | Stop/go        | Can't Stop, Ra, Incan Gold     |
| Memory (UNC-03)                    | Trackable hidden info | Skilled        | Small World, El Grande         |
| Hidden Roles (UNC-04)              | Player identity       | Social         | Werewolf, Battlestar Galactica |
| Roles w/ Asymmetric Info (UNC-05)  | Differential knowledge | Social        | Spyfall, Hanabi                |
| Communication Limits (UNC-06)      | Restricted signaling  | Indirect        | The Mind, Mysterium            |
| Unknown Information (UNC-07)      | Known range           | Adaptive        | Pandemic, Carcassonne          |
| Hidden Information (UNC-08)        | Secret to some        | Deductive       | Clue, Love Letter              |
| Probability Management (UNC-09)   | Influenceable odds    | High            | Dominion, Backgammon           |
| Variable Setup (UNC-10)            | Initial state         | Setup-phase     | Catan, Cosmic Encounter        |
| Hidden Control (UNC-11)            | Secret influence      | Reveal-timing   | Kremlin, Mythology             |

### Input vs. Output Randomness
- **Input**: Randomness before the decision → players respond to a situation (agency). European design school. Example: tile laid before placement choice.
- **Output**: Randomness after commitment → drama and tension around an unknown result. American/wargame style. Example: dice rolled to resolve an attack.

## Worked Example
**Push-Your-Luck in Can't Stop (UNC-02):** The active player rolls four dice, pairs them into two sums, and advances pawns on tracks numbered 2–12. At any point they may stop and lock in progress, or reroll. If a reroll produces no sum matching any of the three active tracks, the player busts and loses all turn progress. Two levers make this work: (1) **sunk-cost fallacy**—the further a player advances, the more emotionally invested they become, biasing toward rerolling even when odds are poor; (2) **probability obfuscation**—calculating the bust probability of matching at least one of three numbers on 4d6 is beyond most players' mental math, unlike 2d6 distributions that Backgammon/Catan players know cold. Risk tolerance escalates: when an opponent nears closing a track or winning three tracks, competitors become aggressive.

## Key Takeaways
1. The source of uncertainty matters more than its amount: dice feel chaotic; simultaneous selection feels like agency even when mathematically equivalent.
2. More luck broadens accessibility—commercially successful games typically have more uncertainty than highly regarded hobby games.
3. Give players tools to mitigate uncertainty (rerolls, deck-tuning, probability management) to add agency without removing tension.
4. Push-Your-Luck depends on sunk-cost psychology and uncalculable odds; if expected value is always computable, the mechanism falls flat.
5. Memory/HTI reduces accessibility; provide tracking aids or design around it for broader audiences.
6. Variable setup is not the same as replayability—ensure randomized setups don't create balance issues, especially in longer games.

## Connects To
- **Ch 4 Resolution**: Output randomness is the engine of most resolution mechanisms; Yomi (UNC-01) drives Force Commitment (RES-14) and Card Play (RES-06).
- **Ch 5 Victory**: Hidden VPs (VIC-05) are a form of Hidden Information (UNC-08); hidden end-game goals leverage uncertainty to prevent leader-tracking.
- **European vs. American design schools**: The input/output randomness distinction aligns with the European (public info, input randomness) vs. American (hidden info, output randomness) divide.
