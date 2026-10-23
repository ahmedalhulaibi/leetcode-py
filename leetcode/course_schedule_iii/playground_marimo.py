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
    # 630. Course Schedule III

    **Hard** · Array, Greedy, Sorting, Heap (Priority Queue)

    There are `n` different online courses numbered from `1` to `n`. You are given an array `courses` where `courses[i] = [duration_i, lastDay_i]` indicate that the `i_th` course should be taken **continuously** for `duration_i` days and must be finished before or on `lastDay_i`.

    You will start on the `1_st` day and you cannot take two or more courses simultaneously.

    Return *the maximum number of courses that you can take*.

    ## Examples

    ```
    Input: courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
    Output: 3
    Explanation: There are totally 4 courses, but you can take 3 courses at most:
    First, take the 1st course, it costs 100 days so you will finish it on the 100th day, and ready to take the next course on the 101st day.
    Second, take the 3rd course, it costs 1000 days so you will finish it on the 1100th day, and ready to take the next course on the 1101st day.
    Third, take the 2nd course, it costs 200 days so you will finish it on the 1300th day.
    The 4th course cannot be taken now, since you will finish it on the 3300th day, which exceeds the closed date.
    ```

    ```
    Input: courses = [[1,2]]
    Output: 1
    ```

    ```
    Input: courses = [[3,2],[4,3]]
    Output: 0
    ```

    ## Constraints

    - `1 <= courses.length <= 10^4`
    - `1 <= duration_i, lastDay_i <= 10^4`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def schedule_course(self, courses: list[list[int]]) -> int:
            raise NotImplementedError('Implement schedule_course')

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
