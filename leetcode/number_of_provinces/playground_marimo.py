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
    # 547. Number of Provinces

    **Medium** · Depth-First Search, Breadth-First Search, Union-Find, Graph Theory

    There are `n` cities. Some of them are connected, while some are not. If city `a` is connected directly with city `b`, and city `b` is connected directly with city `c`, then city `a` is connected indirectly with city `c`.

    A **province** is a group of directly or indirectly connected cities and no other cities outside of the group.

    You are given an `n x n` matrix `isConnected` where `isConnected[i][j] = 1` if the `ith` city and the `jth` city are directly connected, and `isConnected[i][j] = 0` otherwise.

    Return *the total number of **provinces***.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2020/12/24/graph1.jpg)

    ```
    Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
    Output: 2
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2020/12/24/graph2.jpg)

    ```
    Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
    Output: 3
    ```

    ## Constraints

    - 1 <= n <= 200
    - n == isConnected.length
    - n == isConnected[i].length
    - isConnected[i][j] is 1 or 0.
    - isConnected[i][i] == 1
    - isConnected[i][j] == isConnected[j][i]



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def find_circle_num(self, is_connected: list[list[int]]) -> int:
            raise NotImplementedError('Implement find_circle_num')

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
