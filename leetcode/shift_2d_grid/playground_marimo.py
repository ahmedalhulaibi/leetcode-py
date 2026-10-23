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
    # 1260. Shift 2D Grid

    **Easy** · Array, Matrix, Simulation

    Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.

    In one shift operation:

    - Element at grid[i][j] moves to grid[i][j + 1].
    - Element at grid[i][n - 1] moves to grid[i + 1][0].
    - Element at grid[m - 1][n - 1] moves to grid[0][0].

    Return the 2D grid after applying shift operation k times.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2019/11/05/e1.png)

    ```
    Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
    Output: [[9,1,2],[3,4,5],[6,7,8]]
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2019/11/05/e2.png)

    ```
    Input: grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
    Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
    ```

    ```
    Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
    Output: [[1,2,3],[4,5,6],[7,8,9]]
    ```

    ## Constraints

    - m == grid.length
    - n == grid[i].length
    - 1 <= m <= 50
    - 1 <= n <= 50
    - -1000 <= grid[i][j] <= 1000
    - 0 <= k <= 100

    **Follow up:**

    - Can you find a O(n * m) solution?
    - Can you find an in-place solution?

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def shift_grid(self, grid: list[list[int]], k: int) -> list[list[int]]:
            raise NotImplementedError('Implement shift_grid')

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
