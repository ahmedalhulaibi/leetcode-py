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
    # 518. Coin Change II

    **Medium** · Array, Dynamic Programming

    You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.

    Return *the number of combinations that make up that amount*. If that amount of money cannot be made up by any combination of the coins, return `0`.

    You may assume that you have an infinite number of each kind of coin.

    The final answer is **guaranteed** to fit into a signed 32-bit integer.

    ## Examples

    ```
    Input: amount = 5, coins = [1,2,5]
    Output: 4
    ```
    **Explanation:** there are four ways to make up the amount:
    5=5
    5=2+2+1
    5=2+1+1+1
    5=1+1+1+1+1

    ```
    Input: amount = 3, coins = [2]
    Output: 0
    ```
    **Explanation:** the amount of 3 cannot be made up just with coins of 2.

    ```
    Input: amount = 10, coins = [10]
    Output: 1
    ```

    ## Constraints

    - 1 <= coins.length <= 300
    - 1 <= coins[i] <= 5000
    - All the values of `coins` are **unique**.
    - 0 <= amount <= 5000



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def change(self, amount: int, coins: list[int]) -> int:
            raise NotImplementedError('Implement change')

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
