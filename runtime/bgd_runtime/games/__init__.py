from __future__ import annotations

from typing import Callable

from bgd_runtime.core.game import Game
from bgd_runtime.games.micro_scavenger import MicroScavenger


GAMES: dict[str, Callable[[], Game]] = {
    "micro-scavenger": MicroScavenger,
}


def get_game(name: str) -> Callable[[], Game]:
    key = name.lower().strip()
    if key not in GAMES:
        raise KeyError(f"unknown game: {name}. Known: {sorted(GAMES)}")
    return GAMES[key]
