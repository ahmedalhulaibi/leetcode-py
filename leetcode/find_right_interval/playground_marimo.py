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
    # 436. Find Right Interval

    **Medium** · Array, Binary Search, Sorting

    You are given an array of intervals, where intervals[i] = [starti, endi] and each starti is unique.

    The right interval for an interval i is an interval j such that startj >= endi and startj is minimized. Note that i may equal j.

    Return an array of right interval indices for each interval i. If no right interval exists for interval i, then put -1 at index i.

    ## Examples

    ```
    Input: intervals = [[1,2]]
    Output: [-1]
    Explanation: There is only one interval in the collection, so it outputs -1.
    ```

    ```
    Input: intervals = [[3,4],[2,3],[1,2]]
    Output: [-1,0,1]
    Explanation: There is no right interval for [3,4].
    The right interval for [2,3] is [3,4] since start0 = 3 is the smallest start that is >= end1 = 3.
    The right interval for [1,2] is [2,3] since start1 = 2 is the smallest start that is >= end2 = 2.
    ```

    ```
    Input: intervals = [[1,4],[2,3],[3,4]]
    Output: [-1,2,-1]
    Explanation: There is no right interval for [1,4] and [3,4].
    The right interval for [2,3] is [3,4] since start2 = 3 is the smallest start that is >= end1 = 3.
    ```

    ## Constraints

    1 <= intervals.length <= 2 * 10^4
    intervals[i].length == 2
    -10^6 <= starti <= endi <= 10^6
    The start point of each interval is unique.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def find_right_interval(self, intervals: list[list[int]]) -> list[int]:
            raise NotImplementedError('Implement find_right_interval')

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
