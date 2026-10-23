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
    # 2493. Divide Nodes Into the Maximum Number of Groups

    **Hard** · Breadth-First Search, Depth-First Search, Union Find, Graph

    You are given a positive integer `n` representing the number of nodes in an **undirected** graph. The nodes are labeled from `1` to `n`.

    You are also given a 2D integer array `edges`, where `edges[i] = [ai, bi]` indicates that there is a **bidirectional** edge between nodes `ai` and `bi`. **Notice** that the given graph may be disconnected.

    Divide the nodes of the graph into `m` groups (**1-indexed**) such that:

    - Each node in the graph belongs to exactly one group.
    - For every pair of nodes in the graph that are connected by an edge `[ai, bi]`, if `ai` belongs to the group with index `x`, and `bi` belongs to the group with index `y`, then `|y - x| = 1`.

    Return the maximum number of groups (i.e., maximum `m`) into which you can divide the nodes. Return `-1` if it is impossible to group the nodes with the given conditions.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2022/10/13/example1.png)

    ```
    Input: n = 6, edges = [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]
    Output: 4
    Explanation: As shown in the image we:
    - Add node 5 to the first group.
    - Add node 1 to the second group.
    - Add nodes 2 and 4 to the third group.
    - Add nodes 3 and 6 to the fourth group.
    We can see that every edge is satisfied.
    It can be shown that if we create a fifth group and move any node from the third or fourth group to it, at least one of the edges will not be satisfied.
    ```

    ```
    Input: n = 3, edges = [[1,2],[2,3],[3,1]]
    Output: -1
    Explanation: If we add node 1 to the first group, node 2 to the second group, and node 3 to the third group to satisfy the first two edges, we can see that the third edge will not be satisfied.
    It can be shown that no grouping is possible.
    ```

    ## Constraints

    - `1 <= n <= 500`
    - `1 <= edges.length <= 10^4`
    - `edges[i].length == 2`
    - `1 <= ai, bi <= n`
    - `ai != bi`
    - There is at most one edge between any pair of vertices.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def magnificent_sets(self, n: int, edges: list[list[int]]) -> int:
            raise NotImplementedError('Implement magnificent_sets')

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
