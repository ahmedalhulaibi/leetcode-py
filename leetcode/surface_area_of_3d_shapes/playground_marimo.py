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
    # 892. Surface Area of 3D Shapes

    **Easy** · Array, Math, Geometry, Matrix

    You are given an `n x n` `grid` where you have placed some `1 x 1 x 1` cubes. Each value `v = grid[i][j]` represents a tower of `v` cubes placed on top of cell `(i, j)`.

    After placing these cubes, you have decided to glue any directly adjacent cubes to each other, forming several irregular 3D shapes.

    Return the total surface area of the resulting shapes.

    Note: The bottom face of each shape counts toward its surface area.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2021/01/08/tmp-grid2.jpg)

    ```
    Input: grid = [[1,2],[3,4]]
    Output: 34
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2021/01/08/tmp-grid4.jpg)

    ```
    Input: grid = [[1,1,1],[1,0,1],[1,1,1]]
    Output: 32
    ```

    ![Example 3](https://assets.leetcode.com/uploads/2021/01/08/tmp-grid5.jpg)

    ```
    Input: grid = [[2,2,2],[2,1,2],[2,2,2]]
    Output: 46
    ```

    ## Constraints

    - n == grid.length == grid[i].length
    - 1 <= n <= 50
    - 0 <= grid[i][j] <= 50



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def surface_area(self, grid: list[list[int]]) -> int:
            raise NotImplementedError('Implement surface_area')

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
