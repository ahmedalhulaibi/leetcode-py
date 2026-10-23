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
    # 1637. Widest Vertical Area Between Two Points Containing No Points

    **Easy** · Array, Sorting

    Given `n` points on a 2D plane where `points[i] = [xi, yi]`, return the widest vertical area between two points such that no points are inside the area.

    A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height). The widest vertical area is the one with the maximum width.

    Note that points on the edge of a vertical area are not considered included in the area.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2020/09/19/points3.png)

    ```
    Input: points = [[8,7],[9,9],[7,4],[9,7]]
    Output: 1
    Explanation: Both the red and the blue area are optimal.
    ```

    ```
    Input: points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
    Output: 3
    ```

    ## Constraints

    - n == points.length
    - 2 <= n <= 10^5
    - points[i].length == 2
    - 0 <= xi, yi <= 10^9



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def max_width_of_vertical_area(self, points: list[list[int]]) -> int:
            raise NotImplementedError('Implement max_width_of_vertical_area')

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
