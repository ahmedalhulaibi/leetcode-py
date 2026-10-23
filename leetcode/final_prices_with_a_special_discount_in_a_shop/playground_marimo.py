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
    # 1475. Final Prices With a Special Discount in a Shop

    **Easy** · Array, Stack, Monotonic Stack

    Given an integer array `prices` where `prices[i]` is the price of the `i<sup>th</sup>` item in a shop.

    There is a special discount for items in the shop. If you buy the `i<sup>th</sup>` item, then you will receive a discount equivalent to `prices[j]` where `j` is the minimum index such that `j > i` and `prices[j] <= prices[i]`. Otherwise, you will not receive any discount at all.

    Return an integer array `answer` where `answer[i]` is the final price you will pay for the `i<sup>th</sup>` item of the shop, considering the special discount.

    ## Examples

    ```
    Input: prices = [8,4,6,2,3]
    Output: [4,2,4,2,3]
    Explanation:
    For item 0 with price[0]=8 you will receive a discount equivalent to prices[1]=4, therefore, the final price you will pay is 8 - 4 = 4.
    For item 1 with price[1]=4 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 4 - 2 = 2.
    For item 2 with price[2]=6 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 6 - 2 = 4.
    For items 3 and 4 you will not receive any discount at all.
    ```

    ```
    Input: prices = [1,2,3,4,5]
    Output: [1,2,3,4,5]
    Explanation: In this case, for all items, you will not receive any discount at all.
    ```

    ```
    Input: prices = [10,1,1,6]
    Output: [9,0,1,6]
    ```

    ## Constraints

    - `1 <= prices.length <= 500`
    - `1 <= prices[i] <= 1000`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def final_prices(self, prices: list[int]) -> list[int]:
            raise NotImplementedError('Implement final_prices')

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
