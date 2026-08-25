# Hypothesis Record

One hypothesis per file when formalizing outside an experiment. Copy to project `hypotheses/HYP-001.md`. See `reasoning/hypothesis-rules.md`.

## Meta

| Field | Value |
|---|---|
| ID | HYP-001 |
| Date | |
| Status | draft / testing / supported / refuted / inconclusive |
| Confidence | Low / Medium / High |
| Linked experiment | EXP-00X (if any) |
| Preferred fidelity | P0–P5 — see `prototype/selection.md` |
| Minimum fidelity | |
| Evidence type | simulation / digital_playtest / physical_playtest / expert / intuition |
| Simulation profile | e.g. first-player-advantage (if P1) |
| Physical dependency | true / false |

## Claim

We believe **[design change or mechanism choice]**
will cause **[observable behavior or metric]**
because **[causal reasoning]**.

## Evidence refs

List supporting sources: PT-###, EXP-###, SIM-###, playtest quotes. Required when Status is testing or beyond. Evidence type must fit the claim (BG019).

| Ref | Summary |
|---|---|
| | |

## Contradictions

Evidence that weakens or conflicts with this claim. Empty if none.

| Ref | What it suggests |
|---|---|
| | |

## Success Criteria (observable)

Pass if:

## Failure Criteria (refutation)

Fail if:

## Evidence Log

| Date | Source | Observation | Confidence |
|---|---|---|---|
| | | | Low / Med / High |

## Decision

- [ ] Lock in design-state
- [ ] Reject — move to Rejected in design-state
- [ ] Revise hypothesis and re-test

## Next

→ `templates/experiment.md` if ready to test
→ `templates/design-state.md` — sync Active Hypotheses (Claim, Confidence, Evidence refs, Contradictions)
