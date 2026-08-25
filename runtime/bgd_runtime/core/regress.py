from __future__ import annotations

import json
from pathlib import Path
from typing import Any


DEFAULT_THRESHOLDS = {
    "first_player_win_rate": 0.05,
    "average_game_length": 5.0,
    "score_spread": 1.0,
    "dominant_action_rate": 0.1,
    "comeback_rate": 0.1,
}


def load_metrics(path: str | Path) -> dict[str, Any]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if "metrics" in data and isinstance(data["metrics"], dict):
        return data["metrics"]
    return data


def regress(
    baseline: dict[str, Any],
    candidate: dict[str, Any],
    thresholds: dict[str, float] | None = None,
) -> dict[str, Any]:
    """Compare candidate metrics to baseline; fail if abs delta exceeds threshold."""
    th = {**DEFAULT_THRESHOLDS, **(thresholds or {})}
    failures: list[dict[str, Any]] = []
    for key, limit in th.items():
        b, c = baseline.get(key), candidate.get(key)
        if b is None or c is None:
            continue
        delta = abs(float(c) - float(b))
        if delta > float(limit):
            failures.append({"metric": key, "baseline": b, "candidate": c, "delta": delta, "limit": limit})
    return {
        "pass": len(failures) == 0,
        "failures": failures,
        "thresholds": th,
    }
