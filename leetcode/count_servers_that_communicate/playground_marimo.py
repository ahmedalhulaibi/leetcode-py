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
    # 1267. Count Servers that Communicate

    **Medium** · Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix, Counting

    You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.

    Return the number of servers that communicate with any other server.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2019/11/14/untitled-diagram-1-3.jpg)

    ```
    Input: grid = [[1,0],[0,1]]
    Output: 0
    Explanation: No servers can communicate with others.
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2019/11/13/untitled-diagram-4.jpg)

    ```
    Input: grid = [[1,0],[1,1]]
    Output: 3
    Explanation: All three servers can communicate with at least one other server.
    ```

    ![Example 3](https://assets.leetcode.com/uploads/2019/11/14/untitled-diagram-6.jpg)

    ```
    Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
    Output: 4
    Explanation: The two servers in the first row can communicate with each other. The two servers in the third column can communicate with each other. The server at right bottom corner can't communicate with any other server.
    ```

    ## Constraints

    - m == grid.length
    - n == grid[i].length
    - 1 <= m <= 250
    - 1 <= n <= 250
    - grid[i][j] == 0 or 1



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def count_servers(self, grid: list[list[int]]) -> int:
            raise NotImplementedError('Implement count_servers')

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
