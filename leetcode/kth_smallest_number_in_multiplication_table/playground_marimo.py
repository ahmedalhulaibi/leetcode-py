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
    # 668. Kth Smallest Number in Multiplication Table

    **Hard** · Math, Binary Search

    Nearly everyone has used the [Multiplication Table](https://en.wikipedia.org/wiki/Multiplication_table). The multiplication table of size `m x n` is an integer matrix `mat` where `mat[i][j] == i * j` (1-indexed).

    Given three integers `m`, `n`, and `k`, return the kth smallest element in the `m x n` multiplication table.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2021/05/02/multtable1-grid.jpg)

    ```
    Input: m = 3, n = 3, k = 5
    Output: 3
    Explanation: The 5th smallest number is 3.
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2021/05/02/multtable2-grid.jpg)

    ```
    Input: m = 2, n = 3, k = 6
    Output: 6
    Explanation: The 6th smallest number is 6.
    ```

    ## Constraints

    - 1 <= m, n <= 3 * 10^4
    - 1 <= k <= m * n



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def find_kth_number(self, m: int, n: int, k: int) -> int:
            raise NotImplementedError('Implement find_kth_number')

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
