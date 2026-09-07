# Slash commands (`/bgd-*`)

Each subdirectory is a thin, **explicit-only** skill (`disable-model-invocation: true`).
Invoke as `/<name> <description>` — text after the command is the task brief.

Package hub (auto + explicit): `/board-game-design`.

| Command | Focus |
|---|---|
| `/bgd-create` | Create mode |
| `/bgd-diagnose` | Diagnose mode |
| `/bgd-experiment` | Experiment mode |
| `/bgd-simulate` | Simulate mode |
| `/bgd-balance` | Balance mode |
| `/bgd-prototype` | Prototype mode |
| `/bgd-assets` | Free art / digital tabletops |
| `/bgd-export` | Card export pipeline |
| `/bgd-tts` | Tabletop Simulator |
| `/bgd-lint` | Output lint |
| `/bgd-kill` | Continue / kill gate |
| `/bgd-genre` | Genre profile |
| `/bgd-playtest` | Playtest frameworks |
| `/bgd-print` | Print specs |
| `/bgd-workflow` | Workflow milestones |
| `/bgd-cheatsheet` | Decision cheatsheet |
| `/bgd-glossary` | Term lookup |
| `/bgd-resources` | External links by Mode |

Paths inside each slash skill are relative to package root `board-game-design/` (parent of `slash/`).
Hub table: package `SKILL.md` → **Slash commands**.
