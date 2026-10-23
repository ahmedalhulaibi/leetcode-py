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
    # 2285. Maximum Total Importance of Roads

    **Medium** · Greedy, Graph Theory, Sorting, Heap (Priority Queue)

    You are given an integer `n` denoting the number of cities in a country. The cities are numbered from `0` to `n - 1`.

    You are also given a 2D integer array `roads` where `roads[i] = [a<sub>i</sub>, b<sub>i</sub>]` denotes that there exists a **bidirectional** road connecting cities `a<sub>i</sub>` and `b<sub>i</sub>`.

    You need to assign each city with an integer value from `1` to `n`, where each value can only be used **once**. The **importance** of a road is then defined as the **sum** of the values of the two cities it connects.

    Return _the **maximum total importance** of all roads possible after assigning the values optimally._

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2022/04/07/ex1drawio.png)

    ```
    Input: n = 5, roads = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]
    Output: 43
    Explanation: The assigned values are [2,4,5,3,1].
    The total importance of all roads is 6 + 9 + 8 + 7 + 7 + 6 = 43.
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2022/04/07/ex2drawio.png)

    ```
    Input: n = 5, roads = [[0,3],[2,4],[1,3]]
    Output: 20
    Explanation: The assigned values are [4,3,2,5,1].
    The total importance of all roads is 9 + 3 + 8 = 20.
    ```

    ## Constraints

    - 2 <= n <= 5 * 10<sup>4</sup>
    - 1 <= roads.length <= 5 * 10<sup>4</sup>
    - roads[i].length == 2
    - 0 <= a<sub>i</sub>, b<sub>i</sub> <= n - 1
    - a<sub>i</sub> != b<sub>i</sub>
    - There are no duplicate roads.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def maximum_importance(self, n: int, roads: list[list[int]]) -> int:
            raise NotImplementedError('Implement maximum_importance')

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
