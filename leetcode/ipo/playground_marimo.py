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
    # 502. IPO

    **Hard** · Array, Greedy, Sorting, Heap (Priority Queue)

    Suppose LeetCode will start its IPO soon. To sell a good price of its shares, it can only finish at most `k` distinct projects before the IPO. Help LeetCode maximize its total capital.

    You are given `n` projects where the `ith` project has a pure profit `profits[i]` and a minimum capital `capital[i]` is needed to start it.

    Initially, you have `w` capital. When you finish a project, you obtain its pure profit, which is added to your total capital.

    Pick a list of **at most** `k` distinct projects to **maximize your final capital**, and return the final maximized capital.

    ## Examples

    ```
    Input: k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
    Output: 4
    Explanation: Start with capital 0, only project 0 is affordable. Finish it -> capital 1. Now projects 1 and 2 are affordable; finish project 2 -> capital 4.
    ```

    ```
    Input: k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]
    Output: 6
    ```

    ## Constraints

    - 1 <= k <= 10^5
    - 0 <= w <= 10^9
    - n == profits.length
    - n == capital.length
    - 1 <= n <= 10^5
    - 0 <= profits[i] <= 10^4
    - 0 <= capital[i] <= 10^9



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    import heapq

    class Solution:

        def find_maximized_capital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
            raise NotImplementedError('Implement find_maximized_capital')

    practice_exports = {'heapq': heapq, 'Solution': Solution}
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
