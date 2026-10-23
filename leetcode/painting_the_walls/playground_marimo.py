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
    # 2742. Painting the Walls

    **Hard** · Array, Dynamic Programming

    You are given two **0-indexed** integer arrays, `cost` and `time`, of size `n` representing the costs and the time taken to paint `n` different walls respectively. There are two painters available:

    - A **paid painter** that paints the `i<sup>th</sup>` wall in `time[i]` units of time and takes `cost[i]` units of money.
    - A **free painter** that paints **any** wall in `1` unit of time at a cost of `0`. But the free painter can only be used if the paid painter is already **occupied**.

    Return *the minimum amount of money required to paint the `n` walls*.

    ## Examples

    ```
    Input: cost = [1,2,3,2], time = [1,2,3,2]
    Output: 3
    Explanation: The walls at index 0 and 1 will be painted by the paid painter, and it will take 3 units of time; meanwhile, the free painter will paint the walls at index 2 and 3, free of cost in 2 units of time. Thus, the total cost is 1 + 2 = 3.
    ```

    ```
    Input: cost = [2,3,4,2], time = [1,1,1,1]
    Output: 4
    Explanation: The walls at index 0 and 3 will be painted by the paid painter, and it will take 2 units of time; meanwhile, the free painter will paint the walls at index 1 and 2, free of cost in 2 units of time. Thus, the total cost is 2 + 2 = 4.
    ```

    ## Constraints

    - `1 <= cost.length <= 500`
    - `cost.length == time.length`
    - `1 <= cost[i] <= 10^6`
    - `1 <= time[i] <= 500`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def paint_walls(self, cost: list[int], time: list[int]) -> int:
            raise NotImplementedError('Implement paint_walls')

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
