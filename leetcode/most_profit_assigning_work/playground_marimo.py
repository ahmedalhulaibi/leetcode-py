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
    # 826. Most Profit Assigning Work

    **Medium** · Array, Two Pointers, Binary Search, Greedy, Sorting

    You have n jobs and m workers. You are given three arrays: difficulty, profit, and worker where:

    - difficulty[i] and profit[i] are the difficulty and the profit of the ith job, and
    - worker[j] is the ability of jth worker (i.e., the jth worker can only complete a job with difficulty at most worker[j]).

    Every worker can be assigned at most one job, but one job can be completed multiple times.

    - For example, if three workers attempt the same job that pays $1, then the total profit will be $3. If a worker cannot complete any job, their profit is $0.

    Return the maximum profit we can achieve after assigning the workers to the jobs.

    ## Examples

    ```
    Input: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
    Output: 100
    Explanation: Workers are assigned jobs of difficulty [4,4,6,6] and they get a profit of [20,20,30,30] separately.
    ```

    ```
    Input: difficulty = [85,47,57], profit = [24,66,99], worker = [40,25,25]
    Output: 0
    ```

    ## Constraints

    - n == difficulty.length
    - n == profit.length
    - m == worker.length
    - 1 <= n, m <= 10^4
    - 1 <= difficulty[i], profit[i], worker[i] <= 10^5



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def max_profit_assignment(self, difficulty: list[int], profit: list[int], worker: list[int]) -> int:
            raise NotImplementedError('Implement max_profit_assignment')

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
