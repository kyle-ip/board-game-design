# Board Game Design — Maintainer Bibliography

**For skill maintainers only.** Agents should load [`external-resources.md`](../external-resources.md) when users ask for tools, publishing, or further reading — **do not bulk-load this file** during normal design sessions.

Primary mechanism content is synthesized in `chapters/` from Engelstein & Shalev, *Building Blocks of Tabletop Game Design* ([Routledge](https://www.routledge.com/Building-Blocks-of-Tabletop-Game-Design-An-Encyclopedia-of-Mechanisms/Engelstein-Shalev/p/book/9781032985107)). This index tracks **external URLs** and book titles for maintenance.

## Legend

| Field | Meaning |
|---|---|
| **tier: core** | Distilled into a companion file; high authority |
| **tier: optional** | Useful reference; not loaded by agents by default |
| **tier: deprecated** | Removed from agent-facing lists; kept for history or do not use |
| **used-by** | Companion file(s) that embed or route to this source |

---

## 1. Core — Used by Skill Companions

### MDA: A Formal Approach to Game Design and Game Research
- URL: https://www.cs.northwestern.edu/~hunicke/MDA.pdf
- tier: **core** | used-by: `SKILL.md`, `theme-and-experience.md`, `concept-brief.md`

### How to Design a Board Game — Chitmunk (8-step, experience-first)
- URL: https://chitmunk.com/blog/how-to-design-a-board-game
- tier: **core** | used-by: `workflow.md` Milestones 0, 2

### How to Design a Board Game — Board Game Design Lab (MVP)
- URL: https://boardgamedesignlab.com/how-to-design-a-board-game/
- tier: **core** | used-by: `workflow.md` Milestone 1

### Board Game Design: Step-by-Step Guide — 8ration (art last)
- URL: https://www.8ration.com/blogs/board-game-design-guide/
- tier: **core** | used-by: `workflow.md` Milestone 4, `playtesting.md` Framework 5

### Top Playtesting Frameworks — minifiniti (Four Fs, Scattershot, Good/Bad/Meh)
- URL: https://minifiniti.com/blogs/game-talk/playtesting-frameworks-tabletop-games
- tier: **core** | used-by: `playtesting.md` Frameworks 1–3

### Playtesting — Mark Rosewater (Making Magic)
- URL: https://magic.wizards.com/en/news/making-magic/playtesting
- tier: **core** | used-by: `playtesting.md` Framework 4

### MTG Wiki — Set Design (four stages for large card sets)
- URL: https://mtg.wiki/page/Set_design
- tier: **core** | used-by: `workflow.md` (≥100 cards)

### McDie — visual Monte Carlo dice simulator (Engelstein)
- URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC8134935/
- tier: **core** | used-by: `probability-and-balance.md`

### GameTek Newsletter (Engelstein)
- URL: https://gametek.substack.com/
- tier: **core** | used-by: `probability-and-balance.md`

### Panda Graphic Design Guidebook V.4
- URL: https://pandagm.com/wp-content/uploads/2022/10/PandaGM-GraphicDesignGuidebook-V4-0922.pdf
- tier: **core** | used-by: `print-specs.md`

### The Game Crafter Design Guidebook 2023
- URL: https://s3.amazonaws.com/helpscout.net/docs/assets/561c5a919033600a7a36d5dc/attachments/643d87297133de139103ebc2/Design-Guide---2023.pdf
- tier: **core** | used-by: `print-specs.md`

### TGC — Designing for 3D Printing
- URL: https://help.thegamecrafter.com/article/509-designing-for-3d-printing
- tier: **core** | used-by: `print-specs.md`

### Dobeta Games — Print File Requirements (survey)
- URL: https://www.dobetagames.com/the-complete-guide-to-board-game-printing-file-requirements/
- tier: **core** | used-by: `print-specs.md`

### pnp-howto (open-source PnP prep)
- URL: https://github.com/ernierasta/pnp-howto
- tier: **core** | used-by: `print-specs.md`

### NanDeck
- URL: https://www.nand.it/nandeck/
- tier: **core** | used-by: `tools/nanDECK-guide.md`, `probability-and-balance.md`

### Component.Studio
- URL: https://component.studio/
- tier: **core** | used-by: `probability-and-balance.md`, `tools/nanDECK-guide.md`

### Tabletop Simulator (digital playtest, after paper)
- URL: https://www.tabletopsimulator.com/
- tier: **core** | used-by: `tools/TTS-guide.md`

---

## 2. Core — Added v2.2 (workflow / playtest alignment)

### TTGDA — Tips for New Game Designers
- URL: https://www.ttgda.org/get-assistance/newpage
- tier: **core** | used-by: `workflow.md`, `external-resources.md`
- Value: Official stage guide; co-founded by Engelstein. Complements skill milestones.

### Break My Game — Designer Resources
- URL: https://www.breakmygame.com/designer-resources
- tier: **core** | used-by: `playtesting.md`, `external-resources.md`
- Value: TTGDA-endorsed; Tabletop Game Design Guidebook, virtual/PnP playtest log templates.

### TTGDA Blog (Tabletop Designers Association)
- URL: https://blog.tabletopdesign.org/
- tier: **core** | used-by: `external-resources.md`
- Value: Official association articles on approachability, teaching, design process.

### Mark Rosewater — Making Magic (archive)
- URL: https://magic.wizards.com/en/news/making-magic
- tier: **core** | used-by: `playtesting.md`, card-game depth
- Value: Card/TCG design philosophy; 20+ year archive.

---

## 3. Optional — Agent May See via external-resources.md

### Ludology Podcast
- URL: https://ludology.libsyn.com/webpage
- tier: optional | used-by: —
- Value: Design theory; Engelstein co-founded.

### Ludology Game Design Checklist (PDF)
- URL: https://static1.squarespace.com/static/55fc10b1e4b0347ac88a7992/t/570149b01bbee0d8252e5877/1459702192564/Ludology+Game+Design+Checklist.pdf
- tier: optional | used-by: —
- Value: Self-review checklist; overlaps `lint/checklist.md`.

### Skeleton Code Machine
- URL: https://www.skeletoncodemachine.com/
- tier: optional | used-by: —
- Value: Mechanism case studies.

### Daniel Solis — Graphic Design for Board Games (blog)
- URL: https://danielsolisblog.blogspot.com/
- tier: optional | used-by: —
- Value: Icon clarity; see also CRC *Graphic Design for Board Games* (2024).

### Stonemaier Games Blog — Jamey Stegmaier
- URL: https://stonemaiergames.com/e-newsletter/blog/
- tier: optional | used-by: —
- Value: Publishing / crowdfunding perspective.

### LaunchBoom — 11 Step Guide (crowdfunding)
- URL: https://www.launchboom.com/crowdfunding-tips/the-11-step-guide-for-how-to-create-a-board-game/
- tier: optional | used-by: `workflow.md` Milestone 5 (publish only)
- Value: Kickstarter / fulfillment; marketing-adjacent.

### Board Game Design Lab (YouTube)
- URL: https://www.youtube.com/@BoardGameDesignLab
- tier: optional | used-by: —

### Decision Space Podcast
- URL: https://www.decisionspacepodcast.com/
- tier: optional | used-by: —

### We Got Played (Isaac Shalev — Building Blocks co-author)
- URL: https://wegotplayed.com/
- tier: optional | used-by: —
- Value: Design process podcast.

### Playtesting Best Practices (Chris Backe, CRC Press 2025)
- URL: https://www.routledge.com/Playtesting-Best-Practices-Real-World-and-Online/Backe/p/book/9781032787892
- tier: optional | used-by: —
- Value: Book; aligns with skill experiment framework. Cite only; do not load full text.

### Tabletopia
- URL: https://tabletopia.com/
- tier: optional | used-by: —
- Value: Digital demo; skill default is paper-first.

### Game-icons.net (CC BY icons)
- URL: https://game-icons.net/
- tier: optional | used-by: `templates/pnp-checklist.md` (icon clarity)

---

## 4. Communities & Directories

### TTGDA — Blogs and Videos (meta-directory)
- URL: https://www.ttgda.org/blogs-and-videos
- tier: **core** | used-by: `external-resources.md`
- Value: Revisit first when updating this index.

### Cardboard Edison Compendium
- URL: https://cardboardedison.com/directoryinfo
- tier: optional | used-by: `external-resources.md`

### BoardGameGeek
- URL: https://boardgamegeek.com/
- tier: **core** | used-by: `external-resources.md` (comparable games, comps)

### Inspiration to Publication — The Steps (Cormier & Lim)
- URL: https://inspirationtopublication.wordpress.com/the-steps-for-board-games/
- tier: optional | used-by: —

---

## 5. Classic Books (bibliography — no free URLs)

Purchase or library; skill content is synthesized in `chapters/`, not verbatim.

| Title | Authors | Notes |
|---|---|---|
| Building Blocks of Tabletop Game Design | Engelstein & Shalev | Primary mechanism source for this skill |
| GameTek | Engelstein | Math/science companion |
| Achievement Relocked | Engelstein | Loss aversion — cited in `probability-and-balance.md` |
| The Art of Game Design (Lenses) | Schell | Self-review lenses |
| Theory of Fun | Koster | Fun diagnosis |
| Rules of Play | Salen & Zimmerman | Meaningful choice |
| Graphic Design for Board Games | Daniel Solis (CRC 2024) | Icon / layout |
| Thematic Integration in Board Game Design | Sarah Shipp (CRC 2024) | Theme-mechanism fit |

---

## 6. Academic Optional (not agent-facing)

### A Vocabulary of Board Game Dynamics (Kritz & Xexéo, 2024)
- URL: https://arxiv.org/html/2403.10267
- tier: optional | used-by: —
- Value: MDA Dynamics vocabulary extension; not synthesized into skill.

---

## 7. Deprecated — Do Not Add to external-resources.md

Removed in v2.2.0 (redundant, paywalled, unstable, or misleading):

| Former entry | Reason |
|---|---|
| BloomWiki MDA | Tertiary wiki; MDA PDF is primary |
| ResearchGate MTG close reading | Login wall / unstable |
| Taylor & Francis Uncertainty chapter URL | Paywall; see `chapters/ch06-uncertainty.md` |
| boardssey.com design guide blog | Redundant with Chitmunk/BGL |
| Instructables 7-step | Redundant beginner content |
| indienova/qq Dream Teapot repost | Secondary news; weak primary source |
| bg-px, shippboardgames, thedarkimp, daniel.games blogs | Unsynthesized link farm |
| Local `building blocks.pdf` / `book-to-skill/` paths | Not in public repo |
| Shapeways | Service shut down |
| GDC Vault | Mostly paywalled; low agent value |
| Board Game Arena, Roll20 | Out of scope (skill is paper-first) |

---

## Maintainer Checklist

1. New **core** URL → distill into a companion file, add `used-by`, add one line to `external-resources.md`.
2. Broken link → check TTGDA resources page or BGG designer forums.
3. Do not grow this file to replace `chapters/` — mechanism knowledge stays synthesized.

*Last updated: 2026-08-24 (v2.2.0 resource audit)*
