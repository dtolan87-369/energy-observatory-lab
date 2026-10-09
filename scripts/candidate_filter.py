#!/usr/bin/env python3
"""Cheap first-pass duplicate filter for generated Observatory candidates.

Input: JSON array of objects with at least a "name" field.
Output: unique normalized candidates plus a duplicate report.

This does NOT decide scientific validity, novelty, licence or product readiness.
It only removes obvious naming duplicates before human / model review.
"""

from __future__ import annotations
import argparse
import json
import re
from pathlib import Path

def normalize(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9]+", " ", text)
    words = [w for w in text.split() if w not in {"the", "a", "an", "prototype", "concept"}]
    return " ".join(words)

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("input")
    ap.add_argument("--unique", default="unique_candidates.json")
    ap.add_argument("--duplicates", default="duplicate_candidates.json")
    args = ap.parse_args()

    data = json.loads(Path(args.input).read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise SystemExit("Input must be a JSON array.")

    seen = {}
    unique = []
    duplicates = []

    for item in data:
        name = str(item.get("name", "")).strip()
        if not name:
            duplicates.append({"reason": "missing name", "item": item})
            continue
        key = normalize(name)
        if key in seen:
            duplicates.append({
                "reason": "normalized duplicate",
                "matches": seen[key].get("name"),
                "item": item,
            })
        else:
            seen[key] = item
            unique.append(item)

    Path(args.unique).write_text(json.dumps(unique, indent=2), encoding="utf-8")
    Path(args.duplicates).write_text(json.dumps(duplicates, indent=2), encoding="utf-8")

    print(f"Input: {len(data)}")
    print(f"Unique: {len(unique)}")
    print(f"Duplicates/rejected: {len(duplicates)}")

if __name__ == "__main__":
    main()
