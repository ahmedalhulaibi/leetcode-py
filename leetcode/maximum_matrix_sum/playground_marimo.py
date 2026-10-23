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
    # 1975. Maximum Matrix Sum

    **Medium** · Array, Greedy, Matrix

    You are given an `n x n` integer `matrix`. You can do the following operation **any** number of times:

    - Choose any two **adjacent** elements of `matrix` and **multiply** each of them by `-1`.

    Two elements are considered **adjacent** if and only if they share a **border**.

    Your goal is to **maximize** the summation of the matrix's elements. Return *the **maximum** sum of the matrix's elements using the operation mentioned above.*

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2021/07/16/pc79-q2ex1.png)

    ```
    Input: matrix = [[1,-1],[-1,1]]
    Output: 4
    Explanation: We can follow the following steps to reach sum equals 4:
    - Multiply the 2 elements in the first row by -1.
    - Multiply the 2 elements in the first column by -1.
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2021/07/16/pc79-q2ex2.png)

    ```
    Input: matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
    Output: 16
    Explanation: We can follow the following step to reach sum equals 16:
    - Multiply the 2 last elements in the second row by -1.
    ```

    ## Constraints

    - `n == matrix.length == matrix[i].length`
    - `2 <= n <= 250`
    - `-10^5 <= matrix[i][j] <= 10^5`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def max_matrix_sum(self, matrix: list[list[int]]) -> int:
            raise NotImplementedError('Implement max_matrix_sum')

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
