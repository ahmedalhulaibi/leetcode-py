"""Run a problem's test bank against notebook-owned implementations."""

import shutil
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path

import cloudpickle


@dataclass(frozen=True)
class PracticeResult:
    exit_code: int
    passed: int
    failed: int
    skipped: int
    output: str


def run_practice_tests(problem_dir: str | Path, exports: Mapping[str, object]) -> PracticeResult:
    problem_dir = Path(problem_dir)
    with tempfile.TemporaryDirectory(prefix="leetcode-practice-") as temporary:
        root = Path(temporary)
        package = root / "practice_problem"
        package.mkdir()
        (package / "__init__.py").write_text("", encoding="utf-8")
        for name in ("helpers.py", "test_solution.py"):
            shutil.copyfile(problem_dir / name, package / name)
        (package / "solution.pkl").write_bytes(cloudpickle.dumps(dict(exports)))
        (package / "solution.py").write_text(
            "from pathlib import Path\n"
            "import cloudpickle\n"
            "globals().update(cloudpickle.loads("
            "Path(__file__).with_suffix('.pkl').read_bytes()))\n",
            encoding="utf-8",
        )
        report = root / "results.xml"
        process = subprocess.run(
            [
                sys.executable,
                "-m",
                "pytest",
                "-q",
                "--tb=short",
                "-p",
                "no:cacheprovider",
                "--import-mode=importlib",
                f"--rootdir={root}",
                f"--junitxml={report}",
                str(package / "test_solution.py"),
            ],
            cwd=root,
            capture_output=True,
            text=True,
            encoding="utf-8",
            check=False,
        )
        passed = failed = skipped = 0
        if report.is_file():
            for suite in ET.parse(report).getroot().iter("testsuite"):
                failures = int(suite.get("failures", "0")) + int(suite.get("errors", "0"))
                skips = int(suite.get("skipped", "0"))
                passed += int(suite.get("tests", "0")) - failures - skips
                failed += failures
                skipped += skips
        return PracticeResult(
            exit_code=process.returncode,
            passed=passed,
            failed=failed,
            skipped=skipped,
            output=process.stdout + process.stderr,
        )
