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
    # 1074. Number of Submatrices That Sum to Target

    **Hard** · Array, Hash Table, Matrix, Prefix Sum

    Given a <code>matrix</code>&nbsp;and a <code>target</code>, return the number of non-empty submatrices that sum to <code>target</code>.

    A submatrix <code>x1, y1, x2, y2</code> is the set of all cells <code>matrix[x][y]</code> with <code>x1 &lt;= x &lt;= x2</code> and <code>y1 &lt;= y &lt;= y2</code>.

    Two submatrices <code>(x1, y1, x2, y2)</code> and <code>(x1&#39;, y1&#39;, x2&#39;, y2&#39;)</code> are different if they have some coordinate&nbsp;that is different: for example, if <code>x1 != x1&#39;</code>.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2020/09/02/mate1.jpg)

    ```
    Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
    Output: 4
    Explanation: The four 1x1 submatrices that only contain 0.
    ```

    ```
    Input: matrix = [[1,-1],[-1,1]], target = 0
    Output: 5
    Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.
    ```

    ```
    Input: matrix = [[904]], target = 0
    Output: 0
    ```

    ## Constraints

    - <code>1 &lt;= matrix.length &lt;= 100</code>
    - <code>1 &lt;= matrix[0].length &lt;= 100</code>
    - <code>-1000 &lt;= matrix[i][j] &lt;= 1000</code>
    - <code>-10<sup>8</sup> &lt;= target &lt;= 10<sup>8</sup></code>



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def num_submatrix_sum_target(self, matrix: list[list[int]], target: int) -> int:
            raise NotImplementedError('Implement num_submatrix_sum_target')

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
