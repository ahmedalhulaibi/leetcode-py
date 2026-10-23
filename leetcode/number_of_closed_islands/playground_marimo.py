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
    # 1254. Number of Closed Islands

    **Medium** · Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix

    Given a 2D `grid` consists of `0s` (land) and `1s` (water). An *island* is a maximal 4-directionally connected group of `0`s and a *closed island* is an island **totally** (all left, top, right, bottom) surrounded by `1s.`

    Return the number of *closed islands*.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2019/10/31/sample_3_1610.png)

    ```
    Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
    Output: 2
    Explanation: Islands in gray are closed because they are completely surrounded by water (group of 1s).
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2019/10/31/sample_4_1610.png)

    ```
    Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
    Output: 1
    ```

    ```
    Input: grid = [[1,1,1,1,1,1,1],[1,0,0,0,0,0,1],[1,0,1,1,1,0,1],[1,0,1,0,1,0,1],[1,0,1,1,1,0,1],[1,0,0,0,0,0,1],[1,1,1,1,1,1,1]]
    Output: 2
    ```

    ## Constraints

    - `1 <= grid.length, grid[0].length <= 100`
    - `0 <= grid[i][j] <= 1`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def closed_islands(self, grid: list[list[int]]) -> int:
            raise NotImplementedError('Implement closed_islands')

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
