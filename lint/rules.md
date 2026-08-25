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
| BG015 | Prototype Fidelity Mismatch | Evidence fidelity cannot answer the claim (e.g. sim "proves" social tension) | Wrong level per `prototype/selection.md` |
| BG016 | Unvalidated Digital Assumption | DIGITAL-ONLY automation treated as physical truth | No DIGITAL-ONLY / PHYSICAL-DEPENDENT labels |
| BG017 | Missing Simulation Seed | Simulation run lacks seed / rules_version / reproducibility meta | `simulation-run.md` Meta incomplete |
| BG018 | Missing Rules Version | Sim or playtest not tied to rules/build version | No version on SIM/PT/EXP |
| BG019 | Unsupported Claim | Claim's evidence `source_type` unfit for the claim | Type mismatch (see Evidence types) |
| BG020 | Physical Validation Required | Claim has `physical_dependency: true` but only sim/digital evidence | No physical_playtest |

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
| **Low** | 1–2 plays, indirect signal, designer intuition only, or <100 sim runs |
| **Medium** | 3+ plays with partial metrics, or 100–999 stable sim runs, or strong quotes + weak numbers |
| **High** | Clear metric breach + reproducible pattern across sessions/seeds + adequate agent diversity for sim claims |

**Rules:**

- Use **?** when Confidence would be Low **and** evidence column in Rules table is unmet — do not upgrade to ⚠ without data.
- List **Missing** fields the next playtest/sim should capture.
- List **Contradictions** when evidence conflicts — lowers effective confidence.
- Route ⚠ items to `diagnostics/*`; do not propose fixes before hypothesis.
- For BG015–BG020, route to `prototype/selection.md` / `prototype/runtime.md` as appropriate.

## Design Confidence Model

Cross-mode standard for Claims (hypotheses, lint findings, balance flags, kill-gate evidence). Apply in Diagnose, Experiment, Simulate, Balance, and design-state updates.

```text
Claim
  ↓
Evidence
  ├── Simulation Evidence
  ├── Digital Playtest Evidence
  ├── Physical Playtest Evidence
  └── Expert / Designer Evidence
  ↓
Confidence (Low / Medium / High)
  ↓
Contradictions (if any)
  ↓
Decision (continue / experiment / restructure)
```

### Evidence types (`source_type`)

| Type | Fits | Does not fit |
|---|---|---|
| `simulation` | Probability, balance, length, dominant lines | Fun, social tension, table ergonomics |
| `digital_playtest` | Rules clarity, agency, pacing (screen) | Physical footprint, tactile handling |
| `physical_playtest` | Table experience, components, social presence | Cheap large-N balance sweeps alone |
| `expert` | Design judgment, precedent | Sole proof of balance |
| `intuition` | Draft hypotheses only | Lock / High confidence |

Evidence quality = **Question + Evidence type + Fit** — not a fixed ranking of sources.

| Object | Where recorded | Required fields |
|---|---|---|
| Hypothesis | `hypothesis.md`, design-state Active Hypotheses | Claim, Confidence, Evidence refs, Contradictions, preferred fidelity / evidence type |
| Simulation | `simulation-run.md`, design-state Simulation Evidence | Seed, runs, metrics, confidence, limitations |
| Lint finding | Lint report in chat | Confidence, Evidence, Signals, Missing, Contradictions |
| Balance flag | `balance-notes.md`, spreadsheet row | confidence, calibration source, use scope, dependency dims |
| Kill gate | `decision.md`, design-state Evidence | Gate result, Evidence summary, Confidence |

**Decision stability:** If Contradictions exist and Confidence is Low, do not Lock — run experiment first.

**Prohibited phrasing** when Confidence is Low, fidelity mismatched, or dependency dims are High:

- "Mathematically balanced"
- "Proven fair"
- "Definitely broken"
- "Simulation proved it's fun"
- "Digital playtest validated table feel"

Use instead: "Heuristic suggests…", "Confidence: Low — playtest recommended.", "System evidence only — experience unvalidated."

## Example Output (agent)

```
Design Lint — v0.6

⚠ BG001 First Player Advantage
   Confidence: Medium | Evidence: 7 plays
   Signals: P1 won 4/7; first-turn resource advantage noted
   Missing: seat rotation log
   → diagnostics/first-player-advantage.md

⚠ BG015 Prototype Fidelity Mismatch
   Confidence: High | Evidence: claim "players feel tense" backed only by SIM-003
   → prototype/selection.md (prefer P2/P4)

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
| BG015–BG020 | `prototype/selection.md`, `prototype/runtime.md`, `templates/simulation-run.md` |

## Cross-References

- Failure mode table: `probability-and-balance.md`
- Fix via experiment: `experiments/framework.md`
- Rank next test: `reasoning/experiment-priority.md`
- Fidelity: `prototype/fidelity-ladder.md`
