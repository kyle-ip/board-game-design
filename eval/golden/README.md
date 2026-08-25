# Golden Artifacts

Expected structural patterns for automated validation. Maintainers compare agent output against these schemas.

**Not loaded by agents during design sessions** — maintainer and `eval/validators/` only.

## Files

| File | Purpose |
|---|---|
| `design-state-schema.md` | Required sections and v3/v4 optional fields |
| `experiment-minimal.md` | Minimal valid experiment with single variable |
| `hypothesis-minimal.md` | Claim + confidence + evidence refs |
| `playtest-log-minimal.md` | EXP/HYP/Variant linkage |
| `simulation-run-minimal.md` | Seeded P1 simulation artifact shape |

## Usage

1. Run agent on benchmark prompt (Cases A–F, G, J in `eval/benchmark-prompts.md`)
2. Validate output structure:
   ```bash
   python eval/validators/validate.py ./eval-case-a/
   ```
3. Compare key sections to golden files (manual diff or future golden diff script)
4. Behavior criteria (routing, diagnosis, fidelity) still require manual scoring per `eval/README.md`

## Regression

After skill changes, re-run `--fixture-all` on fixtures:

```bash
python eval/validators/validate.py --fixture-all
```

Fixtures should pass structural checks. Behavior benchmarks (Cases A–J) remain manual.
