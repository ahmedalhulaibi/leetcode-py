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
    # 1466. Reorder Routes to Make All Paths Lead to the City Zero

    **Medium** · Depth-First Search, Breadth-First Search, Graph Theory

    There are `n` cities numbered from `0` to `n - 1` and `n - 1` roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

    Roads are represented by `connections` where `connections[i] = [ai, bi]` represents a road from city `ai` to city `bi`.

    This year, there will be a big event in the capital (city `0`), and many people want to travel to this city.

    Your task consists of reorienting some roads such that each city can visit the city `0`. Return the **minimum** number of edges changed.

    It's **guaranteed** that each city can reach city `0` after reorder.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2020/05/13/sample_1_1819.png)

    ```
    Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
    Output: 3
    ```
    **Explanation:** Change the direction of edges show in red such that each node can reach the node 0 (capital).

    ![Example 2](https://assets.leetcode.com/uploads/2020/05/13/sample_2_1819.png)

    ```
    Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
    Output: 2
    ```
    **Explanation:** Change the direction of edges show in red such that each node can reach the node 0 (capital).

    ```
    Input: n = 3, connections = [[1,0],[2,0]]
    Output: 0
    ```

    ## Constraints

    - `2 <= n <= 5 * 10^4`
    - `connections.length == n - 1`
    - `connections[i].length == 2`
    - `0 <= ai, bi <= n - 1`
    - `ai != bi`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def min_reorder(self, n: int, connections: list[list[int]]) -> int:
            raise NotImplementedError('Implement min_reorder')

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
