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
    # 305. Number of Islands II

    **Hard** · Union Find, Array, Hash Table

    You are given an empty 2D binary grid `grid` of size `m x n`. The grid represents a map where `0`s represent water and `1`s represent land. Initially, all the cells of `grid` are water cells (i.e., all the cells are `0`s).

    We may perform an add land operation which turns the water at position into a land. You are given an array `positions` where `positions[i] = [ri, ci]` is the position `(ri, ci)` at which we should operate the ith operation.

    Return *an array of integers* `answer` *where* `answer[i]` *is the number of islands after turning the cell* `(ri, ci)` *into a land*.

    An **island** is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

    ## Examples

    ![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0300-0399/0305.Number%20of%20Islands%20II/images/tmp-grid.jpg)

    ```
    Input: m = 3, n = 3, positions = [[0,0],[0,1],[1,2],[2,1]]
    Output: [1,1,2,3]
    Explanation:
    Initially, the 2d grid is filled with water.
    - Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land. We have 1 island.
    - Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land. We still have 1 island.
    - Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land. We have 2 islands.
    - Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land. We have 3 islands.
    ```

    ```
    Input: m = 1, n = 1, positions = [[0,0]]
    Output: [1]
    ```

    ## Constraints

    - `1 <= m, n, positions.length <= 10^4`
    - `1 <= m * n <= 10^4`
    - `positions[i].length == 2`
    - `0 <= ri < m`
    - `0 <= ci < n`

    **Follow up:** Could you solve it in time complexity `O(k log(mn))`, where `k == positions.length`?

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class UnionFind:

        def __init__(self, n: int) -> None:
            self.p = list(range(n))
            self.size = [1] * n

        def find(self, x: int) -> int:
            if self.p[x] != x:
                self.p[x] = self.find(self.p[x])
            return self.p[x]

        def union(self, a: int, b: int) -> bool:
            pa, pb = (self.find(a), self.find(b))
            if pa == pb:
                return False
            if self.size[pa] > self.size[pb]:
                self.p[pb] = pa
                self.size[pa] += self.size[pb]
            else:
                self.p[pa] = pb
                self.size[pb] += self.size[pa]
            return True

    class Solution:

        def num_islands2(self, m: int, n: int, positions: list[list[int]]) -> list[int]:
            raise NotImplementedError('Implement num_islands2')

    practice_exports = {'UnionFind': UnionFind, 'Solution': Solution}
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
