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
    # 2033. Minimum Operations to Make a Uni-Value Grid

    **Medium** · Array, Math, Sorting, Matrix

    You are given a 2D integer grid of size m x n and an integer x. In one operation, you can add x to or subtract x from any element in the grid.

    A uni-value grid is a grid where all the elements of it are equal.

    Return the minimum number of operations to make the grid uni-value. If it is not possible, return -1.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2021/09/21/gridtxt.png)

    ```
    Input: grid = [[2,4],[6,8]], x = 2
    Output: 4
    Explanation: We can make every element equal to 4 by doing the following:
    - Add x to 2 once.
    - Subtract x from 6 once.
    - Subtract x from 8 twice.
    A total of 4 operations were used.
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2021/09/21/gridtxt-1.png)

    ```
    Input: grid = [[1,5],[2,3]], x = 1
    Output: 5
    Explanation: We can make every element equal to 3.
    ```

    ![Example 3](https://assets.leetcode.com/uploads/2021/09/21/gridtxt-2.png)

    ```
    Input: grid = [[1,2],[3,4]], x = 2
    Output: -1
    Explanation: It is impossible to make every element equal.
    ```

    ## Constraints

    - m == grid.length
    - n == grid[i].length
    - 1 <= m, n <= 10^5
    - 1 <= m * n <= 10^5
    - 1 <= x, grid[i][j] <= 10^4



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def min_operations(self, grid: list[list[int]], x: int) -> int:
            raise NotImplementedError('Implement min_operations')

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
