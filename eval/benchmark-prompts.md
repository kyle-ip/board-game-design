# Skill Evaluation Benchmarks

Behavior checks verify agent routing and judgment. **Structural** checks run via `python eval/validators/validate.py`. See `eval/README.md`.

Pass criteria are checklists; mark pass only if **all** applicable items are true.

Format reference for expected outputs: `templates/examples/micro-scavenger/`

## Case A — Create

**Prompt:**

```
Design a 2–4 player, 45-minute worker-placement game about Mars colony logistics.
Target feel: scarcity tension, long-term planning, light direct conflict.
Compare at least 2 mechanism architectures before recommending one.
Write concept-brief, design-state, and mechanism-skeleton to ./eval-case-a/ — no full rulebook yet.
```

**Pass criteria:**

- [ ] Loads Create mode files (`genre-profile/`, `workflow.md`, `theme-and-experience.md`) — not all 13 chapters
- [ ] Compares 2–4 candidates (decision matrix or equivalent table)
- [ ] Writes `concept-brief.md`, `design-state.md`, `mechanism-skeleton.md` to requested path
- [ ] Records provisional choice + at least one testable hypothesis or Open question
- [ ] Does **not** dump full rules or over-build PnP unprompted

---

## Case B — Diagnose

**Prompt:**

```
After 3 playtests, players say the game is "fine but nothing exciting happens."
Project files are in ./eval/fixtures/case-b/ (or copy to ./eval-case-b/). Read design-state first.
Diagnose before proposing rule changes.
```

**Pass criteria:**

- [ ] Reads `design-state.md` before recommending changes
- [ ] Routes through `routing/symptom-index.md` and `diagnostics/` — not random mechanism suggestions
- [ ] Asks for or cites evidence (scores, quotes, turn counts)
- [ ] Proposes **one** minimal experiment or Open question — does not stack three fixes
- [ ] Updates or drafts `decision.md` if recommending an intervention path

---

## Case C — Experiment

**Prompt:**

```
Seat 1 wins 5 of 7 games at 4 players. Set up EXP-001 to test bid-for-start-player
vs fixed turn order. One variable only. Write experiment.md and a playtest-log template
linked by EXP-001 / HYP-001.
```

**Pass criteria:**

- [ ] Writes `experiment.md` with baseline, variant, success/failure criteria
- [ ] Hypothesis is falsifiable (observable threshold, not "should feel fairer")
- [ ] **One** design variable identified; "everything else held constant" stated
- [ ] Playtest log includes Experiment ID, Hypothesis ID, Variant fields
- [ ] Does not change unrelated rules in the same proposal

---

## Case D — Regression

**Prompt:**

```
Three playtests confirm the core loop is boring — same action every turn.
Run kill-criteria gate. If Restructure, regress to mechanism skeleton and preserve
all playtest history in ./eval/fixtures/case-d/ (copy to ./eval-case-d/ if mutating).
```

**Pass criteria:**

- [ ] Runs `kill-criteria.md` (Continue / Restructure / Pause or Kill)
- [ ] On Restructure: follows `workflow.md` Regression Protocol
- [ ] Writes `decision.md` + `iteration.md`; updates `design-state.md` Rejected/Locked
- [ ] Does **not** delete existing playtest or experiment files
- [ ] Does not tune numbers before chassis rethink

---

## Case E — Balance

**Prompt:**

```
Review CARD-014 through CARD-018 in ./eval/fixtures/case-e/components-sheet.md.
Use value-budget framing. Flag cards where cost vs estimated value differs by >40%.
State clearly these are heuristics, not proven balance facts.
```

**Pass criteria:**

- [ ] Loads `balance/value-budget.md` or `balance-spreadsheet.md` — not eyeball only
- [ ] Per-card rows with cost vs total estimated value
- [ ] At least one **Effective Value Range** narrative block (Base / adj / range / Confidence / Calibration / Use Scope) — not a single point estimate alone
- [ ] Flags outliers with >40% gap (or explains why threshold waived)
- [ ] Treats VP-equivalents as **sanity check**, not empirical truth
- [ ] States **confidence**, **calibration source**, and **use scope** per `balance/value-budget.md`
- [ ] Notes **interaction/combo/timing** dependency when High
- [ ] Recommends playtest to confirm if suggesting numeric changes

---

## Case F — Lint

**Prompt:**

```
Review ./eval/fixtures/case-f/ for design issues. Run design lint BG001–BG014.
Only flag issues with evidence; mark insufficient evidence as ? not ⚠.
```

**Pass criteria:**

- [ ] Outputs lint-style report with BG001–BG020 coverage (or subset with reason)
- [ ] Uses ⚠ / ? / ✓ semantics from `lint/rules.md`
- [ ] For each ⚠ or ?, uses **Confidence Output Template** (Confidence, Evidence, Signals, Missing)
- [ ] Does **not** claim first-player advantage without seat/win data (? if missing)
- [ ] Routes confirmed issues to matching `diagnostics/*.md`
- [ ] Does not bulk-load all chapters

---

## Case G — Simulate

**Prompt:**

```
Suspect first-player advantage at 4 players. Project has a simple Formal Model.
Choose the correct prototype fidelity, plan (or document) a simulation strategy,
and write simulations/SIM-001.md using the simulation-run template. Do not claim the game is fun.
Link to HYP for first-player advantage. Do not auto-change rules from metrics.
```

**Pass criteria:**

- [ ] Selects **P1** (not P4 reprint as first step)
- [ ] Loads `prototype/selection.md` / Simulate mode files — not full PnP pipeline unprompted
- [ ] Writes `simulation-run.md` with seed, rules/game version, runs, agent profiles, metrics fields
- [ ] If companion runtime available: fills Runner (`runtime/bgd-sim` or path), Population (or explicit single-profile mix), and version fields
- [ ] States confidence + limitations; sample-size caution if runs are low
- [ ] Does **not** claim fun / experience validated
- [ ] Does **not** auto-fix costs or rules from a hypothetical anomaly — proposes HYP/EXP instead

---

## Case H — Runtime Regression (optional)

**Prompt:**

```
Optional when runtime/ is installed. Run the same Micro-Scavenger population
simulation twice with identical seed and config. Confirm metrics match (determinism).
Then change one documented rule (e.g. hand limit) and run regress against baseline JSON.
Do not auto-apply the rule change to design-state without HYP/EXP.
```

**Pass criteria:**

- [ ] Same seed → identical (or documented epsilon) metrics
- [ ] `bgd-sim regress` (or equivalent) reports pass/fail vs thresholds
- [ ] Does not silently mutate Locked decisions from regress fail

---

## Case J — Fidelity Selection

**Prompt:**

```
Two open claims:
(1) "First player has excessive win rate."
(2) "Players don't feel enough tension / social presence."
Pick the minimum valid fidelity for each. Explain evidence type fit. Do not run a full redesign.
```

**Pass criteria:**

- [ ] Claim (1) → P1 / simulation
- [ ] Claim (2) → P2–P4 human playtest (not simulation alone)
- [ ] Mentions BG015 / evidence-type fit or equivalent reasoning
- [ ] Does not recommend 10k bot games for social tension
- [ ] Loads `prototype/selection.md` (or fidelity-ladder) — minimal context
- [ ] Respects `routing/context-budget.md` Simulate/Diagnose **forbidden** lists (no bulk chapters, no print/nanDECK for this question)

---

## Case K — Design Quality (optional rubric)

**Prompt:**

```
Players always choose the same opening. Project files describe a light Euro.
Diagnose, propose one hypothesis, one minimal intervention, and one experiment.
Do not stack fixes. Expert (or maintainer) scores the response with the rubric below.
```

**Rubric (1–5 each; record mean):**

| Dimension | 1 | 3 | 5 |
|---|---|---|---|
| Diagnosis quality | Vague / wrong file | Plausible BG002 path | Evidence-aware, discarded alternatives |
| Hypothesis quality | Unfalsifiable | Testable but multi-var | Single-variable, clear metric |
| Intervention quality | Three stacked changes | One change, weak risk note | Minimal + risks named |
| Experiment quality | No success criteria | Criteria present | Linked EXP + fidelity fit |
| Unintended consequences | Ignored | Mentioned | Concrete failure modes |

**Pass (optional for release):** mean ≥ 3.5; no dimension = 1. Does **not** block the 6/8 process gate; record in scoring sheet for research / regression of design judgment.

---

## Scoring (optional)

| Cases passed | Interpretation |
|---|---|
| 8/8 | Integration layer working — ship skill version |
| 6–7/8 | Fix failing mode routing or artifact discipline |
| ≤5/8 | Re-read `SKILL.md` Mode → Required Artifacts; reduce context loading |

Minimum for **5.0+**: **6/8** behavior (Cases A–G, J) with Case B or D mandatory pass, plus Case G or J pass; **all fixtures pass** `--fixture-all`. Cases H and K are optional maintainer records.

Re-run after each skill release that touches `SKILL.md`, `workflow.md`, `prototype/`, or templates.

## Cross-References

- Mode definitions: `SKILL.md` Agent Modes + Mode → Required Artifacts
- Context budget: `routing/context-budget.md`
- Regression steps: `workflow.md` Regression Protocol
- Fixture inputs: `eval/fixtures/` (Cases B–F); maintainer guide: `eval/README.md`
- Fidelity: `prototype/selection.md`
- Optional runtime: `runtime/README.md`
