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
    # 939. Minimum Area Rectangle

    **Medium** · Array, Hash Table, Math, Geometry, Sorting

    You are given an array of points in the **X-Y** plane `points` where `points[i] = [x<sub>i</sub>, y<sub>i</sub>]`.

    Return *the minimum area of a rectangle formed from these points, with sides parallel to the X and Y axes*. If there is not any such rectangle, return `0`.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2021/08/03/rec1.JPG)

    ```
    Input: points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
    Output: 4
    Explanation: The minimum area rectangle is shown in the image, with an area of 2 * 2 = 4.
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2021/08/03/rec2.JPG)

    ```
    Input: points = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
    Output: 2
    Explanation: The minimum area rectangle is shown in the image, with an area of 1 * 2 = 2.
    ```

    ## Constraints

    - 1 <= points.length <= 500
    - points[i].length == 2
    - 0 <= xi, yi <= 4 * 10^4
    - All the given points are unique.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def min_area_rect(self, points: list[list[int]]) -> int:
            raise NotImplementedError('Implement min_area_rect')

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
