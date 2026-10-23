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
    # 1514. Path with Maximum Probability

    **Medium** · Array, Graph Theory, Heap (Priority Queue), Shortest Path, Dijkstra's Algorithm

    You are given an undirected weighted graph of `n` nodes (0-indexed), represented by an edge list where `edges[i] = [a<sub>i</sub>, b<sub>i</sub>]` is an undirected edge connecting the nodes `a<sub>i</sub>` and `b<sub>i</sub>` with a probability of success of traversing that edge `succProb[i]`.

    Given two nodes `start` and `end`, find the path with the maximum probability of success to go from `start` to `end` and return its success probability.

    If there is no path from `start` to `end`, return `0`. Your answer will be accepted if it differs from the correct answer by at most **10<sup>-5</sup>**.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2019/09/20/1558_ex1.png)

    ```
    Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
    Output: 0.25000
    Explanation: There are two paths from start to end, one having a probability of success = 0.2 and the other has 0.5 * 0.5 = 0.25.
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2019/09/20/1558_ex2.png)

    ```
    Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2
    Output: 0.30000
    ```

    ![Example 3](https://assets.leetcode.com/uploads/2019/09/20/1558_ex3.png)

    ```
    Input: n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
    Output: 0.00000
    Explanation: There is no path between 0 and 2.
    ```

    ## Constraints

    - 2 <= n <= 10^4
    - 0 <= start, end < n
    - start != end
    - 0 <= a<sub>i</sub>, b<sub>i</sub> < n
    - a<sub>i</sub> != b<sub>i</sub>
    - 0 <= succProb.length == edges.length <= 2 * 10^4
    - 0 <= succProb[i] <= 1
    - There is at most one edge between every two nodes.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def max_probability(self, n: int, edges: list[list[int]], succ_prob: list[float], start_node: int, end_node: int) -> float:
            raise NotImplementedError('Implement max_probability')

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
