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
    # 329. Longest Increasing Path in a Matrix

    **Hard** · Array, Dynamic Programming, Depth-First Search, Breadth-First Search, Graph Theory, Topological Sort, Memoization, Matrix

    Given an `m x n` integers `matrix`, return *the length of the longest increasing path in* `matrix`.

    From each cell, you can either move in four directions: left, right, up, or down. You **may not** move **diagonally** or move **outside the boundary** (i.e., wrap-around is not allowed).

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2021/01/05/grid1.jpg)

    ```
    Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
    Output: 4
    ```
    **Explanation:** The longest increasing path is `[1, 2, 6, 9]`.

    ![Example 2](https://assets.leetcode.com/uploads/2021/01/27/tmp-grid.jpg)

    ```
    Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
    Output: 4
    ```
    **Explanation:** The longest increasing path is `[3, 4, 5, 6]`. Moving diagonally is not allowed.

    ```
    Input: matrix = [[1]]
    Output: 1
    ```

    ## Constraints

    - m == matrix.length
    - n == matrix[i].length
    - 1 <= m, n <= 200
    - 0 <= matrix[i][j] <= 2^31 - 1



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def longest_increasing_path(self, matrix: list[list[int]]) -> int:
            raise NotImplementedError('Implement longest_increasing_path')

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
