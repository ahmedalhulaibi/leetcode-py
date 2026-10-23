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
    # 2577. Minimum Time to Visit a Cell In a Grid

    **Hard** · Array, Breadth-First Search, Graph Theory, Heap (Priority Queue), Matrix, Shortest Path

    You are given a `m x n` matrix `grid` consisting of non-negative integers where `grid[row][col]` represents the minimum time required to be able to visit the cell `(row, col)`, which means you can visit the cell `(row, col)` only when the time you visit it is greater than or equal to `grid[row][col]`.

    You are standing in the top-left cell of the matrix in the `0th` second, and you must move to any adjacent cell in the four directions: **up**, **down**, **left**, and **right**. Each move you make takes `1` second.

    Return the minimum time required in which you can visit the bottom-right cell of the matrix. If you cannot visit the bottom-right cell, then return `-1`.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2023/02/14/yetgriddrawio-8.png)

    ```
    Input: grid = [[0,1,3,2],[5,1,2,5],[4,3,8,6]]
    Output: 7
    Explanation: One of the paths that we can take is the following:
    - at t = 0, we are on the cell (0,0).
    - at t = 1, we move to the cell (0,1). It is possible because grid[0][1] <= 1.
    - at t = 2, we move to the cell (1,1). It is possible because grid[1][1] <= 2.
    - at t = 3, we move to the cell (1,2). It is possible because grid[1][2] <= 3.
    - at t = 4, we move to the cell (1,1). It is possible because grid[1][1] <= 4.
    - at t = 5, we move to the cell (1,2). It is possible because grid[1][2] <= 5.
    - at t = 6, we move to the cell (1,3). It is possible because grid[1][3] <= 6.
    - at t = 7, we move to the cell (2,3). It is possible because grid[2][3] <= 7.
    The final time is 7. It can be shown that it is the minimum time possible.
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2023/02/14/yetgriddrawio-9.png)

    ```
    Input: grid = [[0,2,4],[3,2,1],[1,0,4]]
    Output: -1
    Explanation: There is no path from the top left to the bottom-right cell.
    ```

    ## Constraints

    - m == grid.length
    - n == grid[i].length
    - 2 <= m, n <= 1000
    - 4 <= m * n <= 10^5
    - 0 <= grid[i][j] <= 10^5
    - grid[0][0] == 0



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def minimum_time(self, grid: list[list[int]]) -> int:
            raise NotImplementedError('Implement minimum_time')

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
