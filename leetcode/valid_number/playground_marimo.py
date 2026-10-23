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
    # 65. Valid Number

    **Hard** · String

    Given a string `s`, return whether `s` is a valid number.

    For example, all the following are valid numbers: `"2"`, `"0089"`, `"-0.1"`, `"+3.14"`, `"4."`, `"-.9"`, `"2e10"`, `"-90E3"`, `"3e+7"`, `"+6e-1"`, `"53.5e93"`, `"-123.456e789"`, while the following are not valid numbers: `"abc"`, `"1a"`, `"1e"`, `"e3"`, `"99e2.5"`, `"--6"`, `"-+3"`, `"95a54e53"`.

    Formally, a valid number is defined using one of the following definitions:

    - An integer number followed by an optional exponent.
    - A decimal number followed by an optional exponent.

    An integer number is defined with an optional sign `'-'` or `'+'` followed by digits.

    A decimal number is defined with an optional sign `'-'` or `'+'` followed by one of the following definitions:

    - Digits followed by a dot `'.'`.
    - Digits followed by a dot `'.'` followed by digits.
    - A dot `'.'` followed by digits.

    An exponent is defined with an exponent notation `'e'` or `'E'` followed by an integer number.

    The digits are defined as one or more digits.

    ## Examples

    ```
    Input: s = "0"
    Output: true
    ```

    ```
    Input: s = "e"
    Output: false
    ```

    ```
    Input: s = "."
    Output: false
    ```

    ## Constraints

    - 1 <= s.length <= 20
    - s consists of only English letters (both uppercase and lowercase), digits (0-9), plus '+', minus '-', or dot '.'.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def is_number(self, s: str) -> bool:
            raise NotImplementedError('Implement is_number')

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
