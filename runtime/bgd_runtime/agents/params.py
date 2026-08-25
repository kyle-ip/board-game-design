from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class PlayerParams:
    planning_horizon: int = 1
    risk_tolerance: float = 0.5
    aggression: float = 0.5
    exploration: float = 0.0
    opponent_awareness: float = 0.5
    mistake_rate: float = 0.0
    profile: str = "custom"

    def clamp(self) -> PlayerParams:
        return PlayerParams(
            planning_horizon=max(1, min(5, int(self.planning_horizon))),
            risk_tolerance=_clamp01(self.risk_tolerance),
            aggression=_clamp01(self.aggression),
            exploration=_clamp01(self.exploration),
            opponent_awareness=_clamp01(self.opponent_awareness),
            mistake_rate=_clamp01(self.mistake_rate),
            profile=self.profile,
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "planning_horizon": self.planning_horizon,
            "risk_tolerance": self.risk_tolerance,
            "aggression": self.aggression,
            "exploration": self.exploration,
            "opponent_awareness": self.opponent_awareness,
            "mistake_rate": self.mistake_rate,
            "profile": self.profile,
        }


def _clamp01(x: float) -> float:
    return max(0.0, min(1.0, float(x)))


PROFILES: dict[str, PlayerParams] = {
    "random": PlayerParams(
        planning_horizon=1,
        risk_tolerance=0.5,
        aggression=0.5,
        exploration=1.0,
        opponent_awareness=0.0,
        mistake_rate=0.0,
        profile="random",
    ),
    "greedy": PlayerParams(
        planning_horizon=1,
        risk_tolerance=0.7,
        aggression=0.6,
        exploration=0.05,
        opponent_awareness=0.2,
        mistake_rate=0.02,
        profile="greedy",
    ),
    "conservative": PlayerParams(
        planning_horizon=2,
        risk_tolerance=0.2,
        aggression=0.2,
        exploration=0.05,
        opponent_awareness=0.4,
        mistake_rate=0.02,
        profile="conservative",
    ),
    "opportunistic": PlayerParams(
        planning_horizon=2,
        risk_tolerance=0.6,
        aggression=0.6,
        exploration=0.15,
        opponent_awareness=0.5,
        mistake_rate=0.03,
        profile="opportunistic",
    ),
    "strategic": PlayerParams(
        planning_horizon=3,
        risk_tolerance=0.5,
        aggression=0.4,
        exploration=0.08,
        opponent_awareness=0.7,
        mistake_rate=0.02,
        profile="strategic",
    ),
    "adversarial": PlayerParams(
        planning_horizon=2,
        risk_tolerance=0.7,
        aggression=0.9,
        exploration=0.1,
        opponent_awareness=1.0,
        mistake_rate=0.01,
        profile="adversarial",
    ),
}


POPULATIONS: dict[str, dict[str, float]] = {
    "experienced": {
        "strategic": 0.4,
        "opportunistic": 0.3,
        "greedy": 0.2,
        "adversarial": 0.1,
    },
    "casual": {
        "random": 0.2,
        "greedy": 0.3,
        "conservative": 0.3,
        "opportunistic": 0.2,
    },
    "mixed": {
        "greedy": 0.2,
        "conservative": 0.2,
        "opportunistic": 0.2,
        "strategic": 0.2,
        "random": 0.1,
        "adversarial": 0.1,
    },
    "adversarial_meta": {
        "adversarial": 0.4,
        "strategic": 0.3,
        "greedy": 0.2,
        "opportunistic": 0.1,
    },
}


def normalize_mix(mix: dict[str, float]) -> dict[str, float]:
    total = sum(mix.values())
    if total <= 0:
        raise ValueError("population mix weights must sum to > 0")
    return {k: v / total for k, v in mix.items()}


def resolve_population(name_or_mix: str | dict[str, float]) -> dict[str, float]:
    if isinstance(name_or_mix, dict):
        return normalize_mix(name_or_mix)
    key = name_or_mix.lower().strip()
    if key not in POPULATIONS:
        raise KeyError(f"unknown population preset: {name_or_mix}")
    return dict(POPULATIONS[key])
