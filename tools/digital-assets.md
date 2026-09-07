# Digital Assets (Free / Open)

Agent-facing catalog for **art, icons, fonts, audio, and digital tabletops** when prototyping or digitizing a tabletop game.

**Not a substitute for** `prototype/selection.md` fidelity choice or paper-first invariants. Prefer the cheapest valid test; use this file when the user needs concrete asset sources.

## Load When

Load this file in **Prototype** mode (optional), or when companion skill **`bgd-assets`** is active, when the user asks about:

- Free / CC0 art, sprites, meeples, tokens, dice, icons
- Fonts (especially CJK), SFX / music for digital builds
- TTS / Tabletopia / Screentop / PlayingCards.io / browser digital prototype
- Card face packs, board textures, table renders
- “Where can I get assets for…” / digitalization art pipeline

**Do not** load in Create / Diagnose / Simulate / Balance unless the user explicitly asks for art sources.

### How to recommend

1. Identify the **need** (row in Quick pick).
2. Suggest **2–4** resources max (prefer CC0 / clear commercial license).
3. State license caveats in one line (CC-BY attribution, personal-use scans, etc.).
4. **Do not** dump the full catalog unless the user asks for a survey.

Also use: `tools/TTS-guide.md`, `tools/nanDECK-guide.md`, `tools/export-pipeline.md`, `external-resources.md` § Prototype.

---

## Quick Pick by Need

| Need | Start here |
|---|---|
| Game-style icons (actions, resources) | [game-icons.net](https://game-icons.net/) (CC BY — attribute) · [Kenney Board Game Icons](https://kenney.nl/assets/board-game-icons) (CC0) · [Iconify](https://iconify.design/) (meta search) |
| Batch custom card art | [nanDECK](https://www.nand.it/nandeck/) · [Squib](https://github.com/andymeneely/squib) · [Component.Studio](https://component.studio/) · [Figma](https://www.figma.com/) (layout) |
| Standard playing-card faces | [Adrian Kennard SVG cards](https://www.me.uk/cards/) (CC0 / public domain) |
| 3D bits for TTS / engines | [KayKit Board Game Bits](https://kaylousberg.itch.io/board-game-bits) (CC0) · [Kenney](https://kenney.nl/) · [Quaternius](https://quaternius.com/) |
| Pixel dice / chips / chess-style sprites | [Rad Potato component kit](https://rad-potato.itch.io/pixel-perfect-ultimate-game-component-kit) (CC0) |
| Wood / felt / paper materials | [Poly Haven](https://polyhaven.com/) · [ambientCG](https://ambientcg.com/) (CC0) |
| Fonts + CJK | [Google Fonts](https://fonts.google.com/) · [猫啃网](https://www.maoken.com/) · [100font](https://www.100font.com/) |
| SFX / music | [Freesound](https://freesound.org/) (filter license) · [Sonniss GDC](https://sonniss.com/gameaudiogdc) · [Mixkit](https://mixkit.co/) |
| Browser digital tabletop (P3) | [Screentop.gg](https://screentop.gg/) · [PlayingCards.io](https://playingcards.io/) · [Tabletopia](https://tabletopia.com/) · TTS after paper (`tools/TTS-guide.md`) |
| 3D-printed tokens | [Printables](https://www.printables.com/) (check per-model license) |
| Theme / historical illustration | [Openverse](https://openverse.org/) → museum CC0 rows below |
| PnP scans / fan files | Use **only** for personal prototype; see License caution |

---

## License Caution

| Source type | Prototype (personal) | Publish / commercial / crowdfunding |
|---|---|---|
| CC0 / public domain | OK | OK |
| CC BY | OK with attribution | Attribution required on product / credits |
| BGG Files, Yelook, fan scans | Often OK for private playtest | **Do not** ship without rights clearance |
| Internet Archive vintage scans | Check each item | Public domain only if clearly PD |
| Mixamo / Adobe-tied free | Check current ToS | Account + ToS constraints |
| BBC Sound Effects (RemArc) | Personal / educational | Commercial needs separate BBC license |

When unclear: prefer CC0 replacements from Quick pick over grey-area scans.

---

## Catalog

### Board-game-specific & general free assets (CC0 / open)

| Resource | URL | License / notes |
|---|---|---|
| Kenney | https://kenney.nl/ | CC0 — 2D/3D, UI, audio; includes [Board Game Icons](https://kenney.nl/assets/board-game-icons) |
| KayKit Board Game Bits | https://kaylousberg.itch.io/board-game-bits | CC0 — meeples, dice, tokens, cards (OBJ/FBX/GLTF) |
| Rad Potato — Ultimate Game Component Kit | https://rad-potato.itch.io/pixel-perfect-ultimate-game-component-kit | CC0 — 1000+ pixel dice, chips, chess, cards |
| OpenGameArt | https://opengameart.org/ | Varies — filter CC0/PD; music & SFX too |
| Screaming Brain Studios | https://screamingbrainstudios.com/ (itch: https://screamingbrainstudios.itch.io/) | CC0 — large public-domain packs |
| itch.io (search “CC0 game assets”) | https://itch.io/ | Varies — Pixel Frog, Ansimuz, 0x72, etc. |
| CraftPix (free section) | https://craftpix.net/ | Free tier — attribution often required; check pack |

### 3D models & textures (CC0)

| Resource | URL | License / notes |
|---|---|---|
| Poly Haven | https://polyhaven.com/ | CC0 — PBR, HDRIs, models (table/board renders) |
| ambientCG | https://ambientcg.com/ | CC0 — wood, paper, felt, metal, stone |
| Quaternius | https://quaternius.com/ | CC0 — stylized low-poly packs |
| Poly Pizza | https://poly.pizza/ | CC0 / CC-BY (filterable) |
| cgbookcase | https://cgbookcase.com/ | CC0 — models & textile textures |
| Sketchfab | https://sketchfab.com/ | Varies — filter Downloadable + CC0/CC-BY |
| Mixamo | https://www.mixamo.com/ | Free with Adobe account — rigged characters |
| Printables | https://www.printables.com/ | Varies — STL tokens/meeples; check each model |

### Digital tabletops (P3)

| Resource | URL | License / notes |
|---|---|---|
| Tabletop Simulator | https://www.tabletopsimulator.com/ | Paid client — after paper; see `tools/TTS-guide.md` |
| Screentop.gg | https://screentop.gg/ | Browser VTT — free tier limits games/storage |
| PlayingCards.io | https://playingcards.io/ | Browser — strong for card-light games |
| Tabletopia | https://tabletopia.com/ | Browser — free for players; creator limits apply |

### Official platforms & community shares

| Resource | URL | License / notes |
|---|---|---|
| Board Game Arena wiki | https://en.doc.boardgamearena.com/ | Official docs; some standard deck sprites |
| GitHub (“card images” + game) | https://github.com/ | Per-repo license |
| BoardGameGeek — Files | https://boardgamegeek.com/ | User uploads — mostly personal use |

### High-quality scans & PnP

| Resource | URL | License / notes |
|---|---|---|
| Internet Archive | https://archive.org/ | Check each item (PD vs restricted) |
| Yelook | https://yelook.com/ | Chinese PnP/scans — copyright often unclear; personal risk |

### Icons & vectors

| Resource | URL | License / notes |
|---|---|---|
| game-icons.net | https://game-icons.net/ | CC BY 3.0 — attribution required |
| Iconify | https://iconify.design/ | Meta search across open icon sets; check per-set license |
| PhyloPic | https://www.phylopic.org/ | PD / CC0 — organism silhouettes |
| Adrian Kennard SVG playing cards | https://www.me.uk/cards/ | CC0 / public domain — customizable SVG decks |
| Wikimedia Commons | https://commons.wikimedia.org/ | Varies (mostly PD or CC) |

### Archival & public-domain images

| Resource | URL | License / notes |
|---|---|---|
| U.S. Library of Congress | https://loc.gov/ | Public domain — maps, illustrations |
| Europeana | https://www.europeana.eu/ | Varies — cultural heritage |
| Smithsonian Open Access | https://www.si.edu/openaccess | CC0 |
| The Met Open Access | https://www.metmuseum.org/art/collection/search?showOnly=withOpenAccess | CC0 — API available |
| NYPL Digital Collections | https://digitalcollections.nypl.org/ | PD items CC0 |
| National Gallery of Art (US) | https://www.nga.gov/open-access-images.html | CC0 |
| Art Institute of Chicago | https://www.artic.edu/open-access | CC0 on PD works |
| Rijksmuseum Rijksstudio | https://www.rijksmuseum.nl/en/rijksstudio | Free high-res PD downloads |
| Rawpixel (PD section) | https://www.rawpixel.com/ | Free CC0 section — cleaned vintage art |

### Free stock photos & CC search

| Resource | URL | License / notes |
|---|---|---|
| Unsplash | https://unsplash.com/ | Unsplash License — commercial, no attribution |
| Pexels | https://www.pexels.com/ | Pexels License |
| Pixabay | https://pixabay.com/ | Pixabay License — photos, vectors, music, SFX |
| Openverse | https://openverse.org/ | Meta search for CC / CC0 media |

### Fonts (free commercial use)

| Resource | URL | License / notes |
|---|---|---|
| Google Fonts | https://fonts.google.com/ | Mostly SIL OFL; Noto / Source Han for CJK |
| Font Squirrel | https://www.fontsquirrel.com/ | Hand-picked commercial-use fonts |
| Font Library | https://fontlibrary.org/ | Varies (OFL/CC) |
| 猫啃网 (Maoken) | https://www.maoken.com/ | Varies — license-verified free CJK commercial fonts |
| 100font | https://www.100font.com/ | Varies (OFL etc.) — CJK focus |

### Sound effects & music

| Resource | URL | License / notes |
|---|---|---|
| Freesound | https://freesound.org/ | Per-sound CC0 / CC-BY / CC-BY-NC — filter |
| Sonniss #GameAudioGDC | https://sonniss.com/gameaudiogdc | Royalty-free annual bundles |
| Pixabay Music & SFX | https://pixabay.com/music/ | Pixabay License |
| Incompetech (Kevin MacLeod) | https://incompetech.com/ | CC BY 4.0 — attribution required |
| Mixkit | https://mixkit.co/ | Mixkit Free License — no attribution |
| BBC Sound Effects | https://sound-effects.bbcrewind.co.uk/ | RemArc — non-commercial by default |
| Musopen | https://musopen.org/ | PD / CC classical recordings |
| jsfxr | https://sfxr.me/ | Free tool — retro SFX generator |

### Production tools (free / freemium)

| Resource | URL | License / notes |
|---|---|---|
| nanDECK | https://www.nand.it/nandeck/ | Freeware — spreadsheet → card decks; `tools/nanDECK-guide.md` |
| Squib | https://github.com/andymeneely/squib | MIT — Ruby DSL for card/PnP images |
| Component.Studio | https://component.studio/ | Spreadsheet-driven art (freemium) |
| Strange Eons | https://strangeeons.cgjennings.ca/ | Free — template-driven card makers |
| Figma | https://www.figma.com/ | Free tier — board/card layout |
| Photopea | https://www.photopea.com/ | Free (ads) — browser PSD editor |
| Inkscape | https://inkscape.org/ | GPL — boards, tokens, vectors |
| Krita | https://krita.org/ | GPL — painting / textures |
| GIMP | https://www.gimp.org/ | GPL — raster editing |

### Miscellaneous

| Resource | URL | License / notes |
|---|---|---|
| DeviantArt | https://www.deviantart.com/ | Varies — always check permissions |

---

## Cross-References

| Topic | File |
|---|---|
| Fidelity / when to go digital | `prototype/selection.md`, `prototype/fidelity-ladder.md` |
| TTS import specs | `tools/TTS-guide.md` |
| Card export pipeline | `tools/export-pipeline.md`, `tools/nanDECK-guide.md` |
| Condensed mode links | `external-resources.md` § Prototype |
| PnP checklist | `templates/pnp-checklist.md` |
| Maintainer bibliography | `references/web-resources.md` |
