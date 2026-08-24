# Chapter 10: Movement

## Core Idea
Movement is the most information-dense action in game design — relocating a single piece changes its relationship to every other piece on the board, yet the change is signaled by simply picking up and placing a piece.

## Frameworks Introduced
- **Tessellation (MOV-01)**: The playing field is divided into spaces to regulate movement.
  - When to use: Any time a board must constrain or measure where pieces can go.
  - How: Choose among tracks (1D), squares/hexagons (2D regular), area maps (irregular), point-to-point, or 3D stacking. Match grid type to realism needs — hexes avoid the diagonal-distance problem of squares.
- **Movement Points (MOV-04)**: A piece is given a number of points to spend on movement, with terrain costing varying amounts.
  - When to use: When units should differ in speed and terrain should matter.
  - How: Assign each unit a point budget; charge per-space costs that vary by terrain (mountains, swamps cost more; roads cost less).
- **Programmed Movement (MOV-10)**: Players simultaneously program a sequence of moves, then reveal and execute them.
  - When to use: When you want simultaneous play, chaotic interaction, and planning under uncertainty.
  - How: Each player selects N action cards in order; reveal and resolve simultaneously. Add board hazards and bumping for emergent chaos.
- **Mancala (MOV-12)**: Movement distance equals the number of pieces at the starting location.
  - When to use: When you want highly interactive, commingled-piece movement with emergent tactics.
  - How: A piece moves N spaces where N = count of pieces (any owner) in its origin space. Variants move all pieces one-by-one (true Mancala) or move a single piece by the count.
- **Map Addition (MOV-16)**: The map is built outward as it is explored.
  - When to use: Exploration games, hidden information, procedural discovery.
  - How: Reveal/place tiles as players reach the edge. Constrained (known shape) or unconstrained. Use gates/edges to restrict movement between tiles.
- **Map Reduction (MOV-17)**: The map shrinks over the course of the game.
  - When to use: When you want rising tension and constriction of options.
  - How: Remove tiles after moves (Hey, That's My Fish!), on a fixed schedule (Sinking of the Titanic), or by claiming routes (Ticket to Ride reduces available options).
- **Hidden Movement (MOV-24)**: Movement occurs that is not visible to all players.
  - When to use: Hidden-role, deduction, and pursuit games (Scotland Yard, Fury of Dracula).
  - How: Hidden player tracks location privately; surfaces at defined intervals or via queued clues. Keep movement rules simple — errors invalidate the whole game.

## Key Concepts
- **Pattern Movement (MOV-03)**: Pieces move in fixed patterns relative to the grid (Chess knight, Shogi lance); includes Fixed Target Spaces, Any-Distance-in-a-Direction, and Jumping.
- **Roll and Move (MOV-02)**: A randomizer determines move distance; an anti-pattern without mitigations like Backgammon's choice or Camel Up's wagering.
- **Resource to Move (MOV-05)**: Players expend a resource (fuel, cards, carrots) to move; mitigates Roll-and-Move randomness.
- **Measurement (MOV-06)**: No grid; movement measured by ruler (miniatures games). Allows premeasurement or not; introduces imprecision and terrain challenges.
- **Different Dice (MOV-07)**: Different dice assigned per unit/state to determine move distance (Formula De gears, Battleball units).
- **Drift (MOV-08)**: Two cards played; sum = forward distance, difference = sideways drift (Snow Tails).
- **Impulse (MOV-09)**: A turn is broken into small impulses; faster units move in more impulses, simulating simultaneous movement (Star Fleet Battles).
- **Relative Position (MOV-11)**: Only relative order is tracked, not absolute position (Formula Motor Racing, Get Bit!).
- **Chaining (MOV-13)**: Pieces are stationary but extended as chains, creating a journey feel (Through the Desert).
- **Bias (MOV-14)**: Pieces auto-move or move more easily in a direction (wind, currents, conveyor belts); Automatic vs Influencer types.
- **Moving Multiple Units (MOV-15)**: A single action moves several pieces, possibly belonging to opponents (Daytona 500, Panamax).
- **Map Deformation (MOV-18)**: The map rotates or shifts, carrying pieces along (Dungeon Twister, Dune's sandstorm).
- **Move Through Deck (MOV-19)**: Players progress through a deck of cards representing rooms/terrain (Chainsaw Warrior, Incan Gold).
- **Movement Template (MOV-20)**: Defined templates (Short Straight, Sharp Right) determine movement (X-Wing Miniatures, Wings of War).
- **Pieces as Map (MOV-21)**: The units themselves compose the map with no separate board (Hive).
- **Multiple Maps (MOV-22)**: Connected maps offer shortcuts or dimensional travel (Iron Dragon, Khronos).
- **Shortcuts (MOV-23)**: A shorter route, sometimes conditional or risky, warps board geometry (Clue's diagonal corners).
- **Promotion**: Pieces reaching the board's end convert to a more powerful version (Chess pawns, Shogi).
- **Anchor/Distance**: A hidden-movement technique where only the last known position (anchor) and a distance counter are tracked; on reveal, the piece is placed anywhere exactly that distance from the anchor (War of the Ring).

## Mental Models
- Use **Tessellation** when you need to regulate movement; pick hexagons over squares when diagonal-distance realism matters, since a 50%-shifted square "brick" grid is isomorphic to hex.
- Think of **Movement Points** as a currency spent on terrain — a wargame's infantry (3 MP) vs armor (6 MP) is the same idea as a racing game's fuel budget.
- Use **Map Reduction** when you want psychology of constriction (Musical Chairs principle); use **Map Addition** when you want discovery and surprise.
- Think of **Hidden Movement** rules as needing to be simpler than open-movement rules, because an error cannot be caught until the game is over.

## Anti-patterns
- **Bare Roll-and-Move**: Players feel zero agency; mitigate by giving choice in how to apply the roll (Backgammon), wagering on movement (Camel Up), or push-your-luck wraps.
- **Diagonal moves on square grids without compensation**: A diagonal move is ~50% further than orthogonal; either disallow, charge more, or switch to hex.
- **Complex Hidden Movement rules**: Any error invalidates the entire experience and is uncatchable mid-game; use color-coded connections and simple point-to-point movement.
- **Hard blocking where soft blocking suffices**: Hard blocking (one worker, one space) frustrates; consider bumping (Euphoria) or cost-increase (Coal Baron) instead.
- **Programmed Movement without labeled turns**: "Right/Left" causes visualization errors; use "Clockwise/Counter-Clockwise" or allow free rotation.

## Reference Tables
### Tessellation Types
| Type | Dimension | Best For | Key Consideration |
|------|-----------|----------|-------------------|
| Track | 1D | Race, roll-and-move | Branches and lane sub-spaces add strategy |
| Squares | 2D regular | Chess-like, grid games | Diagonal distance (~1.5x) must be compensated |
| Hexagons | 2D regular | Wargames, realistic movement | All natural moves equal distance |
| Brick (offset squares) | 2D regular | Prototyping | Isomorphic to hex, easier to build |
| 3D / stacked boards | 3D | Air, space, submarine games | Limit levels for cost and reach |
| Area (irregular) | 2D irregular | Regional/diplomatic games | Areas should be movement-equivalent |
| Point-to-Point | Network | Connection-based games | Shows connections, rivers, borders clearly |
| Combination | Mixed | Trains, grand strategy | Tracks between point-to-point nodes |

### Hidden Movement Detection Methods
| Method | How it works | Example |
|--------|--------------|---------|
| Scheduled surfacing | Hidden player reveals at set turns | Scotland Yard |
| Crime/location trigger | Hidden player reveals by taking required actions | Specter Ops |
| Directional announcements | Other side records movement direction | Captain Sonar |
| Queued location cards | Only the oldest card in a queue is visible | Fury of Dracula |
| Magnetic repulsion | Pieces on opposite sides of a wall repel when co-located | Pyramid of Pengqueen |
| Anchor/Distance | Track only anchor + distance counter; place on reveal | War of the Ring |

## Worked Example
**War of the Ring — Anchor/Distance Hidden Movement.** The Fellowship is hidden from Sauron. Instead of paper-tracking every move:
1. The Fellowship occupies a last-known location (the **Anchor**) on the map.
2. Each time the Fellowship takes a Move action, a **Distance** counter on a track increases by 1.
3. Sauron may hunt (spend actions to attempt a reveal) or the Fellowship may declare its position voluntarily.
4. On reveal, the Fellowship figure is placed on **any space exactly Distance away** from the Anchor.
5. The Fellowship player then traces the actual path taken; if the path passes through enemy-controlled strongholds, corruption/damage is applied.

This eliminates paper tracking and human error. Interactions between Sauron's forces and the Fellowship resolve against the last-known location, but a reveal forces a full accounting of the hidden turns. The mechanism keeps the exact location undetermined turn-by-turn while preserving consequence for route choices.

## Key Takeaways
1. Movement is uniquely information-dense — a single placement reconfigures every piece relationship, yet remains trivially easy to communicate.
2. Choose your tessellation first; it governs movement realism, diagonal-distance problems, and prototyping ease. Hex (or offset-square "brick") avoids the diagonal-distance distortion of square grids.
3. Roll-and-Move is an anti-pattern unless wrapped in player choice (Backgammon), wagering (Camel Up), or push-your-luck (Nur Peanuts!).
4. Distinguish **hard blocking** (one piece per space) from **soft blocking** (bumping, cost increases, duels); the choice dramatically changes player feel.
5. Map Addition (exploration) and Map Reduction (constriction) are opposite psychological levers — discovery vs rising tension.
6. Hidden Movement demands the simplest possible rules because errors are uncatchable until game-end; the Anchor/Distance method eliminates tracking while preserving consequence.
7. Many "movement" mechanisms are subsets of broader categories — Multiple Units is a Command Cards subset; Programmed Movement is an Action Queue subset; Movement Points generalizes to Action Points.

## Connects To
- **Ch 3 (Actions)**: Movement Points generalize to Action Points (ACT-01); Programmed Movement is a subset of Action Queues (ACT-06); Moving Multiple Units is a subset of Command Cards (ACT-05).
- **Ch 6 (Uncertainty)**: Hidden Movement is tightly coupled to uncertainty mechanisms; Different Dice and Roll-and-Move are output randomness.
- **Ch 11 (Area Control)**: Movement mechanisms (especially Force Projection, Zone of Control, Line of Sight) are specialized for area control contexts.
- **Ch 4 (Resolution)**: Pattern Movement often pairs with Promotion; combat resolution interacts with troop positioning.
