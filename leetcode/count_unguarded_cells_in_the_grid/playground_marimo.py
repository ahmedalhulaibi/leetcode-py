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
    # 2257. Count Unguarded Cells in the Grid

    **Medium** · Array, Matrix, Simulation

    You are given two integers `m` and `n` representing a **0-indexed** `m x n` grid. You are also given two 2D integer arrays `guards` and `walls` where `guards[i] = [rowi, coli]` and `walls[j] = [rowj, colj]` represent the positions of the `ith` guard and `jth` wall respectively.

    A guard can see **every** cell in the four cardinal directions (north, east, south, or west) starting from their position unless **obstructed** by a wall or another guard. A cell is **guarded** if there is **at least** one guard that can see it.

    Return *the number of unoccupied cells that are **not** **guarded**.*

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2022/03/10/example1drawio2.png)

    ```
    Input: m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]
    Output: 7
    Explanation: The guarded and unguarded cells are shown in red and green respectively in the above diagram.
    There are a total of 7 unguarded cells, so we return 7.
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2022/03/10/example2drawio.png)

    ```
    Input: m = 3, n = 3, guards = [[1,1]], walls = [[0,1],[1,0],[2,1],[1,2]]
    Output: 4
    Explanation: The unguarded cells are shown in green in the above diagram.
    There are a total of 4 unguarded cells, so we return 4.
    ```

    ## Constraints

    - `1 <= m, n <= 10^5`
    - `2 <= m * n <= 10^5`
    - `1 <= guards.length, walls.length <= 5 * 10^4`
    - `2 <= guards.length + walls.length <= m * n`
    - `guards[i].length == walls[j].length == 2`
    - `0 <= rowi, rowj < m`
    - `0 <= coli, colj < n`
    - All the positions in `guards` and `walls` are **unique**.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def count_unguarded(self, m: int, n: int, guards: list[list[int]], walls: list[list[int]]) -> int:
            raise NotImplementedError('Implement count_unguarded')

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
