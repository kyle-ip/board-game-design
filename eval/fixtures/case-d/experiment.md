# Experiment — Loop Test (Eval Case D)

## Meta

| Field | Value |
|---|---|
| Experiment ID | EXP-001 |
| Status | complete |

## Objective

Test whether raising VP threshold changes player behavior away from gather-convert loop.

## Hypothesis

We believe **raising VP win threshold from 10 to 15**
will cause **≥2 players pursue non-convert actions by turn 4**
because **longer games should force engine building**.

**Success criteria:** ≥2 players take non-convert action by turn 4 in 2/3 playtests
**Failure criteria:** Same gather-convert loop; fun ≤3/5

## Design Variable (one only)

| Field | Value |
|---|---|
| Variable | VP win threshold |
| Baseline | 10 VP to win |
| Variant | 15 VP to win |
| Everything else held constant | gather/convert actions, setup, player count |

## Conclusion

- [x] Refuted — behavior unchanged; structural rethink needed
