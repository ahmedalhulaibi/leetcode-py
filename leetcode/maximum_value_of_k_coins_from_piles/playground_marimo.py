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
    # 2218. Maximum Value of K Coins From Piles

    **Hard** · Array, Dynamic Programming, Prefix Sum

    There are `n` **piles** of coins on a table. Each pile consists of a **positive number** of coins of assorted denominations.

    In one move, you can choose any coin on **top** of any pile, remove it, and add it to your wallet.

    Given a list `piles`, where `piles[i]` is a list of integers denoting the composition of the `i`th pile from **top to bottom**, and a positive integer `k`, return *the **maximum total value** of coins you can have in your wallet if you choose **exactly*** `k` *coins optimally*.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2019/11/09/e1.png)

    ```
    Input: piles = [[1,100,3],[7,8,9]], k = 2
    Output: 101
    Explanation: The above diagram shows the different ways we can choose k coins. The maximum total we can obtain is 101.
    ```

    ```
    Input: piles = [[100],[100],[100],[100],[100],[100],[1,1,1,1,1,1,700]], k = 7
    Output: 706
    Explanation: The maximum total can be obtained if we choose all coins from the last pile.
    ```

    ## Constraints

    - n == piles.length
    - 1 <= piles.length <= 10^3
    - 1 <= piles[i][j] <= 10^5
    - 1 <= k <= sum(piles[i].length) <= 2000



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def max_value_of_coins(self, piles: list[list[int]], k: int) -> int:
            raise NotImplementedError('Implement max_value_of_coins')

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
