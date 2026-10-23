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
    # 469. Convex Polygon

    **Medium** · Geometry, Array, Math, Polygon

    You are given an array of points on the **X-Y** plane `points` where `points[i] = [x_i, y_i]`. The points form a polygon when joined sequentially.

    Return `true` if this polygon is [convex](http://en.wikipedia.org/wiki/Convex_polygon) and `false` otherwise.

    You may assume the polygon formed by given points is always a [simple polygon](http://en.wikipedia.org/wiki/Simple_polygon). In other words, we ensure that exactly two edges intersect at each vertex and that edges otherwise don't intersect each other.

    ## Examples

    ![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0400-0499/0469.Convex%20Polygon/images/covpoly1-plane.jpg)

    ```
    Input: points = [[0,0],[0,5],[5,5],[5,0]]
    Output: true
    ```

    ![Example 2](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0400-0499/0469.Convex%20Polygon/images/covpoly2-plane.jpg)

    ```
    Input: points = [[0,0],[0,10],[10,10],[10,0],[5,5]]
    Output: false
    ```

    ## Constraints

    - `3 <= points.length <= 10^4`
    - `points[i].length == 2`
    - `-10^4 <= x_i, y_i <= 10^4`
    - All the given points are **unique**.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def is_convex(self, points: list[list[int]]) -> bool:
            raise NotImplementedError('Implement is_convex')

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
