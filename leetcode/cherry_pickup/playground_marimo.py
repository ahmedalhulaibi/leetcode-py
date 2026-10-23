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
    # 741. Cherry Pickup

    **Hard** · Array, Dynamic Programming, Matrix

    You are given an `n x n` `grid` representing a field of cherries, each cell is one of three possible integers.

    - `0` means the cell is empty, so you can pass through,
    - `1` means the cell contains a cherry that you can pick up and pass through, or
    - `-1` means the cell contains a thorn that blocks your way.

    Return *the maximum number of cherries you can collect by following the rules below*:

    - Starting at the position `(0, 0)` and reaching `(n - 1, n - 1)` by moving right or down through valid path cells (cells with value `0` or `1`).
    - After reaching `(n - 1, n - 1)`, returning to `(0, 0)` by moving left or up through valid path cells.
    - When passing through a path cell containing a cherry, you pick it up, and the cell becomes an empty cell `0`.
    - If there is no valid path between `(0, 0)` and `(n - 1, n - 1)`, then no cherries can be collected.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2020/12/14/grid.jpg)

    ```
    Input: grid = [[0,1,-1],[1,0,-1],[1,1,1]]
    Output: 5
    Explanation: The player started at (0, 0) and went down, down, right right to reach (2, 2).
    4 cherries were picked up during this single trip, and the matrix becomes [[0,1,-1],[0,0,-1],[0,0,0]].
    Then, the player went left, up, up, left to return home, picking up one more cherry.
    The total number of cherries picked up is 5, and this is the maximum possible.
    ```

    ```
    Input: grid = [[1,1,-1],[1,-1,1],[-1,1,1]]
    Output: 0
    ```

    ## Constraints

    - n == grid.length
    - n == grid[i].length
    - 1 <= n <= 50
    - grid[i][j] is -1, 0, or 1.
    - grid[0][0] != -1
    - grid[n - 1][n - 1] != -1



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def cherry_pickup(self, grid: list[list[int]]) -> int:
            raise NotImplementedError('Implement cherry_pickup')

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
