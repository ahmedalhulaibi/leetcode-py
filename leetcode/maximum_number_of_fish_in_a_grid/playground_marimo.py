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
    # 2658. Maximum Number of Fish in a Grid

    **Medium** · Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix

    You are given a **0-indexed** 2D matrix `grid` of size `m x n`, where `(r, c)` represents:

    - A **land** cell if `grid[r][c] = 0`, or
    - A **water** cell containing `grid[r][c]` fish, if `grid[r][c] > 0`.

    A fisher can start at any **water** cell `(r, c)` and can do the following operations any number of times:

    - Catch all the fish at cell `(r, c)`, or
    - Move to any adjacent **water** cell.

    Return _the **maximum** number of fish the fisher can catch if he chooses his starting cell optimally_, or `0` if no water cell exists.

    An **adjacent** cell of the cell `(r, c)`, is one of the cells `(r, c + 1)`, `(r, c - 1)`, `(r + 1, c)` or `(r - 1, c)` if it exists.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2023/03/29/example.png)

    ```
    Input: grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]
    Output: 7
    Explanation: The fisher can start at cell (1,3) and collect 3 fish, then move to cell (2,3) and collect 4 fish.
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2023/03/29/example2.png)

    ```
    Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]
    Output: 1
    Explanation: The fisher can start at cells (0,0) or (3,3) and collect a single fish.
    ```

    ## Constraints

    - m == grid.length
    - n == grid[i].length
    - 1 <= m, n <= 10
    - 0 <= grid[i][j] <= 10



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def find_max_fish(self, grid: list[list[int]]) -> int:
            raise NotImplementedError('Implement find_max_fish')

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
