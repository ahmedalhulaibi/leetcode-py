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
    # 994. Rotting Oranges

    **Medium** · Array, Breadth-First Search, Matrix

    You are given an `m x n` `grid` where each cell can have one of three values:

    - `0` representing an empty cell,
    - `1` representing a fresh orange, or
    - `2` representing a rotten orange.

    Every minute, any fresh orange that is **4-directionally adjacent** to a rotten orange becomes rotten.

    Return *the minimum number of minutes that must elapse until no cell has a fresh orange*. If *this is impossible, return* `-1`.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2019/02/16/oranges.png)

    ```
    Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
    Output: 4
    ```

    ```
    Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
    Output: -1
    ```
    **Explanation:** The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

    ```
    Input: grid = [[0,2]]
    Output: 0
    ```
    **Explanation:** Since there are already no fresh oranges at minute 0, the answer is just 0.

    ## Constraints

    - `m == grid.length`
    - `n == grid[i].length`
    - `1 <= m, n <= 10`
    - `grid[i][j]` is `0`, `1`, or `2`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def oranges_rotting(self, grid: list[list[int]]) -> int:
            raise NotImplementedError('Implement oranges_rotting')

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
