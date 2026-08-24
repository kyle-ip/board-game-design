# board-game-design

An [Agent Skill](https://agentskills.io/specification) for designing tabletop game **mechanisms** and shipping a **paper print-and-play prototype**. Compatible with Cursor, Claude Code, and other runtimes that load `SKILL.md` skills.

Pipeline this skill teaches agents to follow:

**concept → mechanism skeleton → paper PnP → playtest / balance → (optional) POD or digital**

> Repo-level `README.md` is for humans (install, structure, attribution). Agent instructions live in [`SKILL.md`](SKILL.md) and progressive-disclosure companions — per [Anthropic skill authoring guidance](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills).

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
- Write a concept brief or mechanism skeleton
- Prepare playtests
- Build a print-and-play prototype

Example prompts:

- “Design a 2–4 player, 45-minute worker-placement game about expeditions.”
- “Diagnose snowball in my economy and suggest catch-up options.”
- “Turn this pitch into a paper PnP: rulebook, component sheet, checklist.”

## What you get

| Path | Role |
|------|------|
| [`SKILL.md`](SKILL.md) | Entrypoint: indexes, mental models, **default project outputs** |
| [`chapters/`](chapters/) | 13 mechanism distillations (*Building Blocks* categories) |
| [`patterns.md`](patterns.md) | High-leverage mechanism patterns (selected codes) |
| [`cheatsheet.md`](cheatsheet.md) | Decision rules + symptom → file routing |
| [`glossary.md`](glossary.md) | Term definitions |
| [`workflow.md`](workflow.md) | Stages 0–5 with required template writes |
| [`playtesting.md`](playtesting.md) | Five playtest frameworks |
| [`probability-and-balance.md`](probability-and-balance.md) | Failure modes, dice intuition, McDie rule |
| [`print-specs.md`](print-specs.md) | POD vs mass-production specs |
| [`templates/`](templates/) | Copy-out files for real projects (concept → PnP) |
| [`external-resources.md`](external-resources.md) | Condensed links |
| [`references/web-resources.md`](references/web-resources.md) | Fuller curated resource index |

### Progressive disclosure

Agents should load the **smallest** file that answers the question (metadata → `SKILL.md` → one companion/chapter). Do not bulk-load all chapters for a narrow question.

### Default outputs (not prose-only)

When you ask to design or prototype a game, the agent should **write project files** from `templates/` (concept brief, mechanism skeleton, rulebook draft, components sheet, PnP checklist, playtest log, balance notes) into your game project directory.

Default first playable build: **paper PnP**. TTS / Tabletopia / web demos come after the paper loop works unless you specify otherwise.

## Repository layout

```text
board-game-design/
├── SKILL.md                 # required skill entrypoint
├── README.md                # this file (humans / GitHub)
├── LICENSE
├── chapters/                # ch01–ch13 mechanism references
├── templates/               # project copy-out templates
├── references/              # deeper resource index
├── cheatsheet.md
├── patterns.md
├── glossary.md
├── workflow.md
├── playtesting.md
├── probability-and-balance.md
├── print-specs.md
└── external-resources.md
```

This matches the Agent Skills shape: required `SKILL.md`, optional references/assets (here: chapters, templates, companions).

## Attribution & scope

Mechanism frameworks, codes (e.g. `WPL-01`, `CAR-05`), and trade-off language are **synthesized** from:

> Geoffrey Engelstein & Isaac Shalev, *Building Blocks of Tabletop Game Design*, CRC Press.

Chapter files are **not** a verbatim copy of the book and are **not** a substitute for purchasing it. Workflow, playtesting, print, and template layers also draw on publicly linked designer resources (see `external-resources.md` / `references/web-resources.md`).

## License

Code and original skill text in this repository are released under the [MIT License](LICENSE).

Book titles, game names, and third-party links remain the property of their respective owners. Cite the original sources when you publish commercial design work derived from those ideas.

## Contributing

- Keep [`SKILL.md`](SKILL.md) lean; put deep material in companions and link it with clear “when to load” guidance.
- Prefer decision rules and templates over encyclopedic dumps.
- When adding mechanism codes, update the Chapter Index ranges and `patterns.md` coverage notes together.
- Do not commit vendor print binaries, large PDFs, or personal playtest recordings into the skill package.

## Links

- [Agent Skills specification](https://agentskills.io/specification)
- [Anthropic: Equipping agents with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
- [Anthropic skills examples](https://github.com/anthropics/skills)
