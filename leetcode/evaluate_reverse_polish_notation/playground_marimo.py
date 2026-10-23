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
    # 150. Evaluate Reverse Polish Notation

    **Medium** · Array, Math, Stack

    You are given an array of strings `tokens` that represents an arithmetic expression in a **Reverse Polish Notation**.

    Evaluate the expression. Return *an integer that represents the value of the expression*.

    **Note that:**

    - The valid operators are `'+'`, `'-'`, `'*'`, and `'/'`.
    - Each operand may be an integer or another expression.
    - The division between two integers always **truncates toward zero**.
    - There will not be any division by zero.
    - The input represents a valid arithmetic expression in a reverse polish notation.
    - The answer and all the intermediate calculations can be represented in a **32-bit** integer.

    ## Examples

    ```
    Input: tokens = ["2","1","+","3","*"]
    Output: 9
    ```
    **Explanation:** ((2 + 1) * 3) = 9

    ```
    Input: tokens = ["4","13","5","/","+"]
    Output: 6
    ```
    **Explanation:** (4 + (13 / 5)) = 6

    ```
    Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    Output: 22
    ```
    **Explanation:** ((10 * (6 / ((9 + 3) * -11))) + 17) + 5 = 22

    ## Constraints

    - `1 <= tokens.length <= 10^4`
    - `tokens[i]` is either an operator: `"+"`, `"-"`, `"*"`, or `"/"`, or an integer in the range `[-200, 200]`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def eval_rpn(self, tokens: list[str]) -> int:
            raise NotImplementedError('Implement eval_rpn')

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
