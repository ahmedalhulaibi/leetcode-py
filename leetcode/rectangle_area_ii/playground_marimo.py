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
    # 850. Rectangle Area II

    **Hard** · Array, Segment Tree, Sweep Line, Ordered Set

    You are given a 2D array of axis-aligned rectangles. Each `rectangle[i] = [xi1, yi1, xi2, yi2]` denotes the ith rectangle where `(xi1, yi1)` are the coordinates of the bottom-left corner, and `(xi2, yi2)` are the coordinates of the top-right corner.

    Calculate the total area covered by all rectangles in the plane. Any area covered by two or more rectangles should only be counted once.

    Return the total area. Since the answer may be too large, return it modulo `10^9 + 7`.

    ## Examples

    ![Example 1](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/06/06/rectangle_area_ii_pic.png)

    ```
    Input: rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
    Output: 6
    Explanation: A total area of 6 is covered by all three rectangles, as illustrated in the picture.
    From (1,1) to (2,2), the green and red rectangles overlap.
    From (1,0) to (2,3), all three rectangles overlap.
    ```

    ```
    Input: rectangles = [[0,0,1000000000,1000000000]]
    Output: 49
    Explanation: The answer is 10^18 modulo (10^9 + 7), which is 49.
    ```

    ## Constraints

    - 1 <= rectangles.length <= 200
    - rectangles[i].length == 4
    - 0 <= xi1, yi1, xi2, yi2 <= 10^9
    - xi1 <= xi2
    - yi1 <= yi2
    - All rectangles have non zero area.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def rectangle_area(self, rectangles: list[list[int]]) -> int:
            raise NotImplementedError('Implement rectangle_area')

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
