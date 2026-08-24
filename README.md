# board-game-design

An [Agent Skill](https://agentskills.io/specification) (**v2.2.0**) for designing tabletop game **mechanisms** and shipping a **paper print-and-play prototype** — now with **design state**, **experiments**, **diagnostics**, and **evidence-driven iteration**. Compatible with Cursor, Claude Code, and other runtimes that load `SKILL.md` skills.

Core loop agents follow:

**Intent → Hypothesis → Prototype → Experiment → Evidence → Diagnosis → Decision → (update design-state) → repeat**

Shorthand: **concept → mechanism skeleton → paper PnP → playtest / balance → (optional) POD or digital**

> Repo-level `README.md` is for humans (install, structure, attribution). Agent instructions live in [`SKILL.md`](SKILL.md) and progressive-disclosure companions — per [Anthropic skill authoring guidance](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills).

See [`CHANGELOG.md`](CHANGELOG.md) for version history.

## Install

### Cursor

Copy or clone this repo into your personal or project skills directory, keeping the folder name `board-game-design` (must match the skill `name`):

```text
~/.cursor/skills/board-game-design/   # user-wide
# or
<project>/.cursor/skills/board-game-design/   # project-scoped (preferred when sharing a game repo)
```

Clone example:

```bash
git clone git@github.com:kyle-ip/board-game-design.git ~/.cursor/skills/board-game-design
```

### Claude Code / other Agent Skills hosts

Place the directory where your host discovers skills (often `.claude/skills/board-game-design/`). Requirements:

- Folder contains a root [`SKILL.md`](SKILL.md) with YAML `name` + `description`
- Prefer installing from trusted sources; skim `SKILL.md` and bundled files before use

See the open standard: [agentskills.io/specification](https://agentskills.io/specification).

## When it triggers

The skill description asks agents to load it when you:

- Design or iterate a board / card game
- Choose or balance mechanisms (turn order, auctions, worker placement, cards, …)
- **Diagnose** problems (boring, unfair, snowball, etc.)
- Run **playtest experiments** with falsifiable hypotheses
- Write a concept brief or mechanism skeleton
- Prepare playtests or evaluate **continue / kill**
- Build a print-and-play prototype

## How to prompt (v2)

Good prompts give the agent **mode**, **constraints**, and **artifacts** (or paths). Vague prompts still work, but you get sharper outputs when you include:

| Include | Why |
|---------|-----|
| **Player count, time, audience** | Stops generic mechanism dumps |
| **Target feel** (tension, bluff, puzzle, …) | Drives MDA-first design, not mechanism-first |
| **Project path** or `@design-state.md` | Agent reads Locked/Open/Rejected before suggesting changes |
| **Observed symptom + evidence** | Triggers Diagnose mode instead of random fixes |
| **One variable to test** | Triggers Experiment mode; avoids stacked rule changes |
| **Output ask** ("write files to `./my-game/`") | Gets templates, not prose-only |

**Project-scoped tip:** keep game files in your repo and reference them (`@concept-brief.md`, `@playtests/PT-003.md`). On session 2+, start with: *"Read design-state first, then …"*

### Create — new game from scratch

Compare mechanisms, write concept + skeleton + design-state. Ask for **2–4 candidates** before locking rules.

```
Design a 2–4 player, 45-minute medium-weight game about Mars colony logistics.
Target feel: scarcity tension, long-term planning, light direct conflict.
Audience: hobby gamers who know Wingspan but not heavy euros.
Compare worker placement vs action drafting vs open market — recommend one with trade-offs.
Write concept-brief, design-state, and mechanism-skeleton to ./mars-habitat/ using the micro-scavenger example as format reference.
Do not write full rules yet.
```

```
I want a family co-op card game (2–4p, 20 min) with a Cthulhu investigation theme.
Core experience: dread + teamwork, not alpha-player quarterbacking.
Start with theme-and-experience (emotion curve), then suggest mechanisms that fit — avoid hidden roles if they don't serve the feel.
Output files to ./deep-shallows/.
```

**Weak → strong**

| Weak | Strong |
|------|--------|
| "Make me a worker placement game" | Add players, time, feel, audience, and "compare 2–3 chassis before choosing" |
| "Design a card game about pirates" | Add "2p, 15 min, gateway, tension from hand limits" + output directory |

### Diagnose — something feels wrong

Name the **symptom**, give **playtest facts**, ask for **diagnosis + minimal experiment** — not an immediate redesign.

```
We've playtested 4 times (logs in ./orbital-mining/playtests/). Leader is usually decided by round 3; trailing players say they can't catch up.
Read design-state first. Diagnose (snowball vs low agency vs endgame drag), propose one falsifiable hypothesis, and draft EXP-005 — don't change three rules at once.
```

```
After 3 sessions, seat 1 wins 5/7 games at 4 players. Hypothesis: first pick on the worker track is too strong.
Run first-player-advantage diagnostic. Suggest the smallest rule change to test next, with success criteria (e.g. seat 1 win rate < 35% over 10 plays).
```

```
Players say the game is "fine but boring" in the last 20 minutes. Midgame scores were 12–18 VP; final rounds took 25+ minutes with few decisions.
Diagnose endgame drag vs low agency. Quote which diagnostic guide you used.
```

### Experiment — test one change

Specify **baseline**, **variant**, and **measurable success**.

```
Set up EXP-002: test hand limit 3 → 2 only. Everything else stays v0.6.
Hypothesis: smaller hand increases discard-pile fights without adding AP.
Success: in 4/5 playtests, both players contest discard at least twice; fun ≥ 3.5/5.
Write experiment.md and a blank playtest-log template for the next session.
```

```
We refuted EXP-001 (bid for start player didn't fix seat bias). Design EXP-002 testing Stat Turn Order instead — one variable only. Link to design-state Open questions.
```

### Balance — numbers, cards, economy

Ask for **value budget** or **spreadsheet rows**, not "make it fair."

```
Review CARD-014 through CARD-022 in ./deck-builder/components-sheet.md.
Build balance-spreadsheet rows using value-budget; flag any card where cost vs total estimated value differs by >40%.
Card pool uses triangular set scoring — check curve matches rulebook.
```

```
Dice combat uses 3d6 keep 2 vs target 9+. Should we add a fourth die? Run McDie reasoning before recommending — don't eyeball.
Log conclusion in balance-notes.md.
```

### Prototype — paper PnP deliverables

Ask for **playable paper**, lint check, and tools only if needed.

```
Turn ./v0.5/mechanism-skeleton.md into a paper PnP: rulebook-draft, components-sheet (one row per card id), pnp-checklist.
2–4p, 30 min, index-card prototype — no art. Run lint/checklist before finishing. Match micro-scavenger field granularity.
```

```
components-sheet.csv is ready in ./my-game/data/. Walk me through nanDECK steps to export poker-size card PNGs; don't suggest TTS until paper playtest passes.
```

### Continue, restructure, or kill

After **3+ playtests**, ask for the explicit gate.

```
We've completed PT-001 through PT-004 (./playtests/). Core loop is learnable but average fun was 2.8/5 twice in a row; feedback cites "same thing every turn."
Run kill-criteria.md with me: Continue, Restructure, or Pause/Kill? Cite evidence. Update design-state and decision.md if we restructure.
```

### Mechanism lookup — narrow questions

Single topic or code → agent loads one chapter, not the whole skill.

```
Explain WPL-03 vs soft blocking (bumping) for a 2p game — trade-offs only, no new project files.
```

```
When should I use input vs output randomness for a push-your-luck resource game? Keep it to cheatsheet + Ch 6 level.
```

### Mixed requests (design + PnP + balance)

State priority or let the skill's cheatsheet order apply: **diagnose/balance before prototype** if something is broken.

```
New 2p card game, 15 min — full pipeline: concept through paper PnP in ./duel-scavenge/.
If you see dominant strategy risk in the skeleton, run balance-spreadsheet on the 12-card core set before finalizing rulebook.
```

### Prompt checklist (copy before sending)

- [ ] Players / time / audience / target feel
- [ ] New project vs continuing (`read design-state first`)
- [ ] Desired outputs (which templates, which folder)
- [ ] For iteration: symptom + evidence, not "make it better"
- [ ] For tests: one variable + success metric
- [ ] Optional: `@file` references to your repo artifacts

## What you get

| Path | Role |
|------|------|
| [`SKILL.md`](SKILL.md) | Entrypoint: modes, invariants, indexes, default outputs |
| [`templates/design-state.md`](templates/design-state.md) | Single source of truth for project decisions |
| [`reasoning/`](reasoning/) | Design reasoning, decision matrix, hypothesis rules |
| [`diagnostics/`](diagnostics/) | Symptom guides for 8 core failure modes |
| [`experiments/`](experiments/) | Experiment framework |
| [`kill-criteria.md`](kill-criteria.md) | Continue / Restructure / Pause-or-Kill gate |
| [`lint/`](lint/) | Design lint BG001–BG014 + output checklist |
| [`balance/`](balance/) | Balance model, value budget (links to probability doc) |
| [`theme-and-experience.md`](theme-and-experience.md) | MDA depth, theme-mechanism fit, emotion curve |
| [`tools/`](tools/) | nanDECK and TTS shortest-path guides |
| [`chapters/`](chapters/) | 13 mechanism distillations (*Building Blocks* categories) |
| [`patterns.md`](patterns.md) | High-leverage mechanism patterns |
| [`cheatsheet.md`](cheatsheet.md) | Decision rules + symptom routing + mixed-demand priority |
| [`workflow.md`](workflow.md) | Milestones 0–5 with regression allowed |
| [`playtesting.md`](playtesting.md) | Five playtest frameworks + experiment tie-in |
| [`probability-and-balance.md`](probability-and-balance.md) | Failure modes, McDie, dice intuition |
| [`templates/`](templates/) | Project copy-out files |
| [`templates/examples/micro-scavenger/`](templates/examples/micro-scavenger/) | **Format reference** example game |
| [`eval/benchmark-prompts.md`](eval/benchmark-prompts.md) | Manual skill evaluation cases (Create through Lint) |
| [`CHANGELOG.md`](CHANGELOG.md) | Semver release history |

### Progressive disclosure

Agents should load the **smallest** file that answers the question (metadata → `SKILL.md` → one companion/chapter). Do not bulk-load all chapters for a narrow question.

### Default outputs (not prose-only)

When you ask to design or prototype a game, the agent should **write project files** from `templates/`, maintain **`design-state.md`**, and match output granularity to **`templates/examples/micro-scavenger/`**.

Default first playable build: **paper PnP**. TTS / Tabletopia come after the paper loop works unless you specify otherwise.

## Repository layout

```text
board-game-design/
├── SKILL.md
├── CHANGELOG.md
├── README.md
├── kill-criteria.md
├── theme-and-experience.md
├── workflow.md
├── cheatsheet.md
├── playtesting.md
├── probability-and-balance.md
├── reasoning/
├── diagnostics/
├── experiments/
├── balance/
├── lint/
├── tools/
├── eval/
├── chapters/                # ch01–ch13
├── templates/
│   └── examples/micro-scavenger/
├── references/
└── …
```

## Attribution & scope

Mechanism frameworks, codes (e.g. `WPL-01`, `CAR-05`), and trade-off language are **synthesized** from:

> Geoffrey Engelstein & Isaac Shalev, *Building Blocks of Tabletop Game Design*, CRC Press.

Chapter files are **not** a verbatim copy of the book and are **not** a substitute for purchasing it.

## License

Code and original skill text in this repository are released under the [MIT License](LICENSE).

## Contributing

- Keep [`SKILL.md`](SKILL.md) lean (<500 lines); put deep material in companions.
- Prefer decision rules, state, and experiments over encyclopedic mechanism dumps.
- Update [`CHANGELOG.md`](CHANGELOG.md) on each release.

## Links

- [Agent Skills specification](https://agentskills.io/specification)
- [Anthropic: Equipping agents with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
