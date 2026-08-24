# Playtest Frameworks

Runnable scripts. Pick **one framework per session**; do not mix inside a single playtest.

**Before planning:** skim `kill-criteria.md` to set Continue / Restructure / Kill expectations.

**When testing one rule change:** link session to `experiments/framework.md` and `templates/experiment.md`. Playtest logging alone is not enough for non-trivial changes.

**Log templates:** [Break My Game — Designer Resources](https://www.breakmygame.com/designer-resources) provides virtual and PnP playtest log formats (TTGDA-endorsed). Copy structure into `templates/playtest-log.md` fields; do not replace skill experiment linkage (EXP/HYP IDs).

## Framework 1 — Four Fs (Facts / Feelings / Findings / Future)
Best for **mid-to-late stage**. ([minifiniti](https://minifiniti.com/blogs/game-talk/playtesting-frameworks-tabletop-games))

Ask after the playtest, in this order:

- **Facts** (objective): What happened? Score? Turn count? Rules questions? Rules broken?
- **Feelings** (subjective): Where were you bored? Excited? Confused? Frustrated?
- **Findings** (analytical): Which mechanism felt broken? Which felt inevitable? Which felt lucky?
- **Future** (forward): What would you change first? Would you play again? With whom?

Decision rule: capture verbatim, do not paraphrase. Quote = signal.

## Framework 2 — Good / Bad / Meh Columns
Quick structured input, run during play. ([minifiniti](https://minifiniti.com/blogs/game-talk/playtesting-frameworks-tabletop-games))

| Good (keep) | Bad (cut) | Meh (tweak) |
|---|---|---|
| _mechanism / moment_ | _mechanism / moment_ | _mechanism / moment_ |

Hand each player a sheet. They write during play. Collect at end. Triage with Framework 4.

## Framework 3 — Scattershot Testing
Use **early** when you do not yet know what to test. ([minifiniti](https://minifiniti.com/blogs/game-talk/playtesting-frameworks-tabletop-games))

- Cast wide net: do not script scenarios.
- Capture: every rule question, every hesitation pause, every house-rule players invent.
- Decision rule: stop Scattershot once you have 3+ clear hypotheses — switch to Four Fs + experiments.
- Never ship from Scattershot data alone.

## Framework 4 — Three-Bucket Triage
From [Mark Rosewater, Making Magic](https://magic.wizards.com/en/news/making-magic/playtesting). Run after each playtest to sort mechanisms.

- **Good** — keep as-is. Criteria: works as intended, players enjoy, no balance complaint.
- **Bad** — cut now. Criteria: nobody uses it, broken math, or generates negative play experience.
- **Needs work** — keep iterating. Criteria: sound in theory, fails in practice, fixable with tuning.
- Decision rule: if "needs work" survives 3 iterations without improvement, move to "Bad".

## Framework 5 — Blind Rulebook Test
From [8ration Step 8](https://www.8ration.com/blogs/board-game-design-guide/).

- Hand the rulebook to strangers (not friends, not gamers you know).
- **Leave the room.** Do not answer questions during the test.
- **15-minute rule** — if they cannot complete one round in 15 min unaided, the rulebook failed.
- Watch the recording / take notes. Every question they asked = a rulebook edit.

## Stage → Framework Matrix

| Stage | Recommended | Backup |
|---|---|---|
| Early (mechanism TBD) | Scattershot (F3) | Good/Bad/Meh (F2) |
| Mid (mechanisms locked) | Good/Bad/Meh (F2) + Three-bucket (F4) | Four Fs (F1) |
| Late (rulebook exists) | Blind rulebook (F5) + Four Fs (F1) | Three-bucket (F4) |

## From Playtest to Experiment

| If you learned… | Then |
|---|---|
| Vague "felt off" | More Scattershot or Four Fs — no experiment yet |
| One clear suspect rule | Write `experiment.md` with falsifiable hypothesis |
| Balance tell repeats 2× | `diagnostics/*` + single-variable experiment |
| Core loop rejected | `kill-criteria.md` Restructure, not another tweak |

Update `design-state.md` Evidence after every external session.

## Cross-References
- External (Experiment mode): [Break My Game playtest logs](https://www.breakmygame.com/designer-resources), [TTGDA new designer tips](https://www.ttgda.org/get-assistance/newpage)
- Workflow: `workflow.md` Milestone 3 gate
- Kill criteria: `kill-criteria.md`
- Experiment framework: `experiments/framework.md`
- Hypothesis rules: `reasoning/hypothesis-rules.md`
- Iteration triage: `probability-and-balance.md`, `diagnostics/`
- Session log: `templates/playtest-log.md`
- Example log: `templates/examples/micro-scavenger/playtest-log.md`
