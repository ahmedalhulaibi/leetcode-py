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
    # 317. Shortest Distance from All Buildings

    **Hard** · Breadth-First Search, Array, Matrix

    You are given an `m x n` grid `grid` of values `0`, `1`, or `2`, where:

    - each `0` marks **an empty land** that you can pass by freely,
    - each `1` marks **a building** that you cannot pass through, and
    - each `2` marks **an obstacle** that you cannot pass through.

    You want to build a house on an empty land that reaches all buildings in the **shortest total travel** distance. You can only move up, down, left, and right.

    Return *the **shortest travel distance** for such a house*. If it is not possible to build such a house according to the above rules, return `-1`.

    The **total travel distance** is the sum of the distances between the houses of the friends and the meeting point.

    ## Examples

    ![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0300-0399/0317.Shortest%20Distance%20from%20All%20Buildings/images/buildings-grid.jpg)

    ```
    Input: grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
    Output: 7
    Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2).
    The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal.
    So return 7.
    ```

    ```
    Input: grid = [[1,0]]
    Output: 1
    ```

    ```
    Input: grid = [[1]]
    Output: -1
    ```

    ## Constraints

    - `m == grid.length`
    - `n == grid[i].length`
    - `1 <= m, n <= 50`
    - `grid[i][j]` is either `0`, `1`, or `2`.
    - There will be **at least one** building in the `grid`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def shortest_distance(self, grid: list[list[int]]) -> int:
            raise NotImplementedError('Implement shortest_distance')

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
