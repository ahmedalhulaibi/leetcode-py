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
    # 1059. All Paths from Source Lead to Destination

    **Medium** · Graph, Topological Sort, Depth-First Search, Kosaraju

    Given the `edges` of a directed graph where `edges[i] = [ai, bi]` indicates there is an edge between nodes `ai` and `bi`, and two nodes `source` and `destination` of this graph, determine whether or not all paths starting from `source` eventually, end at `destination`, that is:

    - At least one path exists from the `source` node to the `destination` node
    - If a path exists from the `source` node to a node with no outgoing edges, then that node is equal to `destination`.
    - The number of possible paths from `source` to `destination` is a finite number.

    Return `true` if and only if all roads from `source` lead to `destination`.

    ## Examples

    ```
    Input: n = 3, edges = [[0,1],[0,2]], source = 0, destination = 2
    Output: false
    Explanation: It is possible to reach and get stuck on both node 1 and node 2.
    ```

    ```
    Input: n = 4, edges = [[0,1],[0,3],[1,2],[2,1]], source = 0, destination = 3
    Output: false
    Explanation: We have two possibilities: to end at node 3, or to loop over node 1 and node 2 indefinitely.
    ```

    ```
    Input: n = 4, edges = [[0,1],[0,2],[1,3],[2,3]], source = 0, destination = 3
    Output: true
    ```

    ## Constraints

    - 1 <= n <= 10^4
    - 0 <= edges.length <= 10^4
    - edges[i].length == 2
    - 0 <= ai, bi <= n - 1
    - 0 <= source <= n - 1
    - 0 <= destination <= n - 1
    - The given graph may have self-loops and parallel edges.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def leads_to_destination(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
            raise NotImplementedError('Implement leads_to_destination')

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
