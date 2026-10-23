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
    # 934. Shortest Bridge

    **Medium** · Array, Depth-First Search, Breadth-First Search, Matrix

    <p>You are given an <code>n x n</code> binary matrix <code>grid</code> where <code>1</code> represents land and <code>0</code> represents water.</p>

    <p>An island is a 4-directionally connected group of <code>1</code>&#39;s not connected to any other <code>1</code>&#39;s. There are <strong>exactly two islands</strong> in <code>grid</code>.</p>

    <p>You may change <code>0</code>&#39;s to <code>1</code>&#39;s to connect the two islands to form <strong>one island</strong>.</p>

    <p>Return <em>the smallest number of </em><code>0</code><em>&#39;s you must flip to connect the two islands</em>.</p>

    ## Examples

    ```
    Input: grid = [[0,1],[1,0]]
    Output: 1
    ```

    ```
    Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
    Output: 2
    ```

    ```
    Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
    Output: 1
    ```

    ## Constraints

    - n == grid.length == grid[i].length
    - 2 &lt;= n &lt;= 100
    - grid[i][j] is either 0 or 1.
    - There are exactly two islands in grid.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def shortest_bridge(self, grid: list[list[int]]) -> int:
            raise NotImplementedError('Implement shortest_bridge')

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
