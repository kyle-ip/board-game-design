# Genre Profiles

Load **one** profile at project start (Create mode) or when genre mismatch causes wrong diagnostics. Do not bulk-load all profiles.

| Profile | File | Core experience |
|---|---|---|
| Euro / strategy | `euro.md` | Engine building, scarcity, long-term planning |
| Party | `party.md` | Social fun, low teach, high laughter |
| Social deduction | `social-deduction.md` | Hidden roles, bluff, information asymmetry |
| Solo / Automa | `solo.md` | Puzzle, AI opponent, session length control |
| Cooperative | `coop.md` | Shared win/loss, roles, difficulty curve, anti-alpha |

Future: negotiation, narrative, dexterity, real-time, campaign/legacy.

## When to Load

| Trigger | Action |
|---|---|
| New game design | Ask or infer genre → load matching profile + `theme-and-experience.md` |
| Wrong diagnostic fit | e.g. first-player win rate on hidden-role or co-op → switch profile |
| Kill criteria review | Load profile's recommended thresholds into design-state overrides |

## Profile Contents (each file)

- Core experience & aesthetics
- Typical dynamics & mechanism vocabulary
- Common failure modes → diagnostics routing
- Recommended playtest frameworks by stage
- Kill criteria overrides (starting defaults)
- Prototype constraints

## Cross-References

- Symptom routing: `routing/symptom-index.md`
- Mechanism depth: `chapters/` (Euro-heavy; profiles bridge gaps)
- Kill gate: `kill-criteria.md`
- Experience diagnostics: ED001–ED008 in `diagnostics/`
