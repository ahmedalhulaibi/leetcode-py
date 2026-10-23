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
    # 2706. Buy Two Chocolates

    **Easy** · Array, Greedy, Sorting

    You are given an integer array `prices` representing the prices of various chocolates in a store. You are also given a single integer `money`, which represents your initial amount of money.

    You must buy **exactly** two chocolates in such a way that you still have some **non-negative** leftover money. You would like to minimize the sum of the prices of the two chocolates you buy.

    Return *the amount of money you will have leftover after buying the two chocolates*. If there is no way for you to buy two chocolates without ending up in debt, return `money`. Note that the leftover must be non-negative.

    ## Examples

    ```
    Input: prices = [1,2,2], money = 3
    Output: 0
    ```
    **Explanation:** Purchase the chocolates priced at 1 and 2 units respectively. You will have 3 - 3 = 0 units of money afterwards. Thus, we return 0.

    ```
    Input: prices = [3,2,3], money = 3
    Output: 3
    ```
    **Explanation:** You cannot buy 2 chocolates without going in debt, so we return 3.

    ## Constraints

    - 2 <= prices.length <= 50
    - 1 <= prices[i] <= 100
    - 1 <= money <= 100



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def buy_choco(self, prices: list[int], money: int) -> int:
            raise NotImplementedError('Implement buy_choco')

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
