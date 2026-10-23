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
    # 74. Search a 2D Matrix

    **Medium** · Array, Binary Search, Matrix

    You are given an `m x n` integer matrix `matrix` with the following two properties:

    - Each row is sorted in non-decreasing order.
    - The first integer of each row is greater than the last integer of the previous row.

    Given an integer `target`, return `true` *if* `target` *is in* `matrix` *or* `false` *otherwise*.

    You must write a solution in `O(log(m * n))` time complexity.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2020/10/05/mat.jpg)

    ```
    Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
    Output: true
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2020/10/05/mat2.jpg)

    ```
    Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
    Output: false
    ```

    ## Constraints

    - m == matrix.length
    - n == matrix[i].length
    - 1 <= m, n <= 100
    - -10^4 <= matrix[i][j], target <= 10^4



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def search_matrix(self, matrix: list[list[int]], target: int) -> bool:
            raise NotImplementedError('Implement search_matrix')

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
