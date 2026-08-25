from __future__ import annotations

import random
from typing import Any, Sequence

from bgd_runtime.agents.params import PlayerParams
from bgd_runtime.core.game import Action


class HeuristicAgent:
    """Parametric heuristic: score actions then ε-explore / mistake."""

    def __init__(self, params: PlayerParams):
        self.params = params.clamp()

    def select(self, obs: dict[str, Any], legal: Sequence[Action], rng: random.Random) -> Action:
        if not legal:
            raise ValueError("no legal actions")
        if self.params.exploration >= 1.0 - 1e-9 or rng.random() < self.params.exploration:
            return rng.choice(list(legal))
        scored = [(self._score(a, obs), a) for a in legal]
        scored.sort(key=lambda t: t[0], reverse=True)
        best = scored[0][1]
        if rng.random() < self.params.mistake_rate and len(scored) > 1:
            return rng.choice([a for _, a in scored[1:]])
        return best

    def _score(self, action: Action, obs: dict[str, Any]) -> float:
        scorer = obs.get("action_scores")
        if callable(scorer):
            return float(scorer(action, self.params))
        if isinstance(scorer, dict):
            return float(scorer.get(action.key(), 0.0))
        # Fallback generic shaping
        base = 0.0
        if action.kind == "convert":
            base += 0.5 * self.params.aggression + 0.2 * self.params.risk_tolerance
            n = int(action.payload.get("count", 0) or 0)
            base += 0.15 * n * (self.params.planning_horizon / 5.0)
        if action.kind == "take_discard":
            base += 0.25 * self.params.aggression + 0.2 * self.params.exploration
        if action.kind == "take_deck":
            base += 0.15 * (1.0 - self.params.risk_tolerance)
        return base
