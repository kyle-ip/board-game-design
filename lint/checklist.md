# Design Lint Checklist

Run before delivering **rulebook-draft**, **components-sheet**, or **PnP package** to user. Also run after **3+ playtests** with available logs.

Format reference for project files: `templates/examples/micro-scavenger/`

## Playtest Evidence Lint

Use with `lint/rules.md` BG001–BG020. For each ⚠ or ?, use the **Confidence Output Template** (Confidence, Evidence, Signals, Missing, Contradictions). See **Design Confidence Model** in `lint/rules.md`.

- [ ] Latest playtest / simulation linked from `design-state.md`
- [ ] Evidence `source_type` fits the claim (BG019); fidelity match (BG015)
- [ ] Physical-dependency claims have physical evidence (BG020)
- [ ] Win/seat data recorded if competitive
- [ ] Simulation runs include seed + rules version when used (BG017/BG018)
- [ ] At least one verbatim player quote captured (human tests)
- [ ] Hypothesis or experiment ID noted if change was intentional
- [ ] Turn timing noted if AP suspected

## Concept Brief

- [ ] One-sentence pitch present
- [ ] 1–3 MDA aesthetics named
- [ ] Player count and playtime are exact ranges, not vague
- [ ] Emotion curve sketched or referenced
- [ ] Non-goals listed

## Mechanism Skeleton

- [ ] Core loop ≤3 steps
- [ ] Structure codes chosen before theme coat
- [ ] Candidate comparison table if mechanism was debated
- [ ] Rejected alternatives listed
- [ ] Victory currency ≠ working currency (or intentional snowball noted)

## Rulebook Draft

- [ ] Goal in one sentence
- [ ] Setup numbered; start player rule stated
- [ ] Every action has cost → effect → restriction
- [ ] Win condition and tie-breaker explicit
- [ ] Reference card section present
- [ ] Cross-check: every component in setup appears on components-sheet

## Components Sheet

- [ ] Every card/tile has stable id
- [ ] Quantities sum for min and max players
- [ ] No art-only information (icons/text for colorblind)
- [ ] Tools reference present if user needs print files

## PnP Checklist

- [ ] Solo gate (5×) addressed or explicitly waived with reason
- [ ] Playtest log blank prepared for first external session
- [ ] Physical build list complete

## Design State

- [ ] Locked / Open / Rejected sections populated
- [ ] Prototype State / Simulation Evidence present when sims or multi-fidelity prototypes exist
- [ ] Experiment Backlog ranked if ≥2 hypotheses; rank 1 filled in Next Experiment
- [ ] Version Lineage updated on build bump
- [ ] Current risks ≤5 items

## Balance (if numeric game)

- [ ] `balance-spreadsheet.md` or equivalent started
- [ ] One fix per balance pass documented
- [ ] McDie or spreadsheet used for dice/economy (not eyeball only)

## Output Quality

- [ ] Field granularity matches `templates/examples/micro-scavenger/`
- [ ] No empty required sections left as placeholders without "TBD" flag
- [ ] File cross-links valid (design-state ↔ skeleton ↔ rulebook)

## Agent Action

If any critical item fails (rulebook win condition, component count mismatch, no design-state on iteration 2+):

1. Fix before delivering to user, or
2. Flag explicitly as **TBD** with next step
