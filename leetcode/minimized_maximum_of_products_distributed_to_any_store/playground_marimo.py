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
    # 2064. Minimized Maximum of Products Distributed to Any Store

    **Medium** · Array, Binary Search, Greedy

    You are given an integer `n` indicating there are `n` specialty retail stores. There are `m` product types of varying amounts, which are given as a **0-indexed** integer array `quantities`, where `quantities[i]` represents the number of products of the `i<sup>th</sup>` product type.

    You need to distribute **all products** to the retail stores following these rules:

    - A store can only be given **at most one product type** but can be given **any** amount of it.
    - After distribution, each store will have been given some number of products (possibly `0`). Let `x` represent the maximum number of products given to any store. You want `x` to be as small as possible, i.e., you want to **minimize** the **maximum** number of products that are given to any store.

    Return *the minimum possible* `x`.

    ## Examples

    ```
    Input: n = 6, quantities = [11,6]
    Output: 3
    Explanation: One optimal way is:
    - The 11 products of type 0 are distributed to the first four stores in these amounts: 2, 3, 3, 3
    - The 6 products of type 1 are distributed to the other two stores in these amounts: 3, 3
    The maximum number of products given to any store is max(2, 3, 3, 3, 3, 3) = 3.
    ```

    ```
    Input: n = 7, quantities = [15,10,10]
    Output: 5
    Explanation: One optimal way is:
    - The 15 products of type 0 are distributed to the first three stores in these amounts: 5, 5, 5
    - The 10 products of type 1 are distributed to the next two stores in these amounts: 5, 5
    - The 10 products of type 2 are distributed to the last two stores in these amounts: 5, 5
    The maximum number of products given to any store is max(5, 5, 5, 5, 5, 5, 5) = 5.
    ```

    ```
    Input: n = 1, quantities = [100000]
    Output: 100000
    Explanation: The only optimal way is:
    - The 100000 products of type 0 are distributed to the only store.
    The maximum number of products given to any store is max(100000) = 100000.
    ```

    ## Constraints

    - m == quantities.length
    - 1 <= m <= n <= 10^5
    - 1 <= quantities[i] <= 10^5



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def minimized_maximum(self, n: int, quantities: list[int]) -> int:
            raise NotImplementedError('Implement minimized_maximum')

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
