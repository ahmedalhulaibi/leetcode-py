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
    # 363. Max Sum of Rectangle No Larger Than K

    **Hard** · Array, Binary Search, Matrix, Prefix Sum, Ordered Set

    Given an <code>m x n</code> matrix <code>matrix</code> and an integer <code>k</code>, return <em>the max sum of a rectangle in the matrix such that its sum is no larger than</em> <code>k</code>.

    It is <strong>guaranteed</strong> that there will be a rectangle with a sum no larger than <code>k</code>.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2021/03/18/sum-grid.jpg)

    ```
    Input: matrix = [[1,0,1],[0,-2,3]], k = 2
    Output: 2
    Explanation: Because the sum of the blue rectangle [[0, 1], [-2, 3]] is 2, and 2 is the max number no larger than k (k = 2).
    ```

    ```
    Input: matrix = [[2,2,-1]], k = 3
    Output: 3
    ```

    ## Constraints

    - m == matrix.length
    - n == matrix[i].length
    - 1 <= m, n <= 100
    - -100 <= matrix[i][j] <= 100
    - -10^5 <= k <= 10^5

    **Follow up:** What if the number of rows is much larger than the number of columns?

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def max_sum_submatrix(self, matrix: list[list[int]], k: int) -> int:
            raise NotImplementedError('Implement max_sum_submatrix')

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
