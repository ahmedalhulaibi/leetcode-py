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
    # 785. Is Graph Bipartite?

    **Medium** · Depth-First Search, Breadth-First Search, Union-Find, Graph Theory

    There is an undirected graph with `n` nodes, where each node is numbered between `0` and `n - 1`. You are given a 2D array `graph`, where `graph[u]` is an array of nodes that node `u` is adjacent to. More formally, for each `v` in `graph[u]`, there is an undirected edge between node `u` and node `v`. The graph has the following properties:

    - There are no self-edges (`graph[u]` does not contain `u`).
    - There are no parallel edges (`graph[u]` does not contain duplicate values).
    - If `v` is in `graph[u]`, then `u` is in `graph[v]` (the graph is undirected).
    - The graph may not be connected, meaning there may be two nodes `u` and `v` such that there is no path between them.

    A graph is **bipartite** if the nodes can be partitioned into two independent sets `A` and `B` such that **every** edge in the graph connects a node in set `A` and a node in set `B`.

    Return `true` *if and only if it is **bipartite***.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2020/10/21/bi2.jpg)

    ```
    Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
    Output: false
    Explanation: There is no way to partition the nodes into two independent sets such that every edge connects a node in one and a node in the other.
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2020/10/21/bi1.jpg)

    ```
    Input: graph = [[1,3],[0,2],[1,3],[0,2]]
    Output: true
    Explanation: We can partition the nodes into two sets: {0, 2} and {1, 3}.
    ```

    ## Constraints

    - graph.length == n
    - 1 <= n <= 100
    - 0 <= graph[u].length < n
    - 0 <= graph[u][i] <= n - 1
    - graph[u] does not contain u.
    - All the values of graph[u] are unique.
    - If graph[u] contains v, then graph[v] contains u.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def is_bipartite(self, graph: list[list[int]]) -> bool:
            raise NotImplementedError('Implement is_bipartite')

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
