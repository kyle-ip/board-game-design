# Board Game Design Workflow

Staged, decision-oriented flow. **Milestones**, not a one-way waterfall — regress when evidence demands it.

**Agent rules:**
- Write listed template outputs into the user's project (copy from `templates/`).
- Maintain `design-state.md` on every milestone transition and consequential decision.
- Prose-only advice is not enough when designing or prototyping.

Format reference: `templates/examples/micro-scavenger/`

## Milestone Map

| Milestone | Focus | Typical regression trigger |
|---|---|---|
| 0 Concept | Pitch, aesthetics, constraints | Theme-audience mismatch |
| 1 Core MVP | Paper loop, fun sentence | Fun not found in 2 weeks |
| 2 Structure | Mechanism skeleton, spreadsheet data | Mechanism conflict / paste-on theme |
| 3 Playtest | Experiments, logs | Kill gate → Restructure to 1–2 |
| 4 Polish | Rulebook blind test, balance | Blind test fail → back to 2 |
| 5 Publish | Print specs, crowdfunding | — |

**Allowed regressions:** 3→1, 3→2, 4→2. Record in `design-state.md` + `decision.md`.

## Regression Protocol

Milestones are **not irreversible**. Regress only when:

- New evidence contradicts a locked mechanism assumption
- Diagnosis identifies a **chassis-level** failure (not numbers-only)
- `kill-criteria.md` triggers **Restructure**

When regressing:

1. **Write `decision.md`** — note superseded choice; move failed mechanisms to **Rejected** in `design-state.md`
2. **Write `iteration.md`** — record build version bump, observed problem, and regression target milestone
3. **Preserve history** — do **not** delete `playtests/`, `experiments/`, or prior logs; evidence chain must stay intact
4. **Update `design-state.md`** — set current milestone, update **Version Lineage**, re-rank **Experiment Backlog**, clear stale **Active Hypotheses** tied to rejected chassis
5. **Do not tune numbers** on a broken chassis — restructure mechanism skeleton before balance passes

## Milestone 0 — Concept

Lock before mechanism work ([Chitmunk §1](https://chitmunk.com/blog/how-to-design-a-board-game)). For official stage overview and new-designer guidance, see [TTGDA — Tips for New Game Designers](https://www.ttgda.org/get-assistance/newpage).

- [ ] **1-sentence pitch** — verb + object + twist
- [ ] **Target experience** — 1–3 MDA aesthetics; see `theme-and-experience.md`
- [ ] **Emotion curve** sketched
- [ ] **Player count** — exact range
- [ ] **Playtime** — target minutes
- [ ] **Audience** — hobby / family / party / heavy strategy

**Write:** `concept-brief.md`, initialize `design-state.md`

Exit gate: pitch + audience fit check.

## Milestone 1 — Core Mechanic MVP (paper first)

Per [Board Game Design Lab](https://boardgamedesignlab.com/how-to-design-a-board-game/):

- Paper prototype within **2 weeks** or simplify.
- Find the fun first — no art polish.
- Solo-test 5× before external playtests.
- Kill/pivot if fun is not one sentence after week 2 — see `kill-criteria.md`.

**Write:**
- `mechanism-skeleton.md` (core loop + candidate comparison if debated)
- `rulebook-draft.md`, `components-sheet.md`, `pnp-checklist.md`

Default medium: **paper PnP**. Digital (`tools/TTS-guide.md`) only after paper loop works.

**Update:** `design-state.md` Locked/Rejected as decisions land.

## Milestone 2 — Structure

Default: **Chitmunk 8-step checklist** ([source](https://chitmunk.com/blog/how-to-design-a-board-game)):

1. Experience-first (`theme-and-experience.md`)
2. Core loop diagram
3. Spreadsheet component data (`components-sheet`, `balance-spreadsheet.md`)
4. Mechanism skeleton; theme coat after loop
5. Verify theme does not break loop
6. Variable-cost balance pass (`balance-notes`)
7. Internal solo + first external playtest (`playtest-log`)
8. Iterate weakest mechanism only — one variable per experiment

**Update:** `mechanism-skeleton.md`, `design-state.md`

## Milestone 3 — Playtest

See `playtesting.md`. One framework per session. Non-trivial changes → `experiment.md`.

**Write:** `playtest-log.md` per session; `experiment.md` when testing one variable.

### Decision Gate (required)

After **3+ playtests** (or failed core loop at week 2), run `kill-criteria.md` with user:

| Result | Next |
|---|---|
| **Continue** | Milestone 4 or next experiment |
| **Restructure** | Return to Milestone 1–2; reject failed chassis in design-state |
| **Pause or Kill** | Archive; document in `iteration.md` |

Align playtest log **Decision** field with gate result.

## Milestone 4 — Polish

Per [8ration Step 8](https://www.8ration.com/blogs/board-game-design-guide/):

- Art last; freeze mechanisms
- Blind rulebook test — one round ≤15 min, zero designer help
- Balance pass — `balance/README.md`, `probability-and-balance.md`
- Run `lint/checklist.md` before delivering artifacts

**Write / update:** `balance-notes.md`, `rulebook-draft.md`

Blind test failure → regress to Milestone 2 rulebook/skeleton.

## Milestone 5 — Publish

- `print-specs.md` (POD vs mass)
- Crowdfunding — `external-resources.md`

PnP checklist = playable prototypes. Vendor pre-flight = manufacturing.

## For Large / Card Games

Layer [MTG Wiki Set Design](https://mtg.wiki/page/Set_design) four stages when ≥100 cards:

| Stage | Output |
|---|---|
| Exploratory Design | Mechanism space; kill weak ideas |
| Vision Design | Vision deck; lock the fun |
| Set Design | Fill set; balance arc / curve |
| Play Design | Tournament-level balance |

## Quick Decision Table

| Your situation | Use |
|---|---|
| New designer, first prototype | Milestones 0→1→3 + PnP templates |
| Card game, ≥60 unique cards | Milestones 0→1→2 + MTG 4-stage |
| Approaching retail / Kickstarter | Milestones 0→5 + `print-specs.md` |
| Mechanism unclear | `reasoning/design-reasoning.md` + chapters + cheatsheet |
| Balance smell after playtests | `diagnostics/*` + balance-notes |
| Existing project session 2+ | `design-state.md` first |
