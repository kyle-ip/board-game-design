# Chapter 2: Turn Order and Structure

## Core Idea
Turn structure—when and how often players act—is the rhythm of a game; the right choice reduces downtime, manages first-player advantage, and shapes the strategic feel, while the wrong choice creates frustration or stalls.

## Frameworks Introduced
- **Fixed Turn Order (TRN-01)**: Same sequence all game, typically clockwise from a starting player.
  - When to use: Simple games, teaching tools, low rules overhead.
  - How: Compensate for first-player advantage with bonus VPs/resources (Go, Century: Spice Road); ensure equal turns via round-extension marker.
- **Stat Turn Order (TRN-02)**: Sequence set each round by a player statistic (often VP or population).
  - When to use: Implementing Catch the Leader (VIC-18); balancing uneven positions.
  - How: Use different stats per phase (Civilization: Census vs. VP track); reverse direction per phase for finer control (Power Grid: leader picks plant first, goes last on resources).
- **Bid Turn Order (TRN-03)**: Players bid for turn order.
  - When to use: Turn order matters greatly and varies by situation.
  - How: Any auction type (Chapter 8); provide early-game bid guidelines since turn-order value is nebulous; bundle tie-breaking rights with first place (A Game of Thrones Throne track).
- **Progressive Turn Order (TRN-04)**: First Player token rotates clockwise each round; turns taken clockwise from new first player.
  - When to use: Planning-focused games with short turns; predictable rhythm.
  - How: Beware large gaps between turns in large player counts (9-turn gap in 5p); ensure equal first-player opportunities. Regressive variant passes token counter-clockwise—yields powerful double turns.
- **Claim Turn Order (TRN-05)**: Action to claim first-player spot for next round.
  - When to use: Worker Placement / Action Drafting; turn order advantage is situational.
  - How: Sweeten with bonuses (Agricola: play a Minor Improvement); reward non-claiming positions to avoid player-to-the-left benefit (First Class gives bonuses to all positions).
- **Pass Order (TRN-06)**: First to pass goes first next round.
  - When to use: Drafting games where action count is variable (Caylus).
  - How: Trade-off of more actions now vs. earlier picks next round.
- **Real-Time (TRN-07)**: No turns; play as fast as possible until end condition.
  - When to use: Short, intense experiences (20 min max for uninterrupted).
  - How: Keep rules simple; resolve conflicts via card stacks or "touch first" rules; structure with Action + Resolution phases; design for cheating mitigation (open info, large text, fixed placements).
- **Punctuated Real-Time (TRN-08)**: Real-time interrupted by player-triggered stoppages for resolution.
  - When to use: Longer real-time experiences; complex resolutions (Captain Sonar, Space Cadets: Dice Duel).
  - How: Player shouts to pause; resolve; resume; allows complexity in stoppage time and longer overall sessions.
- **Simultaneous Action Selection (TRN-09)**: Players plan secretly, reveal simultaneously, resolve in turn order.
  - When to use: Reducing downtime; introducing Yomi (anticipation of opponents).
  - How: Use priority numbers for tie-breaking (Libertalia, Robo Rally); or resolve in fixed role order (Race for the Galaxy).
- **Role Order (TRN-10)**: Subset of Simultaneous Action Selection—selected role determines resolution order.
  - When to use: Citadels-style role drafting; Race for the Galaxy role selection.
  - How: Call roles in fixed order; players who chose each role reveal and act; targeting roles (not players) avoids the "lose a turn" feel (Citadels Assassin).
- **Random Turn Order (TRN-11)**: Pieces/players drawn from a container.
  - When to use: Tactical, lighter games; war games simulating battlefield uncertainty.
  - How: Chit-pull; veteran units get multiple chits (A Victory Lost); wild card/category tokens reduce luck (Battle Masters).
- **Action Timer (TRN-12)**: Sand timers on action spaces/pieces.
  - When to use: Real-time feel with breathing room; longer sessions than pure Real-Time.
  - How: Action taken when timer placed (not when expired); multiple timers of varying durations add tactical depth (Wartime: 30/60/90 sec); beware manufacturing variation in sand timers.
- **Time Track (TRN-13)**: Linear track with markers; lowest marker acts; action cost = spaces moved.
  - When to use: Player control over who goes next; balance powerful actions with long durations.
  - How: Tie via LIFO (last in moves first) or random; or limit one piece per space forcing skips (Glen More, Kraftwagen); can pair with Action Selection (High Rise).
- **Passed Action Token (TRN-14)**: Token passed clockwise; only token-holders may act.
  - When to use: Async real-time with oversight against cheating.
  - How: Use multiple tokens; penalty if same player holds two (Camelot skips them—player-controlled "lose a turn"); or "no-lapping" version (Diner).
- **Interleaved vs. Sequential Phases (TRN-15)**: Meta-structure—all players do phase 1 then phase 2 (Interleaved), or one player does all phases then next (Sequential).
  - When to use: Interleaved for low downtime (modern preferred); Sequential for thematic swings (war games).
  - How: Mix structures in same game; Power Grid uses Interleaved + Stat Order.
- **Lose a Turn (TRN-16)**: Player skips next turn—meta-mechanism.
  - When to use: Avoid as anti-pattern unless player-controlled.
  - How: If using, ensure player agency (Camelot's slow-play penalty); or remove resources / give others extra turns instead (psychological framing).
- **Interrupts (TRN-17)**: Actions taken during another's turn.
  - When to use: Engagement, downtime reduction, chaos/uncertainty.
  - How: Define pause conventions (Squad Leader); use LIFO stack (Magic: The Gathering); some designs let the interrupter become the active player (Mille Bornes).

## Key Concepts
- **Turn / Round / Phase / Stage**: Hierarchical time units; Phases are named (Feeding, Scoring), Rounds are uniform, Stages sit above Rounds.
- **Yomi**: Japanese term for anticipating opponents' moves; central to simultaneous selection mechanisms.
- **Catch the Leader**: Mechanism for helping trailing players; Stat Turn Order is one implementation.
- **LIFO / FIFO**: Last-In-First-Out vs. First-In-First-Out stack/tie resolution.
- **First-Player Advantage**: Common imbalance favoring one position; design must compensate.
- **Become First Player Action**: Subtype where one of the available actions grants first-player status next round.
- **Hate Drafting**: Taking a sub-optimal choice to deny an opponent.
- **Bonus Time**: Real-Time phase-end extension for non-finishing players (Show & Tile flips timer).
- **Information Horizon**: Look-ahead determined by hand size and known info (Command Cards).
- **LIFO Stack Resolution**: Top-down resolution of stacked interrupts (Magic: The Gathering).

## Mental Models
- Use Interleaved phases by default; only use Sequential when you want epic swings of momentum.
- Think of Time Track as a "price tag" on each action—paying more time means waiting longer to act again.
- Use Real-Time when you want intensity under 20 minutes; use Punctuated Real-Time when you want intensity plus complexity.
- Think of Simultaneous Action Selection as a "Yomi enabler"—the gameplay is in anticipating others.

## Anti-patterns
- **Lose a Turn as random outcome**: Removes player participation, frustrates intent; deprecated (Monopoly Jail, Snakes & Ladders exact-count rule).
- **Large gaps between turns in Progressive**: 9-turn gap in 5p games creates unacceptable downtime.
- **Scripted play in Claim Turn Order**: When one move is obviously best, the choice becomes fake (Twilight Imperium VP-card script; Stone Age expand-fields-then-workers).
- **Player-to-the-left benefit in Claim Turn Order**: Free bonus for being seated next to claimer; balance with bonuses to other positions (First Class).
- **Manufacturing variation in sand timers**: A 30-sec timer may run 40 sec; acceptable for casual play, costly to screen in production.
- **Real-Time without resolution phase**: Complexity mistakes cascade with no time to adjudicate.

## Reference Tables

### Real-Time Family Comparison
| Mechanism | Duration | Complexity | Resolution | Cheating Risk |
|---|---|---|---|---|
| Real-Time (TRN-07) | Short (~20 min max) | Very low | Action + Resolution phases | High—needs open info, fixed placements |
| Punctuated Real-Time (TRN-08) | Medium | Medium (resolved in stoppage) | Player-triggered pauses | Lower—peers observe during pauses |
| Action Timer (TRN-12) | Longer | Medium | Timer expiry | Medium—timer contention disputes |
| Passed Action Token (TRN-14) | Flexible | Medium | Real-time + turn structure | Low—non-active players observe |

### Interleaved vs. Sequential Phases
| Property | Interleaved | Sequential |
|---|---|---|
| Downtime | Low | High |
| Strategic feel | Modern euro | War-game swings |
| Example | Power Grid (3 phases, all players each) | The Russian Campaign (one player completes all phases) |
| Phases can mix | Yes—different turn order per phase | Yes—planning may be Simultaneous even if execution Sequential |

## Worked Example
**Power Grid's turn structure** combines Interleaved Phases (TRN-15) with Stat Turn Order (TRN-02) to balance a game with strong positional advantages.

- **3 phases per round**: Buy Power Plants / Buy Raw Materials / Build Power Lines.
- **Interleaved**: All players do Phase 1, then all do Phase 2, etc.
- **Stat**: Number of connected cities (proxy for leader).
- **Phase 1 (auction)**: Leader must select and bid on the first power plant (disadvantage—less choice).
- **Phases 2-3 (resources, building)**: Leader goes LAST (more expensive resources, may be blocked from building locations).
- **Result**: Stat-based reordering each phase creates a self-balancing Catch the Leader dynamic without a separate balancing mechanism.
- **Designer's lever**: Reversing stat direction between phases gives fine-grained control—the same stat helps the leader in one phase and hurts in the next.

## Key Takeaways
1. Choose turn structure early—it sets the game's rhythm and downtime ceiling.
2. Interleaved > Sequential for reducing downtime, but Sequential can create thematic swings (war games like The Russian Campaign).
3. Stat Turn Order enables Catch the Leader balancing without extra mechanics—use reverse direction per phase for finer control.
4. Real-Time mechanisms need short durations and simple rules; pair with Resolution phases for complex games.
5. Time Tracks put a "price" on each action in time, enabling strategic trade-offs.
6. Avoid Lose a Turn as a random outcome; if needed, make it player-controlled (Camelot) or use psychological framing (give others extra turns).
7. Simultaneous Action Selection introduces Yomi—anticipation of opponents' moves—but requires priority/tie-break systems.

## Connects To
- **Ch 1 (Game Structure)**: Co-op/alpha-player concerns drive Real-Time adoption; team-based and One vs. All structures dictate Interleaved vs. Sequential needs.
- **Ch 3 (Actions)**: Action Point systems and Action Queues interact tightly with turn structure; Follow (ACT-08) keeps all players engaged on every turn.
- **Ch 4 (Resolution)**: LIFO stacks in Interrupts mirror card resolution systems; Squad Leader Defensive Fire ties to combat resolution.
- **Ch 8 (Auctions)**: Bid Turn Order uses auction mechanics; Throne track in A Game of Thrones bundles auction + tie-breaking.
- **War game design tradition**: Chit-pull systems and "I Go, You Go" structures are foundational war-gaming patterns.
- **RPG initiative systems**: Time Track and Stat Turn Order parallel RPG initiative mechanics.
