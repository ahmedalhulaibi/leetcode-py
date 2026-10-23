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
    # 2392. Build a Matrix With Conditions

    **Hard** · Array, Graph Theory, Topological Sort, Matrix

    You are given a **positive** integer `k`. You are also given:

    - a 2D integer array `rowConditions` of size `n` where `rowConditions[i] = [above_i, below_i]`, and
    - a 2D integer array `colConditions` of size `m` where `colConditions[i] = [left_i, right_i]`.

    The two arrays contain integers from `1` to `k`.

    You have to build a `k x k` matrix that contains each of the numbers from `1` to `k` **exactly once**. The remaining cells should have the value `0`.

    The matrix should also satisfy the following conditions:

    - The number `above_i` should appear in a **row** that is strictly **above** the row at which the number `below_i` appears for all `i` from `0` to `n - 1`.
    - The number `left_i` should appear in a **column** that is strictly **left** of the column at which the number `right_i` appears for all `i` from `0` to `m - 1`.

    Return ***any** matrix that satisfies the conditions*. If no answer exists, return an empty matrix.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2022/07/06/gridosdrawio.png)

    ```
    Input: k = 3, rowConditions = [[1,2],[3,2]], colConditions = [[2,1],[3,2]]
    Output: [[3,0,0],[0,0,1],[0,2,0]]
    Explanation: The diagram above shows a valid example of a matrix that satisfies all the conditions.
    The row conditions are the following:
    - Number 1 is in row 1, and number 2 is in row 2, so 1 is above 2 in the matrix.
    - Number 3 is in row 0, and number 2 is in row 2, so 3 is above 2 in the matrix.
    The column conditions are the following:
    - Number 2 is in column 1, and number 1 is in column 2, so 2 is left of 1 in the matrix.
    - Number 3 is in column 0, and number 2 is in column 1, so 3 is left of 2 in the matrix.
    Note that there may be multiple correct answers.
    ```

    ```
    Input: k = 3, rowConditions = [[1,2],[2,3],[3,1],[2,3]], colConditions = [[2,1]]
    Output: []
    Explanation: From the first two conditions, 3 has to be below 1 but the third conditions needs 3 to be above 1 to be satisfied.
    No matrix can satisfy all the conditions, so we return the empty matrix.
    ```

    ## Constraints

    - 2 <= k <= 400
    - 1 <= rowConditions.length, colConditions.length <= 10^4
    - rowConditions[i].length == colConditions[i].length == 2
    - 1 <= above_i, below_i, left_i, right_i <= k
    - above_i != below_i
    - left_i != right_i



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def build_matrix(self, k: int, row_conditions: list[list[int]], col_conditions: list[list[int]]) -> list[list[int]]:
            raise NotImplementedError('Implement build_matrix')

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
