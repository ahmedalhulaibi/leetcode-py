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
    # 1614. Maximum Nesting Depth of the Parentheses

    **Easy** · String, Stack, Bracket Sequences

    Given a valid parentheses string `s`, return the nesting depth of `s`. The nesting depth is the maximum number of nested parentheses.

    ## Examples

    ```
    Input: s = "(1+(2*3)+((8)/4))+1"
    Output: 3
    Explanation: Digit 8 is inside of 3 nested parentheses in the string.
    ```

    ```
    Input: s = "(1)+((2))+(((3)))"
    Output: 3
    Explanation: Digit 3 is inside of 3 nested parentheses in the string.
    ```

    ```
    Input: s = "()(())((()()))"
    Output: 3
    ```

    ## Constraints

    - `1 <= s.length <= 100`
    - `s` consists of digits `0-9` and characters `'+'`, `'-'`, `'*'`, `'/'`, `'('`, and `')'`.
    - It is guaranteed that parentheses expression `s` is a VPS.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def max_depth(self, s: str) -> int:
            raise NotImplementedError('Implement max_depth')

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
