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
    # 133. Clone Graph

    **Medium** · Hash Table, Depth-First Search, Breadth-First Search, Graph

    Given a reference of a node in a **connected** undirected graph.

    Return a **deep copy** (clone) of the graph.

    Each node in the graph contains a value (`int`) and a list (`List[Node]`) of its neighbors.

    ```
    class Node {
        public int val;
        public List<Node> neighbors;
    }
    ```

    **Test case format:**

    For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with `val == 1`, the second node with `val == 2`, and so on. The graph is represented in the test case using an adjacency list.

    **An adjacency list** is a collection of unordered **lists** used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

    The given node will always be the first node with `val = 1`. You must return the **copy of the given node** as a reference to the cloned graph.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2019/11/04/133_clone_graph_question.png)

    ```
    Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
    Output: [[2,4],[1,3],[2,4],[1,3]]
    ```
    **Explanation:** There are 4 nodes in the graph.
    1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
    2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
    3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
    4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

    ![Example 2](https://assets.leetcode.com/uploads/2020/01/07/graph.png)

    ```
    Input: adjList = [[]]
    Output: [[]]
    ```
    **Explanation:** Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.

    ```
    Input: adjList = []
    Output: []
    ```
    **Explanation:** This an empty graph, it does not have any nodes.

    ## Constraints

    - The number of nodes in the graph is in the range `[0, 100]`.
    - `1 <= Node.val <= 100`
    - `Node.val` is unique for each node.
    - There are no repeated edges and no self-loops in the graph.
    - The Graph is connected and all nodes can be visited starting from the given node.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from leetcode_py import GraphNode

    class Solution:

        def clone_graph(self, node: GraphNode | None) -> GraphNode | None:
            raise NotImplementedError('Implement clone_graph')

    practice_exports = {'GraphNode': GraphNode, 'Solution': Solution}
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
