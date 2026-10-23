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
    # 1568. Minimum Number of Days to Disconnect Island

    **Hard** · Array, Depth-First Search, Breadth-First Search, Matrix, Strongly Connected Component, Articulation Point

    You are given an `m x n` binary grid `grid` where `1` represents land and `0` represents water. An **island** is a maximal 4-directionally (horizontal or vertical) connected group of `1`s.

    The grid is said to be **connected** if we have **exactly one island**, otherwise is said **disconnected**.

    In one day, we are allowed to change **any** single land cell `(1)` into a water cell `(0)`.

    Return *the minimum number of days to disconnect the grid*.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2021/12/24/land1.jpg)

    ```
    Input: grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]
    Output: 2
    Explanation: We need at least 2 days to get a disconnected grid.
    Change land grid[1][1] and grid[0][2] to water and get 2 disconnected island.
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2021/12/24/land2.jpg)

    ```
    Input: grid = [[1,1]]
    Output: 2
    Explanation: Grid of full water is also disconnected ([[1,1]] -> [[0,0]]), 0 islands.
    ```

    ## Constraints

    - m == grid.length
    - n == grid[i].length
    - 1 <= m, n <= 30
    - grid[i][j] is either 0 or 1.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def min_days(self, grid: list[list[int]]) -> int:
            raise NotImplementedError('Implement min_days')

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
