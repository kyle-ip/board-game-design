# Decision Matrix

Score each **candidate mechanism architecture** when comparing options. Use in Create mode with `design-reasoning.md`.

## Matrix Template

Copy into `mechanism-skeleton.md` Candidate Comparison section.

| Candidate | Agency | Interaction | Complexity | Variance | AP Risk | Theme fit | Notes |
|---|---|---|---|---|---|---|---|
| A. | H/M/L | H/M/L | H/M/L | H/M/L | H/M/L | H/M/L | |
| B. | | | | | | | |
| C. | | | | | | | |

**Legend:** H = high, M = medium, L = low.

## Dimension Definitions

| Dimension | High means | Low means |
|---|---|---|
| **Agency** | Many meaningful choices per turn | Few or scripted choices |
| **Interaction** | Direct blocking, trading, contest | Multiplayer solitaire |
| **Complexity** | Rules overhead, exception count | Teach in 5 min |
| **Variance** | Swingy outcomes, luck-heavy | Predictable, skill-dominant |
| **AP Risk** | Analysis paralysis likely | Fast turns |
| **Theme fit** | Mechanism reinforces setting | Paste-on theme |

## Decision Rules

- If **Interaction** is the design goal, eliminate candidates scored Low on interaction unless solo/async.
- If **family / party** audience, cap **Complexity** and **AP Risk** at Medium.
- If **Variance** is High and **Agency** is Low → check `diagnostics/randomness-dominates-skill.md`.
- If two candidates tie, prefer the one with **fewer components** for first paper MVP.
- Tie-breaker: pick the variant easiest to **kill** if the hypothesis fails (smaller rules delta).

## Example (abbreviated)

**Goal:** scarce resource competition, 2–4 players, 45 min, moderate blocking OK.

| Candidate | Agency | Interaction | Complexity | Variance | AP Risk |
|---|---|---|---|---|---|
| Worker Placement | H | H | M | L | M |
| Action Drafting | H | M | L | L | L |
| Open Market | M | M | M | L | L |

**Recommendation:** Worker Placement — highest interaction + agency for stated goal.

**Risk:** 2P blocking weak → test with 3 worker spaces vs 5 (`experiment.md`).

## Cross-References

- Full reasoning chain: `design-reasoning.md`
- Lock outcome: `design-state.md`, `decision.md`
