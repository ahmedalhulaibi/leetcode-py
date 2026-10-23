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
    # 2290. Minimum Obstacle Removal to Reach Corner

    **Hard** · Array, Breadth-First Search, Graph Theory, Heap (Priority Queue), Matrix, Shortest Path, 0-1 BFS, Dijkstra's Algorithm

    You are given a **0-indexed** 2D integer array `grid` of size `m x n`. Each cell has one of two values:

    - `0` represents an **empty** cell,
    - `1` represents an **obstacle** that may be removed.

    You can move up, down, left, or right from and to an empty cell.

    Return the **minimum** number of **obstacles** to **remove** so you can move from the upper left corner `(0, 0)` to the lower right corner `(m - 1, n - 1)`.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2022/04/06/example1drawio-1.png)

    ```
    Input: grid = [[0,1,1],[1,1,0],[1,1,0]]
    Output: 2
    Explanation: We can remove the obstacles at (0, 1) and (0, 2) to create a path from (0, 0) to (2, 2).
    It can be shown that we need to remove at least 2 obstacles, so we return 2.
    Note that there may be other ways to remove 2 obstacles to create a path.
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2022/04/06/example1drawio.png)

    ```
    Input: grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]
    Output: 0
    Explanation: We can move from (0, 0) to (2, 4) without removing any obstacles, so we return 0.
    ```

    ## Constraints

    - `m == grid.length`
    - `n == grid[i].length`
    - `1 <= m, n <= 10^5`
    - `2 <= m * n <= 10^5`
    - `grid[i][j]` is either `0` or `1`.
    - `grid[0][0] == grid[m - 1][n - 1] == 0`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from collections import deque

    class Solution:

        def minimum_obstacles(self, grid: list[list[int]]) -> int:
            raise NotImplementedError('Implement minimum_obstacles')

    practice_exports = {'deque': deque, 'Solution': Solution}
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
