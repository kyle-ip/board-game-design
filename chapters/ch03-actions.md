# Chapter 3: Actions

## Core Idea
Actions are the atomic steps players take to drive a game forward; the way actions are made available—fixed menu, drafting, queues, rondels, tech tracks—sets the game's complexity, interactivity, and pacing.

## Frameworks Introduced
- **Action Points (ACT-01)**: Player receives N points per turn to spend on Actions.
  - When to use: Flexible turn structure with combo potential.
  - How: Costs may be uniform 1 (Pandemic) or variable 1-4 (Tikal); multiple currencies possible (Through the Ages: Civil + Military); allow carryover or force spend.
- **Action Drafting (ACT-02)**: Players select from a shared pool, denying others.
  - When to use: Adding interaction to action selection; marketplace of actions.
  - How: Worker Placement (Ch 9), Role Selection (Puerto Rico, Citadels), Dice Pool (La Granja); watch for first-player advantage; "hate drafting" emerges.
- **Action Retrieval (ACT-03)**: Used actions spent until retrieved; retrieval itself is an action.
  - When to use: Encouraging efficiency, balanced strategies, multi-turn planning.
  - How: Retrieval restores all used cards (Assault of the Giants); can scale power based on prior plays (Move after Recruit+Attack = 3 units moved vs. 1 in isolation).
- **Action/Event (ACT-04)**: Card offers Action Points OR an Event; choosing one may let opponent trigger the other.
  - When to use: Historical simulations, integrating theme with mechanical choice.
  - How: Some events player-eligible only (We The People); Twilight Struggle—opponent triggers event if you use AP for their card—drives sequencing depth.
- **Command Cards (ACT-05)**: Hand limits which units/regions can be activated.
  - When to use: Lighter war games; reducing decision complexity.
  - How: Cards = geographic regions or unit types (Memoir '44); hand size = information horizon; reduces to Chit Draw (TRN-11) at one-unit limit.
- **Action Queue (ACT-06)**: Players pre-program sequences of actions.
  - When to use: Planning + chaos from hidden future board state; spatial reasoning needed.
  - How: Rolling Queue (Nuclear War—add to end, execute head) or Batch Queue (Robo Rally—plan N, resolve interleaved); Twin Tin Bots replaces one card per turn; longer queues increase chaos.
- **Shared Action Queue (ACT-07)**: All players add to a central queue; all execute.
  - When to use: Higher interactivity, planning for opponents as well as self.
  - How: Add to end, execute all (Impulse); Mottainai executes opponents' cards before your own; Major General allows insert anywhere in queue.
- **Follow (ACT-08)**: Other players may perform (a version of) the active player's action.
  - When to use: Engagement during others' turns; considering opponents' needs.
  - How: Active player gets bonus (Puerto Rico Builder = discount); cost to follow via discarding cards (Eminent Domain) or spending resources (Tiny Epic Galaxies); Glory to Rome/SPQF allow echo with multiple cards for stronger version.
- **Order Counters (ACT-09)**: Tokens placed face-down in regions, executed in sequence.
  - When to use: Strategic planning with hidden info; heavy strategy games.
  - How: LIFO ("chicken" feel—last in executes first) or FIFO (less cognitive load); or fixed action order ignoring stack order (A Game of Thrones).
- **Rondel (ACT-10)**: Pie wedges represent actions; moving further costs more.
  - When to use: Trade-offs between desired action and cost.
  - How: Move 1 step free, further = pay; Finca variant uses multiple tokens with action power based on token count in ending wedge (overlaps Mancala, MOV-12).
- **Action Selection Restrictions (ACT-11)**: Various novel limiting mechanisms.
  - When to use: Constraint as innovation source.
  - How: Pyramid levels (Kemet), grid adjacency (Goa), rotating wheels (Noria, Tzolk'in), house selection (Keyforge), dual-action cards (Warpgate).
- **Variable Player Powers (ACT-12)**: Each player has unique actions/modifiers.
  - When to use: Asymmetry, theme emphasis, replayability.
  - How: Best on simple frameworks (Cosmic Encounter); risk of "one correct strategy" per faction; convey via player mat (Cosmic, Spirit Island) or distributed through deck (Sentinels).
- **Once-Per-Game Abilities (ACT-13)**: Single-use powerful abilities.
  - When to use: Adding timing tension; player-defining moments.
  - How: Vary per character (Warmachine Feats); unused tokens may give endgame VPs (Finca).
- **Advantage Token (ACT-14)**: Special action/modifier that passes to another player after use.
  - When to use: Ebb-and-flow conflict; strategic timing decisions.
  - How: Trade off use vs. losing it (Storm Over Arnhem); Twilight Struggle's China Card; can also be passive ongoing benefit or tie-breaker (A Game of Thrones Iron Throne).
- **Gating and Unlocking (ACT-15)**: New actions made available at game points.
  - When to use: Controlling complexity ramp; forward momentum; narrative arc.
  - How: Triggered by turn/stage, depleting pool, or track threshold (Agricola new action cards per round); 18xx train exhaustion triggers effects.
- **Tech Trees/Tech Tracks/Track Bonuses (ACT-16)**: Personal action upgrades unlocked by resource spend.
  - When to use: Player-driven progression; specialization.
  - How: Buy techs with currency (Civilization money, Eclipse/Through the Ages research); tracks may give bonuses when reached first; techs can be disguised thematically (Titan creature recruiting).
- **Events (ACT-17)**: Actions outside player control affecting game state.
  - When to use: Variety, theme, forcing plan re-evaluation.
  - How: Immediate (Monopoly Chance) or delayed (Core Worlds reveals round-ahead, Through the Ages stack); can be global (Evo temperature) or regional (Empire Builder blizzards).
- **Narrative Choice (ACT-18)**: Multiple action options presented narratively.
  - When to use: Story-driven experiences; thematic immersion.
  - How: Numbered paragraph books (Tales of the Arabian Nights); Crossroads triggers based on player actions (Dead of Winter); story points create memory (Legacy of Dragonholt).

## Key Concepts
- **Action**: Atomic step or compound steps chosen by player to advance the game.
- **Hate Drafting**: Taking a sub-optimal choice to deny an opponent.
- **Yomi**: Anticipating opponents' moves (cross-reference UNC-01); emerges in Action Queue and Shared Queue.
- **Rolling vs. Batch Queue**: Two Action Queue sub-types—head execution vs. full-replacement execution.
- **LIFO vs. FIFO**: Stack resolution orders (also referenced in TRN-13, TRN-17).
- **Information Horizon**: Look-ahead based on hand/known info (Command Cards).
- **Echo**: Glory to Rome/SPQF Follow variant where multiple matching cards power the action.
- **Crossroads**: Hidden-trigger cards revealed based on player action (Dead of Winter).
- **Story Points**: Narrative memory markers in Legacy of Dragonholt enabling context-continuity.
- **Representational AI**: Automa principle (Ch 1 link); relevant to event-driven NPC behavior.

## Mental Models
- Use Action Points when flexibility > strictness; use Action Retrieval when strictness > flexibility.
- Think of Action Drafting as a marketplace—denial is as valuable as acquisition.
- Use Tech Trees when you want player-driven specialization; use Gating when you want designer-controlled pacing.
- Think of Follow systems as "everyone plays on everyone's turn"—engagement up, pace down.

## Anti-patterns
- **Variable Player Powers on complex frameworks**: Cognitive load overwhelms; best on simple frameworks (Cosmic Encounter combat is just "highest number wins").
- **One correct strategy per faction**: Powers that strongly suggest a single strategy limit player choice and replayability.
- **Disconnect of Narrative Choice from game context**: Arabian Nights adventures lack unified narrative; use Crossroads triggers or story points to bind.
- **Visible outcome of narrative choices**: Hides the character-driven experience (Dead of Winter tabletop vs. digital—tabletop shows outcomes, digital hides them).
- **Action Queue chaos without spatial-reasoning support**: Long queues with movement/rotation create a heavy feel that some players reject.

## Reference Tables

### Action Queue Variants
| Variant | Execution | Replacement | Example |
|---|---|---|---|
| Rolling Queue | Head card on each turn | Add one to end | Nuclear War, The Dragon & Flagon |
| Batch Queue | All cards interleaved | Replace all at once | RoboRally, Colt Express, Space Alert |
| Partial Replacement | All cards each turn | Replace one per turn | Twin Tin Bots, Mechs vs. Minions |
| Insert Anywhere | End of queue closest to player | Insert at chosen position | Major General: Duel of Time |

### Tech Progression Variants (ACT-16)
| Form | Trigger | Scope | Example |
|---|---|---|---|
| Tech Tree | Player spends resource, may have prerequisites | Personal | Civilization, Stellar Conquest, Through the Ages |
| Tech Track | Player advances marker along track | Personal | Orleans, Russian Railroads |
| Themed Tech | Disguised as recruiting/hiring/building | Personal | Titan (creature recruiting chain) |

## Worked Example
**Twilight Struggle's Action/Event tension** (ACT-04) creates agonizing choices via the card-play mechanism.

Setup: USA player holds the "Warsaw Pact" card, which provides 3 Action Points but its Event (forming the Warsaw Pact / allowing Soviet influence operations) can ONLY be triggered by the USSR.

- **Scenario A — USA plays for AP**: USA uses 3 AP for standard influence operations. The USSR immediately performs the Warsaw Pact event, gaining their own benefits. USA gains tempo; USSR gains event value.
- **Scenario B — USA holds the card**: USA cannot use AP or trigger the event. Card sits in hand, possibly forcing discard at end of round. USA denies USSR the event trigger.
- **Designer's lever**: Cards with opponent-only events make sequencing central—USA must plan around which opponent events to trigger and when, trading their tempo for USSR event value.

## Key Takeaways
1. Action system choice sets complexity and interactivity—Action Points for flexibility, Action Drafting for interaction, Action Retrieval for planning.
2. Action/Event systems deepen strategy by forcing sequencing decisions, especially when events can benefit opponents.
3. Variable Player Powers work best on simple frameworks—complexity budget goes to interactions, not base rules.
4. Tech Trees are player-driven specialization; Gating is designer-driven pacing—choose based on who controls progression.
5. Follow systems keep all players engaged but slow pace—use a token to track active player.
6. Action Queues (Rolling vs. Batch) trade planning depth for chaos—Batch + spatial movement can overwhelm some players.
7. Narrative Choice needs context-tying mechanisms (Crossroads triggers, story points) to avoid disconnected vignettes.

## Connects To
- **Ch 2 (Turn Order)**: Action Queue uses Interleaved resolution (TRN-15); Follow uses Interleaved turns within the active player's turn; Order Counters are inherently Interleaved.
- **Ch 4 (Resolution)**: Action/Event + Resolution systems pair naturally (Twilight Struggle); Narrative Choice frequently uses Stat Checks (ReS-02).
- **Ch 6 (Uncertainty)**: Yomi (UNC-01) emerges from Shared Action Queues and Simultaneous Selection; Hidden Information (UNC-08) underpins Role Order.
- **Ch 9 (Worker Placement)**: Subset of Action Drafting; first-player advantage concerns carry over.
- **Ch 13 (Card Mechanisms)**: Command Cards, Action/Event, and Narrative Choice all rely on cards; Trick Taking (CAR-01) shares priority-number concepts with Simultaneous Action Selection.
- **RPG character abilities**: Variable Player Powers and Once-Per-Game Abilities mirror RPG Feats and class abilities.
- **RTS tech trees**: Digital real-time strategy games share the Tech Tree pattern.
