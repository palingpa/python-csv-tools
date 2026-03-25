#!/usr/bin/env python3
"""Normalize CSV headers to lowercase snake_case."""
import argparse
import csv
import re
from pathlib import Path


def snake(s: str) -> str:
    s = s.strip().lower()
    s = re.sub(r"[^a-z0-9]+", "_", s)
    return s.strip("_")


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("input", type=Path)
    p.add_argument("-o", "--output", type=Path, required=True)
    args = p.parse_args()

    with args.input.open(newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)

    if not rows:
        raise SystemExit("empty csv")

    headers = [snake(h) for h in rows[0]]
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows[1:])
    print(f"headers -> {headers}")


if __name__ == "__main__":
    main()

