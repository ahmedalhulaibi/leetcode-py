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
    # 980. Unique Paths III

    **Hard** · Array, Backtracking, Bit Manipulation, Matrix

    You are given an `m x n` integer array `grid` where `grid[i][j]` could be:

    - `1` representing the starting square. There is exactly one starting square.
    - `2` representing the ending square. There is exactly one ending square.
    - `0` representing empty squares we can walk over.
    - `-1` representing obstacles that we cannot walk over.

    Return *the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once*.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2021/08/02/lc-unique1.jpg)

    ```
    Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
    Output: 2
    Explanation: We have the following two paths:
    1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
    2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2021/08/02/lc-unique2.jpg)

    ```
    Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
    Output: 4
    Explanation: We have the following four paths:
    1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
    2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
    3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
    4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
    ```

    ![Example 3](https://assets.leetcode.com/uploads/2021/08/02/lc-unique3-.jpg)

    ```
    Input: grid = [[0,1],[2,0]]
    Output: 0
    Explanation: There is no path that walks over every empty square exactly once.
    Note that the starting and ending square can be anywhere in the grid.
    ```

    ## Constraints

    - `m == grid.length`
    - `n == grid[i].length`
    - `1 <= m, n <= 20`
    - `1 <= m * n <= 20`
    - `-1 <= grid[i][j] <= 2`
    - There is exactly one starting cell and one ending cell.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def unique_paths_iii(self, grid: list[list[int]]) -> int:
            raise NotImplementedError('Implement unique_paths_iii')

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
