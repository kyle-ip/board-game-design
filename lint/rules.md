# Design Lint Rules

Agent-side design linter (Markdown instructions, no CLI). Run before locking mechanisms or shipping PnP artifacts. Full checklist: `lint/checklist.md`.

## Rules

| ID | Name | What to check | Evidence insufficient if |
|---|---|---|---|
| BG001 | First Player Advantage | Seat 1 win rate vs fair share | <5 plays, no seat tracking |
| BG002 | Dominant Strategy | Same path wins regardless of opponents | <3 plays or no strategy notes |
| BG003 | Runaway Leader | Early lead compounds each round | No round-by-round score notes |
| BG004 | Low Agency | Trailing player cannot affect outcome | No observation of dead turns |
| BG005 | Dead Turn | Turn with no meaningful decision | Not tested at max player count |
| BG006 | Kingmaking | Eliminated/hopeless player picks winner | No elimination or endgame log |
| BG007 | Unbounded Engine | Income/score grows without pivot or sink | No spreadsheet or income trace |
| BG008 | Randomness Dominates Skill | Outcomes feel arbitrary; skill irrelevant | No input/output randomness audit |
| BG009 | Analysis Paralysis | Turns routinely >5 min | No timing notes |
| BG010 | Negative Interaction | Blocking/trash feels punitive not strategic | No player quotes |
| BG011 | Score Opacity | Players cannot estimate standing | Hidden VP without tracking aid |
| BG012 | Endgame Drag | Final rounds add time without decisions | No turn-count by phase |
| BG013 | Component Ambiguity | Setup counts wrong or ids missing | components-sheet not cross-checked |
| BG014 | Rule Ambiguity | Blind test failed or repeat questions | No blind test or playtest log |

## Severity

| Mark | Meaning |
|---|---|
| ⚠ | Evidence suggests issue — run diagnostic + experiment |
| ? | Insufficient evidence — collect in next playtest |
| ✓ | No evidence of issue |

## Example Output (agent)

```
Design Lint — v0.6

⚠ BG001 First Player Advantage — P1 won 4/7 games
⚠ BG003 Runaway Leader — leader income +1/round from round 3
? BG009 Analysis Paralysis — no turn timing recorded
✓ BG005 Dead Turn — no dead turns observed at 4p
```

## Routing

| Rule fired | Load |
|---|---|
| BG001 | `diagnostics/first-player-advantage.md` |
| BG002 | `diagnostics/dominant-strategy.md` |
| BG003 | `diagnostics/runaway-leader.md` |
| BG004, BG005 | `diagnostics/low-agency.md` |
| BG006 | `diagnostics/kingmaking.md` |
| BG008 | `diagnostics/randomness-dominates-skill.md` |
| BG012 | `diagnostics/endgame-drag.md` |
| BG013, BG014 | `lint/checklist.md` artifact sections |

## Cross-References

- Failure mode table: `probability-and-balance.md`
- Fix via experiment: `experiments/framework.md`
