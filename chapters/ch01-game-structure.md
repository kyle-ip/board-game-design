# Chapter 1: Game Structure

## Core Idea
A game's basic structure—who wins, who loses, and the overall scope of the experience—must be chosen first by the designer; this chapter catalogues the major archetypes from competitive to cooperative to legacy games, and the design challenges each one raises.

## Frameworks Introduced
- **Competitive Games (STR-01)**: Two or more players, single winner.
  - When to use: Default for symmetric "fair fight" experiences.
  - How: Ensure roughly equal starting positions, or balance asymmetries via meta-structures (bidding in bridge, alliances in Diplomacy); break ties decisively because players remember endings.
- **Cooperative Games (STR-02)**: All players win or lose together against the game.
  - When to use: Gateway for new players, lower pressure, shared experience.
  - How: Use AI deck (Sentinels) or pure puzzle (Hanabi); counter the "alpha player problem" via communication limits, real-time pressure, hidden info per player, or complex personal powers.
- **Team-Based Games (STR-03)**: Teams compete (2v2, 2v2v2, One vs. All).
  - When to use: Bilateral conflicts, supporting more players, role separation.
  - How: Assign openly or secretly; asymmetric factions in One vs. All need distinct victory conditions; reserve role rotation for advanced play.
- **Solo Games (STR-04)**: Single-player mode or standalone.
  - When to use: Catering to solo market or as add-on mode.
  - How: Classify as goal-based (VP target), record-based (beat high score), or AI-based (Automa); the Automa is representational (mimics outputs) not procedural (doesn't simulate a player).
- **Semi-Cooperative Games (STR-05)**: Group wins/loses, but one player is crowned individual winner.
  - When to use: Blending co-op survival with personal ambition.
  - How: Ensure all players agree on whether group win + individual loss beats total group loss; mismatched incentives cause sabotage.
- **Single Loser Games (STR-06)**: One player loses; others survive.
  - When to use: Light/party games, stacking/dexterity.
  - How: Avoid bash-the-loser runaway; encourage lighter confrontation.
- **Traitor Games (STR-07)**: Hidden traitors inside a cooperative game.
  - When to use: Building suspense and betrayal narrative.
  - How: Add obfuscation (shuffle crisis card contributions in Dead of Winter); design post-reveal gameplay; provide reference materials because players can't ask questions without revealing loyalty.
- **Scenario/Mission/Campaign Games (STR-08)**: Variable maps, resources, win conditions assembled into narrative or standalone scenarios.
  - When to use: Extending replayability; storytelling.
  - How: Reuse core rules across maps/missions; link sessions in campaign structure.
- **Score-and-Reset Games (STR-09)**: Stop, score, reset, repeat; cumulative score determines winner.
  - When to use: Card games, dexterity, games with strong turn-order advantage.
  - How: Use cumulative scoring across rounds; partial resets possible (Amun-Re pyramids persist; Blue Lagoon huts persist).
- **Legacy Games (STR-10)**: Multi-session with permanent, irreversible changes; gated content unlocked between sessions.
  - When to use: Long-form narrative commitment, visceral permanent change.
  - How: Combine irreversible destruction (tearing cards, writing on boards) with unlocks (gated content revealed at session end, often whole new mechanisms/factions); tradeoff between novel unrepeatable experience and replayability.

## Key Concepts
- **Alpha Player Problem / Quarterbacking**: One player dominates group decisions in co-ops, ruining others' experience.
- **AI vs. Non-AI Co-op**: AI co-ops have an opponent with a behavior algorithm; non-AI co-ops present a puzzle without villain.
- **Partnership vs. Collaborative play**: Partnership = each player retains agency; collaborative = consensus decisions.
- **Automa**: Solo AI philosophy (Pedersen) that mimics multiplayer feel by representing outputs without simulating a full player—claims action spaces and blocks routes but doesn't collect resources or score VPs.
- **One vs. All**: Asymmetric structure where one player (overlord) controls many units vs. individual heroes.
- **Unlocks**: Gated legacy content revealed at session end, often introducing entirely new mechanisms (not just buffs).
- **Crossroads mechanism**: Hidden-trigger narrative choices activated by player actions.
- **Bash-the-loser**: Pattern where the falling-behind player becomes everyone's target.
- **Score-and-Reset**: Round-based structure with cumulative scoring across multiple rounds.
- **Consumable vs. resettable legacy**: Spectrum from physically altered components (Pandemic Legacy) to reorderable decks (Fabled Fruit).

## Mental Models
- Think of game structure as the chassis—pick it first; everything downstream bolts onto it.
- Use cooperative communication limits when you want to defeat the alpha-player problem by force (Magic Maze, The Mind).
- Think of legacy unlocks as game-design "patch notes" the players earn—new mechanisms arrive mid-campaign.
- Use score-and-reset when the gameplay arc is short but you want a meta-narrative across multiple rounds.

## Anti-patterns
- **Lose a Turn as a random outcome**: Removes player agency and engagement; deprecated in modern design (see TRN-16).
- **Bash-the-loser in single-loser games**: Falling-behind player becomes a target with no path to recover.
- **Mismatched incentives in semi-cooperative games**: If players disagree on whether group win + individual loss beats total group loss, sabotage and unhappiness follow.
- **Forced role rotation in team games with new players**: Disorienting; players must learn every mini-game before play begins.

## Reference Tables

### Solo Game Types
| Type | Goal | AI Behavior | Examples |
|---|---|---|---|
| Goal-based | Hit VP target in N turns | Asymmetric villain or abstract process (e.g., spreading fire) | Flash Point, Friday |
| Record-based | Beat previous high score | None or abstract | Ganz schön clever |
| AI-based | Recreate multiplayer feel | Automa (representational, not procedural) | Scythe, Anachrony, Between Two Cities |

### Co-op Anti-Alpha Techniques
| Technique | Mechanism | Examples |
|---|---|---|
| Communication limits | Rule-based info sharing constraints | Magic Maze, The Mind, Hanabi |
| Real-time pressure | Force independent decisions under time | Space Cadets, FUSE, Space Alert |
| Hidden information per player | Personal hand/deck only owner understands | Sentinels of the Multiverse, Spirit Island |
| Complex personal powers | Hard for others to evaluate your options | Mechs vs. Minions, Spirit Island |

## Worked Example
**Pedersen Automa (Scythe solo mode)** demonstrates how a representational AI mimics multiplayer feel without simulating a human brain.

- **Goal**: Make solo Scythe feel like a multiplayer game without bookkeeping an AI player's full state.
- **Principle**: AI is representational, not procedural—it produces outputs that mimic a player's effects without following the rules.
- **What the Automa does**: Claims action spaces, drafts cards, blocks routes, interferes with the human player.
- **What the Automa does NOT do**: Collect resources, build buildings, or score victory points. In Viticulture, the Automa has no vineyards—only the impression of having them.
- **Implementation**: Card-driven algorithm with randomizers for AI choices; behaves like a "Potemkin player" (shell only).
- **Result**: Human feels pressure competing for spaces and routes, without tracking AI resources or scoring.

## Key Takeaways
1. Pick game structure first—it sets the design constraints for everything downstream.
2. Cooperative games need a defense against the alpha-player problem; the strongest tools are communication limits, real-time pressure, and hidden information per player.
3. In semi-cooperative games, aligned player expectations about what "winning" means are mandatory; mismatched incentives break the game.
4. Solo AI design (Automa) favors representation over simulation—mimic outputs, don't model the full player.
5. Legacy games combine irreversible destruction with gated unlocks to create visceral narrative stakes; the tradeoff is replayability.
6. Tie-breaking matters in competitive games—design for decisive conclusions because players remember endings.
7. Scenario/campaign structures extend replayability by reusing a core system across varied setups.

## Connects To
- **Ch 2 (Turn Order)**: Team-based and One vs. All structures dictate turn-order needs; the Interleaved vs. Sequential choice (TRN-15) depends heavily on game structure.
- **Ch 3 (Actions)**: Variable Player Powers (ACT-12) is often paired with asymmetric structures (Dune, Root, Cosmic Encounter).
- **Ch 6 (Uncertainty)**: Hidden Roles (UNC-04) overlap heavily with Traitor Games; semi-coop incentives tie to Prisoner's Dilemma (ReS-08).
- **RPG design**: Semi-co-op and Narrative Choice mechanisms borrow directly from RPG character motivations and choice trees.
