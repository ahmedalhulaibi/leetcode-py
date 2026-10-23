# /// script
# requires-python = ">=3.10"
# dependencies = ["marimo==0.25.2", "leetcode-py-sdk[practice]==0.0.0"]
# [tool.uv.sources]
# leetcode-py-sdk = { path = "../..", editable = true }
# ///

import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell(hide_code=True)
def _():
    import marimo as mo
    from leetcode_py.practice import run_practice_tests

    return mo, run_practice_tests


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # 163. Missing Ranges

    **Easy** · Array

    You are given an inclusive range `[lower, upper]` and a **sorted unique** integer array `nums`, where all elements are within the inclusive range.

    A number `x` is considered **missing** if `x` is in the range `[lower, upper]` and `x` is not in `nums`.

    Return the **shortest sorted** list of ranges that **exactly covers all the missing numbers**. That is, no element of `nums` is included in any of the ranges, and each missing number is covered by one of the ranges.

    ## Examples

    ```
    Input: nums = [0,1,3,50,75], lower = 0, upper = 99
    Output: [[2,2],[4,49],[51,74],[76,99]]
    Explanation: The ranges are:
    [2,2]
    [4,49]
    [51,74]
    [76,99]
    ```

    ```
    Input: nums = [-1], lower = -1, upper = -1
    Output: []
    Explanation: There are no missing ranges since there are no missing numbers.
    ```

    ## Constraints

    - -10^9 <= lower <= upper <= 10^9
    - 0 <= nums.length <= 100
    - lower <= nums[i] <= upper
    - All values of nums are unique



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def find_missing_ranges(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
            raise NotImplementedError('Implement find_missing_ranges')

    practice_exports = {'Solution': Solution}
    return (practice_exports,)


@app.cell(hide_code=True)
def _(mo):
    run_tests = mo.ui.run_button(label="Run tests")
    run_tests
    return (run_tests,)


@app.cell(hide_code=True)
def _(mo, practice_exports, run_practice_tests, run_tests):
    mo.stop(not run_tests.value, mo.md("Implement your solution, then run the tests."))
    test_result = run_practice_tests(mo.notebook_dir(), practice_exports)
    mo.vstack([
        mo.md(f"**{test_result.passed} passed · {test_result.failed} failed · "
              f"{test_result.skipped} skipped**"),
        mo.md("**All tests passed.**" if test_result.exit_code == 0 else "**Tests are not passing yet.**"),
        mo.accordion({"Test output": mo.plain_text(test_result.output)}),
    ])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Notes

    Record your approach, complexity, and edge cases here.
    """)
    return


if __name__ == "__main__":
    app.run()
