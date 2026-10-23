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
    # 228. Summary Ranges

    **Easy** · Array

    You are given a **sorted unique** integer array `nums`.

    A **range** `[a,b]` is the set of all integers from `a` to `b` (inclusive).

    Return *the **smallest sorted** list of ranges that **cover all the numbers in the array exactly***. That is, each element of `nums` is covered by exactly one of the ranges, and there is no integer `x` such that `x` is in one of the ranges but not in `nums`.

    Each range `[a,b]` in the list should be output as:

    - `"a->b"` if `a != b`
    - `"a"` if `a == b`

    ## Examples

    ```
    Input: nums = [0,1,2,4,5,7]
    Output: ["0->2","4->5","7"]
    ```
    **Explanation:** The ranges are:
    [0,2] --> "0->2"
    [4,5] --> "4->5"
    [7,7] --> "7"

    ```
    Input: nums = [0,2,3,4,6,8,9]
    Output: ["0","2->4","6","8->9"]
    ```
    **Explanation:** The ranges are:
    [0,0] --> "0"
    [2,4] --> "2->4"
    [6,6] --> "6"
    [8,9] --> "8->9"

    ## Constraints

    - `0 <= nums.length <= 20`
    - `-2^31 <= nums[i] <= 2^31 - 1`
    - All the values of `nums` are **unique**.
    - `nums` is sorted in ascending order.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def summary_ranges(self, nums: list[int]) -> list[str]:
            raise NotImplementedError('Implement summary_ranges')

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
