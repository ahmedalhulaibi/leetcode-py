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
    # 638. Shopping Offers

    **Medium** · Array, Dynamic Programming, Backtracking, Bit Manipulation, Memoization, Bitmask, Knapsack Problem, Complete Knapsack

    In LeetCode Store, there are `n` items to sell. Each item has a price. However, there are some special offers, and a special offer consists of one or more different kinds of items with a sale price.

    You are given an integer array `price` where `price[i]` is the price of the `i_th` item, and an integer array `needs` where `needs[i]` is the number of pieces of the `i_th` item you want to buy.

    You are also given an array `special` where `special[i]` is of size `n + 1` where `special[i][j]` is the number of pieces of the `j_th` item in the `i_th` offer and `special[i][n]` (i.e., the last integer in the array) is the price of the `i_th` offer.

    Return *the lowest price you have to pay for exactly certain items as given, where you could make optimal use of the special offers*. You are not allowed to buy more items than you want, even if that would lower the overall price. You could use any of the special offers as many times as you want.

    ## Examples

    ```
    Input: price = [2,5], special = [[3,0,5],[1,2,10]], needs = [3,2]
    Output: 14
    ```
    **Explanation:** There are two kinds of items, A and B. Their prices are $2 and $5 respectively. In special offer 1, you can pay $5 for 3A and 0B. In special offer 2, you can pay $10 for 1A and 2B. You need to buy 3A and 2B, so you may pay $10 for 1A and 2B (special offer #2), and $4 for 2A.

    ```
    Input: price = [2,3,4], special = [[1,1,0,4],[2,2,1,9]], needs = [1,2,1]
    Output: 11
    ```
    **Explanation:** The price of A is $2, and $3 for B, $4 for C. You may pay $4 for 1A and 1B, and $9 for 2A, 2B and 1C. You need to buy 1A, 2B and 1C, so you may pay $4 for 1A and 1B (special offer #1), and $3 for 1B, $4 for 1C. You cannot add more items, though only $9 for 2A, 2B and 1C.

    ## Constraints

    - `n == price.length == needs.length`
    - `1 <= n <= 6`
    - `0 <= price[i], needs[i] <= 10`
    - `1 <= special.length <= 100`
    - `special[i].length == n + 1`
    - `0 <= special[i][j] <= 50`
    - The input is generated that at least one of `special[i][j]` is non-zero for `0 <= j <= n - 1`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def shopping_offers(self, price: list[int], special: list[list[int]], needs: list[int]) -> int:
            raise NotImplementedError('Implement shopping_offers')

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
