from __future__ import annotations

from bgd_runtime.agents.params import normalize_mix, resolve_population
from bgd_runtime.core.metrics import metrics_close
from bgd_runtime.core.population import run_campaign
from bgd_runtime.core.regress import regress
from bgd_runtime.games.micro_scavenger import MicroScavenger, convert_vp


def test_convert_vp():
    assert convert_vp(2) == 1
    assert convert_vp(3) == 3
    assert convert_vp(4) == 6
    assert convert_vp(1) == 0


def test_population_normalize():
    m = normalize_mix({"a": 1, "b": 1})
    assert abs(m["a"] - 0.5) < 1e-9
    mix = resolve_population("mixed")
    assert abs(sum(mix.values()) - 1.0) < 1e-9


def test_determinism_same_seed():
    a = run_campaign(MicroScavenger, runs=30, seed=7, population="mixed")
    b = run_campaign(MicroScavenger, runs=30, seed=7, population="mixed")
    assert metrics_close(a["metrics"], b["metrics"])


def test_metrics_keys():
    out = run_campaign(MicroScavenger, runs=20, seed=1, profiles=["greedy", "random"])
    m = out["metrics"]
    for k in (
        "runs",
        "first_player_win_rate",
        "average_game_length",
        "score_spread",
        "dominant_action_rate",
        "comeback_rate",
        "strategy_distribution",
    ):
        assert k in m
    assert m["runs"] == 20


def test_regress_pass_and_fail():
    base = {"first_player_win_rate": 0.5, "average_game_length": 40.0}
    same = {"first_player_win_rate": 0.51, "average_game_length": 41.0}
    assert regress(base, same)["pass"] is True
    bad = {"first_player_win_rate": 0.8, "average_game_length": 40.0}
    assert regress(base, bad)["pass"] is False


def test_game_terminates():
    g = MicroScavenger()
    g.reset(99)
    from bgd_runtime.core.population import play_one

    r = play_one(MicroScavenger, 99, ["random", "random"])
    assert r["game_length"] > 0
    assert len(r["scores"]) == 2
