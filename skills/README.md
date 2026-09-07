# Companion skills (`skills/`)

Each subdirectory is a **standalone Agent Skill** with its own `name` + `description`. Cursor, Codex, Claude Code, and other Agent Skills hosts can:

1. **Auto-invoke** the matching companion when the user request fits its description
2. **Manually select** it from the host skill / slash menu (hosts often show `/bgd-*` as UI sugar — slash is optional, not required)

Hub skill: `board-game-design` (package root `SKILL.md`) — overview, modes, indexes, routing.

| Skill `name` | Focus |
|---|---|
| `bgd-create` | Create mode |
| `bgd-diagnose` | Diagnose mode |
| `bgd-experiment` | Experiment mode |
| `bgd-simulate` | Simulate mode |
| `bgd-balance` | Balance mode |
| `bgd-prototype` | Prototype mode |
| `bgd-assets` | Free art / digital tabletops |
| `bgd-export` | Card export pipeline |
| `bgd-tts` | Tabletop Simulator |
| `bgd-lint` | Output lint |
| `bgd-kill` | Continue / kill gate |
| `bgd-genre` | Genre profile |
| `bgd-playtest` | Playtest frameworks |
| `bgd-print` | Print specs |
| `bgd-workflow` | Workflow milestones |
| `bgd-cheatsheet` | Decision cheatsheet |
| `bgd-glossary` | Term lookup |
| `bgd-resources` | External links by Mode |

Paths inside each companion are relative to package root `board-game-design/` (parent of `skills/`).

**Install note:** clone or copy the whole `board-game-design` package. Hosts that recursively discover `**/SKILL.md` will register the hub and these companions. If a host only loads the package root, the hub `SKILL.md` still routes to the same files.
