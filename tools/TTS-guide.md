# Tabletop Simulator Quick Guide

Optional **after paper loop works**. Import art from PnP or nanDECK output.

## Image Specs

| Asset | Recommended |
|---|---|
| Card face | 1024×1424 px (or 409×585 px minimum), PNG |
| Card back | One shared back PNG |
| Board | 2048×2048 or larger, PNG/JPG |
| Tokens | 256×256 px, transparent PNG |

Use readable text at table zoom — prototype clarity over beauty.

## Cards from Images

1. In TTS: **Objects → Components → Custom → Deck**
2. Import card **front** images (multi-select in order matching ids)
3. Set single **back** image
4. Name deck; set width/height to match aspect ratio
5. Save deck object to chest

Tip: filename prefix `001_`, `002_` preserves sort order.

## Custom Board

1. **Objects → Components → Custom → Board**
2. Import board image
3. Snap grid if using zones; or manual zone tools for regions

## Quick Playtest Setup

1. Table → save after placing deck, board, tokens
2. **Save & Load → Create** → name `ProjectName_v0.3`
3. Share `.json` + images folder with playtesters if remote

## Checklist

- [ ] Card ids visible on prototype faces (debug)
- [ ] Rulebook PDF in-table (Notebook object) or external link
- [ ] No color-only information (add icons)
- [ ] Undo enabled for prototype rules mistakes

## Limitations

- TTS physics ≠ paper feel — validate timing and AP on paper first
- Scripting optional — not required for first digital smoke test

## Cross-References

- Paper first: `SKILL.md` Hard Invariants / default medium
- PnP checklist digital section: `templates/pnp-checklist.md`
- Card generation: `tools/nanDECK-guide.md`
