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
    # 1727. Largest Submatrix With Rearrangements

    **Medium** · Array, Greedy, Sorting, Matrix

    You are given a binary matrix `matrix` of size `m x n`, and you are allowed to rearrange the **columns** of the `matrix` in any order.

    Return *the area of the largest submatrix within* `matrix` *where **every** element of the submatrix is* `1` *after reordering the columns optimally.*

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2020/12/29/screenshot-2020-12-30-at-40536-pm.png)

    ```
    Input: matrix = [[0,0,1],[1,1,1],[1,0,1]]
    Output: 4
    Explanation: You can rearrange the columns as shown above.
    The largest submatrix of 1s, in bold, has an area of 4.
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2020/12/29/screenshot-2020-12-30-at-40852-pm.png)

    ```
    Input: matrix = [[1,0,1,0,1]]
    Output: 3
    Explanation: You can rearrange the columns as shown above.
    The largest submatrix of 1s, in bold, has an area of 3.
    ```

    ```
    Input: matrix = [[1,1,0],[1,0,1]]
    Output: 2
    Explanation: Notice that you must rearrange entire columns, and there is no way to make a submatrix of 1s larger than an area of 2.
    ```

    ## Constraints

    - m == matrix.length
    - n == matrix[i].length
    - 1 <= m * n <= 10^5
    - matrix[i][j] is either 0 or 1.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def largest_submatrix(self, matrix: list[list[int]]) -> int:
            raise NotImplementedError('Implement largest_submatrix')

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
