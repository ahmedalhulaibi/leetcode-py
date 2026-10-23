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
    # 2924. Find Champion II

    **Medium** · Array, Graph Theory

    There are `n` teams numbered from `0` to `n - 1` in a tournament; each team is also a node in a <strong>DAG</strong>.

    You are given the integer `n` and a <strong>0-indexed</strong> 2D integer array `edges` of length `m` representing the <strong>DAG</strong>, where `edges[i] = [u_i, v_i]` indicates that there is a directed edge from team `u_i` to team `v_i` in the graph.

    A directed edge from `a` to `b` in the graph means that team `a` is <strong>stronger</strong> than team `b` and team `b` is <strong>weaker</strong> than team `a`.

    Team `a` will be the <strong>champion</strong> of the tournament if there is no team `b` that is <strong>stronger</strong> than team `a`.

    Return <em>the team that will be the <strong>champion</strong> of the tournament if there is a <strong>unique</strong> champion, otherwise, return </em><code>-1</code><em>.</em>

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2023/10/19/graph-3.png)

    ```
    Input: n = 3, edges = [[0,1],[1,2]]
    Output: 0
    Explanation: Team 1 is weaker than team 0. Team 2 is weaker than team 1. So the champion is team 0.
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2023/10/19/graph-4.png)

    ```
    Input: n = 4, edges = [[0,2],[1,3],[1,2]]
    Output: -1
    Explanation: Team 2 is weaker than team 0 and team 1. Team 3 is weaker than team 1. But team 1 and team 0 are not weaker than any other teams. So the answer is -1.
    ```

    ## Constraints

    - 1 <= n <= 100
    - m == edges.length
    - 0 <= m <= n * (n - 1) / 2
    - `edges[i].length == 2`
    - 0 <= edges[i][j] <= n - 1
    - `edges[i][0] != edges[i][1]`
    - The input is generated such that if team `a` is stronger than team `b`, team `b` is not stronger than team `a`.
    - The input is generated such that if team `a` is stronger than team `b` and team `b` is stronger than team `c`, then team `a` is stronger than team `c`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def find_champion(self, n: int, edges: list[list[int]]) -> int:
            raise NotImplementedError('Implement find_champion')

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
