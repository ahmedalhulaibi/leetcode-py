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
    # 856. Score of Parentheses

    **Medium** · String, Stack, Bracket Sequences

    Given a balanced parentheses string `s`, return *the **score** of the string*.

    The **score** of a balanced parentheses string is based on the following rule:

    - `"()"` has score `1`.
    - `AB` has score `A + B`, where `A` and `B` are balanced parentheses strings.
    - `(A)` has score `2 * A`, where `A` is a balanced parentheses string.

    ## Examples

    ```
    Input: s = "()"
    Output: 1
    ```

    ```
    Input: s = "(())"
    Output: 2
    ```

    ```
    Input: s = "()()"
    Output: 2
    ```

    ## Constraints

    - 2 <= s.length <= 50
    - s consists of only `'('` and `')'`.
    - s is a balanced parentheses string.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def score_of_parentheses(self, s: str) -> int:
            raise NotImplementedError('Implement score_of_parentheses')

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
