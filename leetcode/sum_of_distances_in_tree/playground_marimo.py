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
    # 834. Sum of Distances in Tree

    **Hard** · Dynamic Programming, Tree, Depth-First Search, Graph Theory, DP on Trees

    There is an undirected connected tree with `n` nodes labeled from `0` to `n - 1` and `n - 1` edges.

    You are given the integer `n` and the array `edges` where `edges[i] = [a<sub>i</sub>, b<sub>i</sub>]` indicates that there is an edge between nodes `a<sub>i</sub>` and `b<sub>i</sub>` in the tree.

    Return an array `answer` of length `n` where `answer[i]` is the sum of the distances between the `i<sup>th</sup>` node in the tree and all other nodes.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2021/07/23/lc-sumdist1.jpg)

    ```
    Input: n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
    Output: [8,12,6,10,10,10]
    Explanation: The tree is shown above.
    We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
    equals 1 + 1 + 2 + 2 + 2 = 8.
    Hence, answer[0] = 8, and so on.
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2021/07/23/lc-sumdist2.jpg)

    ```
    Input: n = 1, edges = []
    Output: [0]
    ```

    ![Example 3](https://assets.leetcode.com/uploads/2021/07/23/lc-sumdist3.jpg)

    ```
    Input: n = 2, edges = [[1,0]]
    Output: [1,1]
    ```

    ## Constraints

    - 1 <= n <= 3 * 10^4
    - edges.length == n - 1
    - edges[i].length == 2
    - 0 <= a<sub>i</sub>, b<sub>i</sub> < n
    - a<sub>i</sub> != b<sub>i</sub>
    - The given input represents a valid tree.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def sum_of_distances_in_tree(self, n: int, edges: list[list[int]]) -> list[int]:
            raise NotImplementedError('Implement sum_of_distances_in_tree')

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
