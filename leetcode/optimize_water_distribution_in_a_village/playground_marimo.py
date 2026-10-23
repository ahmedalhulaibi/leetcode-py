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
    # 1168. Optimize Water Distribution in a Village

    **Hard** · Union Find, Graph, Minimum Spanning Tree, Heap (Priority Queue)

    There are `n` houses in a village. We want to supply water for all the houses by building wells and laying pipes.

    For each house `i`, we can either build a well inside it directly with cost `wells[i - 1]` (note the `-1` due to **0-indexing**), or pipe in water from another well to it. The costs to lay pipes between houses are given by the array `pipes` where each `pipes[j] = [house1_j, house2_j, cost_j]` represents the cost to connect `house1_j` and `house2_j` together using a pipe. Connections are bidirectional, and there could be multiple valid connections between the same two houses with different costs.

    Return *the minimum total cost to supply water to all houses*.

    ## Examples

    ![Example 1](https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1100-1199/1168.Optimize%20Water%20Distribution%20in%20a%20Village/images/1359_ex1.png)

    ```
    Input: n = 3, wells = [1,2,2], pipes = [[1,2,1],[2,3,1]]
    Output: 3
    Explanation: The image shows the costs of connecting houses using pipes.
    The best strategy is to build a well in the first house with cost 1 and connect the other houses to it with cost 2 so the total cost is 3.
    ```

    ```
    Input: n = 2, wells = [1,1], pipes = [[1,2,1],[1,2,2]]
    Output: 2
    Explanation: We can supply water with cost two using one of the three options:
    Option 1:
      - Build a well inside house 1 with cost 1.
      - Build a well inside house 2 with cost 1.
    The total cost will be 2.
    Option 2:
      - Build a well inside house 1 with cost 1.
      - Connect house 2 with house 1 with cost 1.
    The total cost will be 2.
    Option 3:
      - Build a well inside house 2 with cost 1.
      - Connect house 1 with house 2 with cost 1.
    The total cost will be 2.
    Note that we can connect houses 1 and 2 with cost 1 or with cost 2 but we will always choose **the cheapest option**.
    ```

    ## Constraints

    - 2 <= n <= 10^4
    - wells.length == n
    - 0 <= wells[i] <= 10^5
    - 1 <= pipes.length <= 10^4
    - pipes[j].length == 3
    - 1 <= house1_j, house2_j <= n
    - 0 <= cost_j <= 10^5
    - house1_j != house2_j



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def min_cost_to_supply_water(self, n: int, wells: list[int], pipes: list[list[int]]) -> int:
            raise NotImplementedError('Implement min_cost_to_supply_water')

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
