#!/usr/bin/env python3
"""Filter CSV rows by column equality (case-sensitive)."""
import argparse
import csv
from pathlib import Path


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("input", type=Path)
    p.add_argument("-o", "--output", type=Path, required=True)
    p.add_argument("--column", required=True)
    p.add_argument("--equals", required=True)
    args = p.parse_args()

    with args.input.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []
        if args.column not in fieldnames:
            raise SystemExit(f"unknown column: {args.column}")
        rows = [r for r in reader if r.get(args.column) == args.equals]

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"kept {len(rows)} rows")


if __name__ == "__main__":
    main()

