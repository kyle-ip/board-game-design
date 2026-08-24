# Chapter 11: Area Control

## Core Idea
Area control is the central mechanism of conflict games: how a game represents who owns or influences a space, and what benefits that grants, defines the texture of the conflict from theater-level abstraction down to squad-level force projection.

## Frameworks Introduced
- **Absolute Control (ARC-01)**: One player has binary control of a territory; others are barred from co-existing.
  - When to use: When territory ownership should feel exclusive and contested entry triggers combat.
  - How: A territory is controlled by a single player or uncontrolled. Entry by another player triggers battle. Mark ownership with control tokens when units evacuate.
- **Area Majority/Influence (ARC-02)**: Multiple players co-exist in a space and gain benefits proportional to their presence.
  - When to use: When you want indirect conflict, rapid resolution, and auction-like efficiency without direct combat.
  - How: Players place tokens into shared spaces; at scoring, award VPs by rank (1st/2nd/3rd most tokens). Decide tie rules: friendly (all tied players get 1st-place points) or unfriendly (tied players get 2nd-place points).
- **Force Projection (ARC-06)**: The movement, attack, and ability range of units shapes opponent decisions across multiple spaces.
  - When to use: When unit positioning should matter beyond the space a unit occupies.
  - How: Give units threat ranges (move distance, attack range, spell area, line of sight). A unit's value is the set of spaces it can affect, not just the one it stands on.
- **Zone of Control (ARC-07)**: Spaces adjacent to a unit impact opposing units' ability to move or attack.
  - When to use: In conflict games where you want to form defensive lines with gaps enemies cannot easily exploit.
  - How: **Hard ZOC** — units must stop and attack when entering adjacent enemy space. **Soft ZOC** — units may continue but expend extra Movement Points. Restrict ZOC to certain unit types (cavalry) or states (un-supplied).
- **Line of Sight (ARC-08)**: Units may only see certain areas, restricting attack and detection.
  - When to use: In squad-level tactical games where visibility should shape the battlefield.
  - How: Trace shortest path from attacker to target; terrain blocks LOS. Methods include path-tracing on hexes, thread-laying (Advanced Squad Leader), model's-eye-view (miniatures), color-coded paths (Tannhäuser), or lookup tables (Nuns on the Run).

## Key Concepts
- **Area Influence**: The highest-level umbrella category covering all relationships between players, tokens, and areas; Area Majority and Area Control are its two main sub-branches.
- **Troop Types (ARC-03)**: Units vary in strength, cost, and abilities; some can establish control, others cannot (Axis & Allies: only infantry/armor take territory; planes cannot land on captured ground).
- **Territories and Regions (ARC-04)**: Hierarchical maps where controlling a set of territories within a region grants bonus rewards — a spatial Set Collection mechanism.
- **Area Parameters (ARC-05)**: Attributes tied to controlling areas: VP rewards, resource production, special powers, stacking/unit limits, terrain-based movement and combat modifiers.
- **Stacking Limits**: Caps on how many units may occupy a space, sometimes global (Heroes of Land, Air & Sea: 5 units), sometimes command-based (a general leads up to 7), or terrain/unit-type restricted.
- **Control Transfer**: Control can change via unit occupation, diplomacy actions (Pax Britannica, Divine Right), or scheduled resets (Diplomacy: only Supply Centers change every other turn).
- **Trigger-Number Resolution**: Scoring fires when the sum of forces on a space reaches a threshold (Smash Up bases, Retreat to Darkmoor hero attacks).
- **Homeland Benefits**: Factions gain bonuses when fighting in their own regions (Risk Legacy).

## Mental Models
- Think of **Area Majority** as a Multiple-Lot simultaneous Auction (AUC-11) themed as conflict — El Grande is won by auction efficiency, not tactical brilliance.
- Use **Absolute Control** when entry should trigger combat; use **Area Majority** when opposing forces should co-exist peacefully.
- Think of **Force Projection** as the spatial equivalent of remaining money in an auction — a unit's potential to act in adjacent spaces threatens and shapes every opponent decision.
- Use **Hard ZOC** for wargame-style must-attack friction; use **Soft ZOC** when you want movement to remain possible but costly.

## Anti-patterns
- **Tie ambiguity in Area Majority**: Forgetting to specify friendly vs unfriendly ties leaves a rules gap; decide explicitly or ban ties outright.
- **Requiring players to remember control without markers**: Diplomacy gets away with it only because few spaces matter; otherwise always use control tokens.
- **LOS systems that invite arguments**: Thread-laying and model's-eye-view methods can produce "just grazing" disputes; use cylinder proxies (Warmachine) or lookup tables to avoid this.
- **Mixing ZOC types without clear signaling**: If some units project Hard ZOC and others Soft, players will misjudge stopping requirements — restrict ZOC to identifiable unit types.
- **Force Projection without a board to read it on**: Onitama works because all five movement cards are visible; hidden projection information creates analysis paralysis.

## Reference Tables
### Control Model Comparison
| Feature | Absolute Control | Area Majority/Influence |
|---------|------------------|-------------------------|
| Co-existence | No — entry triggers battle | Yes — opposing tokens share space |
| Resolution | Combat (Chapter 4) | Scoring by rank at intervals |
| Conflict style | Direct | Indirect (auction-like) |
| Designer origin | American school | European school |
| Tie handling | N/A (battle decides) | Must specify friendly/unfriendly |
| Examples | Risk, Axis & Allies | El Grande, Twilight Struggle |

### Line of Sight Methods
| Method | How | Tradeoff |
|--------|-----|----------|
| Path tracing (hex) | Shortest path of hexes; blocking terrain breaks LOS | Simple but odd edge cases on squares |
| Thread-laying | Physical thread center-to-center; obstacles block | Accurate but fiddly, argues over grazes |
| Model's-eye-view | Lean to table level, look at models | Cinematic but subjective; ignore decorative elements |
| Cylinder proxy | Standard cylinder represents each model | Sidesteps decoration arguments |
| Color-coded paths | Spaces grouped into colored paths; same color = visible | Simplifies, less granular |
| Lookup table | Numbered spaces; table says which pairs see each other | Eliminates disputes, no spatial feel |

### ZOC Types
| Type | Effect on mover | Use case |
|------|-----------------|----------|
| Hard ZOC | Must stop and attack | Classic wargame friction |
| Soft ZOC | May continue, extra MP cost | Movement possible but costly |
| Opportunity attacks | Reactive attack when enemy moves adjacent/past | Organic ZOC without explicit rules |
| Restricted ZOC | Only certain unit types or states project | Cavalry, skirmishers; not in Square formation |

## Worked Example
**Twilight Struggle — Influence, Presence, and Control.** In each country, players track their Influence points; a country has a Stability number (Japan = 4, Lebanon = 1).
- **Presence**: Any influence > 0 grants the ability to spread influence to adjacent countries — even when losing the country.
- **Control**: A player controls a country when their influence exceeds the opponent's by at least the country's Stability number. Control doubles the cost for the opponent to add influence via normal operations.
- **Battle for Japan (stability 4)**: If the US has 4 influence and USSR has 0, the US controls (4 - 0 >= 4). The USSR must now spend 2 ops per influence point to try to catch up. If the USSR reaches 1 influence (US still 4), the US no longer controls (4 - 1 = 3 < 4), but the USSR gains Presence and can spread to adjacent countries.

This layered system — Presence, Domination, Control — gives different tactical and strategic value to the same investment, rewarding partial commitment even when full control is out of reach.

## Key Takeaways
1. The umbrella term is **Area Influence**; Area Majority and Area Control are its two dominant mechanical sub-branches, and the distinction is frequently ignored.
2. Absolute Control is the American-school binary model (entry = battle); Area Majority is the European-school indirect model (co-exist, score by rank) and behaves like a simultaneous auction.
3. Always specify tie rules for Area Majority: friendly ties (all get 1st-place points) vs unfriendly ties (tied players get 2nd-place points).
4. Force Projection extends a unit's relevance beyond its space — a unit's value is the set of spaces it can affect, not the one it occupies.
5. Zone of Control lets sparse units form defensible lines with gaps; choose Hard (must stop/attack) or Soft (extra MP) based on desired friction.
6. Line of Sight is "bedeviling" — prefer lookup tables or color-coded paths to avoid arguments, especially with decorative miniatures.
7. Territories-within-Regions is a spatial Set Collection mechanism that creates bonus rewards and "homeland" hooks.

## Connects To
- **Ch 10 (Movement)**: Force Projection, ZOC, and LOS are specialized movement/constraint mechanisms; Point-to-Point movement underpins many area control maps.
- **Ch 4 (Resolution)**: Combat resolution determines how Absolute Control transfers; trigger-number resolution fires scoring on force thresholds.
- **Ch 8 (Auctions)**: Area Majority is mathematically a Multiple-Lot simultaneous Auction (AUC-11).
- **Ch 12 (Set Collection)**: Territories and Regions is a spatial set collection; regional control bonuses work like completed sets.
