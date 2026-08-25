#!/usr/bin/env python3
"""
Validate cards.json against tools/component-schema.json.
Maintainer / optional pipeline tool — not required for agent Markdown workflow.

Usage:
  python eval/validators/validate_components.py path/to/cards.json
  python eval/validators/validate_components.py tools/examples/cards.json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_SCHEMA = SKILL_ROOT / "tools" / "component-schema.json"

ID_PATTERN = re.compile(r"^[A-Z]+-\d{3}$")
ALLOWED_TYPES = {"card", "tile", "board", "token", "die", "other"}


def load_json(path: Path) -> object:
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def validate_instance(data: object, schema: dict) -> list[str]:
    """Minimal Draft-2020-12 subset matching component-schema.json (no external deps)."""
    errors: list[str] = []

    if not isinstance(data, dict):
        return ["root: expected object"]

    for key in schema.get("required", []):
        if key not in data:
            errors.append(f"root: missing required property '{key}'")

    if "game" in data and not isinstance(data["game"], str):
        errors.append("game: must be string")
    if "version" in data and not isinstance(data["version"], str):
        errors.append("version: must be string")

    cards = data.get("cards")
    if cards is None:
        return errors
    if not isinstance(cards, list):
        errors.append("cards: must be array")
        return errors

    item_schema = (
        schema.get("properties", {})
        .get("cards", {})
        .get("items", {})
    )
    required_card = item_schema.get("required", ["id", "name", "type"])

    for i, card in enumerate(cards):
        prefix = f"cards[{i}]"
        if not isinstance(card, dict):
            errors.append(f"{prefix}: expected object")
            continue
        for key in required_card:
            if key not in card:
                errors.append(f"{prefix}: missing required property '{key}'")
        if "id" in card:
            if not isinstance(card["id"], str) or not ID_PATTERN.match(card["id"]):
                errors.append(f"{prefix}.id: must match ^[A-Z]+-\\d{{3}}$ (got {card['id']!r})")
        if "type" in card and card["type"] not in ALLOWED_TYPES:
            errors.append(f"{prefix}.type: must be one of {sorted(ALLOWED_TYPES)}")
        if "name" in card and not isinstance(card["name"], str):
            errors.append(f"{prefix}.name: must be string")
        if "qty" in card:
            if not isinstance(card["qty"], int) or isinstance(card["qty"], bool) or card["qty"] < 1:
                errors.append(f"{prefix}.qty: must be integer >= 1")
        if "vp" in card:
            if not isinstance(card["vp"], int) or isinstance(card["vp"], bool) or card["vp"] < 0:
                errors.append(f"{prefix}.vp: must be integer >= 0")
        for str_field in ("cost", "effect", "tags", "notes"):
            if str_field in card and not isinstance(card[str_field], str):
                errors.append(f"{prefix}.{str_field}: must be string")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate component JSON against skill schema")
    parser.add_argument("cards_json", help="Path to cards.json")
    parser.add_argument(
        "--schema",
        default=str(DEFAULT_SCHEMA),
        help="Path to component-schema.json",
    )
    args = parser.parse_args()

    cards_path = Path(args.cards_json)
    schema_path = Path(args.schema)

    if not cards_path.exists():
        print(f"FAIL: file not found: {cards_path}", file=sys.stderr)
        return 2
    if not schema_path.exists():
        print(f"FAIL: schema not found: {schema_path}", file=sys.stderr)
        return 2

    try:
        data = load_json(cards_path)
        schema = load_json(schema_path)
    except json.JSONDecodeError as e:
        print(f"FAIL: invalid JSON: {e}", file=sys.stderr)
        return 1

    if not isinstance(schema, dict):
        print("FAIL: schema root must be object", file=sys.stderr)
        return 1

    errors = validate_instance(data, schema)
    if errors:
        print(f"FAIL: {cards_path} ({len(errors)} error(s))")
        for err in errors:
            print(f"  - {err}")
        return 1

    n = len(data["cards"]) if isinstance(data, dict) and isinstance(data.get("cards"), list) else 0
    print(f"PASS: {cards_path} ({n} cards) against {schema_path.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
