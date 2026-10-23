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
    # 743. Network Delay Time

    **Medium** · Depth-First Search, Breadth-First Search, Graph Theory, Heap (Priority Queue), Shortest Path

    You are given a network of `n` nodes, labeled from `1` to `n`. You are also given `times`, a list of travel times as directed edges `times[i] = (u<sub>i</sub>, v<sub>i</sub>, w<sub>i</sub>)`, where `u<sub>i</sub>` is the source node, `v<sub>i</sub>` is the target node, and `w<sub>i</sub>` is the time it takes for a signal to travel from source to target.

    We will send a signal from a given node `k`. Return _the **minimum** time it takes for all the_ `n` _nodes to receive the signal_. If it is impossible for all the `n` nodes to receive the signal, return `-1`.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2019/05/23/931_example_1.png)

    ```
    Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
    Output: 2
    ```

    ```
    Input: times = [[1,2,1]], n = 2, k = 1
    Output: 1
    ```

    ```
    Input: times = [[1,2,1]], n = 2, k = 2
    Output: -1
    ```

    ## Constraints

    - 1 <= k <= n <= 100
    - 1 <= times.length <= 6000
    - times[i].length == 3
    - 1 <= u<sub>i</sub>, v<sub>i</sub> <= n
    - u<sub>i</sub> != v<sub>i</sub>
    - 0 <= w<sub>i</sub> <= 100
    - All the pairs (u<sub>i</sub>, v<sub>i</sub>) are **unique**. (i.e., no multiple edges.)



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    import heapq

    class Solution:

        def network_delay_time(self, times: list[list[int]], n: int, k: int) -> int:
            raise NotImplementedError('Implement network_delay_time')

    practice_exports = {'heapq': heapq, 'Solution': Solution}
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
