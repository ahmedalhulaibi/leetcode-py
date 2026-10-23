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
    # 3203. Find Minimum Diameter After Merging Two Trees

    **Hard** · Tree, Depth-First Search, Breadth-First Search, Graph Theory

    There exist two **undirected** trees with `n` and `m` nodes, numbered from `0` to `n - 1` and from `0` to `m - 1`, respectively. You are given two 2D integer arrays `edges1` and `edges2` of lengths `n - 1` and `m - 1`, respectively, where `edges1[i] = [ai, bi]` indicates that there is an edge between nodes `ai` and `bi` in the first tree and `edges2[i] = [ui, vi]` indicates that there is an edge between nodes `ui` and `vi` in the second tree.

    You must connect one node from the first tree with another node from the second tree with an edge.

    Return the **minimum** possible **diameter** of the resulting tree.

    The **diameter** of a tree is the length of the longest path between any two nodes in the tree.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2024/04/22/example11-transformed.png)

    ```
    Input: edges1 = [[0,1],[0,2],[0,3]], edges2 = [[0,1]]
    Output: 3
    ```

    **Explanation:** We can obtain a tree of diameter 3 by connecting node 0 from the first tree with any node from the second tree.

    ![Example 2](https://assets.leetcode.com/uploads/2024/04/22/example211.png)

    ```
    Input: edges1 = [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]], edges2 = [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]]
    Output: 5
    ```

    **Explanation:** We can obtain a tree of diameter 5 by connecting node 0 from the first tree with node 0 from the second tree.

    ## Constraints

    - `1 <= n, m <= 10^5`
    - `edges1.length == n - 1`
    - `edges2.length == m - 1`
    - `edges1[i].length == edges2[i].length == 2`
    - `edges1[i] = [ai, bi]`
    - `0 <= ai, bi < n`
    - `edges2[i] = [ui, vi]`
    - `0 <= ui, vi < m`
    - The input is generated such that `edges1` and `edges2` represent valid trees.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def minimum_diameter_after_merge(self, edges1: list[list[int]], edges2: list[list[int]]) -> int:
            raise NotImplementedError('Implement minimum_diameter_after_merge')

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
