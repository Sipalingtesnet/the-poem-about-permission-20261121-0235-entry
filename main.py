#!/usr/bin/env python3
"""make.fun entry: writes the poem about permission to /output/entry.txt.

Reads poem.txt from the directory beside this file (never a relative path,
because the grader runs main.py from a different working directory), validates
that it is UTF-8 text of 1-280 Unicode code points and not only white space,
then writes its exact contents to the output directory (env MAKEFUN_OUTPUT_DIR,
default /output) as entry.txt, creating the directory if needed.
"""

import os
import sys
from pathlib import Path

# The poem lives beside this script, wherever the script is invoked from.
POEM_PATH = Path(__file__).resolve().parent / "poem.txt"


def main() -> int:
    if not POEM_PATH.is_file():
        raise FileNotFoundError(
            f"poem.txt not found beside main.py (looked at {POEM_PATH})"
        )

    poem = POEM_PATH.read_text(encoding="utf-8")

    # Hard gate: 1-280 Unicode code points, and not only white space.
    if not (1 <= len(poem) <= 280):
        raise ValueError(
            f"poem.txt must be 1-280 Unicode code points, got {len(poem)}"
        )
    if poem.strip() == "":
        raise ValueError("poem.txt must contain at least one non-white-space character")

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / "entry.txt"
    out_file.write_text(poem, encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())