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
    # 1091. Shortest Path in Binary Matrix

    **Medium** · Array, Breadth-First Search, Matrix

    Given an `n x n` binary matrix `grid`, return *the length of the shortest **clear path*** in the matrix. If there is no clear path, return `-1`.

    A **clear path** in a binary matrix is a path from the top-left cell (i.e., `(0, 0)`) to the bottom-right cell (i.e., `(n - 1, n - 1)`) such that:

    - All the visited cells of the path are `0`.
    - All the adjacent cells of the path are **8-directionally** connected (i.e., they are different and they share an edge or a corner).

    The length of a clear path is the number of visited cells of this path.

    ## Examples

    ```
    Input: grid = [[0,1],[1,0]]
    Output: 2
    ```

    ```
    Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
    Output: 4
    ```

    ```
    Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
    Output: -1
    ```

    ## Constraints

    - `n == grid.length`
    - `n == grid[i].length`
    - `1 <= n <= 100`
    - `grid[i][j] is 0 or 1`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from collections import deque

    class Solution:

        def shortest_path_binary_matrix(self, grid: list[list[int]]) -> int:
            raise NotImplementedError('Implement shortest_path_binary_matrix')

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
