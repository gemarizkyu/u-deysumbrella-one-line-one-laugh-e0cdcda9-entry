#!/usr/bin/env python3
"""One Line, One Laugh — entry program.

Writes a single funny line (1-140 characters) to /output/entry.txt.
Deterministic: no network, no randomness, no wall clock, no model calls.
The joke turns on one word — "cloud" — where a will's bequest lands.
"""
import os

LINE = "I asked AI to write my will, and it left everything to the cloud."

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"Wrote {len(LINE)} characters to {path}")

if __name__ == "__main__":
    main()
