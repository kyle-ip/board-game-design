from __future__ import annotations

import random
from typing import Any, Callable

from bgd_runtime.agents.heuristic import HeuristicAgent
from bgd_runtime.agents.params import PROFILES, PlayerParams, resolve_population
from bgd_runtime.core.game import Game
from bgd_runtime.core.metrics import summarize_runs


def make_agent(profile: str) -> HeuristicAgent:
    if profile not in PROFILES:
        raise KeyError(f"unknown profile: {profile}")
    return HeuristicAgent(PROFILES[profile])


def play_one(
    game_factory: Callable[[], Game],
    seed: int,
    profiles: list[str],
) -> dict[str, Any]:
    game = game_factory()
    game.reset(seed)
    agents = [make_agent(p) for p in profiles]
    rng = random.Random(seed ^ 0xA5A5A5A5)
    steps = 0
    max_steps = 10_000
    while not game.is_terminal() and steps < max_steps:
        p = game.current_player
        legal = list(game.legal_actions())
        obs = game.observation(p)
        action = agents[p].select(obs, legal, rng)
        game.step(action)
        steps += 1
    scores = game.scores()
    return {
        "seed": seed,
        "winner": game.winner(),
        "scores": scores,
        "score_spread": max(scores) - min(scores) if scores else 0.0,
        "game_length": steps,
        "action_hist": game.action_histogram(),
        "lead_changes": getattr(game, "_lead_changes", 0),
        "profiles": profiles,
        "num_players": game.num_players,
    }


def run_campaign(
    game_factory: Callable[[], Game],
    *,
    runs: int,
    seed: int,
    population: str | dict[str, float] | None = None,
    profiles: list[str] | None = None,
) -> dict[str, Any]:
    """Run N games. Either fixed seat profiles or population mix sampling per seat."""
    mix = resolve_population(population) if population else None
    results: list[dict[str, Any]] = []
    seat_profile_counts: dict[str, int] = {}

    for i in range(runs):
        game_seed = seed + i * 9973
        if mix is not None:
            seat_rng = random.Random(game_seed ^ 0x1234)
            keys = list(mix.keys())
            weights = [mix[k] for k in keys]
            seat_profiles = [seat_rng.choices(keys, weights=weights, k=1)[0] for _ in range(2)]
        else:
            assert profiles is not None and len(profiles) >= 2
            seat_profiles = profiles[:2]
        for p in seat_profiles:
            seat_profile_counts[p] = seat_profile_counts.get(p, 0) + 1
        results.append(play_one(game_factory, game_seed, seat_profiles))

    metrics = summarize_runs(results)
    return {
        "seed": seed,
        "runs": runs,
        "population": population if isinstance(population, str) else "custom",
        "population_mix": mix,
        "fixed_profiles": profiles,
        "seat_profile_counts": seat_profile_counts,
        "metrics": metrics,
        "results_sample": results[:5],
    }
