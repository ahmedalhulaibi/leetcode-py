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
    # 757. Set Intersection Size At Least Two

    **Hard** · Array, Greedy, Sorting

    You are given a 2D integer array `intervals` where `intervals[i] = [starti, endi]` represents all the integers from `starti` to `endi` inclusively.

    A **containing set** is an array `nums` where each interval from `intervals` has **at least two** integers in `nums`.

    For example, if `intervals = [[1,3], [3,7], [8,9]]`, then `[1,2,4,7,8,9]` and `[2,3,4,8,9]` are containing sets.

    Return the minimum possible size of a containing set.

    ## Examples

    ```
    Input: intervals = [[1,3],[3,7],[8,9]]
    Output: 5
    ```
    **Explanation:** let nums = [2, 3, 4, 8, 9]. It can be shown that there cannot be any containing array of size 4.

    ```
    Input: intervals = [[1,3],[1,4],[2,5],[3,5]]
    Output: 3
    ```
    **Explanation:** let nums = [2, 3, 4]. It can be shown that there cannot be any containing array of size 2.

    ```
    Input: intervals = [[1,2],[2,3],[2,4],[4,5]]
    Output: 5
    ```
    **Explanation:** let nums = [1, 2, 3, 4, 5]. It can be shown that there cannot be any containing array of size 4.

    ## Constraints

    - `1 <= intervals.length <= 3000`
    - `intervals[i].length == 2`
    - `0 <= starti < endi <= 10^8`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def intersection_size_two(self, intervals: list[list[int]]) -> int:
            raise NotImplementedError('Implement intersection_size_two')

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
