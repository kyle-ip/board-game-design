# Prototype Fidelity Selection

Map the **question type** to the minimum valid fidelity. Prefer the lowest level that can produce appropriate evidence.

Prerequisite: read `prototype/fidelity-ladder.md`.

## Hypothesis → Fidelity Matrix

| Question | Preferred | Evidence type |
|---|---|---|
| Dominant strategy exists? | P1 | simulation |
| First-player advantage? | P1 | simulation |
| Economy runaway / inflation? | P1 | simulation |
| Average game length / termination? | P1 | simulation |
| Card / action utilization? | P1 | simulation |
| Win-rate distribution? | P1 | simulation |
| Players understand rules? | P2 | digital_playtest or physical_playtest |
| Decision space feels meaningful? | P2 | digital_playtest or physical_playtest |
| Negotiation / social deduction holds? | P3 | digital_playtest / physical_playtest |
| Hidden information creates intended experience? | P3 | digital_playtest / physical_playtest |
| Table footprint / component handling? | P4 | physical_playtest |
| Setup / teardown burden? | P4 | physical_playtest |
| Production feel / manufacturing? | P5 | physical_playtest / expert |

## Selection algorithm

```text
1. Classify question: system | experience | physical
2. Check genre caveats (party / social → skip P1 unless rules integrity only)
3. If no Formal Model (P0) and question is system → draft P0 first, or fall back to human playtest
4. Pick preferred fidelity from matrix
5. Record preferred_fidelity + evidence_type on hypothesis / experiment
6. Escalate only if evidence is insufficient or physical_dependency = true
```

## Physical dependency (force P4+)

Do **not** close these claims with simulation alone:

- Dexterity, simultaneous grabbing, tactile bluffing
- Table space, readability at arm's length, shuffle/count friction
- Component ambiguity that only appears in print

Mark hypothesis `physical_dependency: true` → lint **BG020** if only digital/sim evidence exists.

## Evidence plan fields (copy into experiment)

| Field | Example |
|---|---|
| Minimum evidence source | simulation / digital_playtest / physical_playtest |
| Prototype fidelity | P1 |
| Simulation profile | first-player-advantage (if P1) |
| Human playtest required | yes / no |
| Physical validation required | yes / no |

## Cross-References

- Priority with fidelity: `reasoning/experiment-priority.md`
- Lint: BG015, BG019, BG020 in `lint/rules.md`
- Experiment template: `templates/experiment.md`
