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
    # 1730. Shortest Path to Get Food

    **Medium** · Array, Breadth-First Search, Matrix

    You are starving and you want to eat food as quickly as possible. You want to find the shortest path to arrive at any food cell.

    You are given an `m x n` character matrix, `grid`, of these different types of cells:

    - `'*'` is your location. There is exactly one `'*'` cell.
    - `'#'` is a food cell. There may be multiple food cells.
    - `'O'` is free space, and you can travel through these cells.
    - `'X'` is an obstacle, and you cannot travel through these cells.

    You can travel to any adjacent cell north, east, south, or west of your current location if there is not an obstacle.

    Return the length of the shortest path for you to reach any food cell. If there is no path for you to reach food, return `-1`.

    ## Examples

    ```
    Input: grid = [["X","X","X","X","X","X"],["X","*","O","O","O","X"],["X","O","O","#","O","X"],["X","X","X","X","X","X"]]
    Output: 3
    Explanation: It takes 3 steps to reach the food.
    ```

    ```
    Input: grid = [["X","X","X","X","X"],["X","*","X","O","X"],["X","O","X","#","X"],["X","X","X","X","X"]]
    Output: -1
    Explanation: It is not possible to reach the food.
    ```

    ```
    Input: grid = [["X","X","X","X","X","X","X","X"],["X","*","O","X","O","#","O","X"],["X","O","O","X","O","O","X","X"],["X","O","O","O","O","#","O","X"],["X","X","X","X","X","X","X","X"]]
    Output: 6
    Explanation: There can be multiple food cells. It only takes 6 steps to reach the bottom food.
    ```

    ```
    Input: grid = [["O","*"],["#","O"]]
    Output: 2
    ```

    ## Constraints

    - `m == grid.length`
    - `n == grid[i].length`
    - `1 <= m, n <= 200`
    - `grid[row][col]` is `'*'`, `'X'`, `'O'`, or `'#'`.
    - The `grid` contains exactly one `'*'`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def get_food(self, grid: list[list[str]]) -> int:
            raise NotImplementedError('Implement get_food')

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
