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
    # 2017. Grid Game

    **Medium** · Array, Matrix, Prefix Sum

    You are given a <strong>0-indexed</strong> 2D array <code>grid</code> of size <code>2 x n</code>, where <code>grid[r][c]</code> represents the number of points at position <code>(r, c)</code> on the matrix. Two robots are playing a game on this matrix.

    Both robots initially start at <code>(0, 0)</code> and want to reach <code>(1, n-1)</code>. Each robot may only move to the <strong>right</strong> (<code>(r, c)</code> to <code>(r, c + 1)</code>) or <strong>down</strong> (<code>(r, c)</code> to <code>(r + 1, c)</code>).

    At the start of the game, the <strong>first</strong> robot moves from <code>(0, 0)</code> to <code>(1, n-1)</code>, collecting all the points from the cells on its path. For all cells <code>(r, c)</code> traversed on the path, <code>grid[r][c]</code> is set to <code>0</code>. Then, the <strong>second</strong> robot moves from <code>(0, 0)</code> to <code>(1, n-1)</code>, collecting the points on its path. Note that their paths may intersect with one another.

    The <strong>first</strong> robot wants to <strong>minimize</strong> the number of points collected by the <strong>second</strong> robot. In contrast, the <strong>second</strong> robot wants to <strong>maximize</strong> the number of points it collects. If both robots play <strong>optimally</strong>, return the <em>number of points</em> collected by the <strong>second</strong> robot.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2021/09/08/a1.png)

    ```
    Input: grid = [[2,5,4],[1,5,1]]
    Output: 4
    Explanation: The optimal path taken by the first robot is shown in red, and the optimal path taken by the second robot is shown in blue.
    The cells visited by the first robot are set to 0.
    The second robot will collect 0 + 0 + 4 + 0 = 4 points.
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2021/09/08/a2.png)

    ```
    Input: grid = [[3,3,1],[8,5,2]]
    Output: 4
    Explanation: The optimal path taken by the first robot is shown in red, and the optimal path taken by the second robot is shown in blue.
    The cells visited by the first robot are set to 0.
    The second robot will collect 0 + 3 + 1 + 0 = 4 points.
    ```

    ![Example 3](https://assets.leetcode.com/uploads/2021/09/08/a3.png)

    ```
    Input: grid = [[1,3,1,15],[1,3,3,1]]
    Output: 7
    Explanation: The optimal path taken by the first robot is shown in red, and the optimal path taken by the second robot is shown in blue.
    The cells visited by the first robot are set to 0.
    The second robot will collect 0 + 1 + 3 + 3 + 0 = 7 points.
    ```

    ## Constraints

    - grid.length == 2
    - n == grid[r].length
    - 1 <= n <= 5 * 10^4
    - 1 <= grid[r][c] <= 10^5



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def grid_game(self, grid: list[list[int]]) -> int:
            raise NotImplementedError('Implement grid_game')

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
