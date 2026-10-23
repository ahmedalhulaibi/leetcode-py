#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["marimo==0.25.2", "jupytext==1.19.6"]
# ///
"""Convert Jupytext playgrounds to sibling playground_marimo.py notebooks."""

import argparse
import subprocess
import sys
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from functools import partial
from pathlib import Path

PROBLEMS_DIR = Path(__file__).resolve().parent.parent / "leetcode"


def convert_notebook(source: Path, *, force: bool) -> tuple[str, str]:
    output = source.with_name("playground_marimo.py")
    if output.exists() and not force:
        return "skipped", ""

    try:
        result = subprocess.run(
            [sys.executable, "-m", "marimo", "convert", str(source)],
            capture_output=True,
            text=True,
            encoding="utf-8",
            check=True,
        )
        output.write_text(result.stdout.rstrip("\n") + "\n", encoding="utf-8")
    except subprocess.CalledProcessError as error:
        return "failed", f"{source}: {error.stderr.strip()}"
    except OSError as error:
        return "failed", f"{source}: {error}"

    return "converted", ""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "directory",
        nargs="?",
        type=Path,
        default=PROBLEMS_DIR,
        help="Problem directory or problem bank to search (default: repository leetcode/)",
    )
    parser.add_argument("--jobs", type=int, default=8, help="Parallel conversions (default: 8)")
    parser.add_argument("--force", action="store_true", help="Overwrite existing marimo notebooks")
    args = parser.parse_args()
    if args.jobs < 1:
        parser.error("--jobs must be at least 1")

    directory = args.directory.resolve()
    if not directory.is_dir():
        parser.error(f"Not a directory: {directory}")
    sources = sorted(directory.rglob("playground.py"))
    if not sources:
        parser.error(f"No playground.py notebooks found in {directory}")

    counts: Counter[str] = Counter()
    with ThreadPoolExecutor(max_workers=args.jobs) as executor:
        for status, error in executor.map(partial(convert_notebook, force=args.force), sources):
            counts[status] += 1
            if error:
                print(error, file=sys.stderr)

    print(
        f"Converted {counts['converted']}, skipped {counts['skipped']}, "
        f"failed {counts['failed']} notebook(s)."
    )
    return 1 if counts["failed"] else 0


if __name__ == "__main__":
    sys.exit(main())
