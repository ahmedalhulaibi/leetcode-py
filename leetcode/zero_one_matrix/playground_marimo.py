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
    # 542. 01 Matrix

    **Medium** · Array, Dynamic Programming, Breadth-First Search, Matrix

    Given an `m x n` binary matrix `mat`, return the distance of the nearest `0` for each cell.

    The distance between two cells sharing a common edge is `1`.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2021/04/24/01-1-grid.jpg)

    ```
    Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
    Output: [[0,0,0],[0,1,0],[0,0,0]]
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2021/04/24/01-2-grid.jpg)

    ```
    Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
    Output: [[0,0,0],[0,1,0],[1,2,1]]
    ```

    ## Constraints

    - `m == mat.length`
    - `n == mat[i].length`
    - `1 <= m, n <= 10^4`
    - `1 <= m * n <= 10^4`
    - `mat[i][j]` is either `0` or `1`
    - There is at least one `0` in `mat`

    **Note:** This question is the same as 1765: [Map of Highest Peak](https://leetcode.com/problems/map-of-highest-peak/)

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def update_matrix(self, mat: list[list[int]]) -> list[list[int]]:
            raise NotImplementedError('Implement update_matrix')

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
