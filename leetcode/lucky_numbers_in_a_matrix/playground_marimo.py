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
    # 1380. Lucky Numbers in a Matrix

    **Easy** · Array, Matrix

    Given an `m x n` matrix of **distinct** numbers, return all **lucky numbers** in the matrix in **any** order.

    A **lucky number** is an element of the matrix such that it is the minimum element in its row and maximum in its column.

    ## Examples

    ```
    Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
    Output: [15]
    ```
    **Explanation:** 15 is the only lucky number since it is the minimum in its row and the maximum in its column.

    ```
    Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
    Output: [12]
    ```
    **Explanation:** 12 is the only lucky number since it is the minimum in its row and the maximum in its column.

    ```
    Input: matrix = [[7,8],[1,2]]
    Output: [7]
    ```

    ## Constraints

    - m == mat.length
    - n == mat[i].length
    - 1 <= n, m <= 50
    - 1 <= matrix[i][j] <= 10^5
    - All elements in the matrix are distinct.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def lucky_numbers(self, matrix: list[list[int]]) -> list[int]:
            raise NotImplementedError('Implement lucky_numbers')

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
