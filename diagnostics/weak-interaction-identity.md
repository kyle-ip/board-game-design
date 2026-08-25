# Diagnostic: Weak Interaction Identity

Lint: **ED006**. Related: negative interaction patterns; genre profiles (party / social / euro).

**Evidence type:** experience + behavioral (P2–P4). Multiplayer sim with bots is weak evidence for "felt interaction."

## Symptom

Parallel solitaire; interaction feels transactional or absent; "we shared a table, not a game"; no clear interaction fantasy (deny / negotiate / race / bluff).

## Evidence to Collect

- Count of turns that change another player's options
- Quotes: "I never needed to look at your board"
- Genre expectation vs observed interaction density
- Target Player `experience.social` and `motivation.negotiation`

## Diagnostic Questions

1. What is the intended interaction identity (one phrase)?
2. Is interaction accidental (race for VP) or designed (deny, trade, bluff)?
3. Do players prefer polite non-interaction (euro tolerance)?
4. Is spite the only interaction (kingmaking risk)?

## Likely Causes

| Cause | Tell |
|---|---|
| Independent engines | No shared spaces / markets |
| Soft blocking | Blocking never worth the tempo |
| Hidden everything | No readable contest |
| Audience fear of mean | Designers removed teeth |

## Candidate Interventions

| Fix | Risk |
|---|---|
| Shared scarce space or market | AP / blocking feels mean |
| Direct but bounded take-that | Party backlash if mis-genred |
| Public race with visible leaders | Runaway feel |
| Forced trade / negotiation window | Alpha / downtime |

## Minimal Experiment

**Variable:** one shared contested resource or readable race.

**Metric:** ≥1 meaningful cross-player effect per player per game (logged).

**Success:** Players name the interaction identity unprompted.

## Success Criteria

Interaction identity matches genre and Target Player social/motivation weights.

## Cross-References

- `diagnostics/kingmaking.md` (spite without identity)
- `diagnostics/low-agency.md` (blocked without agency)
- `diagnostics/generic-decision-space.md` (ED005)
