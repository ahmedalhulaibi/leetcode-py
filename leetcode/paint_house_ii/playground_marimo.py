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
    # 265. Paint House II

    **Hard** · Array, Dynamic Programming

    There are a row of `n` houses, each house can be painted with one of the `k` colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

    The cost of painting each house with a certain color is represented by an `n x k` cost matrix `costs`.

    - For example, `costs[0][0]` is the cost of painting house `0` with color `0`; `costs[1][2]` is the cost of painting house `1` with color `2`, and so on...

    Return *the minimum cost to paint all houses*.

    ## Examples

    ```
    Input: costs = [[1,5,3],[2,9,4]]
    Output: 5
    Explanation:
    Paint house 0 into color 0, paint house 1 into color 2. Minimum cost: 1 + 4 = 5;
    Or paint house 0 into color 2, paint house 1 into color 0. Minimum cost: 3 + 2 = 5.
    ```

    ```
    Input: costs = [[1,3],[2,4]]
    Output: 5
    ```

    ## Constraints

    - `costs.length == n`
    - `costs[i].length == k`
    - `1 <= n <= 100`
    - `2 <= k <= 20`
    - `1 <= costs[i][j] <= 20`

    **Follow up:** Could you solve it in `O(nk)` runtime?

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def min_cost_ii(self, costs: list[list[int]]) -> int:
            raise NotImplementedError('Implement min_cost_ii')

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
