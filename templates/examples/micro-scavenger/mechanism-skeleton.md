# Mechanism Skeleton — Micro Scavenger (Example)

## Core Loop

1. **Input**: Take 1 card from deck or top of discard OR play a convert set from hand.
2. **Process**: Discarded cards go to open discard pile; sets score VP immediately.
3. **Output**: VP track advances; deck shrinks.

**The fun (one sentence):** Snatch the right junk at the right moment to combo before your rival does.

## Candidate Comparison (example)

| Candidate | Agency | Interaction | Complexity | Variance | AP Risk |
|---|---|---|---|---|---|
| A. Open discard market (chosen) | M | H | L | L | L |
| B. Closed hand only | M | L | L | M | L |
| C. Worker placement 2p | H | M | M | L | M |

**Recommendation:** A — highest interaction for 2p in 10 min.

## Structure First

| Slot | Chosen code | Why |
|---|---|---|
| Game structure (STR-*) | STR-01 competitive | 2p race |
| Turn order (TRN-*) | TRN-01 sequential | Simple teach |
| Action economy (ACT-*) | ACT-01 one action/turn | Light |
| Victory / end (VIC-*) | VIC-03 depletion end | Deck empty |

## Supporting Mechanisms

| Category | Code(s) | Role in the loop |
|---|---|---|
| Set Collection (SET-*) | SET-01 triangular | 1/3/6 VP sets by tag |
| Economics (ECO-*) | ECO open discard | Interaction |
| Card (CAR-*) | CAR hand management | Timing |

## Rejected Alternatives

| Rejected | Why not |
|---|---|
| Auction (AUC-*) | Overtime for target audience |
| Dice combat | Randomness dominates skill |

## Currencies

| Name | Working or victory? | How earned | How spent |
|---|---|---|---|
| Scrap cards | Working | Draw/discard | Convert to VP sets |
| VP | Victory | Set conversion | N/A |

## Randomness Stance

| Spot in the loop | Input or output? | Desired aesthetic |
|---|---|---|
| Deck order | Input | Plan around visible discard |
| Draw from deck | Input | Take-or-leave before commit |

## Component Implications

- 24 cards (6 tags × 4 copies simplified to 24 unique-ish cards for prototype)
- VP track 0–20
- No board

## Exit Gate

- [x] Core loop fun articulable in one sentence
- [x] Structure chosen before theme coat
- [x] Rejected alternatives recorded
- [x] Currencies split (victory vs working)

## Sync

Locked items → `design-state.md`

## Next

→ `components-sheet.md` + `rulebook-draft.md`
