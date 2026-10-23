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
    # 554. Brick Wall

    **Medium** · Array, Hash Table

    There is a rectangular brick wall in front of you with `n` rows of bricks. The i<sup>th</sup> row has some number of bricks each of the same height (i.e., one unit) but they can be of different widths. The total width of each row is the same.

    Draw a vertical line from the top to the bottom and cross the least bricks. If your line goes through the edge of a brick, then the brick is not considered as crossed. You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.

    Given the 2D integer array `wall` that contains the information about the wall, return *the minimum number of crossed bricks after drawing such a vertical line*.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2025/01/17/a.png)

    ```
    Input: wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
    Output: 2
    ```

    ```
    Input: wall = [[1],[1],[1]]
    Output: 3
    ```

    ## Constraints

    - n == wall.length
    - 1 <= n <= 10^4
    - 1 <= wall[i].length <= 10^4
    - 1 <= sum(wall[i].length) <= 2 * 10^4
    - sum(wall[i]) is the same for each row i.
    - 1 <= wall[i][j] <= 2^31 - 1



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from collections import Counter

    class Solution:

        def least_bricks(self, wall: list[list[int]]) -> int:
            raise NotImplementedError('Implement least_bricks')

    practice_exports = {'Counter': Counter, 'Solution': Solution}
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
