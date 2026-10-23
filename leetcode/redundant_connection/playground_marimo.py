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
    # 684. Redundant Connection

    **Medium** · Depth-First Search, Breadth-First Search, Union-Find, Graph Theory

    In this problem, a tree is an **undirected graph** that is connected and has no cycles.

    You are given a graph that started as a tree with `n` nodes labeled from `1` to `n`, with one additional edge added. The added edge has two **different** vertices chosen from `1` to `n`, and was not an edge that already existed. The graph is represented as an array `edges` of length `n` where `edges[i] = [a<sub>i</sub>, b<sub>i</sub>]` indicates that there is an edge between nodes `a<sub>i</sub>` and `b<sub>i</sub>` in the graph.

    Return _an edge that can be removed so that the resulting graph is a tree of_ `n` _nodes_. If there are multiple answers, return the answer that occurs last in the input.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2021/05/02/reduntant1-1-graph.jpg)

    ```
    Input: edges = [[1,2],[1,3],[2,3]]
    Output: [2,3]
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2021/05/02/reduntant1-2-graph.jpg)

    ```
    Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
    Output: [1,4]
    ```

    ## Constraints

    - n == edges.length
    - 3 <= n <= 1000
    - edges[i].length == 2
    - 1 <= a<sub>i</sub> < b<sub>i</sub> <= edges.length
    - a<sub>i</sub> != b<sub>i</sub>
    - There are no repeated edges.
    - The given graph is connected.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def find_redundant_connection(self, edges: list[list[int]]) -> list[int]:
            raise NotImplementedError('Implement find_redundant_connection')

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
