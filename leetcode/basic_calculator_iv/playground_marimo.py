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
    # 770. Basic Calculator IV

    **Hard** · Hash Table, Math, String, Stack, Recursion

    Given an expression such as `expression = "e + 8 - a + 5"` and an evaluation map such as `{"e": 1}` (given in terms of `evalvars = ["e"]` and `evalints = [1]`), return a list of tokens representing the simplified expression, such as `["-1*a","14"]`

    - An expression alternates chunks and symbols, with a space separating each chunk and symbol.
    - A chunk is either an expression in parentheses, a variable, or a non-negative integer.
    - A variable is a string of lowercase letters (not including digits.) Note that variables can be multiple letters, and note that variables never have a leading coefficient or unary operator like `"2x"` or `"-x"`.

    Expressions are evaluated in the usual order: brackets first, then multiplication, then addition and subtraction.

    - For example, `expression = "1 + 2 * 3"` has an answer of `["7"]`.

    The format of the output is as follows:

    - For each term of free variables with a non-zero coefficient, we write the free variables within a term in sorted order lexicographically.

      - For example, we would never write a term like `"b*a*c"`, only `"a*b*c"`.

    - Terms have degrees equal to the number of free variables being multiplied, counting multiplicity. We write the largest degree terms of our answer first, breaking ties by lexicographic order ignoring the leading coefficient of the term.

      - For example, `"a*a*b*c"` has degree `4`.

    - The leading coefficient of the term is placed directly to the left with an asterisk separating it from the variables (if they exist.) A leading coefficient of 1 is still printed.
    - An example of a well-formatted answer is `["-2*a*a*a", "3*a*a*b", "3*b*b", "4*a", "5*c", "-6"]`.
    - Terms (including constant terms) with coefficient `0` are not included.

      - For example, an expression of `"0"` has an output of `[]`.

    **Note:** You may assume that the given expression is always valid. All intermediate results will be in the range of `[-2^31, 2^31 - 1]`.

    ## Examples

    ```
    Input: expression = "e + 8 - a + 5", evalvars = ["e"], evalints = [1]
    Output: ["-1*a","14"]
    ```

    ```
    Input: expression = "e - 8 + temperature - pressure", evalvars = ["e", "temperature"], evalints = [1, 12]
    Output: ["-1*pressure","5"]
    ```

    ```
    Input: expression = "(e + 8) * (e - 8)", evalvars = [], evalints = []
    Output: ["1*e*e","-64"]
    ```

    ## Constraints

    - 1 <= expression.length <= 250
    - expression consists of lowercase English letters, digits, '+', '-', '*', '(', ')', and ' '.
    - expression does not contain any leading or trailing spaces.
    - All the tokens in expression are separated by a single space.
    - 0 <= evalvars.length <= 100
    - 1 <= evalvars[i].length <= 20
    - evalvars[i] consists of lowercase English letters.
    - evalints.length == evalvars.length
    - -100 <= evalints[i] <= 100



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def basic_calculator_iv(self, expression: str, evalvars: list[str], evalints: list[int]) -> list[str]:
            raise NotImplementedError('Implement basic_calculator_iv')

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
