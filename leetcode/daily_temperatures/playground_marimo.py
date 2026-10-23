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
    # 739. Daily Temperatures

    **Medium** · Array, Stack, Monotonic Stack

    Given an array of integers `temperatures` represents the daily temperatures, return an array `answer` such that `answer[i]` is the number of days you have to wait after the `ith` day to get a warmer temperature. If there is no future day for which this is possible, keep `answer[i] == 0` instead.

    ## Examples

    ```
    Input: temperatures = [73,74,75,71,69,72,76,73]
    Output: [1,1,4,2,1,1,0,0]
    ```
    **Explanation:**
    - For input `[73,74,75,71,69,72,76,73]`, the output should be `[1,1,4,2,1,1,0,0]`.
    - For example, the first temperature is 73. The next warmer temperature is 74, which is 1 day later, so we put 1.
    - The second temperature is 74. The next warmer temperature is 75, which is 1 day later, so we put 1.
    - The third temperature is 75. The next warmer temperature is 76, which is 4 days later, so we put 4.

    ```
    Input: temperatures = [30,40,50,60]
    Output: [1,1,1,0]
    ```

    ```
    Input: temperatures = [30,60,90]
    Output: [1,1,0]
    ```

    ## Constraints

    - `1 <= temperatures.length <= 10^5`
    - `30 <= temperatures[i] <= 100`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def daily_temperatures(self, temperatures: list[int]) -> list[int]:
            raise NotImplementedError('Implement daily_temperatures')

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
