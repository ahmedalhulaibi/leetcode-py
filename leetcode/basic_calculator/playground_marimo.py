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
    # 224. Basic Calculator

    **Hard** · Math, String, Stack, Recursion

    Given a string `s` representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

    **Note:** You are **not** allowed to use any built-in function which evaluates strings as mathematical expressions, such as `eval()`.

    ## Examples

    ```
    Input: s = "1 + 1"
    Output: 2
    ```

    ```
    Input: s = " 2-1 + 2 "
    Output: 3
    ```

    ```
    Input: s = "(1+(4+5+2)-3)+(6+8)"
    Output: 23
    ```

    ## Constraints

    - `1 <= s.length <= 3 * 10^5`
    - `s` consists of digits, `'+'`, `'-'`, `'('`, `')'`, and `' '`.
    - `s` represents a valid expression.
    - `'+'` is **not** used as a unary operation (i.e., `"+1"` and `"+(2 + 3)"` is invalid).
    - `'-'` could be used as a unary operation (i.e., `"-1"` and `"-(2 + 3)"` is valid).
    - There will be no two consecutive operators in the input.
    - Every number and running calculation will fit in a signed 32-bit integer.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def calculate(self, s: str) -> int:
            raise NotImplementedError('Implement calculate')

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
