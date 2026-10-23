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
    # 1905. Count Sub Islands

    **Medium** · Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix

    You are given two `m x n` binary matrices `grid1` and `grid2` containing only `0`s (representing water) and `1`s (representing land). An *island* is a group of `1`s connected **4-directionally** (horizontal or vertical). Any cells outside of the grid are considered water cells.

    An island in `grid2` is considered a *sub-island* if there is an island in `grid1` that contains **all** the cells that make up **this** island in `grid2`.

    Return the number of islands in `grid2` that are considered *sub-islands*.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2021/06/10/test1.png)

    ```
    Input: grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
    Output: 3
    Explanation: The grid on the left is grid1 and the grid on the right is grid2. The 1s colored red in grid2 are those considered to be part of a sub-island. There are three sub-islands.
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2021/06/03/testcasex2.png)

    ```
    Input: grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
    Output: 2
    Explanation: The grid on the left is grid1 and the grid on the right is grid2. The 1s colored red in grid2 are those considered to be part of a sub-island. There are two sub-islands.
    ```

    ## Constraints

    - `m == grid1.length == grid2.length`
    - `n == grid1[i].length == grid2[i].length`
    - `1 <= m, n <= 500`
    - `grid1[i][j]` and `grid2[i][j]` are either `0` or `1`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def count_sub_islands(self, grid1: list[list[int]], grid2: list[list[int]]) -> int:
            raise NotImplementedError('Implement count_sub_islands')

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
