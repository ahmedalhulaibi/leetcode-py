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
    # 1489. Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree

    **Hard** · Union-Find, Graph Theory, Sorting, Minimum Spanning Tree, Strongly Connected Component

    Given a weighted undirected connected graph with `n` vertices numbered from `0` to `n - 1`, and an array `edges` where `edges[i] = [ai, bi, weighti]` represents a bidirectional and weighted edge between nodes `ai` and `bi`. A minimum spanning tree (MST) is a subset of the graph's edges that connects all vertices without cycles and with the minimum possible total edge weight.

    Find *all the critical and pseudo-critical edges in the given graph's minimum spanning tree (MST)*. An MST edge whose deletion from the graph would cause the MST weight to increase is called a *critical edge*. On the other hand, a pseudo-critical edge is that which can appear in some MSTs but not all.

    Note that you can return the indices of the edges in any order.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2020/06/04/ex1.png)

    ```
    Input: n = 5, edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
    Output: [[0,1],[2,3,4,5]]
    Explanation: The two edges 0 and 1 appear in all MSTs, therefore they are critical edges.
    The edges 2, 3, 4, and 5 are only part of some MSTs, therefore they are considered pseudo-critical edges.
    ```

    ![All possible MSTs](https://assets.leetcode.com/uploads/2020/06/04/msts.png)

    ![Example 2](https://assets.leetcode.com/uploads/2020/06/04/ex2.png)

    ```
    Input: n = 4, edges = [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]
    Output: [[],[0,1,2,3]]
    Explanation: Since all 4 edges have equal weight, choosing any 3 edges from the given 4 will yield an MST. Therefore all 4 edges are pseudo-critical.
    ```

    ## Constraints

    - `2 <= n <= 100`
    - `1 <= edges.length <= min(200, n * (n - 1) / 2)`
    - `edges[i].length == 3`
    - `0 <= ai < bi < n`
    - `1 <= weighti <= 1000`
    - All pairs `(ai, bi)` are **distinct**



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def find_critical_and_pseudo_critical_edges(self, n: int, edges: list[list[int]]) -> list[list[int]]:
            raise NotImplementedError('Implement find_critical_and_pseudo_critical_edges')

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
