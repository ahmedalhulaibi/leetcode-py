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
    # 1135. Connecting Cities With Minimum Cost

    **Medium** · Union Find, Graph, Minimum Spanning Tree, Heap (Priority Queue)

    There are `n` cities labeled from `1` to `n`. You are given the integer `n` and an array `connections` where `connections[i] = [xi, yi, costi]` indicates that the cost of connecting city `xi` and city `yi` (bidirectional connection) is `costi`.

    Return *the minimum **cost** to connect all the* `n` *cities such that there is at least one path between each pair of cities*. If it is impossible to connect all the `n` cities, return `-1`.

    The **cost** is the sum of the connections' costs used.

    ## Examples

    ![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1100-1199/1135.Connecting%20Cities%20With%20Minimum%20Cost/images/1314_ex2.png)

    ```
    Input: n = 3, connections = [[1,2,5],[1,3,6],[2,3,1]]
    Output: 6
    Explanation: Choosing any 2 edges will connect all cities so we choose the minimum 2.
    ```

    ![Example 2](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1100-1199/1135.Connecting%20Cities%20With%20Minimum%20Cost/images/1314_ex1.png)

    ```
    Input: n = 4, connections = [[1,2,3],[3,4,4]]
    Output: -1
    Explanation: There is no way to connect all cities even if all edges are used.
    ```

    ## Constraints

    - 1 <= n <= 10^4
    - 1 <= connections.length <= 10^4
    - connections[i].length == 3
    - 1 <= xi, yi <= n
    - xi != yi
    - 0 <= costi <= 10^5



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def minimum_cost(self, n: int, connections: list[list[int]]) -> int:
            raise NotImplementedError('Implement minimum_cost')

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
