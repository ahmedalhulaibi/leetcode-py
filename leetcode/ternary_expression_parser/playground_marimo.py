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
    # 439. Ternary Expression Parser

    **Medium** · Stack, Recursion, String

    Given a string `expression` representing arbitrarily nested ternary expressions, evaluate the expression, and return the result of it.

    You can always assume that the given expression is valid and only contains digits, `'?'`, `':'`, `'T',` and `'F'` where `'T'` is true and `'F'` is false. All the numbers in the expression are **one-digit** numbers (i.e., in the range `[0, 9]`).

    The conditional expressions group right-to-left (as usual in most languages), and the result of the expression will always evaluate to either a digit, `'T'` or `'F'`.

    ## Examples

    ```
    Input: expression = "T?2:3"
    Output: "2"
    Explanation: If true, then result is 2; otherwise result is 3.
    ```

    ```
    Input: expression = "F?1:T?4:5"
    Output: "4"
    Explanation: The conditional expressions group right-to-left. Using parenthesis, it is read/evaluated as: "(F ? 1 : (T ? 4 : 5))" --> "(F ? 1 : 4)" --> "4".
    ```

    ```
    Input: expression = "T?T?F:5:3"
    Output: "F"
    Explanation: The conditional expressions group right-to-left. Using parenthesis, it is read/evaluated as: "(T ? (T ? F : 5) : 3)" --> "(T ? F : 5)" --> "F".
    ```

    ## Constraints

    - `5 <= expression.length <= 10^4`.
    - `expression` consists of digits, `'?'`, `':'`, `'T'`, and `'F'`.
    - It is **guaranteed** that `expression` is a valid ternary expression and that each number is a **one-digit number**.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def parse_ternary(self, expression: str) -> str:
            raise NotImplementedError('Implement parse_ternary')

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
