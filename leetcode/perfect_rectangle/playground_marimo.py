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
    # 391. Perfect Rectangle

    **Hard** · Array, Hash Table, Math, Geometry, Sweep Line

    Given an array `rectangles` where `rectangles[i] = [x<sub>i</sub>, y<sub>i</sub>, a<sub>i</sub>, b<sub>i</sub>]` represents an axis-aligned rectangle. The bottom-left point of the rectangle is `(x<sub>i</sub>, y<sub>i</sub>)` and the top-right point of it is `(a<sub>i</sub>, b<sub>i</sub>)`.

    Return `true` *if all the rectangles together form an exact cover of a rectangular region*.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2021/03/27/perectrec1-plane.jpg)

    ```
    Input: rectangles = [[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]
    Output: true
    Explanation: All 5 rectangles together form an exact cover of a rectangular region.
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2021/03/27/perfectrec2-plane.jpg)

    ```
    Input: rectangles = [[1,1,2,3],[1,3,2,4],[3,1,4,2],[3,2,4,4]]
    Output: false
    Explanation: Because there is a gap between the two rectangular regions.
    ```

    ![Example 3](https://assets.leetcode.com/uploads/2021/03/27/perfecrrec4-plane.jpg)

    ```
    Input: rectangles = [[1,1,3,3],[3,1,4,2],[1,3,2,4],[2,2,4,4]]
    Output: false
    Explanation: Because two of the rectangles overlap with each other.
    ```

    ## Constraints

    - 1 <= rectangles.length <= 2 * 10^4
    - rectangles[i].length == 4
    - -10^5 <= xi < ai <= 10^5
    - -10^5 <= yi < bi <= 10^5



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def is_rectangle_cover(self, rectangles: list[list[int]]) -> bool:
            raise NotImplementedError('Implement is_rectangle_cover')

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
