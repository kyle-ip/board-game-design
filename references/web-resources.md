# Board Game Design & Development — Curated Resource Index

A curated web resource list assembled for building the "Board Game Designer" skill. Each entry includes language, source, and notes on how it can be used by the skill. Companion local materials:
- `building blocks of tabletop game design.pdf` — Engelstein & Shalev, *Building Blocks of Tabletop Game Design*, 2nd ed. (primary mechanism reference)
- `book-to-skill/` — toolchain for turning books/PDFs into skills

---

## Contents

1. [Core Theoretical Frameworks](#1-core-theoretical-frameworks)
2. [Classic Books & Textbooks](#2-classic-books--textbooks)
3. [Mechanism Encyclopedias & Design Patterns](#3-mechanism-encyclopedias--design-patterns)
4. [Probability, Math & Balance](#4-probability-math--balance)
5. [Prototyping & Playtesting](#5-prototyping--playtesting)
6. [Design & Development Workflow Guides](#6-design--development-workflow-guides)
7. [Publishing, Manufacturing & Print File Specs](#7-publishing-manufacturing--print-file-specs)
8. [Expert Columns & Blogs](#8-expert-columns--blogs)
9. [Podcasts & Video Channels](#9-podcasts--video-channels)
10. [Chinese-Language Resources](#10-chinese-language-resources)
11. [Tools & Platforms](#11-tools--platforms)
12. [Communities & Meta-Directories](#12-communities--meta-directories)

---

## 1. Core Theoretical Frameworks

### MDA: A Formal Approach to Game Design and Game Research
- Source: https://www.cs.northwestern.edu/~hunicke/MDA.pdf (Hunicke, LeBlanc, Zubek, GDC 2004)
- Language: English
- Value: The foundational formal framework for game design. Mechanics → Dynamics → Aesthetics. Recommended as the backbone for design analysis and player-experience reverse-engineering inside the skill.

### A Vocabulary of Board Game Dynamics
- Source: https://arxiv.org/html/2403.10267 (Kritz & Xexéo, 2024)
- Language: English
- Value: Fills the gap in MDA where Dynamics lacked a systematic vocabulary; provides a taxonomic set of dynamic concepts. Useful as a lookup table when mapping mechanics to experiences.

### Game Mechanics, the Core Loop, and the MDA Framework
- Source: https://bloomwiki.org/index.php/Game_Mechanics,_the_Core_Loop,_and_the_MDA_Framework
- Language: English
- Value: Walks through MDA, core loops, feedback loops, flow, and emergence across six Bloom taxonomy levels (Remembering → Creating). Good template for the skill's educational output.

### MDA: The Game Design Trilogy (Chinese intro)
- Source: https://blog.csdn.net/qq526978749/article/details/132668024
- Language: Chinese
- Value: A Chinese-language introduction to MDA for terminology consistency when the skill addresses Chinese-speaking users.

---

## 2. Classic Books & Textbooks

> Canonical academic/industry texts. The skill can cite these for depth and, where PDFs are available, run them through the book-to-skill toolchain to produce searchable text.

### The Art of Game Design: A Book of Lenses — Jesse Schell
- "100+ lenses" framework, each a set of probing questions. Well suited for extracting a design self-review checklist in the skill.

### Theory of Fun for Game Design — Raph Koster
- Explains "why games are fun" from a cognitive-science perspective. Useful for the skill's "fun diagnosis" step.

### Rules of Play: Game Design Fundamentals — Katie Salen & Eric Zimmerman
- Academic, systematic design textbook. Defines key concepts like "meaningful choice."

### Game Design Workshop: A Playcentric Approach — Tracy Fullerton
- Playcentric methodology with the Formal/Dramatic/Dynamic elements framework. 4th ed. (2024).

### Challenges for Game Designers — Brenda Brathwaite & Ian Schreiber
- A series of design exercises (karate-kata style) covering balance, loops, etc. The skill can generate similar exercise prompts.

### GameTek: The Math and Science of Gaming — Geoff Engelstein
- Distilled math/science/psychology of tabletop games. Companion to the Dice Tower segment of the same name.

### Achievement Relocked: Loss Aversion and Game Design — Geoff Engelstein
- Application of behavioral economics' "loss aversion" to game design.

### Kobold Guide to Board Game Design — Selinker, Howell, et al.
- Multi-author collection by veteran designers; industry perspective.

### Dice Games Properly Explained — Reiner Knizia
- Classic reference on dice mechanisms and probability.

### Characteristics of Games — George Skaff Elias et al. (MIT Press)
- Academic reference that abstracts and analyzes game properties.

---

## 3. Mechanism Encyclopedias & Design Patterns

### Building Blocks of Tabletop Game Design, 2nd Edition — Engelstein & Shalev
- Local PDF available. CRC Press. An encyclopedia organized by mechanism category (hundreds of patterns). This should be the primary index for the skill's "mechanism lookup / selection" feature.

### Uncertainty (book chapter) — Engelstein & Shalev
- Source: https://www.taylorfrancis.com/chapters/mono/10.1201/9781003179184-6/uncertainty-geoffrey-engelstein-isaac-shalev
- Language: English
- Value: The full "Uncertainty" chapter from *Building Blocks*, ideal as a deep dive on randomness design.

### MTG Wiki — Set Design
- Source: https://mtg.wiki/page/Set_design
- Language: English
- Value: Magic: The Gathering's modern design process: Exploratory Design → Vision Design → Set Design → Play Design. A staged division of labor worth borrowing for large card/TCG projects.

### A Close Reading of Magic: The Gathering's Core Mechanics
- Source: https://www.researchgate.net/publication/333119003_A_Close_Reading_of_Magic_The_Gathering%27s_Core_Mechanics
- Language: English
- Value: Uses "close reading" to identify three core TCG/CCG mechanics: thinking ahead, deck-building, card collecting. A worked example for "card game mechanism deconstruction."

---

## 4. Probability, Math & Balance

### McDie: A visual probability analysis tool for board game designers
- Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC8134935/ (Geoff Engelstein, Patterns 2021)
- Language: English
- Value: A node-based Monte Carlo dice simulator — free, visual, no coding required. The skill can recommend this directly to users during probability tuning.

### GameTek Newsletter (Substack)
- Source: https://gametek.substack.com/
- Language: English
- Value: Engelstein's short essays on tabletop math/science/psychology. Good source for "tip-of-the-day" snippets in the skill.

### Ludology Game Design Checklist (PDF)
- Source: https://static1.squarespace.com/static/55fc10b1e4b0347ac88a7992/t/570149b01bbee0d8252e5877/1459702192564/Ludology+Game+Design+Checklist.pdf
- Language: English
- Value: Design self-review checklist. Can be used as the skill's review template output.

---

## 5. Prototyping & Playtesting

### Top Playtesting Frameworks for Tabletop Games
- Source: https://minifiniti.com/blogs/game-talk/playtesting-frameworks-tabletop-games
- Language: English
- Value: Comparative table of five frameworks: Four Fs (Facts/Feelings/Findings/Future), Scattershot, Paper Prototyping, Good/Bad/Meh, community-based testing. The skill can directly generate playtest scripts from these.

### How to Design a Board Game — Board Game Design Lab
- Source: https://boardgamedesignlab.com/how-to-design-a-board-game/
- Language: English (Gabe Barrett)
- Value: End-to-end beginner guide (concept → prototype → playtest), with an MVP mindset. Useful as the skill's main workflow reference.

### Playtesting — Mark Rosewater (Making Magic)
- Source: https://magic.wizards.com/en/news/making-magic/playtesting
- Language: English
- Value: Magic R&D's four-stage playtest methodology (Exploratory/Vision/Set/Play Design), including the "good/bad/needs-work" three-bucket system. A playtest governance template for large projects.

### The Complete Guide to Board Game Design: From Concept to Tabletop
- Source: https://boardssey.com/blog/the-complete-guide-to-board-game-design-from-concept-to-tabletop/
- Language: English
- Value: Covers mechanical balance, mathematical modeling, component selection, and publishing paths. Clear structure — a good skeleton for the skill's chapters.

---

## 6. Design & Development Workflow Guides

### How to Design a Board Game: From Idea to Prototype — Chitmunk
- Source: https://chitmunk.com/blog/how-to-design-a-board-game
- Language: English
- Value: An 8-step process that stresses "experience before mechanics" and structured card data in spreadsheets. Especially useful when the skill handles card-game projects.

### Board Game Design: A Complete Step-by-Step Guide — 8ration
- Source: https://www.8ration.com/blogs/board-game-design-guide/
- Language: English
- Value: 9-step method, explicit "art last" principle, with market sizing data and companion-app trade-offs. Useful for staging the skill's workflow output.

### The 11 Step Guide on How to Create a Board Game — LaunchBoom
- Source: https://www.launchboom.com/crowdfunding-tips/the-11-step-guide-for-how-to-create-a-board-game/
- Language: English
- Value: Full 11 steps from concept to crowdfunding to fulfillment, with a comparison of Kickstarter/BackerKit/Gamefound. Useful when users ask "I want to publish."

### How to Design "Board" Games — Instructables
- Source: https://www.instructables.com/How-To-Design-Board-Games/
- Language: English
- Value: 7-step minimalist process (Concept → Goal → Path → Flesh out → Prototype → Playtest → Polish). Good for the skill's quick onboarding of new users.

---

## 7. Publishing, Manufacturing & Print File Specs

### Panda Graphic Design Guidebook V.4
- Source: https://pandagm.com/wp-content/uploads/2022/10/PandaGM-GraphicDesignGuidebook-V4-0922.pdf
- Language: English
- Value: Official specs from Panda GM, the industry-standard mass-production manufacturer: CMYK, 300 ppi, 3 mm bleed and safe zone, FOGRA39 color profile, one file per component. The preferred spec when the skill handles "ready for mass printing."

### The Game Crafter Design Guidebook 2023
- Source: https://s3.amazonaws.com/helpscout.net/docs/assets/561c5a919033600a7a36d5dc/attachments/643d87297133de139103ebc2/Design-Guide---2023.pdf
- Language: English
- Value: Specs from The Game Crafter (TGC), the leading print-on-demand vendor: PNG uploads, template system, drift mitigation, 1/8" bleed. Suits small-batch / indie-designer paths.

### The Complete Guide to Board Game Printing File Requirements — Dobeta Games
- Source: https://www.dobetagames.com/the-complete-guide-to-board-game-printing-file-requirements/
- Language: English
- Value: A horizontal survey of print file specs: bleed, safe zone, CMYK, black overprint, line weights, and component-specific rules (cards, boards, punchboards, boxes). A good "print-spec overview" for the skill.

### pnp-howto — Board game: how to prepare files for printing
- Source: https://github.com/ernierasta/pnp-howto
- Language: English (author: Leszek Cimała)
- Value: Open-source practical guide covering crop marks, bleed, duplex printing, gutter fold, A4 vs US Letter, and more. Suits print-and-play scenarios.

### Designing for 3D Printing — The Game Crafter
- Source: https://help.thegamecrafter.com/article/509-designing-for-3d-printing
- Language: English
- Value: Engineering specs for 3D-printed components: 0.4 mm nozzle, 0.12 mm layer height, overhang angle, footprint area, 25 mm / 15 mm base sizes. Use when the skill handles custom component design.

---

## 8. Expert Columns & Blogs

### Mark Rosewater — Making Magic (Wizards of the Coast)
- Source: https://magic.wizards.com/en/news/making-magic
- Language: English
- Value: The head designer of Magic's column running for 20+ years, covering design philosophy, card iteration, player psychology, and playtest process. The gold-standard source for card game / TCG topics. Representative pieces:
  - Big-Picture Questions, Part 1 — design philosophy Q&A
  - The Design of Mood Swings, Part 2 — a 28-year iteration case study
  - Playtesting — the four-stage playtest methodology

### Stonemaier Games Blog — Jamey Stegmaier
- Source: https://stonemaiergames.com/e-newsletter/blog/
- Language: English
- Value: Successful-publisher perspective covering the full chain: design, crowdfunding, publishing, fulfillment.

### Daniel Solis — Graphic Design for Board Games
- Source: https://danielsolisblog.blogspot.com/
- Language: English
- Value: Focused on tabletop graphic design and icon systems. Use when the skill handles "visual / icon clarity" tasks.

### Think Like a Game Designer — Justin Gary
- Source: https://justingarydesign.substack.com/
- Language: English
- Value: Design-thinking column from the designer of Ascension; free and paid content.

### Skeleton Code Machine
- Source: https://www.skeletoncodemachine.com/
- Language: English
- Value: Weekly deep dives into individual mechanisms across board games and RPGs. A good "mechanism case library" for the skill.

### BG PX — Patrick McNeil
- Source: https://bg-px.com/
- Language: English
- Value: UX-perspective tabletop design blog.

### ShippBoard Games — Sarah Shipp
- Source: https://shippboardgames.blogspot.com/
- Language: English
- Value: Design theory and analysis.

### The Dark Imp — Ellie Dix
- Source: https://www.thedarkimp.com/blog/
- Language: English
- Value: Design notes leaning toward family / educational games.

### Daniel Piechnik — daniel.games
- Source: https://daniel.games/
- Language: English
- Value: Practical experience from the designer of *Radlands*.

---

## 9. Podcasts & Video Channels

### Ludology Podcast
- Source: https://ludology.libsyn.com/webpage
- Language: English
- Value: Biweekly podcast co-founded by Engelstein, focused on tabletop design theory. The most academic option.

### Board Game Design Lab — Gabe Barrett
- Source: https://www.youtube.com/@BoardGameDesignLab
- Language: English
- Value: Designer interviews plus hands-on videos, broad coverage.

### Board Game Blueprint — The Game Crafter
- Source: https://www.youtube.com/@BoardGameBlueprint
- Language: English
- Value: Weekly design videos from a print-on-demand perspective.

### Decision Space Podcast
- Source: https://www.decisionspacepodcast.com/
- Language: English
- Value: Deep analysis focused on "decision space" design.

### Game Design Roundtable
- Source: https://thegamedesignroundtable.com/
- Language: English
- Value: Roundtable discussions among designers.

### GDC Vault
- Source: https://gdcvault.com/
- Language: English
- Value: GDC talk archive (recent paywalled, older free), including tabletop design sessions.

---

## 10. Chinese-Language Resources

### Dream Teapot: A Design Exploration of an Asymmetric Card Battler — indienova
- Source: https://view.inews.qq.com/a/20251017A01IKE00
- Language: Chinese
- Value: An adapted version of a European game-design master's thesis. Uses RtD (Research through Design) to document the full five-stage design of an asymmetric 1v3 card battler: concept design → loop construction → theory/game research → mechanism filling → two iterations. A rare academic-style process example in Chinese; useful when the skill outputs "portfolio / academic-track" workflows.

### BoardGameGeek (BGG)
- Source: https://boardgamegeek.com/
- Language: English (multilingual subforums)
- Value: Global board game database and designer forums. Main entry point for the skill's "comparable game research."

> Note: High-quality native Chinese content on tabletop design is relatively scarce. When translating English sources into Chinese, prefer each game's official or mainstream Chinese name when one exists; otherwise keep the English name.

---

## 11. Tools & Platforms

### Digital Playtest Platforms
- Tabletopia — https://tabletopia.com/ (web-based full-3D tabletop simulator, supports public demos)
- Board Game Arena — https://en.boardgamearena.com/ (online play platform)
- Tabletop Simulator — https://www.tabletopsimulator.com/ (Steam sandbox, most flexible)
- Yucata — https://www.yucata.de/en (async online play)
- Roll20 — https://roll20.net/ (RPG-leaning but usable)

### Component / Card Automation
- Component.Studio — https://component.studio/ (data-driven card/board file generation)
- NanDeck — https://nandeck.com/ (scripted card generation, free)

### Print-on-Demand & Mass Production
- The Game Crafter — https://www.thegamecrafter.com/ (POD, no minimum)
- Panda Game Manufacturing — https://pandagm.com/ (mainstream mass production)
- Board Games Maker — https://www.boardgamesmaker.com/ (small-batch custom)
- MakePlayingCards (MPC) — https://www.makeplayingcards.com/ (cards only)
- Print & Play Productions — http://printplaygames.com/
- Shapeways (3D printing; shut down — look for alternatives)

### Components & Consumables
- Chessex (dice) — http://www.chessex.com/
- MeepleSource — http://www.meeplesource.com/
- Litko — http://www.litko.net/
- Spielmaterial — http://www.spielematerial.de/en/

### Prototyping & Design Aids
- Boardssey (includes Idea Generator, Theme Matcher, Variables Distribution) — https://boardssey.com/
- Game-icons.net — https://game-icons.net/ (CCBY icon library)
- Google Patents — https://patents.google.com/ (mechanism patent search)

---

## 12. Communities & Meta-Directories

### Tabletop Game Designers Association (TTGDA) — Resources
- Source: https://www.ttgda.org/blogs-and-videos
- Language: English
- Value: The most authoritative directory in this space — many entries in sections 8–9 originated from this curated list. Revisit this page first when maintaining "resource updates" in the skill.

### Cardboard Edison Compendium
- Source: https://cardboardedison.com/directoryinfo
- Language: English
- Value: Directory of designer articles and resources.

### BoardGameGeek (BGG) — Designer Forums
- Source: https://boardgamegeek.com/
- Language: English
- Value: Game database, reviews, designer subforums. Main entry point for "comparable game research."

### Board Game Design Course — Joe Slack
- Source: https://boardgamedesigncourse.com/bgdc-home/blog/
- Language: English
- Value: Free blog + podcast, with paid courses.

### The Steps (design steps outline) — Jay Cormier & Sen-Foong Lim
- Source: https://inspirationtopublication.wordpress.com/the-steps-for-board-games/
- Language: English
- Value: A design-step outline compiled by veteran designers.

---

## Suggested Usage for Skill Builders

1. **Mechanism lookup**: Prefer the local `building blocks of tabletop game design.pdf`; slice by mechanism category and feed to the LLM as needed.
2. **Workflow output**: Use [Section 6, Chitmunk's 8 steps] as the main skeleton; layer in [MTG Wiki's four stages] for complex projects.
3. **Playtest scripts**: Directly reuse [Section 5, Four Fs] and other frameworks to generate structured questionnaires.
4. **Probability tuning**: Recommend [McDie] to users; the skill itself can inline simple Monte Carlo pseudocode.
5. **Print specs**: Use [Section 7, Panda/TGC] as hard specs — POD via TGC, mass production via Panda.
6. **Card-game specialty**: [Section 8, Mark Rosewater] + [Section 3, MTG Wiki Set Design] are the gold standard.
7. **Chinese context**: Prefer official/mainstream Chinese game names when they exist; otherwise keep English names.
8. **book-to-skill pipeline**: This index can serve as a "supplementary corpus list" for that toolchain, fed in by topic batches.

---

*Index compiled on 2026-08-24. If links break, revisit the TTGDA resources page or BoardGameGeek designer forums for the latest entry points.*
