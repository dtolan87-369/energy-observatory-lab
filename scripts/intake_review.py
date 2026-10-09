#!/usr/bin/env python3
"""Automation 001: offline, read-only candidate identity screen.

Use on explicitly selected local JSON exports. No network, credentials,
Airtable writes, GitHub issues, evidence upgrades, merging or publication.

Output means 'check these candidates' rather than 'duplicates proven'.
Absence of a hit never proves novelty or that an archive was checked.
"""
from __future__ import annotations

import argparse
from difflib import SequenceMatcher
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

from candidate_filter import normalize

_DOI = re.compile(r"10\.\d{4,9}/[^\s\"<>]+", re.IGNORECASE)


def field(record: dict, *keys: str) -> str:
    payload = record.get("fields", record)
    for key in keys:
        value = payload.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()
    return ""


def name(record: dict) -> str:
    return field(record, "Candidate", "name", "Name", "title", "Title")


def source(record: dict) -> str:
    return field(record, "Source / URL", "source", "url", "URL")


def doi(record: dict) -> str:
    raw = " ".join([field(record, "doi", "DOI"), source(record)])
    m = _DOI.search(unquote(raw))
    return m.group(0).rstrip(".,;:)]}").lower() if m else ""


def canonical_url(raw: str) -> str:
    raw = raw.strip()
    if not raw or not re.match(r"^https?://", raw, re.IGNORECASE):
        return ""
    u = urlsplit(raw)
    host = (u.hostname or "").lower().removeprefix("www.")
    path = unquote(u.path).rstrip("/")
    if host == "github.com":
        path = path.removesuffix(".git")
    # For other hosts, query components can be significant identifiers.
    suffix = "" if host in {"github.com", "gitlab.com", "codeberg.org"} else (
        "?" + u.query if u.query else "")
    return host + path.lower() + suffix


def screen(incoming: list[dict], existing: list[dict]) -> list[dict]:
    reports = []
    for candidate in incoming:
        candidate_name = name(candidate)
        if not candidate_name:
            reports.append({"candidate": None, "review_required": True,
                            "error": "missing candidate name", "possible_matches": [],
                            "archive_coverage": "NOT CHECKED"})
            continue
        nk, sk, dk = normalize(candidate_name), canonical_url(source(candidate)), doi(candidate)
        matches = []
        for record in existing:
            if not name(record):
                continue
            rk, rs, rd = normalize(name(record)), canonical_url(source(record)), doi(record)
            reasons = []
            if nk and rk == nk:
                reasons.append("normalized-name match")
            if sk and rs == sk:
                reasons.append("source URL match")
            if dk and rd == dk:
                reasons.append("DOI match")
            if not reasons and len(nk) >= 10 and len(rk) >= 10:
                ratio = SequenceMatcher(None, nk, rk).ratio()
                if ratio >= 0.86:
                    reasons.append(f"similar-name hint ({ratio:.2f})")
            if reasons:
                matches.append({"candidate": name(record), "source": source(record),
                                "reasons": reasons})
        reports.append({"candidate": candidate_name, "source": source(candidate),
                        "possible_matches": matches, "review_required": True,
                        "result": ("possible identity overlap — human check" if matches else
                                   "no match in supplied snapshot — NOT a novelty finding"),
                        "archive_coverage": "ONLY supplied local JSON; Dropbox/Drive/GitHub not checked"})
    return reports


def read_records(path: str) -> list[dict]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if isinstance(data, dict) and isinstance(data.get("records"), list):
        data = data["records"]
    if not isinstance(data, list) or not all(isinstance(row, dict) for row in data):
        raise ValueError(f"{path}: expected JSON array (or object with records array)")
    return data


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--incoming", required=True, help="Local JSON candidate(s)")
    parser.add_argument("--existing", required=True, help="Local JSON candidate snapshot")
    parser.add_argument("--output", default="intake_review.local.json")
    args = parser.parse_args()
    report = screen(read_records(args.incoming), read_records(args.existing))
    Path(args.output).write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Review candidates: {len(report)}; possible overlaps: "
          f"{sum(bool(row['possible_matches']) for row in report)}")
    print("Read-only screen complete. Verify archive aliases, licence and GitHub issues.")


if __name__ == "__main__":
    main()
