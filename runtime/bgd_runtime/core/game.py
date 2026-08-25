from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Protocol, Sequence


@dataclass(frozen=True)
class Action:
    """Opaque action token for a game adapter."""

    kind: str
    payload: dict[str, Any] = field(default_factory=dict)

    def key(self) -> str:
        if not self.payload:
            return self.kind
        items = ",".join(f"{k}={self.payload[k]}" for k in sorted(self.payload))
        return f"{self.kind}:{items}"


class Game(Protocol):
    """Minimal stateful game protocol for Monte Carlo."""

    name: str
    rules_version: str

    def reset(self, seed: int) -> None: ...

    @property
    def current_player(self) -> int: ...

    @property
    def num_players(self) -> int: ...

    def legal_actions(self) -> Sequence[Action]: ...

    def step(self, action: Action) -> None: ...

    def is_terminal(self) -> bool: ...

    def scores(self) -> list[float]: ...

    def winner(self) -> int | None:
        """Seat index of sole winner, or None on tie / ongoing."""
        ...

    def observation(self, player: int) -> dict[str, Any]: ...

    def action_histogram(self) -> dict[str, int]:
        """Counts of action kinds taken this game (for metrics)."""
        ...
