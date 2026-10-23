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
    # 1579. Remove Max Number of Edges to Keep Graph Fully Traversable

    **Hard** · Union-Find, Graph Theory

    Alice and Bob have an undirected graph of `n` nodes and three types of edges:

    - Type 1: Can be traversed by Alice only.
    - Type 2: Can be traversed by Bob only.
    - Type 3: Can be traversed by both Alice and Bob.

    Given an array `edges` where `edges[i] = [typei, ui, vi]` represents a bidirectional edge of type `typei` between nodes `ui` and `vi`, find the maximum number of edges you can remove so that after removing the edges, the graph can still be fully traversed by both Alice and Bob. The graph is fully traversed by Alice and Bob if starting from any node, they can reach all other nodes.

    Return *the maximum number of edges you can remove, or return* `-1` *if Alice and Bob cannot fully traverse the graph.*

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2020/08/19/ex1.png)

    ```
    Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
    Output: 2
    Explanation: If we remove the 2 edges [1,1,2] and [1,1,3]. The graph will still be fully traversable by Alice and Bob. Removing any additional edge will not make it so. So the maximum number of edges we can remove is 2.
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2020/08/19/ex2.png)

    ```
    Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
    Output: 0
    Explanation: Notice that removing any edge will not make the graph fully traversable by Alice and Bob.
    ```

    ![Example 3](https://assets.leetcode.com/uploads/2020/08/19/ex3.png)

    ```
    Input: n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]
    Output: -1
    Explanation: In the current graph, Alice cannot reach node 4 from the other nodes. Likewise, Bob cannot reach 1. Therefore it's impossible to make the graph fully traversable.
    ```

    ## Constraints

    - 1 <= n <= 10^5
    - 1 <= edges.length <= min(10^5, 3 * n * (n - 1) / 2)
    - edges[i].length == 3
    - 1 <= typei <= 3
    - 1 <= ui < vi <= n
    - All tuples (typei, ui, vi) are distinct.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def max_num_edges_to_remove(self, n: int, edges: list[list[int]]) -> int:
            raise NotImplementedError('Implement max_num_edges_to_remove')

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
