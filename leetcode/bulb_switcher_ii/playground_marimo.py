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
    # 672. Bulb Switcher II

    **Medium** · Math, Bit Manipulation, Depth-First Search, Breadth-First Search

    There is a room with `n` bulbs labeled from `1` to `n` that all are turned on initially, and **four buttons** on the wall. Each of the four buttons has a different functionality where:

    - **Button 1:** Flips the status of all the bulbs.
    - **Button 2:** Flips the status of all the bulbs with even labels (i.e., `2, 4, ...`).
    - **Button 3:** Flips the status of all the bulbs with odd labels (i.e., `1, 3, ...`).
    - **Button 4:** Flips the status of all the bulbs with a label `j = 3k + 1` where `k = 0, 1, 2, ...` (i.e., `1, 4, 7, 10, ...`).

    You must make **exactly** `presses` button presses in total. For each press, you may pick **any** of the four buttons to press.

    Given the two integers `n` and `presses`, return the number of different possible statuses after performing all `presses` button presses.

    ## Examples

    ```
    Input: n = 1, presses = 1
    Output: 2
    Explanation: Status can be:
    - [off] by pressing button 1
    - [on] by pressing button 2
    ```

    ```
    Input: n = 2, presses = 1
    Output: 3
    Explanation: Status can be:
    - [off, off] by pressing button 1
    - [on, off] by pressing button 2
    - [off, on] by pressing button 3
    ```

    ```
    Input: n = 3, presses = 1
    Output: 4
    Explanation: Status can be:
    - [off, off, off] by pressing button 1
    - [on, off, on] by pressing button 2
    - [off, on, off] by pressing button 3
    - [off, on, on] by pressing button 4
    ```

    ## Constraints

    - 1 <= n <= 1000
    - 0 <= presses <= 1000



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def flip_lights(self, n: int, presses: int) -> int:
            raise NotImplementedError('Implement flip_lights')

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
