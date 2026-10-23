#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["marimo==0.25.2", "jupytext==1.19.6", "jinja2==3.1.6"]
# ///
"""Generate unsolved practice notebooks with marimo convert."""

import argparse
import ast
import json
import os
import re
import subprocess
import sys
import tempfile
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from functools import partial
from pathlib import Path

import jupytext
from jinja2 import Environment, StrictUndefined

PROBLEMS_DIR = Path(__file__).resolve().parent.parent / "leetcode"
RESOURCES_DIR = PROBLEMS_DIR.parent / "src/leetcode_py/cli/resources/leetcode"


def notebook_metadata(output: Path) -> str:
    package_path = Path(os.path.relpath(PROBLEMS_DIR.parent, output.parent)).as_posix()
    return (
        "# /// script\n"
        '# requires-python = ">=3.10"\n'
        '# dependencies = ["marimo==0.25.2", "leetcode-py-sdk[practice]==0.0.0"]\n'
        "# [tool.uv.sources]\n"
        f"# leetcode-py-sdk = {{ path = {json.dumps(package_path)}, editable = true }}\n"
        "# ///\n\n"
    )


def practice_cells(problem_name: str) -> list[tuple[str, bool]]:
    data = json.loads((RESOURCES_DIR / "cookiecutter.json").read_text(encoding="utf-8"))
    data.update(json.loads((RESOURCES_DIR / "json/problems" / f"{problem_name}.json").read_text()))
    template = (RESOURCES_DIR / "{{cookiecutter.problem_name}}/solution.py").read_text()
    solution = (
        Environment(undefined=StrictUndefined).from_string(template).render(cookiecutter=data)
    )
    module = ast.parse(solution)
    deferred = any(
        isinstance(node, ast.ImportFrom) and node.module == "__future__" for node in module.body
    )
    module.body = [
        node
        for node in module.body
        if not (isinstance(node, ast.ImportFrom) and node.module == "__future__")
    ]
    if deferred:
        for node in ast.walk(module):
            if isinstance(node, (ast.arg, ast.AnnAssign)) and node.annotation is not None:
                node.annotation = ast.Constant(ast.unparse(node.annotation))
            elif (
                isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
                and node.returns is not None
            ):
                node.returns = ast.Constant(ast.unparse(node.returns))
    method_names = {item["name"] for item in data["_solution_methods"]["list"]}
    class_name = data["solution_class_name"].split("(")[0]
    for node in module.body:
        if isinstance(node, ast.ClassDef) and node.name == class_name:
            for method in node.body:
                if (
                    isinstance(method, (ast.FunctionDef, ast.AsyncFunctionDef))
                    and method.name in method_names
                ):
                    method.body = ast.parse(
                        f"raise NotImplementedError({f'Implement {method.name}'!r})"
                    ).body
    exports = []
    for node in module.body:
        if isinstance(node, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)):
            exports.append(node.name)
        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            for alias in node.names:
                if alias.name == "*":
                    raise ValueError(f"Wildcard solution import in {problem_name}")
                exports.append(alias.asname or alias.name.split(".")[0])
        elif isinstance(node, (ast.Assign, ast.AnnAssign)):
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            for target in targets:
                exports.extend(n.id for n in ast.walk(target) if isinstance(n, ast.Name))
    bindings = ", ".join(f"{name!r}: {name}" for name in dict.fromkeys(exports))
    solution = ast.unparse(ast.fix_missing_locations(module))
    solution += f"\n\npractice_exports = {{{bindings}}}"
    examples = "\n\n".join(item["content"] for item in data["_readme_examples"]["list"])
    statement = (
        f"# {data['problem_number']}. {data['problem_title']}\n\n"
        f"**{data['difficulty']}** · {data['topics']}\n\n"
        f"{data['readme_description']}\n\n## Examples\n\n{examples}\n\n"
        f"## Constraints\n\n{data['readme_constraints']}\n\n"
        f"{data.get('readme_additional', '')}\n\n"
        "## Your solution\n\nImplement the unfinished methods below, then press **Run tests**."
    )
    statement = "\n".join(line.expandtabs(4).rstrip() for line in statement.splitlines())
    statement_quotes = "'''" if '"""' in statement else '"""'
    return [
        ("import marimo as mo\nfrom leetcode_py.practice import run_practice_tests", True),
        (f"mo.md(r{statement_quotes}\n{statement}\n{statement_quotes})", True),
        (solution, False),
        ('run_tests = mo.ui.run_button(label="Run tests")\nrun_tests', True),
        (
            'mo.stop(not run_tests.value, mo.md("Implement your solution, then run the tests."))\n'
            "test_result = run_practice_tests(mo.notebook_dir(), practice_exports)\n"
            "mo.vstack([\n"
            '    mo.md(f"**{test_result.passed} passed · {test_result.failed} failed · "\n'
            '          f"{test_result.skipped} skipped**"),\n'
            '    mo.md("**All tests passed.**" if test_result.exit_code == 0 '
            'else "**Tests are not passing yet.**"),\n'
            '    mo.accordion({"Test output": mo.plain_text(test_result.output)}),\n'
            "])",
            True,
        ),
        ('mo.md("## Notes\\n\\nRecord your approach, complexity, and edge cases here.")', True),
    ]


def convert_notebook(source: Path, *, force: bool) -> tuple[str, str]:
    output = source.with_name("playground_marimo.py")
    if output.exists() and not force:
        return "skipped", ""

    try:
        cells = practice_cells(source.parent.name)
        with tempfile.TemporaryDirectory(prefix="leetcode-notebook-") as temporary:
            percent = Path(temporary) / "practice.py"
            percent.write_text(
                "\n\n".join(f"# %%\n{code}" for code, _ in cells) + "\n", encoding="utf-8"
            )
            ipynb = percent.with_suffix(".ipynb")
            jupytext.write(jupytext.read(percent), ipynb)
            result = subprocess.run(
                [sys.executable, "-m", "marimo", "convert", str(ipynb)],
                capture_output=True,
                text=True,
                encoding="utf-8",
                check=True,
            )
        decorators = iter(hidden for _, hidden in cells)
        notebook, count = re.subn(
            r"^@app\.cell$",
            lambda _: "@app.cell(hide_code=True)" if next(decorators) else "@app.cell",
            result.stdout,
            flags=re.MULTILINE,
        )
        if count != len(cells):
            raise ValueError(f"Expected {len(cells)} converted cells, received {count}")
        output.write_text(
            notebook_metadata(output) + notebook.rstrip("\n") + "\n", encoding="utf-8"
        )
    except subprocess.CalledProcessError as error:
        return "failed", f"{source}: {error.stderr.strip()}"
    except (OSError, ValueError, SyntaxError) as error:
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
    parser.add_argument(
        "--exclude", action="append", default=[], metavar="PROBLEM", help="Skip a problem by name"
    )
    args = parser.parse_args()
    if args.jobs < 1:
        parser.error("--jobs must be at least 1")

    directory = args.directory.resolve()
    if not directory.is_dir():
        parser.error(f"Not a directory: {directory}")
    sources = sorted(
        source
        for source in directory.rglob("playground.py")
        if source.parent.name not in args.exclude
    )
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
