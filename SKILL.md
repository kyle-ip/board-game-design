---
name: board-game-design
description: "Design tabletop game mechanisms and paper prototypes using Building Blocks of Tabletop Game Design (13 mechanism chapters) plus workflow, playtesting, balance, and PnP templates. Invoke when the user designs or iterates a board/card game, chooses or balances mechanisms (turn order, auctions, worker placement, cards, etc.), writes a concept brief or mechanism skeleton, prepares playtests, or builds a print-and-play prototype/demo."
license: MIT
compatibility: "Agent Skills hosts (Cursor, Claude Code, and other SKILL.md-compatible runtimes). Markdown-only; no required network or packages."
metadata:
  open-standard: "https://agentskills.io/specification"
  primary-source: "Building Blocks of Tabletop Game Design (Engelstein & Shalev)"
---

# Board Game Design

Knowledge base from *Building Blocks of Tabletop Game Design* by Geoffrey Engelstein & Isaac Shalev (CRC Press, ~517 pages, 13 chapters), plus workflow, playtesting, balance, print guidance, and **project templates** that turn advice into files you can playtest.

Pipeline: **concept → mechanism skeleton → paper PnP prototype → playtest/balance → (optional) POD/digital**.

## How to Use This Skill

**Invocation patterns:**

- **No argument** — return this file (overview + indexes).
- **Topic** (e.g., "auctions", "worker placement", "deck building") — load matching `chapters/chNN-*.md` and the relevant entry in `patterns.md`.
- **Chapter number** (e.g., "ch07") — load that chapter file.
- **Decision needed** — load `cheatsheet.md`; cross-ref `patterns.md`.
- **Term lookup** — load `glossary.md`.
- **Design / iterate a game** — follow **Default Project Outputs** below; load `workflow.md` + needed templates.
- **Workflow / playtest / probability / print** — load the companion file.

**Always load the smallest file that answers the question.** Do not bulk-load chapters unless the user asks for a survey.

## Default Project Outputs

When the user asks to design, iterate, prototype, or develop a tabletop game, **write project files** (copy from `templates/`; do not only give prose). Prefer the user's project directory; if none, ask where to put them.

| Stage | Write | From template |
|---|---|---|
| 0 Concept | concept brief | `templates/concept-brief.md` |
| 1–2 Mechanisms | mechanism skeleton | `templates/mechanism-skeleton.md` |
| 1 Paper MVP | rulebook draft + components sheet + PnP checklist | `templates/rulebook-draft.md`, `components-sheet.md`, `pnp-checklist.md` |
| 3 Playtest | playtest log | `templates/playtest-log.md` |
| 4 Balance | balance notes | `templates/balance-notes.md` |

Paper PnP is the default first playable build. TTS / Tabletopia / web demos come only after the paper loop works, unless the user specifies another medium.

## Core Frameworks & Mental Models

### MDA alignment
Mechanics → Dynamics → Aesthetics. Choose Aesthetics first, then design Mechanics that produce Dynamics that evoke them. ([MDA paper](https://www.cs.northwestern.edu/~hunicke/MDA.pdf))

### Mechanism categories (13 chapters)
Structure → Turn Order → Actions → Resolution → Victory → Uncertainty → Economics → Auctions → Worker Placement → Movement → Area Control → Set Collection → Card Mechanisms. Pick **structure first**.

### Input vs Output randomness
- **Input** — random result informs decision *before* commitment → agency.
- **Output** — random outcome resolves a committed decision → drama.

### Action economy
Action Points (flexibility) vs Action Retrieval (strictness) vs Action Drafting (denial).

### Resolution curve
Stat Check (unit quality), High Number (force quantity), RPS (no unit always best), Force Commitment (intent), Critical Hits (jackpot).

### Uncertainty types
Match uncertainty type to aesthetic; mismatch causes "feels random" complaints.

### Victory currency separation
Keep victory currency separate from working currency or you get snowball (Monopoly cash).

### Catch-the-leader
Prefer subtle assistance (e.g. Stat Turn Order). Overt catch-up feels punishing.

### Economy openness
Open (easier balance) / Closed (zero-sum timing) / One-in-One-Out (modern card default).

### Auction purpose
English (max value), Dutch (speed), Vickrey (truthful sealed), Constrained (finite token budget).

### Turn-order binding
Strong left-right binding (auctions, worker placement) needs catch-up or asymmetry compensation.

### Print paths
POD (TGC) vs mass (Panda) — see `print-specs.md`. Prototype-first uses `templates/pnp-checklist.md`, not vendor PDFs.

## Chapter Index

`patterns.md` holds **selected** high-leverage patterns; full definitions live in the chapter files.

| # | File | Title (mechanism codes) |
|---|---|---|
| 1 | [ch01](chapters/ch01-game-structure.md) | Game Structure (STR-01 to STR-10) |
| 2 | [ch02](chapters/ch02-turn-order.md) | Turn Order and Structure (TRN-01 to TRN-17) |
| 3 | [ch03](chapters/ch03-actions.md) | Actions (ACT-01 to ACT-18) |
| 4 | [ch04](chapters/ch04-resolution.md) | Resolution (RES-01 to RES-22) |
| 5 | [ch05](chapters/ch05-victory.md) | Game End and Victory (VIC-01 to VIC-20) |
| 6 | [ch06](chapters/ch06-uncertainty.md) | Uncertainty (UNC-01 to UNC-11) |
| 7 | [ch07](chapters/ch07-economics.md) | Economics (ECO-01 to ECO-19) |
| 8 | [ch08](chapters/ch08-auctions.md) | Auctions (AUC-01 to AUC-16) |
| 9 | [ch09](chapters/ch09-worker-placement.md) | Worker Placement (WPL-01 to WPL-08) |
| 10 | [ch10](chapters/ch10-movement.md) | Movement (MOV-01 to MOV-24) |
| 11 | [ch11](chapters/ch11-area-control.md) | Area Control (ARC-01 to ARC-08) |
| 12 | [ch12](chapters/ch12-set-collection.md) | Set Collection (SET-01 to SET-05) |
| 13 | [ch13](chapters/ch13-card-mechanisms.md) | Card Mechanisms (CAR-01 to CAR-06) |

## Topic Index

| If you're asking... | See |
|---|---|
| Co-op alpha-player problem | Ch 1, Ch 6 |
| Solo mode / Automa design | Ch 1, Ch 3 |
| Legacy & campaign structure | Ch 1, Ch 5 |
| First-player advantage / catch-up | Ch 2 |
| Real-time vs turn-based | Ch 2 |
| Action selection (drafting, points, retrieval) | Ch 3 |
| Tech trees / gating / progression | Ch 3 |
| Combat resolution / dice pools | Ch 4 |
| Randomness: input vs output | Ch 4, Ch 6 |
| Snowball / runaway leader | Ch 5, Ch 7, `probability-and-balance.md` |
| Hidden vs exposed victory points | Ch 5 |
| End-game triggers | Ch 5 |
| Hidden information, hidden roles | Ch 6 |
| Push-your-luck design | Ch 6 |
| Open vs closed economy | Ch 7 |
| Trading & negotiation | Ch 7 |
| Bidding forms & auction selection | Ch 8 |
| Worker placement | Ch 9 |
| Movement / roll-and-move mitigation | Ch 10 |
| Hidden movement | Ch 6, Ch 10 |
| Area majority / force projection | Ch 11 |
| Set collection curves | Ch 12 |
| Deck building / drafting / trick-taking | Ch 13 |
| Concept → paper prototype pipeline | `workflow.md`, `templates/` |
| Playtest frameworks | `playtesting.md` |
| Balance failure modes & McDie | `probability-and-balance.md` |
| PnP then POD/mass print | `templates/pnp-checklist.md`, `print-specs.md` |
| External resources | `external-resources.md` |

## Companion Files

| File | Purpose |
|---|---|
| [workflow.md](workflow.md) | Stages 0–5 with required template outputs |
| [playtesting.md](playtesting.md) | Five playtest frameworks |
| [probability-and-balance.md](probability-and-balance.md) | Failure modes, dice intuition, McDie rule |
| [print-specs.md](print-specs.md) | POD vs mass production specs |
| [cheatsheet.md](cheatsheet.md) | Decision rules + symptom → file routing |
| [patterns.md](patterns.md) | Selected mechanism patterns |
| [glossary.md](glossary.md) | Term definitions |
| [external-resources.md](external-resources.md) | Condensed links; full index in `references/web-resources.md` |
| [templates/](templates/) | Copy-out project files for design and PnP |

## Scope & Limits

- **Book is mechanisms-focused** — trade-offs and catalogues; project process lives in companions + templates.
- **Synthesized, not verbatim** — not a substitute for the original book.
- **Language** — in Chinese context, prefer each game's official/mainstream Chinese name when one exists; otherwise keep English (optional short gloss on first mention).
- **Single-designer focus** — multi-agent design collaboration is out of scope.
- **Default prototype medium** — paper PnP; digital/web only when requested or after paper works.
