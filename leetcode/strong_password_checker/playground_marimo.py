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
    # 420. Strong Password Checker

    **Hard** · String, Greedy, Heap (Priority Queue)

    A password is considered strong if the below conditions are all met:

    - It has at least `6` characters and at most `20` characters.
    - It contains at least **one lowercase** letter, at least **one uppercase** letter, and at least **one digit**.
    - It does not contain three repeating characters in a row (i.e., `"B**aaa**bb0"` is weak, but `"B**aa**b**a**0"` is strong).

    Given a string `password`, return *the minimum number of steps required to make `password` strong. if `password` is already strong, return `0`.*

    In one step, you can:

    - Insert one character to `password`,
    - Delete one character from `password`, or
    - Replace one character of `password` with another character.

    ## Examples

    ```
    Input: password = "a"
    Output: 5
    ```

    ```
    Input: password = "aA1"
    Output: 3
    ```

    ```
    Input: password = "1337C0d3"
    Output: 0
    ```

    ## Constraints

    - 1 <= password.length <= 50
    - password consists of letters, digits, dot '.' or exclamation mark '!'.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def strong_password_checker(self, password: str) -> int:
            raise NotImplementedError('Implement strong_password_checker')

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
