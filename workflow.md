# Board Game Design Workflow

A staged, decision-oriented flow. Pick the row that matches your project state; do not run stages in parallel.

**Agent rule:** at each stage, write the listed template outputs into the user's project (copy from `templates/`). Prose-only advice is not enough when the user is designing or prototyping a game.

## Stage 0 — Concept
Lock these before any mechanism work ([Chitmunk §1](https://chitmunk.com/blog/how-to-design-a-board-game), [8ration §1](https://www.8ration.com/blogs/board-game-design-guide/)):

- [ ] **1-sentence pitch** — verb + object + twist
- [ ] **Target experience** — 1–3 MDA aesthetics ([MDA paper](https://www.cs.northwestern.edu/~hunicke/MDA.pdf))
- [ ] **Player count** — exact range; declare async/solo if applicable
- [ ] **Playtime** — target minutes, not "30–90"
- [ ] **Audience** — hobby / family / party / heavy strategy

**Write:** `templates/concept-brief.md` → project `concept-brief.md`

Exit gate: pitch + audience fit check.

## Stage 1 — Core Mechanic MVP (paper first)
Per [Board Game Design Lab](https://boardgamedesignlab.com/how-to-design-a-board-game/):

- Build a **paper prototype within 2 weeks**. If longer, the core loop is too complex.
- Find the fun first. **No art, no theme polish.** Just the loop.
- Solo-test before showing others. If you cannot stand 5× solo, redesign.
- Kill/pivot if "the fun" is not one sentence after week 2.

**Write:**
- `templates/mechanism-skeleton.md` (at least core loop + structure codes)
- `templates/rulebook-draft.md`
- `templates/components-sheet.md`
- `templates/pnp-checklist.md` — complete until a full paper game is playable

Default medium: **paper PnP**. Digital tables (TTS/Tabletopia) only after the paper loop works, unless the user requires another medium.

## Stage 2 — Structure
Default: **Chitmunk 8-step checklist** ([source](https://chitmunk.com/blog/how-to-design-a-board-game)):

1. Experience-first: write the feeling, design backward.
2. Core loop diagram (one box in, one box out).
3. Spreadsheet all card data **before** visual design (`components-sheet`).
4. Mechanism skeleton; ignore theme coat.
5. Add theme coat; verify it does not break the loop.
6. Variable-cost balance pass (`balance-notes`).
7. Internal solo + first external playtest (`playtest-log`).
8. Iterate only the weakest mechanism.

**Alternative:** [8ration's 9-step method](https://www.8ration.com/blogs/board-game-design-guide/) when art-last discipline or market sizing matters.

**Update:** `mechanism-skeleton.md` with rejected alternatives and full code list.

## Stage 3 — Playtest
See `playtesting.md`. One framework per session.

**Write:** `templates/playtest-log.md` per session.

## Stage 4 — Polish
Per [8ration Step 8](https://www.8ration.com/blogs/board-game-design-guide/):

- **Art last.** Freeze mechanisms first.
- **Icon clarity > illustration quality.**
- Blind rulebook test — one round ≤15 min, zero designer help.
- Balance pass — `probability-and-balance.md`.

**Write / update:** `templates/balance-notes.md`; revise rulebook from blind-test questions.

## Stage 5 — Publish
- Print file specs — `print-specs.md` (POD vs mass).
- Crowdfunding — `external-resources.md` and [LaunchBoom 11-step guide](https://www.launchboom.com/crowdfunding-tips/the-11-step-guide-for-how-to-create-a-board-game/).

PnP checklist is for **playable prototypes**. Vendor pre-flight in `print-specs.md` is for **manufacturing**.

## For Large / Card Games
Layer [MTG Wiki Set Design](https://mtg.wiki/page/Set_design) four stages when ≥100 cards, rarity curves, or organized play:

| Stage | Output |
|---|---|
| Exploratory Design | Mechanism space; kill weak ideas |
| Vision Design | Vision deck; lock the fun |
| Set Design | Fill set; balance arc / curve |
| Play Design | Tournament-level balance |

Otherwise Chitmunk 8-step suffices.

## Quick Decision Table

| Your situation | Use |
|---|---|
| New designer, first prototype | Stages 0→1→3 + PnP templates |
| Card game, ≥60 unique cards | Stages 0→1→2 + MTG 4-stage |
| Approaching retail / Kickstarter | Stages 0→5 + `print-specs.md` |
| Mechanism unclear | chapters + `cheatsheet.md` + `probability-and-balance.md` |
| Balance smell after playtests | `balance-notes` + failure-mode table |
