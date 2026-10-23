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
    # 319. Bulb Switcher

    **Medium** · Math, Brainteaser

    <p>There are <code>n</code> bulbs that are initially off. You first turn on all the bulbs, then you turn off every second bulb.</p>

    <p>On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the <code>i<sup>th</sup></code> round, you toggle every <code>i</code> bulb. For the <code>n<sup>th</sup></code> round, you only toggle the last bulb.</p>

    <p>Return <em>the number of bulbs that are on after <code>n</code> rounds</em>.</p>

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2020/11/05/bulb.jpg)

    ```
    Input: n = 3
    Output: 1
    Explanation: At first, the three bulbs are [off, off, off].
    After the first round, the three bulbs are [on, on, on].
    After the second round, the three bulbs are [on, off, on].
    After the third round, the three bulbs are [on, off, off].
    So you should return 1 because there is only one bulb is on.
    ```

    ```
    Input: n = 0
    Output: 0
    ```

    ```
    Input: n = 1
    Output: 1
    ```

    ## Constraints

    - 0 <= n <= 10<sup>9</sup>



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def bulb_switch(self, n: int) -> int:
            raise NotImplementedError('Implement bulb_switch')

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
