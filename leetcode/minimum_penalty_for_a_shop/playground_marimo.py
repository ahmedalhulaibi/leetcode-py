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
    # 2483. Minimum Penalty for a Shop

    **Medium** · String, Prefix Sum

    You are given the customer visit log of a shop represented by a **0-indexed** string `customers` consisting only of characters `'N'` and `'Y'`:

    - if the `i<sup>th</sup>` character is `'Y'`, it means that customers come at the `i<sup>th</sup>` hour
    - whereas `'N'` indicates that no customers come at the `i<sup>th</sup>` hour.

    If the shop closes at the `j<sup>th</sup>` hour (`0 <= j <= n`), the **penalty** is calculated as follows:

    - For every hour when the shop is open and no customers come, the penalty increases by `1`.
    - For every hour when the shop is closed and customers come, the penalty increases by `1`.

    Return *the **earliest** hour at which the shop must be closed to incur a **minimum** penalty*.

    **Note** that if a shop closes at the `j<sup>th</sup>` hour, it means the shop is closed at the hour `j`.

    ## Examples

    ```
    Input: customers = "YYNY"
    Output: 2
    Explanation:
    - Closing the shop at the 0th hour incurs in 1+1+0+1 = 3 penalty.
    - Closing the shop at the 1st hour incurs in 0+1+0+1 = 2 penalty.
    - Closing the shop at the 2nd hour incurs in 0+0+0+1 = 1 penalty.
    - Closing the shop at the 3rd hour incurs in 0+0+1+1 = 2 penalty.
    - Closing the shop at the 4th hour incurs in 0+0+1+0 = 1 penalty.
    Closing the shop at 2nd or 4th hour gives a minimum penalty. Since 2 is earlier, the optimal closing time is 2.
    ```

    ```
    Input: customers = "NNNNN"
    Output: 0
    Explanation: It is best to close the shop at the 0th hour as no customers arrive.
    ```

    ```
    Input: customers = "YYYY"
    Output: 4
    Explanation: It is best to close the shop at the 4th hour as customers arrive at each hour.
    ```

    ## Constraints

    - `1 <= customers.length <= 10<sup>5</sup>`
    - `customers` consists only of characters `'Y'` and `'N'`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def best_closing_time(self, customers: str) -> int:
            raise NotImplementedError('Implement best_closing_time')

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
