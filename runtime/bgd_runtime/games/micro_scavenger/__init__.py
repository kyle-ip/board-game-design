from __future__ import annotations

"""Micro-Scavenger — 2p set-collection example from skill templates."""

from collections import Counter
from dataclasses import dataclass, field
import random
from typing import Any, Sequence

from bgd_runtime.agents.params import PlayerParams
from bgd_runtime.core.game import Action

# Deck: 4× each of 6 cards; tags from components-sheet
CARD_DEFS: list[tuple[str, str]] = [
    ("CARD-01", "metal"),
    ("CARD-02", "glass"),
    ("CARD-03", "rubber"),
    ("CARD-04", "tech"),
    ("CARD-05", "cloth"),
    ("CARD-06", "metal"),
]

HAND_LIMIT = 3
PLAYERS = 2


def convert_vp(n: int) -> int:
    if n >= 4:
        return 6
    if n == 3:
        return 3
    if n == 2:
        return 1
    return 0


@dataclass
class Card:
    card_id: str
    tag: str


def build_deck() -> list[Card]:
    deck: list[Card] = []
    for card_id, tag in CARD_DEFS:
        for _ in range(4):
            deck.append(Card(card_id=card_id, tag=tag))
    return deck


@dataclass
class MicroScavenger:
    name: str = "micro-scavenger"
    rules_version: str = "R-ms-001"
    hand_limit: int = HAND_LIMIT
    _rng: random.Random = field(default_factory=random.Random, repr=False)
    _deck: list[Card] = field(default_factory=list)
    _discard: list[Card] = field(default_factory=list)
    _hands: list[list[Card]] = field(default_factory=list)
    _scores: list[float] = field(default_factory=list)
    _current: int = 0
    _turns_after_empty: int = 0
    _deck_was_empty: bool = False
    _action_hist: dict[str, int] = field(default_factory=dict)
    _turn_count: int = 0
    _lead_changes: int = 0
    _last_leader: int | None = None

    @property
    def num_players(self) -> int:
        return PLAYERS

    @property
    def current_player(self) -> int:
        return self._current

    def reset(self, seed: int) -> None:
        self._rng = random.Random(seed)
        self._deck = build_deck()
        self._rng.shuffle(self._deck)
        self._discard = []
        if self._deck:
            self._discard.append(self._deck.pop())
        self._hands = [[], []]
        for p in range(PLAYERS):
            for _ in range(3):
                if self._deck:
                    self._hands[p].append(self._deck.pop())
        self._scores = [0.0, 0.0]
        self._current = 0
        self._turns_after_empty = 0
        self._deck_was_empty = False
        self._action_hist = {}
        self._turn_count = 0
        self._lead_changes = 0
        self._last_leader = None

    def legal_actions(self) -> Sequence[Action]:
        if self.is_terminal():
            return []
        p = self._current
        hand = self._hands[p]
        actions: list[Action] = []
        if self._deck:
            actions.append(Action("take_deck"))
        if self._discard:
            actions.append(Action("take_discard"))
        # Convert: discard 2+ cards sharing a tag
        tags = Counter(c.tag for c in hand)
        for tag, count in tags.items():
            if count >= 2:
                for n in range(2, count + 1):
                    actions.append(Action("convert", {"tag": tag, "count": n}))
        # Always need at least one action — if hand empty and no deck/discard (shouldn't happen), pass
        if not actions:
            actions.append(Action("pass"))
        return actions

    def step(self, action: Action) -> None:
        if self.is_terminal():
            raise RuntimeError("game already terminal")
        p = self._current
        kind = action.kind
        self._action_hist[kind] = self._action_hist.get(kind, 0) + 1
        self._turn_count += 1

        if kind == "take_deck":
            if not self._deck:
                raise ValueError("deck empty")
            self._hands[p].append(self._deck.pop())
        elif kind == "take_discard":
            if not self._discard:
                raise ValueError("discard empty")
            self._hands[p].append(self._discard.pop())
        elif kind == "convert":
            tag = action.payload["tag"]
            n = int(action.payload["count"])
            idxs = [i for i, c in enumerate(self._hands[p]) if c.tag == tag]
            if len(idxs) < n:
                raise ValueError("not enough tagged cards")
            # Discard first n matching (stable order)
            remove = set(idxs[:n])
            kept: list[Card] = []
            for i, c in enumerate(self._hands[p]):
                if i in remove:
                    self._discard.append(c)
                else:
                    kept.append(c)
            self._hands[p] = kept
            self._scores[p] += convert_vp(n)
        elif kind == "pass":
            pass
        else:
            raise ValueError(f"unknown action {kind}")

        # Hand limit at end of turn
        while len(self._hands[p]) > self.hand_limit:
            # Discard last card (simple deterministic policy for rules)
            self._discard.append(self._hands[p].pop())

        self._track_leader()

        if not self._deck:
            if not self._deck_was_empty:
                self._deck_was_empty = True
                self._turns_after_empty = 0
            else:
                self._turns_after_empty += 1
        self._current = 1 - self._current

    def _track_leader(self) -> None:
        if self._scores[0] == self._scores[1]:
            leader = None
        else:
            leader = 0 if self._scores[0] > self._scores[1] else 1
        if leader is not None and self._last_leader is not None and leader != self._last_leader:
            self._lead_changes += 1
        if leader is not None:
            self._last_leader = leader

    def is_terminal(self) -> bool:
        # When deck empties, finish the round so both have equal turns
        if not self._deck_was_empty:
            return False
        # After deck first becomes empty on someone's turn, we need one more turn for the opponent
        # _turns_after_empty counts completed turns after the emptying turn's end.
        # Emptying turn: deck_was_empty set, turns_after=0, switch player.
        # Opponent plays → turns_after=1 → terminal.
        return self._turns_after_empty >= 1

    def scores(self) -> list[float]:
        return list(self._scores)

    def winner(self) -> int | None:
        if not self.is_terminal():
            return None
        if self._scores[0] > self._scores[1]:
            return 0
        if self._scores[1] > self._scores[0]:
            return 1
        # Tie-break: most cards in hand
        h0, h1 = len(self._hands[0]), len(self._hands[1])
        if h0 > h1:
            return 0
        if h1 > h0:
            return 1
        return None

    def action_histogram(self) -> dict[str, int]:
        return dict(self._action_hist)

    def observation(self, player: int) -> dict[str, Any]:
        hand = self._hands[player]
        top = self._discard[-1] if self._discard else None

        def action_scores(action: Action, params: PlayerParams) -> float:
            return self._score_action(action, player, params)

        return {
            "player": player,
            "hand": [(c.card_id, c.tag) for c in hand],
            "hand_tags": [c.tag for c in hand],
            "scores": list(self._scores),
            "deck_size": len(self._deck),
            "discard_top": (top.card_id, top.tag) if top else None,
            "turn": self._turn_count,
            "action_scores": action_scores,
        }

    def _score_action(self, action: Action, player: int, params: PlayerParams) -> float:
        hand = self._hands[player]
        opp = 1 - player
        score = 0.0
        if action.kind == "convert":
            n = int(action.payload["count"])
            vp = convert_vp(n)
            score += vp * (1.0 + 0.3 * params.aggression)
            # Prefer converting when hand near limit
            if len(hand) >= self.hand_limit:
                score += 1.0
            # Strategic: prefer larger sets slightly
            score += 0.2 * n * (params.planning_horizon / 3.0)
            # Weak 2-card converts should not eternally block deck draws
            if n == 2:
                score -= 0.4
        elif action.kind == "take_discard":
            top = self._discard[-1]
            tags = Counter(c.tag for c in hand)
            score += 0.5 + tags.get(top.tag, 0) * (0.8 + 0.4 * params.aggression)
            if params.opponent_awareness > 0.5:
                score += 0.2 * params.opponent_awareness
        elif action.kind == "take_deck":
            tags = Counter(c.tag for c in hand)
            # Strong baseline so games progress toward empty deck
            score += 1.2 + 0.02 * self._turn_count
            score += 0.4 * (1.0 - params.risk_tolerance)
            if len(hand) < self.hand_limit:
                score += 0.3
            if len(tags) <= 1:
                score += 0.2 * params.exploration
        elif action.kind == "pass":
            score -= 10.0
        # Adversarial: slight preference to keep lead
        if params.aggression > 0.7 and self._scores[player] <= self._scores[opp]:
            if action.kind == "convert":
                score += 0.5
        return score
