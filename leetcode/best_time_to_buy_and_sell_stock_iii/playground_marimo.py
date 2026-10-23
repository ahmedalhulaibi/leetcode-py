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
    # 123. Best Time to Buy and Sell Stock III

    **Hard** · Array, Dynamic Programming

    You are given an array `prices` where `prices[i]` is the price of a given stock on the `i^th` day.

    Find the maximum profit you can achieve. You may complete at most **two transactions**.

    **Note:** You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

    ## Examples

    ```
    Input: prices = [3,3,5,0,0,3,1,4]
    Output: 6
    ```
    **Explanation:** Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3. Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3. Total profit is 3 + 3 = 6.

    ```
    Input: prices = [1,2,3,4,5]
    Output: 4
    ```
    **Explanation:** Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4. Total profit is 4.

    ```
    Input: prices = [7,6,4,3,1]
    Output: 0
    ```
    **Explanation:** In this case, no transaction is done, i.e. max profit = 0.

    ## Constraints

    - 1 <= prices.length <= 10^5
    - 0 <= prices[i] <= 10^5



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def max_profit(self, prices: list[int]) -> int:
            raise NotImplementedError('Implement max_profit')

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
