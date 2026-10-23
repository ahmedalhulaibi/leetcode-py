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
    # 812. Largest Triangle Area

    **Easy** · Array, Math, Geometry, Polygons

    Given an array of points on the X-Y plane `points` where `points[i] = [xi, yi]`, return *the area of the largest triangle that can be formed by any three different points*. Answers within `10^-5` of the actual answer will be accepted.

    ## Examples

    ![Example 1](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/04/1027.png)

    ```
    Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
    Output: 2.00000
    Explanation: The five points are shown in the above figure. The red triangle is the largest.
    ```

    ```
    Input: points = [[1,0],[0,0],[0,1]]
    Output: 0.50000
    ```

    ## Constraints

    - 3 <= points.length <= 50
    - -50 <= xi, yi <= 50
    - All the given points are unique.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def largest_triangle_area(self, points: list[list[int]]) -> float:
            raise NotImplementedError('Implement largest_triangle_area')

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
