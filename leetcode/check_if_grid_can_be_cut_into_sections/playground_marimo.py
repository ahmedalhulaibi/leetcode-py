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
    # 3394. Check if Grid can be Cut into Sections

    **Medium** · Array, Sorting

    You are given an integer <code>n</code> representing the dimensions of an <code>n x n</code> grid, with the origin at the bottom-left corner of the grid. You are also given a 2D array of coordinates <code>rectangles</code>, where <code>rectangles[i]</code> is in the form <code>[start<sub>x</sub>, start<sub>y</sub>, end<sub>x</sub>, end<sub>y</sub>]</code>, representing a rectangle on the grid. Each rectangle is defined as follows:

    - <code>(start<sub>x</sub>, start<sub>y</sub>)</code>: The bottom-left corner of the rectangle.
    - <code>(end<sub>x</sub>, end<sub>y</sub>)</code>: The top-right corner of the rectangle.

    <strong>Note </strong>that the rectangles do not overlap. Your task is to determine if it is possible to make <strong>either two horizontal or two vertical cuts</strong> on the grid such that:

    - Each of the three resulting sections formed by the cuts contains <strong>at least</strong> one rectangle.
    - Every rectangle belongs to <strong>exactly</strong> one section.

    Return <code>true</code> if such cuts can be made; otherwise, return <code>false</code>.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2024/10/23/tt1drawio.png)

    ```
    Input: n = 5, rectangles = [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]
    Output: true
    ```
    **Explanation:** The grid is shown in the diagram. We can make horizontal cuts at <code>y = 2</code> and <code>y = 4</code>. Hence, the output is true.

    ![Example 2](https://assets.leetcode.com/uploads/2024/10/23/tc2drawio.png)

    ```
    Input: n = 4, rectangles = [[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]]
    Output: true
    ```
    **Explanation:** We can make vertical cuts at <code>x = 2</code> and <code>x = 3</code>. Hence, the output is true.

    ```
    Input: n = 4, rectangles = [[0,2,2,4],[1,0,3,2],[2,2,3,4],[3,0,4,2],[3,2,4,4]]
    Output: false
    ```
    **Explanation:** We cannot make two horizontal or two vertical cuts that satisfy the conditions. Hence, the output is false.

    ## Constraints

    - 3 <= n <= 10^9
    - 3 <= rectangles.length <= 10^5
    - 0 <= rectangles[i][0] < rectangles[i][2] <= n
    - 0 <= rectangles[i][1] < rectangles[i][3] <= n
    - No two rectangles overlap.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def check_valid_cuts(self, n: int, rectangles: list[list[int]]) -> bool:
            raise NotImplementedError('Implement check_valid_cuts')

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
