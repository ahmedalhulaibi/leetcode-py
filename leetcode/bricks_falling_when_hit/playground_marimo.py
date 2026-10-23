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
    # 803. Bricks Falling When Hit

    **Hard** · Array, Union-Find, Matrix

    You are given an `m x n` binary grid, where each `1` represents a brick and `0` represents an empty space. A brick is **stable** if:

    - It is directly connected to the top of the grid, or
    - At least one other brick in its four adjacent cells is **stable**.

    You are also given an array `hits`, which is a sequence of erasures we want to apply. Each time we want to erase the brick at the location `hits[i] = (row<sub>i</sub>, col<sub>i</sub>)`. The brick on that location (if it exists) will disappear. Some other bricks may no longer be stable because of that erasure and will **fall**. Once a brick falls, it is immediately erased from the grid (i.e., it does not land on other stable bricks).

    Return an array `result`, where each `result[i]` is the number of bricks that will fall after the `i<sup>th</sup>` erasure is applied.

    **Note** that an erasure may refer to a location with no brick, and if it does, no bricks drop.

    ## Examples

    ```
    Input: grid = [[1,0,0,0],[1,1,1,0]], hits = [[1,0]]
    Output: [2]
    Explanation: Starting with the grid:
    [[1,0,0,0],
     [1,1,1,0]]
    We erase the brick at (1,0), resulting in the grid:
    [[1,0,0,0],
     [0,1,1,0]]
    The two bricks are no longer stable as they are no longer connected to the top nor adjacent to another stable brick, so they will fall. The resulting grid is:
    [[1,0,0,0],
     [0,0,0,0]]
    Hence the result is [2].
    ```

    ```
    Input: grid = [[1,0,0,0],[1,1,0,0]], hits = [[1,1],[1,0]]
    Output: [0,0]
    Explanation: Starting with the grid:
    [[1,0,0,0],
     [1,1,0,0]]
    We erase the brick at (1,1), resulting in the grid:
    [[1,0,0,0],
     [1,0,0,0]]
    All remaining bricks are still stable, so no bricks fall. Next, we erase the brick at (1,0), resulting in the grid:
    [[1,0,0,0],
     [0,0,0,0]]
    Once again, all remaining bricks are still stable, so no bricks fall.
    Hence the result is [0,0].
    ```

    ## Constraints

    - `m == grid.length`
    - `n == grid[i].length`
    - `1 <= m, n <= 200`
    - `grid[i][j]` is `0` or `1`.
    - `1 <= hits.length <= 4 * 10^4`
    - `hits[i].length == 2`
    - `0 <= x_i <= m - 1`
    - `0 <= y_i <= n - 1`
    - All `(x_i, y_i)` are unique.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def hit_bricks(self, grid: list[list[int]], hits: list[list[int]]) -> list[int]:
            raise NotImplementedError('Implement hit_bricks')

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
