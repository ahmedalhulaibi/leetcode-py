#!/usr/bin/env bash
set -euo pipefail

repo_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
cd -- "$repo_dir"

exec uv run --project "$repo_dir" --with marimo==0.25.2 \
    python -m marimo edit "$repo_dir" \
    --sandbox --headless --host 127.0.0.1 --port 2718 --no-token "$@"
