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

## Confidence Output Template

For each fired rule (⚠ or ?), expand beyond the one-line summary. Use this block so Lint → Diagnosis handoff is explicit.

```
BG001 First Player Advantage — ⚠

Confidence: Medium
Evidence: 7 plays, seat tracked
Signals:
- P1 win rate 57% (fair share 25% at 4p)
- P1 took best market slot turn 1 in 5/7 games
Missing:
- Player count distribution across sessions
- Skill/experience pairing by seat
Contradictions:
- (none — or evidence that weakens the signal)
```

| Confidence | When to use |
|---|---|
| **Low** | 1–2 plays, indirect signal, or designer intuition only |
| **Medium** | 3+ plays with partial metrics, or strong quotes + weak numbers |
| **High** | Clear metric breach + reproducible pattern across sessions |

**Rules:**

- Use **?** when Confidence would be Low **and** evidence column in Rules table is unmet — do not upgrade to ⚠ without data.
- List **Missing** fields the next playtest should capture.
- List **Contradictions** when evidence conflicts — lowers effective confidence.
- Route ⚠ items to `diagnostics/*`; do not propose fixes before hypothesis.

## Design Confidence Model

Cross-mode standard for Claims (hypotheses, lint findings, balance flags, kill-gate evidence). Apply in Diagnose, Experiment, Balance, and design-state updates.

```text
Claim
  ↓
Evidence refs (PT-###, EXP-###, metrics)
  ↓
Confidence (Low / Medium / High)
  ↓
Contradictions (if any)
  ↓
Decision (continue / experiment / restructure)
```

| Object | Where recorded | Required fields |
|---|---|---|
| Hypothesis | `hypothesis.md`, design-state Active Hypotheses | Claim, Confidence, Evidence refs, Contradictions |
| Lint finding | Lint report in chat | Confidence, Evidence, Signals, Missing, Contradictions |
| Balance flag | `balance-notes.md`, spreadsheet row | confidence, calibration source, use scope, dependency dims |
| Kill gate | `decision.md`, design-state Evidence | Gate result, Evidence summary, Confidence |

**Decision stability:** If Contradictions exist and Confidence is Low, do not Lock — run experiment first.

**Prohibited phrasing** when Confidence is Low or dependency dims are High:

- "Mathematically balanced"
- "Proven fair"
- "Definitely broken"

Use instead: "Heuristic suggests…", "Confidence: Low — playtest recommended."

## Example Output (agent)

```
Design Lint — v0.6

⚠ BG001 First Player Advantage
   Confidence: Medium | Evidence: 7 plays
   Signals: P1 won 4/7; first-turn resource advantage noted
   Missing: seat rotation log
   → diagnostics/first-player-advantage.md

⚠ BG003 Runaway Leader
   Confidence: Low | Evidence: 3 plays, round scores partial
   Signals: leader +2 VP by round 3 in 2/3 games
   Missing: income trace per round

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
- Rank next test: `reasoning/experiment-priority.md`
