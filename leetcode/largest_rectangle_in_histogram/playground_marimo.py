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
    # 84. Largest Rectangle in Histogram

    **Hard** · Array, Stack, Monotonic Stack

    Given an array of integers `heights` representing the histogram's bar height where the width of each bar is `1`, return the area of the largest rectangle in the histogram.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2021/01/04/histogram.jpg)

    ```
    Input: heights = [2,1,5,6,2,3]
    Output: 10
    ```
    **Explanation:** The above is a histogram where width of each bar is 1. The largest rectangle is shown in the red area, which has an area = 10 units.

    ![Example 2](https://assets.leetcode.com/uploads/2021/01/04/histogram-1.jpg)

    ```
    Input: heights = [2,4]
    Output: 4
    ```

    ## Constraints

    - `1 <= heights.length <= 10^5`
    - `0 <= heights[i] <= 10^4`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def largest_rectangle_area(self, heights: list[int]) -> int:
            raise NotImplementedError('Implement largest_rectangle_area')

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
