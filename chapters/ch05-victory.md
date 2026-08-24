# Chapter 5: Game End and Victory

## Core Idea
Games are defined by having a goal and a defined end point. This chapter covers how winners are determined (Victory Points in many flavors, Race, elimination, positional control) and when games end (fixed rounds, resource exhaustion, target completion, elapsed time, sudden death). The choice of victory and end-game mechanisms shapes the entire player experience—from strategic depth to pacing to kingmaking dynamics.

## Frameworks Introduced
- **Victory Points from Game State (VIC-01)**: An event causes the game state to be evaluated against a scoring condition; players earn points based on how well the state matches it.
  - When to use: When board position or market state should drive scoring (Area Majority, economic games).
  - How: Choose a scoring trigger—Scheduled (fixed intervals, best for strategic planning), Player Action (player-controlled timing, best for tactical play), or Random (cards shuffled into deck, best for tension). Beware edge effects: players who know exactly when scoring occurs over-optimize the final actions, lengthening the game.

- **End-Game Bonuses (VIC-06)**: Players earn bonus VPs at the end of the game from personal or public goals.
  - When to use: To give players strategic direction early, especially new players who need a roadmap.
  - How: Assign goals early (random or drafted); hidden personal goals add deduction and prevent leader-tracking; consider the ratio of in-game to end-game points—too many hidden bonuses makes standing hard to judge.

- **Race (VIC-07)**: The winner is the first to reach the end of a track or a target quantity.
  - When to use: For intuitive, visual goal clarity; the oldest victory mechanism (Senet, Backgammon).
  - How: Any VP-threshold game (Catan: 10 pts) is mechanically a Race. Note: games about betting on a race (Royal Turf, Downforce) are actually VP from Game State, not true Races.

- **Exhausting Resources (VIC-10)**: The game end is triggered by a resource being exhausted; players can affect game length by how they use resources.
  - When to use: To balance driving toward conclusion with player-controlled pacing.
  - How: Use a shared pool (bank money in 18xx, VP token pool in Race for the Galaxy) or an individual pool (Ticket to Ride: one player at 0–2 trains). Also common as a cooperative loss condition (Pandemic: disease cubes run out).

- **Circuit Breaker/Sudden Death (VIC-15)**: A fixed victory condition plus a special variable condition that ends the game prematurely.
  - When to use: To end lopsided games early (Circuit Breaker) or to open alternate strategic paths to victory (Sudden Death).
  - How: Set an immediate-win threshold (Twilight Struggle: 20 VPs on the track) or a special condition card (Space Base: "You Win" card). Most cooperative loss conditions are Sudden Death. Risk: Hail Mary conditions can cheapen the main game if too easy.

- **Catch the Leader (VIC-18)**: The game systems advantage players behind or disadvantage players ahead.
  - When to use: To keep games competitive and prevent runaway leaders—especially in games where the victory currency also fuels growth (economic games are highly susceptible to snowballs).
  - How: Implement overtly (Power Grid: last place gets best turn order; Age of Steam: lose VPs proportional to total) or subtly (King of the Hill exposes the leader to attack). Beware: too-strong catch-up encourages sandbagging; splitting the victory currency from the working currency (buy antiques with cash for VPs) alleviates snowballs.

- **Tug of War (VIC-19)**: A marker moves up and back on a track toward or away from a neutral position.
  - When to use: For clean, visual scoring that doubles as an end-game trigger, especially in 2-player games.
  - How: Each player owns one end; actions move the marker toward their end. Reaching the end triggers victory (Sudden Death) or scoring. Extends to 3+ players with branching tracks (Churchill). Reduces tension vs. Completing Targets because as one player nears victory, the other is far away.

- **Highest Lowest (VIC-20)**: Each player's score equals the lowest value across several categories; the highest such lowest value wins.
  - When to use: To force players to generalize across multiple paths rather than specialize.
  - How: Track each category (Tigris & Euphrates: four cube colors); final score = lowest category. Ingenious adds tension by rewarding high single-category values during play, creating a balance-vs-specialize tension.

## Key Concepts
- **Victory Points from Player Actions (VIC-02)**: Points earned from discrete actions (Go: capturing stones); can create a "pivot" where players must transition from building an engine to cashing it in (Dominion, Splendor).
- **Temporary and Permanent Victory Points (VIC-03)**: Permanent VPs drive the game to conclusion; temporary VPs (from board state) allow sudden grabs for victory and leader-pulling; a mix is ideal (Kemet).
- **Victory Points as a Resource (VIC-04)**: VPs spendable as currency (economic games, Small World's draft-skip cost); players are more cautious spending VPs when not themed as money.
- **Hidden and Exposed Victory Points (VIC-05)**: Hidden VPs alleviate last-turn over-analysis; exposed VPs with fixed turns create edge-effect distortions. Vinci → Small World's key change was hiding scores.
- **Player Elimination (VIC-08)**: The winner is the only player remaining; generally an anti-pattern except in short/light games or thematically consonant designs (Nuclear War's Final Retaliation).
- **Fixed Number of Rounds (VIC-09)**: Game ends after set rounds; prefer natural tracking (depleting card stacks) over a round marker to reduce rules burden.
- **Completing Targets (VIC-11)**: Game ends after a set number of goals are completed (Pandemic: cure all diseases); can trigger over-analysis if the completer doesn't necessarily win.
- **Fixed Number of Events (VIC-12)**: Game ends after an event occurs N times; special trigger cards shuffled into a deck. Use deck-splitting (The Expanse: three piles, two scoring cards each) to avoid clustering.
- **King of the Hill (VIC-17)**: Points earned by occupying a special board position; forces conflict, prevents turtling, and naturally creates catch-the-leader dynamics.
- **Finale (VIC-16)**: A special mini-game determines the victor after the main game ends; rewards efficiency but can cheapen the main game's meaning—best for lighter games.
- **Connections (VIC-14)**: Game ends when a specified number of board connections are made; can be both end-game trigger and victory measure (Twixt, TransAmerica). Disallowing crossing paths leads to static, optimal play; allow crossing via penalty or special tiles.
- **Elapsed Real Time (VIC-13)**: Game ends after set actual time elapses; players know exactly how long it will take. Watch for stalling—use "everyone loses" conditions, simultaneous play, or co-op structure (Space Alert, Escape).

## Mental Models
- Think of any VP-threshold game as a **Race** in disguise—Catan's "10 points" is a race to 10.
- Use **End-Game Bonuses** as a roadmap for new players: personal goals tell them what to pursue from turn one.
- Use **Catch the Leader** subtly when overt mechanisms would feel punishing; a King of the Hill position naturally exposes the leader to attack.
- Think of **Highest Lowest** as the anti-specialization mechanism—it forces breadth and typically drives player interaction since everyone competes in the same areas.

## Anti-patterns
- **All-temporary VPs with a threshold end**: Encourages perpetual leader-bashing and lengthens the game indefinitely (Munchkin, Dune); mix in permanent VPs.
- **Exposed VPs with fixed turns and deterministic scoring**: The final turn becomes an over-optimized calculation exercise (Vinci's unsatisfying last turn); hide scores or add randomness.
- **Random end-game elimination**: Players feel they lost to luck, not mistakes (Hunger Games: District 12); prefer deterministic end-game elimination (High Society: least money cannot win).
- **Snowball without catch-up**: When the victory currency also fuels growth (Monopoly: cash), the rich get richer; split victory currency from working currency.
- **Finale in serious games**: A dominant main-game player losing the finale cheapens the first part; reserve for quick, light games.

## Reference Tables

### Scoring Trigger Categories (VIC-01)
| Trigger Type   | Characteristics                                  | Best For                          | Risk                                   |
|----------------|--------------------------------------------------|-----------------------------------|----------------------------------------|
| Scheduled      | Fixed intervals; players know timing            | Long-term strategic planning      | Edge-effect over-analysis on final turn |
| Player Action  | Player-controlled timing within a band          | Tactical play; hidden scoring     | Other players free-ride on the trigger  |
| Random         | Scoring cards/tokens mixed into a deck          | Tension; variety                 | Can reward being ahead by luck          |

### End-Game Trigger Comparison
| Mechanism                  | Player Pacing Control | Tension | Example              |
|----------------------------|-----------------------|---------|----------------------|
| Fixed Number of Rounds (VIC-09) | None              | Low     | Castles of Burgundy  |
| Exhausting Resources (VIC-10)   | High              | Medium  | 18xx, Ticket to Ride |
| Completing Targets (VIC-11)     | High              | High    | Pandemic, War of Ring|
| Fixed Number of Events (VIC-12) | Low               | High    | Airlines, High Society|
| Elapsed Real Time (VIC-13)     | None              | High    | Space Alert, Escape  |
| Circuit Breaker/Sudden Death (VIC-15) | Low          | High    | Twilight Struggle     |

## Worked Example
**Hidden VP redesign: Vinci to Small World (VIC-05).** Vinci had players control rising-and-falling civilizations across Europe. Scores were open, the turn count was fixed, and end-of-turn scoring was deterministic. Reviewers found the final turn deeply unsatisfying—players could calculate exactly how to maximize their score and spent excessive time squeezing out one more point. Years later, the game was reworked as Small World. The main structural change was making scores **hidden** (players announce per-turn gains but not running totals) and adding a minor random element. These changes alone alleviated the last-turn optimization problem and gave the game a much lighter feel, turning it into an evergreen staple. The lesson: when fixed-turn, exposed-VP games produce analysis paralysis at the end, hiding scores is a high-leverage fix.

## Key Takeaways
1. Any victory system can be expressed as Victory Points, but designers should seek formulations that match the theme (money in economic games, territory in war games).
2. Mix temporary and permanent VPs: permanent drives conclusion, temporary enables dramatic late grabs and leader-pulling.
3. Hide scores when the end is fixed and known to prevent last-turn over-analysis; expose them when the end is variable.
4. Give players some control over game length (Exhausting Resources, Completing Targets) to balance pacing with tension.
5. Watch for snowballs in economic games where the victory currency fuels growth—split the two or add catch-up.
6. End-game bonuses serve as onboarding: personal goals tell new players what to do from turn one.
7. Tie-breakers for final victory should reward the harder route (going last, using fewer resources) rather than breaking randomly.

## Connects To
- **Ch 4 Resolution**: Battle resolution (RES-01 through RES-22) feeds VPs from Player Actions (VIC-02) and Race progress (VIC-07).
- **Ch 6 Uncertainty**: Hidden VPs are a form of Hidden Information (UNC-08); Variable Setup (UNC-10) affects end-game bonus assignment.
- **Ch 7 Economics**: Victory Points as a Resource (VIC-04) is the core of economic games where money is both the working currency and the victory currency.
