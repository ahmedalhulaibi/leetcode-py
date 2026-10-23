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
    # 972. Equal Rational Numbers

    **Hard** · Math, String

    Given two strings `s` and `t`, each of which represents a non-negative rational number, return `true` if and only if they represent the same number. The strings may use parentheses to denote the repeating part of the rational number.

    A **rational number** can be represented using up to three parts: `<IntegerPart>`, `<NonRepeatingPart>`, and a `<RepeatingPart>`. The number will be represented in one of the following three ways:

    - `<IntegerPart>`
      - For example, `12`, `0`, and `123`.
    - `<IntegerPart>`.`<NonRepeatingPart>`
      - For example, `0.5`, `1.`, `2.12`, and `123.0001`.
    - `<IntegerPart>`.`<NonRepeatingPart>`(`<RepeatingPart>`)
      - For example, `0.1(6)`, `1.(9)`, and `123.00(1212)`.

    The repeating portion of a decimal expansion is conventionally denoted within a pair of round brackets. For example:

    - `1/6 = 0.16666666... = 0.1(6) = 0.1666(6) = 0.166(66)`.

    ## Examples

    ```
    Input: s = "0.(52)", t = "0.5(25)"
    Output: true
    Explanation: Because "0.(52)" represents 0.52525252..., and "0.5(25)" represents 0.52525252525..... , the strings represent the same number.
    ```

    ```
    Input: s = "0.1666(6)", t = "0.166(66)"
    Output: true
    ```

    ```
    Input: s = "0.9(9)", t = "1."
    Output: true
    Explanation: "0.9(9)" represents 0.999999999... repeated forever, which equals 1.
    "1." represents the number 1, which is formed correctly: (IntegerPart) = "1" and (NonRepeatingPart) = "\".
    ```

    ## Constraints

    - Each part consists only of digits.
    - The `<IntegerPart>` does not have leading zeros (except for the zero itself).
    - 1 <= `<IntegerPart>`.length <= 4
    - 0 <= `<NonRepeatingPart>`.length <= 4
    - 1 <= `<RepeatingPart>`.length <= 4



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def is_rational_equal(self, s: str, t: str) -> bool:
            raise NotImplementedError('Implement is_rational_equal')

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
