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
    # 2872. Maximum Number of K-Divisible Components

    **Hard** · Tree, Depth-First Search

    There is an undirected tree with `n` nodes labeled from `0` to `n - 1`. You are given the integer `n` and a 2D integer array `edges` of length `n - 1`, where `edges[i] = [a<sub>i</sub>, b<sub>i</sub>]` indicates that there is an edge between nodes `a<sub>i</sub>` and `b<sub>i</sub>` in the tree.

    You are also given a **0-indexed** integer array `values` of length `n`, where `values[i]` is the **value** associated with the `i<sup>th</sup>` node, and an integer `k`.

    A **valid split** of the tree is obtained by removing any set of edges, possibly empty, from the tree such that the resulting components all have values that are divisible by `k`, where the **value of a connected component** is the sum of the values of its nodes.

    Return *the **maximum number of components** in any valid split*.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2023/08/07/example12-cropped2svg.jpg)

    ```
    Input: n = 5, edges = [[0,2],[1,2],[1,3],[2,4]], values = [1,8,1,4,4], k = 6
    Output: 2
    Explanation: We remove the edge connecting node 1 with 2. The resulting split is valid because:
    - The value of the component containing nodes 1 and 3 is values[1] + values[3] = 12.
    - The value of the component containing nodes 0, 2, and 4 is values[0] + values[2] + values[4] = 6.
    It can be shown that no other valid split has more than 2 connected components.
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2023/08/07/example21svg-1.jpg)

    ```
    Input: n = 7, edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]], values = [3,0,6,1,5,2,1], k = 3
    Output: 3
    Explanation: We remove the edge connecting node 0 with 2, and the edge connecting node 0 with 1. The resulting split is valid because:
    - The value of the component containing node 0 is values[0] = 3.
    - The value of the component containing nodes 2, 5, and 6 is values[2] + values[5] + values[6] = 9.
    - The value of the component containing nodes 1, 3, and 4 is values[1] + values[3] + values[4] = 6.
    It can be shown that no other valid split has more than 3 connected components.
    ```

    ## Constraints

    - 1 <= n <= 3 * 10^4
    - edges.length == n - 1
    - edges[i].length == 2
    - 0 <= ai, bi < n
    - values.length == n
    - 0 <= values[i] <= 10^9
    - 1 <= k <= 10^9
    - Sum of values is divisible by k.
    - The input is generated such that edges represents a valid tree.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def max_k_divisible_components(self, n: int, edges: list[list[int]], values: list[int], k: int) -> int:
            raise NotImplementedError('Implement max_k_divisible_components')

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
