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
    # 931. Minimum Falling Path Sum

    **Medium** · Array, Dynamic Programming, Matrix

    <p>Given an <code>n x n</code> array of integers <code>matrix</code>, return <em>the minimum sum of any <strong>falling path</strong> through</em> <code>matrix</code>.</p>

    <p>A <strong>falling path</strong> starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position <code>(row, col)</code> will be <code>(row + 1, col - 1)</code>, <code>(row + 1, col)</code>, or <code>(row + 1, col + 1)</code>.</p>

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2021/11/03/failing1-grid.jpg)

    ```
    Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
    Output: 13
    Explanation: There are two falling paths with a minimum sum as shown.
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2021/11/03/failing2-grid.jpg)

    ```
    Input: matrix = [[-19,57],[-40,-5]]
    Output: -59
    Explanation: The falling path with a minimum sum is shown.
    ```

    ## Constraints

    - n == matrix.length == matrix[i].length
    - 1 &lt;= n &lt;= 100
    - -100 &lt;= matrix[i][j] &lt;= 100



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def min_falling_path_sum(self, matrix: list[list[int]]) -> int:
            raise NotImplementedError('Implement min_falling_path_sum')

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
