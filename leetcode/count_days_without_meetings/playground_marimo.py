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
    # 3169. Count Days Without Meetings

    **Medium** · Array, Sorting

    You are given a positive integer `days` representing the total number of days an employee is available for work (starting from day 1). You are also given a 2D array `meetings` of size `n` where, `meetings[i] = [starti, endi]` represents the starting and ending days of meeting `i` (inclusive).

    Return the count of days when the employee is available for work but no meetings are scheduled.

    **Note:** The meetings may overlap.

    ## Examples

    ```
    Input: days = 10, meetings = [[5,7],[1,3],[9,10]]
    Output: 2
    ```
    **Explanation:** There is no meeting scheduled on the 4th and 8th days.

    ```
    Input: days = 5, meetings = [[2,4],[1,3]]
    Output: 1
    ```
    **Explanation:** There is no meeting scheduled on the 5th day.

    ```
    Input: days = 6, meetings = [[1,6]]
    Output: 0
    ```
    **Explanation:** Meetings are scheduled for all working days.

    ## Constraints

    - `1 <= days <= 10^9`
    - `1 <= meetings.length <= 10^5`
    - `meetings[i].length == 2`
    - `1 <= meetings[i][0] <= meetings[i][1] <= days`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def count_days(self, days: int, meetings: list[list[int]]) -> int:
            raise NotImplementedError('Implement count_days')

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
