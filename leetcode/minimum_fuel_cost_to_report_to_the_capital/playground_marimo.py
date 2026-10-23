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
    # 2477. Minimum Fuel Cost to Report to the Capital

    **Medium** · Tree, Depth-First Search, Breadth-First Search, Graph Theory

    There is a tree (i.e., a connected, undirected graph with no cycles) structure country network consisting of `n` cities numbered from `0` to `n - 1` and exactly `n - 1` roads. The capital city is city `0`. You are given a 2D integer array `roads` where `roads[i] = [a_i, b_i]` denotes that there exists a **bidirectional road** connecting cities `a_i` and `b_i`.

    There is a meeting for the representatives of each city. The meeting is in the capital city.

    There is a car in each city. You are given an integer `seats` that indicates the number of seats in each car.

    A representative can use the car in their city to travel or change the car and ride with another representative. The cost of traveling between two cities is one liter of fuel.

    Return *the minimum number of liters of fuel to reach the capital city*.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2022/09/22/a4c380025e3ff0c379525e96a7d63a3.png)

    ```
    Input: roads = [[0,1],[0,2],[0,3]], seats = 5
    Output: 3
    Explanation:
    - Representative1 goes directly to the capital with 1 liter of fuel.
    - Representative2 goes directly to the capital with 1 liter of fuel.
    - Representative3 goes directly to the capital with 1 liter of fuel.
    It costs 3 liters of fuel at minimum.
    It can be proven that 3 is the minimum number of liters of fuel needed.
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2022/11/16/2.png)

    ```
    Input: roads = [[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]], seats = 2
    Output: 7
    Explanation:
    - Representative2 goes directly to city 3 with 1 liter of fuel.
    - Representative2 and representative3 go together to city 1 with 1 liter of fuel.
    - Representative2 and representative3 go together to the capital with 1 liter of fuel.
    - Representative1 goes directly to the capital with 1 liter of fuel.
    - Representative5 goes directly to the capital with 1 liter of fuel.
    - Representative6 goes directly to city 4 with 1 liter of fuel.
    - Representative4 and representative6 go together to the capital with 1 liter of fuel.
    It costs 7 liters of fuel at minimum.
    It can be proven that 7 is the minimum number of liters of fuel needed.
    ```

    ![Example 3](https://assets.leetcode.com/uploads/2022/09/27/efcf7f7be6830b8763639cfd01b690a.png)

    ```
    Input: roads = [], seats = 1
    Output: 0
    Explanation: No representatives need to travel to the capital city.
    ```

    ## Constraints

    - 1 <= n <= 10^5
    - roads.length == n - 1
    - roads[i].length == 2
    - 0 <= a_i, b_i < n
    - a_i != b_i
    - roads represents a valid tree.
    - 1 <= seats <= 10^5



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def minimum_fuel_cost(self, roads: list[list[int]], seats: int) -> int:
            raise NotImplementedError('Implement minimum_fuel_cost')

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
