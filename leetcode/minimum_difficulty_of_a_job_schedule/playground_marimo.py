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
    # 1335. Minimum Difficulty of a Job Schedule

    **Hard** · Array, Dynamic Programming

    You want to schedule a list of jobs in d days. Jobs are dependent (i.e. To work on the ith job, you have to finish all the jobs j where 0 <= j < i).

    You have to finish at least one task every day. The difficulty of a job schedule is the sum of difficulties of each day of the d days. The difficulty of a day is the maximum difficulty of a job done on that day.

    You are given an integer array jobDifficulty and an integer d. The difficulty of the ith job is jobDifficulty[i].

    Return the minimum difficulty of a job schedule. If you cannot find a schedule for the jobs return -1.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2020/01/16/untitled.png)

    ```
    Input: jobDifficulty = [6,5,4,3,2,1], d = 2
    Output: 7
    Explanation: First day you can finish the first 5 jobs, total difficulty = 6.
    Second day you can finish the last job, total difficulty = 1.
    The difficulty of the schedule = 6 + 1 = 7
    ```

    ```
    Input: jobDifficulty = [9,9,9], d = 4
    Output: -1
    Explanation: If you finish a job per day you will still have a free day. you cannot find a schedule for the given jobs.
    ```

    ```
    Input: jobDifficulty = [1,1,1], d = 3
    Output: 3
    Explanation: The schedule is one job per day, total difficulty = 3.
    ```

    ## Constraints

    - 1 <= jobDifficulty.length <= 300
    - 0 <= jobDifficulty[i] <= 1000
    - 1 <= d <= 10



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def min_difficulty(self, job_difficulty: list[int], d: int) -> int:
            raise NotImplementedError('Implement min_difficulty')

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
