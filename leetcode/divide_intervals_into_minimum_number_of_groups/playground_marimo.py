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
    # 2406. Divide Intervals Into Minimum Number of Groups

    **Medium** · Array, Two Pointers, Greedy, Sorting, Heap (Priority Queue), Prefix Sum

    You are given a 2D integer array `intervals` where `intervals[i] = [lefti, righti]` represents the inclusive interval `[lefti, righti]`.

    You have to divide the intervals into one or more groups such that each interval is in exactly one group, and no two intervals that are in the same group intersect each other.

    Return the minimum number of groups you need to make.

    Two intervals intersect if there is at least one common number between them. For example, the intervals `[1, 5]` and `[5, 8]` intersect.

    ## Examples

    ```
    Input: intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]
    Output: 3
    Explanation: We can divide the intervals into the following groups:
    - Group 1: [1, 5], [6, 8].
    - Group 2: [2, 3], [5, 10].
    - Group 3: [1, 10].
    It can be proven that it is not possible to divide the intervals into fewer than 3 groups.
    ```

    ```
    Input: intervals = [[1,3],[5,6],[8,10],[11,13]]
    Output: 1
    Explanation: None of the intervals overlap, so we can put all of them in one group.
    ```

    ## Constraints

    - `1 <= intervals.length <= 10^5`
    - `intervals[i].length == 2`
    - `1 <= lefti <= righti <= 10^6`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def min_groups(self, intervals: list[list[int]]) -> int:
            raise NotImplementedError('Implement min_groups')

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
