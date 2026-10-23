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
    # 2503. Maximum Number of Points From Grid Queries

    **Hard** · Array, Two Pointers, Breadth-First Search, Union-Find, Sorting, Heap (Priority Queue), Matrix

    You are given an `m x n` integer matrix `grid` and an array `queries` of size `k`.

    Find an array `answer` of size `k` such that for each integer `queries[i]` you start in the top left cell of the matrix and repeat the following process:

    - If `queries[i]` is strictly greater than the value of the current cell that you are in, then you get one point if it is your first time visiting this cell, and you can move to any adjacent cell in all `4` directions: up, down, left, and right.
    - Otherwise, you do not get any points, and you end this process.

    After the process, `answer[i]` is the maximum number of points you can get. Note that for each query you are allowed to visit the same cell multiple times.

    Return the resulting array `answer`.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2025/03/15/image1.png)

    ```
    Input: grid = [[1,2,3],[2,5,7],[3,5,1]]
    queries = [5,6,2]
    Output: [5,8,1]
    Explanation: The diagrams above show which cells we visit to get points for each query.
    ```

    ```
    Input: grid = [[5,2,1],[1,1,2]]
    queries = [3]
    Output: [0]
    Explanation: We can not get any points because the value of the top left cell is already greater than or equal to 3.
    ```

    ## Constraints

    - `m == grid.length`
    - `n == grid[i].length`
    - `2 <= m, n <= 10^3`
    - `4 <= m * n <= 10^5`
    - `k == queries.length`
    - `1 <= k <= 10^4`
    - `1 <= grid[i][j], queries[i] <= 10^6`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def max_points(self, grid: list[list[int]], queries: list[int]) -> list[int]:
            raise NotImplementedError('Implement max_points')

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
