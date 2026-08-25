from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from bgd_runtime import AGENT_VERSION, SIMULATION_VERSION, __version__
from bgd_runtime.core.metrics import metrics_close
from bgd_runtime.core.population import run_campaign
from bgd_runtime.core.regress import load_metrics, regress
from bgd_runtime.digital.play import play_cli
from bgd_runtime.games import get_game


def _write_json(path: Path | None, payload: dict) -> None:
    text = json.dumps(payload, indent=2, sort_keys=True)
    if path:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text + "\n", encoding="utf-8")
        print(f"Wrote {path}")
    else:
        print(text)


def cmd_run(args: argparse.Namespace) -> int:
    factory = get_game(args.game)
    if args.population:
        payload = run_campaign(
            factory,
            runs=args.runs,
            seed=args.seed,
            population=args.population,
        )
    else:
        profiles = [p.strip() for p in args.profiles.split(",") if p.strip()]
        if len(profiles) < 2:
            profiles = ["greedy", "greedy"]
        payload = run_campaign(
            factory,
            runs=args.runs,
            seed=args.seed,
            profiles=profiles,
        )
    out = {
        "simulation_version": SIMULATION_VERSION,
        "agent_version": AGENT_VERSION,
        "runtime_version": __version__,
        "game": args.game,
        "rules_version": factory().rules_version,
        "seed": args.seed,
        "runs": args.runs,
        **payload,
    }
    _write_json(Path(args.out) if args.out else None, out)
    m = out["metrics"]
    print(
        f"runs={m['runs']} fp_win={m['first_player_win_rate']} "
        f"len={m['average_game_length']:.1f} spread={m['score_spread']:.2f}"
    )
    return 0


def cmd_regress(args: argparse.Namespace) -> int:
    baseline = load_metrics(args.baseline)
    candidate = load_metrics(args.candidate)
    thresholds = None
    if args.threshold_json:
        thresholds = json.loads(Path(args.threshold_json).read_text(encoding="utf-8"))
    result = regress(baseline, candidate, thresholds)
    _write_json(Path(args.out) if args.out else None, result)
    print("PASS" if result["pass"] else "FAIL")
    if not result["pass"]:
        for f in result["failures"]:
            print(f"  {f['metric']}: delta={f['delta']} limit={f['limit']}")
        return 1
    return 0


def cmd_check_determinism(args: argparse.Namespace) -> int:
    factory = get_game(args.game)
    a = run_campaign(factory, runs=args.runs, seed=args.seed, population=args.population or "mixed")
    b = run_campaign(factory, runs=args.runs, seed=args.seed, population=args.population or "mixed")
    ok = metrics_close(a["metrics"], b["metrics"])
    print("deterministic" if ok else "NON-DETERMINISTIC")
    return 0 if ok else 1


def cmd_play(args: argparse.Namespace) -> int:
    play_cli(args.game, args.seed, args.opponent)
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="bgd-sim", description="board-game-design optional simulation CLI")
    sub = p.add_subparsers(dest="command", required=True)

    run = sub.add_parser("run", help="Monte Carlo campaign")
    run.add_argument("--game", default="micro-scavenger")
    run.add_argument("--runs", type=int, default=100)
    run.add_argument("--seed", type=int, default=42)
    run.add_argument("--population", default=None, help="experienced|casual|mixed|adversarial_meta")
    run.add_argument("--profiles", default="greedy,strategic", help="comma profiles if no population")
    run.add_argument("--out", default=None, help="write JSON metrics")
    run.set_defaults(func=cmd_run)

    reg = sub.add_parser("regress", help="Compare candidate metrics to baseline")
    reg.add_argument("--baseline", required=True)
    reg.add_argument("--candidate", required=True)
    reg.add_argument("--threshold-json", default=None)
    reg.add_argument("--out", default=None)
    reg.set_defaults(func=cmd_regress)

    det = sub.add_parser("check-determinism", help="Same seed twice must match")
    det.add_argument("--game", default="micro-scavenger")
    det.add_argument("--runs", type=int, default=50)
    det.add_argument("--seed", type=int, default=42)
    det.add_argument("--population", default="mixed")
    det.set_defaults(func=cmd_check_determinism)

    play = sub.add_parser("play", help="P2 CLI human vs heuristic")
    play.add_argument("--game", default="micro-scavenger")
    play.add_argument("--seed", type=int, default=42)
    play.add_argument("--opponent", default="greedy")
    play.set_defaults(func=cmd_play)

    return p


def main(argv: list[str] | None = None) -> None:
    parser = build_parser()
    args = parser.parse_args(argv)
    code = args.func(args)
    raise SystemExit(code)


if __name__ == "__main__":
    main()
