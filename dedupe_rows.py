#!/usr/bin/env python3
"""Drop duplicate CSV rows by one or more columns."""
import argparse
import csv
from pathlib import Path


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("input", type=Path)
    p.add_argument("-o", "--output", type=Path, required=True)
    p.add_argument(
        "-k",
        "--keys",
        nargs="+",
        help="Column names used for uniqueness (default: all columns)",
    )
    args = p.parse_args()

    with args.input.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []
        keys = args.keys or fieldnames
        seen = set()
        rows = []
        for row in reader:
            key = tuple(row.get(k, "") for k in keys)
            if key in seen:
                continue
            seen.add(key)
            rows.append(row)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"wrote {len(rows)} rows -> {args.output}")


if __name__ == "__main__":
    main()

