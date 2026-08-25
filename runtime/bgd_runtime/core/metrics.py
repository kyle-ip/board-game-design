from __future__ import annotations

import math
import statistics
from dataclasses import dataclass, field
from typing import Any


def summarize_runs(results: list[dict[str, Any]]) -> dict[str, Any]:
    """Aggregate per-game result dicts into campaign metrics."""
    if not results:
        return {
            "runs": 0,
            "first_player_win_rate": None,
            "average_game_length": None,
            "score_spread": None,
            "dominant_action_rate": None,
            "comeback_rate": None,
            "strategy_distribution": {},
            "win_rate_by_seat": [],
            "ties": 0,
        }

    n = len(results)
    fp_wins = sum(1 for r in results if r.get("winner") == 0)
    ties = sum(1 for r in results if r.get("winner") is None)
    lengths = [r["game_length"] for r in results]
    spreads = [r["score_spread"] for r in results]
    comebacks = sum(1 for r in results if r.get("lead_changes", 0) > 0)

    action_totals: dict[str, int] = {}
    profile_wins: dict[str, int] = {}
    profile_games: dict[str, int] = {}
    for r in results:
        for k, v in r.get("action_hist", {}).items():
            action_totals[k] = action_totals.get(k, 0) + int(v)
        for seat, prof in enumerate(r.get("profiles", [])):
            profile_games[prof] = profile_games.get(prof, 0) + 1
            if r.get("winner") == seat:
                profile_wins[prof] = profile_wins.get(prof, 0) + 1

    total_actions = sum(action_totals.values()) or 1
    dominant_kind = max(action_totals, key=action_totals.get) if action_totals else None
    dominant_rate = (action_totals[dominant_kind] / total_actions) if dominant_kind else None

    strategy_distribution = {
        p: {
            "games": profile_games[p],
            "wins": profile_wins.get(p, 0),
            "win_rate": profile_wins.get(p, 0) / profile_games[p] if profile_games[p] else 0.0,
        }
        for p in sorted(profile_games)
    }

    decided = n - ties
    return {
        "runs": n,
        "ties": ties,
        "first_player_win_rate": (fp_wins / decided) if decided else None,
        "average_game_length": statistics.mean(lengths),
        "score_spread": statistics.mean(spreads),
        "dominant_action_rate": dominant_rate,
        "dominant_action": dominant_kind,
        "comeback_rate": comebacks / n,
        "strategy_distribution": strategy_distribution,
        "win_rate_by_seat": [
            sum(1 for r in results if r.get("winner") == s) / decided if decided else None
            for s in range(results[0].get("num_players", 2))
        ],
        "score_mean": statistics.mean([statistics.mean(r["scores"]) for r in results]),
    }


def metrics_close(a: dict[str, Any], b: dict[str, Any], abs_tol: float = 1e-9) -> bool:
    """Structural equality for regression of deterministic runs."""
    keys = [
        "runs",
        "first_player_win_rate",
        "average_game_length",
        "score_spread",
        "dominant_action_rate",
        "comeback_rate",
        "ties",
    ]
    for k in keys:
        va, vb = a.get(k), b.get(k)
        if va is None and vb is None:
            continue
        if isinstance(va, (int, float)) and isinstance(vb, (int, float)):
            if not math.isclose(float(va), float(vb), abs_tol=abs_tol, rel_tol=0):
                return False
        elif va != vb:
            return False
    return True
