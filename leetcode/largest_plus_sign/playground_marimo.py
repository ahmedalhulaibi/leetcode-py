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
    # 764. Largest Plus Sign

    **Medium** · Array, Dynamic Programming

    You are given an integer `n`. You have an `n x n` binary grid `grid` with all values initially `1`'s except for some indices given in the array `mines`. The `i^th` element of the array `mines` is defined as `mines[i] = [x_i, y_i]` where `grid[x_i][y_i] == 0`.

    Return *the order of the largest **axis-aligned** plus sign of* 1*'s contained in* `grid`. If there is none, return `0`.

    An **axis-aligned plus sign** of `1`'s of order `k` has some center `grid[r][c] == 1` along with four arms of length `k - 1` going up, down, left, and right, and made of `1`'s. Note that there could be `0`'s or `1`'s beyond the arms of the plus sign, only the relevant area of the plus sign is checked for `1`'s.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2021/06/13/plus1-grid.jpg)

    ```
    Input: n = 5, mines = [[4,2]]
    Output: 2
    Explanation: In the above grid, the largest plus sign can only be of order 2. One of them is shown.
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2021/06/13/plus2-grid.jpg)

    ```
    Input: n = 1, mines = [[0,0]]
    Output: 0
    Explanation: There is no plus sign, so return 0.
    ```

    ## Constraints

    - 1 <= n <= 500
    - 1 <= mines.length <= 5000
    - 0 <= xi, yi < n
    - All the pairs (xi, yi) are unique.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def order_of_largest_plus_sign(self, n: int, mines: list[list[int]]) -> int:
            raise NotImplementedError('Implement order_of_largest_plus_sign')

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
