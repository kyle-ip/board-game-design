# Skill Evaluation Benchmarks

Manual checks to verify the agent follows v2 workflow — not automated tests. Run after skill changes or when tuning Agent behavior.

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

- [ ] Loads Create mode files (`workflow.md`, `theme-and-experience.md`) — not all 13 chapters
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
- [ ] Routes through `diagnostics/` (e.g. low-agency, endgame-drag) — not random mechanism suggestions
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
- [ ] Flags outliers with >40% gap (or explains why threshold waived)
- [ ] Treats VP-equivalents as **sanity check**, not empirical truth
- [ ] States **confidence**, **calibration source**, and **use scope** per `balance/value-budget.md`
- [ ] Recommends playtest to confirm if suggesting numeric changes

---

## Case F — Lint

**Prompt:**

```
Review ./eval/fixtures/case-f/ for design issues. Run design lint BG001–BG014.
Only flag issues with evidence; mark insufficient evidence as ? not ⚠.
```

**Pass criteria:**

- [ ] Outputs lint-style report with BG001–BG014 coverage (or subset with reason)
- [ ] Uses ⚠ / ? / ✓ semantics from `lint/rules.md`
- [ ] For each ⚠ or ?, uses **Confidence Output Template** (Confidence, Evidence, Signals, Missing)
- [ ] Does **not** claim first-player advantage without seat/win data (? if missing)
- [ ] Routes confirmed issues to matching `diagnostics/*.md`
- [ ] Does not bulk-load all chapters

---

## Scoring (optional)

| Cases passed | Interpretation |
|---|---|
| 6/6 | Integration layer working — ship skill version |
| 4–5/6 | Fix failing mode routing or artifact discipline |
| ≤3/6 | Re-read `SKILL.md` Mode → Required Artifacts; reduce context loading |

Re-run after each skill release that touches `SKILL.md`, `workflow.md`, or templates.

## Cross-References

- Mode definitions: `SKILL.md` Agent Modes + Mode → Required Artifacts
- Regression steps: `workflow.md` Regression Protocol
- Fixture inputs: `eval/fixtures/` (Cases B–F); maintainer guide: `eval/README.md`
