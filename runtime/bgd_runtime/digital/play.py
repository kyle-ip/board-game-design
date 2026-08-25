from __future__ import annotations

"""Minimal P2: human vs heuristic CLI for supported adapters."""

import random
import sys

from bgd_runtime.agents.heuristic import HeuristicAgent
from bgd_runtime.agents.params import PROFILES
from bgd_runtime.games import get_game


def play_cli(game_name: str = "micro-scavenger", seed: int = 42, opponent: str = "greedy") -> None:
    factory = get_game(game_name)
    game = factory()
    game.reset(seed)
    bot = HeuristicAgent(PROFILES[opponent])
    rng = random.Random(seed ^ 0xBEEF)

    print(f"{game_name} | seed={seed} | you=seat0 | opponent={opponent}")
    print("System evidence only — this does not validate fun.\n")

    while not game.is_terminal():
        p = game.current_player
        legal = list(game.legal_actions())
        obs = game.observation(p)
        if p == 0:
            print(f"--- Your turn | scores={game.scores()} | deck={obs.get('deck_size')} ---")
            print(f"Hand: {obs.get('hand')}")
            print(f"Discard top: {obs.get('discard_top')}")
            for i, a in enumerate(legal):
                print(f"  [{i}] {a.key()}")
            while True:
                raw = input("Choose action index (or q): ").strip()
                if raw.lower() == "q":
                    print("Aborted.")
                    return
                try:
                    idx = int(raw)
                    action = legal[idx]
                    break
                except (ValueError, IndexError):
                    print("Invalid.")
            game.step(action)
        else:
            action = bot.select(obs, legal, rng)
            print(f"Opponent plays: {action.key()}")
            game.step(action)

    print(f"\nFinal scores: {game.scores()} winner={game.winner()}")
    print("Escalate to P3/P4 for experience evidence (TTS / paper).")


def main(argv: list[str] | None = None) -> None:
    argv = list(sys.argv[1:] if argv is None else argv)
    game = "micro-scavenger"
    seed = 42
    opponent = "greedy"
    # tiny argv parse: --seed N --opponent P
    i = 0
    while i < len(argv):
        if argv[i] == "--seed" and i + 1 < len(argv):
            seed = int(argv[i + 1])
            i += 2
        elif argv[i] == "--opponent" and i + 1 < len(argv):
            opponent = argv[i + 1]
            i += 2
        elif argv[i] == "--game" and i + 1 < len(argv):
            game = argv[i + 1]
            i += 2
        else:
            i += 1
    play_cli(game, seed, opponent)


if __name__ == "__main__":
    main()
