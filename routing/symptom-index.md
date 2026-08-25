# Symptom Routing Index

Formal routing ontology — resolve ambiguous symptoms to **one primary diagnostic path** before loading files. Use before `cheatsheet.md` detail tables when symptom is vague.

Principle: **surface symptom → discriminate → one diagnostic → hypothesis → experiment**.

## Symptom Classes

| Class | Examples | Discriminate with |
|---|---|---|
| **Surface** | "boring", "flat", "not fun" | Quotes, turn pattern, when boredom starts |
| **Behavioral** | same action every turn, no interaction | Turn log, action variety count |
| **Structural** | can't explain win condition, rules bloat | Teach test, sentence count |
| **Statistical** | seat 1 wins 5/7, score spread | Seat data, round-by-round scores |

## Ambiguous: "Boring" / "Flat" / "Nothing Exciting"

Ask or infer from evidence (do not guess). Split **system boring** vs **experience forgettable**:

```text
When does it feel flat?
├── Opening only        → ED003 flat-emotional-curve OR weak hook (theme-and-experience)
├── Midgame (turns 3–7) → PRIMARY system: low-agency.md
│   └── Same action loop? → dominant-strategy.md OR structural rethink (kill gate)
├── Endgame only        → PRIMARY: endgame-drag.md; also check ED008 insufficient-escalation
├── Whole game "fine"   → Experience path below (not only kill gate)
└── "Forgettable" / no stories → Experience Diagnostics (ED*), not P1 sim
```

**Routing priority — system (first match wins):**

1. Identical turns 3+ in a row → `diagnostics/low-agency.md` + `dominant-strategy.md`
2. Game runs long, final rounds empty → `diagnostics/endgame-drag.md`
3. Players wait, no decisions → `diagnostics/low-agency.md`
4. No quotes, only "fine" → Open question in design-state; run Good-Bad-Meh next session

## Ambiguous: Experience / Theme / Forgettable

These are **experience** questions. Prefer P2–P4 human evidence. **Never** claim High confidence from P1 simulation alone.

```text
Experience complaint
├── Don't know who I am / no fantasy     → weak-player-fantasy.md (ED001)
├── Theme feels pasted on                → theme-mechanism-disconnect.md (ED002)
├── Intensity flat all game              → flat-emotional-curve.md (ED003)
├── Nothing memorable / no stories       → low-memorable-moments.md (ED004)
│                                         + poor-narrative-emergence.md (ED007)
├── Feels like every other game          → generic-decision-space.md (ED005)
├── Parallel solitaire / no interaction ID → weak-interaction-identity.md (ED006)
├── No build-up / late = early           → insufficient-escalation.md (ED008)
└── Also "broken" systems?               → route system diagnostics FIRST, then ED*
```

## Ambiguous: "Unfair" / "Broken"

```text
Unfair complaint
├── Specific seat always wins     → first-player-advantage.md (if turn-based euro)
├── One strategy always wins      → dominant-strategy.md
├── Leader uncatchable            → runaway-leader.md
├── Random decides outcome        → randomness-dominates-skill.md
├── Eliminated player picks winner → kingmaking.md
└── Hidden role feels unfair      → genre-profile/social-deduction.md (NOT first-player)
```

## Ambiguous: "Too Long" / "Slow"

```text
Too long
├── Turns take >5 min each    → analysis-paralysis.md
├── Game exceeds target time  → endgame-drag.md OR trim end trigger (Ch 5)
├── Teach >15 min (party)     → simplify rules — lint BG014
└── Downtime between turns    → Ch 2 turn structure; Follow actions
```

## Ambiguous: "Too Random"

```text
Too random
├── Before decision (input)   → may be OK — check aesthetic match (Ch 6)
├── After commitment (output) → randomness-dominates-skill.md
└── Role/deal variance (social) → setup audit, not dice fix
```

## Genre Override

If genre profile loaded, check profile's **Common Failure Modes** table before euro-default routing.

| Genre | Disable or de-prioritize |
|---|---|
| social-deduction | first-player win rate metrics |
| party | winner score spread, VP balance |
| solo | kingmaking, first-player |
| coop | first-player win rate; competitive runaway as primary |
| euro | (default routing applies) |

## Evidence Discriminator Checklist

Before routing, confirm what evidence exists:

| Evidence | Enables routing to |
|---|---|
| Seat/win log | BG001, runaway-leader |
| Turn-by-turn actions | low-agency, dominant-strategy |
| Round scores | runaway-leader |
| Turn timing | analysis-paralysis |
| Player quotes | theme fit, ED001–ED008, negative interaction |
| 24h recall / stories | ED004, ED007 |
| Emotion curve ratings | ED003, ED008 |
| Blind test result | rule ambiguity BG014 |

Missing evidence → mark `?` in lint; do not pick diagnostic with High confidence.

## Output

After routing, state in design-state or decision:

```text
Symptom: [user words]
Class: behavioral
Primary diagnostic: diagnostics/low-agency.md
Discarded paths: endgame-drag (endgame fine), randomness (not cited)
Evidence: PT-003 turn log
Next: HYP-001 experiment — single variable
```

## Cross-References

- Detail routing table: `cheatsheet.md` Symptom → File Routing
- Genre profiles: `genre-profile/`
- Diagnostics: `diagnostics/`
- Experiment: `experiments/framework.md`
