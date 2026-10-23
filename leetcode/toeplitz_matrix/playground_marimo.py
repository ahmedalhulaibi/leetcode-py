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
    # 766. Toeplitz Matrix

    **Easy** · Array, Matrix

    Given an `m x n` `matrix`, return `true` if the matrix is Toeplitz. Otherwise, return `false`.

    A matrix is **Toeplitz** if every diagonal from top-left to bottom-right has the same elements.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2020/11/04/ex1.jpg)

    ```
    Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
    Output: true
    Explanation:
    In the above grid, the diagonals are:
    "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
    In each diagonal all elements are the same, so the answer is True.
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2020/11/04/ex2.jpg)

    ```
    Input: matrix = [[1,2],[2,2]]
    Output: false
    Explanation:
    The diagonal "[1, 2]" has different elements.
    ```

    ## Constraints

    - m == matrix.length
    - n == matrix[i].length
    - 1 <= m, n <= 20
    - 0 <= matrix[i][j] <= 99

    **Follow up:**

    - What if the `matrix` is stored on disk, and the memory is limited such that you can only load at most one row of the matrix into the memory at once?
    - What if the `matrix` is so large that you can only load up a partial row into the memory at once?

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def is_toeplitz_matrix(self, matrix: list[list[int]]) -> bool:
            raise NotImplementedError('Implement is_toeplitz_matrix')

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
