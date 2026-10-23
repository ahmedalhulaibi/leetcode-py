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
    # 1553. Minimum Number of Days to Eat N Oranges

    **Hard** · Dynamic Programming, Memoization

    There are `n` oranges in the kitchen and you decided to eat some of these oranges every day as follows:

    - Eat one orange.
    - If the number of remaining oranges `n` is divisible by `2` then you can eat `n / 2` oranges.
    - If the number of remaining oranges `n` is divisible by `3` then you can eat `2 * (n / 3)` oranges.

    You can only choose one of the actions per day.

    Given the integer `n`, return *the minimum number of days to eat* `n` *oranges*.

    ## Examples

    ```
    Input: n = 10
    Output: 4
    Explanation: You have 10 oranges.
    Day 1: Eat 1 orange,  10 - 1 = 9.
    Day 2: Eat 6 oranges, 9 - 2*(9/3) = 9 - 6 = 3. (Since 9 is divisible by 3)
    Day 3: Eat 2 oranges, 3 - 2*(3/3) = 3 - 2 = 1.
    Day 4: Eat the last orange  1 - 1  = 0.
    You need at least 4 days to eat the 10 oranges.
    ```

    ```
    Input: n = 6
    Output: 3
    Explanation: You have 6 oranges.
    Day 1: Eat 3 oranges, 6 - 6/2 = 6 - 3 = 3. (Since 6 is divisible by 2).
    Day 2: Eat 2 oranges, 3 - 2*(3/3) = 3 - 2 = 1. (Since 3 is divisible by 3)
    Day 3: Eat the last orange  1 - 1  = 0.
    You need at least 3 days to eat the 6 oranges.
    ```

    ## Constraints

    - `1 <= n <= 2 * 10^9`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def min_days(self, n: int) -> int:
            raise NotImplementedError('Implement min_days')

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
