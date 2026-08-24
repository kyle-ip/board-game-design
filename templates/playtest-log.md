# Playtest Log

One framework per session — do not mix. Copy into the project folder. See `playtesting.md`.

Format reference: `templates/examples/micro-scavenger/playtest-log.md`

Non-trivial rule tests: link to `templates/experiment.md`. Hypotheses must be falsifiable — `reasoning/hypothesis-rules.md`.

## Session Meta

| Field | Value |
|---|---|
| Date | |
| Build / version | |
| Experiment ID | EXP-00X (blank if Scattershot / exploratory) |
| Hypothesis ID | HYP-00X (blank if none) |
| Variant | baseline / variant / n/a |
| Stage | early / mid / late |
| Framework | Scattershot / Good-Bad-Meh / Four Fs / Three-bucket / Blind Rulebook |
| Players | (count, familiarity) |
| Duration | |

## Hypothesis Under Test

What one thing are you trying to learn? Must match Experiment ID / Hypothesis ID above when set.

## Raw Notes

Capture verbatim where possible. Quote = signal.

### Facts
-

### Feelings
-

### Findings
-

### Future / Changes
-

## Good / Bad / Meh (if used)

| Good (keep) | Bad (cut) | Meh (tweak) |
|---|---|---|
| | | |

## Three-Bucket Triage (after session)

| Mechanism | Bucket | Note |
|---|---|---|
| | Good / Bad / Needs work | |

Rule: "Needs work" that survives 3 iterations without improvement → Bad.

## Blind Rulebook (if used)

- [ ] Designer left the room
- [ ] One round completed unaided in ≤15 min
- Failures / questions asked:

## Decision

Align with `kill-criteria.md`:

- [ ] **Continue** — next experiment or polish
- [ ] **Restructure** — return to mechanism skeleton
- [ ] **Pause or Kill**

Single change for next build (one variable):

## Sync

- [ ] Evidence row in `design-state.md`
- [ ] Linked `experiment.md` updated (Observed Data / Conclusion) if Experiment ID set
