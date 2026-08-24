# Print File Preparation Decision Rules

## Decision Tree — POD vs Mass Production

```
Quantity?
├─ <10 copies / prototype          → The Game Crafter (POD)        [TGC path]
├─ 10–999 / small custom batch     → Board Games Maker            [custom batch]
└─ 1000+ copies / retail           → Panda GM (mass production)   [Panda path]
```

| Constraint | Choose |
|---|---|
| Tiny budget, no minimum | TGC |
| Need custom components, low run | Board Games Maker |
| Retail / Kickstarter fulfillment | Panda GM |
| Cards only, low quantity | MakePlayingCards |

## POD Path — The Game Crafter
Source: [TGC Design Guidebook 2023](https://s3.amazonaws.com/helpscout.net/docs/assets/561c5a919033600a7a36d5dc/attachments/643d87297133de139103ebc2/Design-Guide---2023.pdf)

- File format: **PNG uploads** (per template)
- Bleed: **1/8"** beyond cut line
- Use TGC templates — do not invent dimensions
- Drift mitigation: avoid borders / frames on edges; allow visual bleed past safe area
- Color: design in CMYK, expect RGB-converted preview — preview colors may drift
- Resolution: 300 ppi minimum

## Mass Production Path — Panda GM
Source: [Panda Graphic Design Guidebook V.4](https://pandagm.com/wp-content/uploads/2022/10/PandaGM-GraphicDesignGuidebook-V4-0922.pdf)

- File format: **PDF** (one file per component)
- Color: **CMYK**, profile **FOGRA39**
- Resolution: **300 ppi**
- Bleed: **3 mm** + safe zone **3 mm**
- Layout tool: **Adobe InDesign** — NOT Photoshop — for final PDFs
- Black text: pure black **C:0 M:0 Y:0 K:100** with **overprint** on
- One file per component — no combined files

## Component-Specific Rules

| Component | Critical specs |
|---|---|
| Cards | Rounded corners (3 mm typical); full bleed; CMYK; 300 ppi |
| Boards | Fold lines on separate layer; gutter allowance for folds; quad-fold common |
| Punchboards | Die-lines on separate layer; minimum 5 mm tab spacing; slot widths per chipboard gauge |
| Boxes | Wrap + tray separate files; wrap wraparound bleed; tuck-flap scores |
| Booklets | Saddle-stitch or perfect-bound; cover + interior separate; spine width per page count |

## 3D Printing Specs (TGC)
Source: [TGC — Designing for 3D Printing](https://help.thegamecrafter.com/article/509-designing-for-3d-printing)

- Nozzle: **0.4 mm**
- Layer height: **0.12 mm**
- Base sizes: **25 mm** or **15 mm**
- File format: **STL** or **OBJ**
- **No supports** in file — design for printability

## Pre-Flight Checklist (Before Submitting)

- [ ] CMYK verified (no RGB images embedded)
- [ ] 300 ppi confirmed at final print size
- [ ] Bleed + safe zone applied (3 mm Panda / 1/8" TGC)
- [ ] One file per component
- [ ] Fonts outlined (no live font dependencies)
- [ ] Black overprint set on text (Panda path)
- [ ] Dielines on separate named layer

## Cross-References
- Workflow placement: `workflow.md` Stage 5 (Publish) for manufacturing; Stage 1 + `templates/pnp-checklist.md` for playable paper prototypes.
- Platform comparison: `external-resources.md` §7.
- Print-and-play file prep: [pnp-howto](https://github.com/ernierasta/pnp-howto).
- Horizontal print spec survey: [Dobeta Games guide](https://www.dobetagames.com/the-complete-guide-to-board-game-printing-file-requirements/).
- Component data before layout: `templates/components-sheet.md`.
