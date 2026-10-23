import runpy
import shutil
from dataclasses import FrozenInstanceError
from pathlib import Path

import pytest

from leetcode_py.practice import PracticeResult, run_practice_tests

REPOSITORY = Path(__file__).resolve().parents[2]
INPUTS = REPOSITORY / "tests" / "testdata" / "inputs" / "practice"


@pytest.mark.parametrize(
    "problem,case_count,path_type",
    [
        ("two_sum", 15, str),
        ("reverse_linked_list", 15, Path),
        ("lru_cache", 12, Path),
    ],
)
def test_current_notebook_exports_control_the_full_bank(
    tmp_path: Path, problem: str, case_count: int, path_type: type
) -> None:
    problem_dir = tmp_path / problem
    problem_dir.mkdir()
    for name in ("__init__.py", "helpers.py", "test_solution.py"):
        shutil.copyfile(REPOSITORY / "leetcode" / problem / name, problem_dir / name)
    shutil.copyfile(INPUTS / "poison_reference.py", problem_dir / "solution.py")
    sources_before = {path.name: path.read_bytes() for path in problem_dir.iterdir()}
    make_exports = runpy.run_path(str(INPUTS / f"{problem}.py"))["make_exports"]

    for completed in (False, True, False):
        result = run_practice_tests(path_type(problem_dir), make_exports(completed))

        assert isinstance(result, PracticeResult)
        assert (result.exit_code, result.passed, result.failed, result.skipped) == (
            (0, case_count, 0, 0) if completed else (1, 0, case_count, 0)
        ), result.output
        assert isinstance(result.output, str)
        assert result.output.strip() != ""
        assert {
            name: (problem_dir / name).read_bytes() for name in sources_before
        } == sources_before
        assert sorted(path.name for path in problem_dir.glob("*.py")) == sorted(sources_before)


@pytest.mark.parametrize("attribute", ("exit_code", "passed", "failed", "skipped", "output"))
def test_result_is_immutable(attribute: str) -> None:
    result = PracticeResult(exit_code=0, passed=15, failed=0, skipped=0, output="15 passed")

    with pytest.raises(FrozenInstanceError):
        setattr(result, attribute, 1)
