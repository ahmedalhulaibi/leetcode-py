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
    # 2812. Find the Safest Path in a Grid

    **Medium** · Array, Binary Search, Breadth-First Search, Union-Find, Heap (Priority Queue), Matrix

    You are given a **0-indexed** 2D matrix `grid` of size `n x n`, where `(r, c)` represents:

    - A cell containing a thief if `grid[r][c] = 1`
    - An empty cell if `grid[r][c] = 0`

    You are initially positioned at cell `(0, 0)`. In one move, you can move to any adjacent cell in the grid, including cells containing thieves.

    The **safeness factor** of a path on the grid is defined as the **minimum** manhattan distance from any cell in the path to any thief in the grid.

    Return *the **maximum safeness factor** of all paths leading to cell `(n - 1, n - 1)`*.

    An **adjacent** cell of cell `(r, c)`, is one of the cells `(r, c + 1)`, `(r, c - 1)`, `(r + 1, c)` and `(r - 1, c)` if it exists.

    The **Manhattan distance** between two cells `(a, b)` and `(x, y)` is equal to `|a - x| + |b - y|`, where `|val|` denotes the absolute value of val.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2023/07/02/example1.png)

    ```
    Input: grid = [[1,0,0],[0,0,0],[0,0,1]]
    Output: 0
    Explanation: All paths from (0, 0) to (n - 1, n - 1) go through the thieves in cells (0, 0) and (n - 1, n - 1).
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2023/07/02/example2.png)

    ```
    Input: grid = [[0,0,1],[0,0,0],[0,0,0]]
    Output: 2
    Explanation: The path depicted in the picture above has a safeness factor of 2 since:
    - The closest cell of the path to the thief at cell (0, 2) is cell (0, 0). The distance between them is | 0 - 0 | + | 0 - 2 | = 2.
    It can be shown that there are no other paths with a higher safeness factor.
    ```

    ![Example 3](https://assets.leetcode.com/uploads/2023/07/02/example3.png)

    ```
    Input: grid = [[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]
    Output: 2
    Explanation: The path depicted in the picture above has a safeness factor of 2 since:
    - The closest cell of the path to the thief at cell (0, 3) is cell (1, 2). The distance between them is | 0 - 1 | + | 3 - 2 | = 2.
    - The closest cell of the path to the thief at cell (3, 0) is cell (3, 2). The distance between them is | 3 - 3 | + | 0 - 2 | = 2.
    It can be shown that there are no other paths with a higher safeness factor.
    ```

    ## Constraints

    - `1 <= grid.length == n <= 400`
    - `grid[i].length == n`
    - `grid[i][j]` is either `0` or `1`.
    - There is at least one thief in the `grid`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def maximum_safeness_factor(self, grid: list[list[int]]) -> int:
            raise NotImplementedError('Implement maximum_safeness_factor')

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
