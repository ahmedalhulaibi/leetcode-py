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
    # 2421. Number of Good Paths

    **Hard** · Array, Hash Table, Tree, Union-Find, Graph Theory, Sorting

    There is a tree (i.e. a connected, undirected graph with no cycles) consisting of `n` nodes numbered from `0` to `n - 1` and exactly `n - 1` edges.

    You are given a **0-indexed** integer array `vals` of length `n` where `vals[i]` denotes the value of the `i`th node. You are also given a 2D integer array `edges` where `edges[i] = [ai, bi]` denotes that there exists an **undirected** edge connecting nodes `ai` and `bi`.

    A **good path** is a simple path that satisfies the following conditions:

    1. The starting node and the ending node have the **same** value.
    2. All nodes between the starting node and the ending node have values **less than or equal to** the starting node (i.e. the starting node's value should be the maximum value along the path).

    Return *the number of distinct good paths*.

    Note that a path and its reverse are counted as the **same** path. For example, `0 -> 1` is considered to be the same as `1 -> 0`. A single node is also considered as a valid path.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2022/08/04/f9caaac15b383af9115c5586779dec5.png)

    ```
    Input: vals = [1,3,2,1,3], edges = [[0,1],[0,2],[2,3],[2,4]]
    Output: 6
    Explanation: There are 5 good paths consisting of a single node.
    There is 1 additional good path: 1 -> 0 -> 2 -> 4.
    (The reverse path 4 -> 2 -> 0 -> 1 is treated as the same as 1 -> 0 -> 2 -> 4.)
    Note that 0 -> 2 -> 3 is not a good path because vals[2] > vals[0].
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2022/08/04/149d3065ec165a71a1b9aec890776ff.png)

    ```
    Input: vals = [1,1,2,2,3], edges = [[0,1],[1,2],[2,3],[2,4]]
    Output: 7
    Explanation: There are 5 good paths consisting of a single node.
    There are 2 additional good paths: 0 -> 1 and 2 -> 3.
    ```

    ![Example 3](https://assets.leetcode.com/uploads/2022/08/04/31705e22af3d9c0a557459bc7d1b62d.png)

    ```
    Input: vals = [1], edges = []
    Output: 1
    Explanation: The tree consists of only one node, so there is one good path.
    ```

    ## Constraints

    - n == vals.length
    - 1 <= n <= 3 * 10^4
    - 0 <= vals[i] <= 10^5
    - edges.length == n - 1
    - edges[i].length == 2
    - 0 <= ai, bi < n
    - ai != bi
    - edges represents a valid tree.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def number_of_good_paths(self, vals: list[int], edges: list[list[int]]) -> int:
            raise NotImplementedError('Implement number_of_good_paths')

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
