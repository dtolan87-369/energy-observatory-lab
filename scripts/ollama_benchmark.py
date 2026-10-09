#!/usr/bin/env python3
"""Small repeatable Ollama benchmark for Observatory Local Lab v0.

Usage:
    python scripts/ollama_benchmark.py --model MODEL_NAME

Requires only Python standard library and a locally running Ollama server.
"""

from __future__ import annotations
import argparse
import json
import time
import urllib.request
from pathlib import Path

PROMPTS = [
    """Continue the existing Energy Observatory without inventing a new taxonomy.
Generate 30 candidate Impossible Book phenomenon pages. For each give:
PHENOMENON, USER ACTION, VISIBLE CONSEQUENCE, SIMPLEST MECHANISM, MAIN BUILD RISK.
Prefer diverse physical effects and avoid duplicates.""",

    """Classify the following note without inventing a new Observatory category.
Return: EXISTING FAMILY, EVIDENCE STATUS, WHAT IS ACTUALLY NEW, NEXT SMALLEST ACTION.
Note: A printable compliant joint returns close to its starting angle after manual displacement,
but no force measurement, endurance test or repeatability series has been performed.""",

    """Generate 10 machine-native connector concepts that do not need to be comfortable for a human hand.
For each state the robot-oriented feature, why it helps machine vision/alignment,
and the likely physical failure mode. Avoid cosmetic-only differences."""
]

def ask(model: str, prompt: str) -> tuple[str, float]:
    body = json.dumps({
        "model": model,
        "prompt": prompt,
        "stream": False
    }).encode("utf-8")
    req = urllib.request.Request(
        "http://127.0.0.1:11434/api/generate",
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    t0 = time.perf_counter()
    with urllib.request.urlopen(req, timeout=900) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    return data.get("response", ""), time.perf_counter() - t0

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True)
    ap.add_argument("--out", default="local_ai/benchmark_results")
    args = ap.parse_args()

    outdir = Path(args.out)
    outdir.mkdir(parents=True, exist_ok=True)

    results = []
    for i, prompt in enumerate(PROMPTS, start=1):
        response, seconds = ask(args.model, prompt)
        results.append({
            "task": i,
            "seconds": round(seconds, 2),
            "prompt": prompt,
            "response": response,
        })
        print(f"Task {i}: {seconds:.2f}s")

    stamp = time.strftime("%Y%m%d_%H%M%S")
    outfile = outdir / f"{args.model.replace('/', '_')}_{stamp}.json"
    outfile.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(f"Saved: {outfile}")

if __name__ == "__main__":
    main()
