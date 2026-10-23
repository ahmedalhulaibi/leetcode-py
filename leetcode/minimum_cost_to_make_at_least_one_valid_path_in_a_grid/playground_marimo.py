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
    mo.md(r"""
    # 1368. Minimum Cost to Make at Least One Valid Path in a Grid

    **Medium** · Array, Breadth-First Search, Graph, Heap (Priority Queue), Matrix, Shortest Path

    Given an <code>m x n</code> grid. Each cell of the grid has a sign pointing to the next cell you should visit if you are currently in this cell. The sign of <code>grid[i][j]</code> can be:

    <ul>
        <li><code>1</code> which means go to the cell to the right. (i.e go from <code>grid[i][j]</code> to <code>grid[i][j + 1]</code>)</li>
        <li><code>2</code> which means go to the cell to the left. (i.e go from <code>grid[i][j]</code> to <code>grid[i][j - 1]</code>)</li>
        <li><code>3</code> which means go to the lower cell. (i.e go from <code>grid[i][j]</code> to <code>grid[i + 1][j]</code>)</li>
        <li><code>4</code> which means go to the upper cell. (i.e go from <code>grid[i][j]</code> to <code>grid[i - 1][j]</code>)</li>
    </ul>

    Notice that there could be some signs on the cells of the grid that point outside the grid.

    You will initially start at the upper left cell <code>(0, 0)</code>. A valid path in the grid is a path that starts from the upper left cell <code>(0, 0)</code> and ends at the bottom-right cell <code>(m - 1, n - 1)</code> following the signs on the grid. The valid path does not have to be the shortest.

    You can modify the sign on a cell with <strong>cost = 1</strong>. You can modify the sign on a cell <strong>one time only</strong>.

    Return the <em>minimum cost to make the grid have at least one <strong>valid path</strong></em>.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2020/02/13/grid1.png)

    ```
    Input: grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
    Output: 3
    Explanation: You will start at point (0, 0).
    The path to (3, 3) is as follows. (0, 0) --> (0, 1) --> (0, 2) --> (0, 3) change the arrow to down with cost = 1 --> (1, 3) --> (1, 2) --> (1, 1) --> (1, 0) change the arrow to down with cost = 1 --> (2, 0) --> (2, 1) --> (2, 2) --> (2, 3) change the arrow to down with cost = 1 --> (3, 3)
    The total cost = 3.
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2020/02/13/grid2.png)

    ```
    Input: grid = [[1,1,3],[3,2,2],[1,1,4]]
    Output: 0
    Explanation: You can follow the path from (0, 0) to (2, 2).
    ```

    ![Example 3](https://assets.leetcode.com/uploads/2020/02/13/grid3.png)

    ```
    Input: grid = [[1,2],[4,3]]
    Output: 1
    ```

    ## Constraints

    - m == grid.length
    - n == grid[i].length
    - 1 <= m, n <= 100
    - 1 <= grid[i][j] <= 4



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def min_cost(self, grid: list[list[int]]) -> int:
            raise NotImplementedError('Implement min_cost')

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
