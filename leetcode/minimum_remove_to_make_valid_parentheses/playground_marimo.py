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
    # 1249. Minimum Remove to Make Valid Parentheses

    **Medium** · String, Stack

    Given a string `s` of `'('` , `')'` and lowercase English characters.

    Your task is to remove the minimum number of parentheses ( `'('` or `')'`, in any positions ) so that the resulting *parentheses string* is valid and return **any** valid string.

    Formally, a *parentheses string* is valid if and only if:

    - It is the empty string, contains only lowercase characters, or
    - It can be written as `AB` (`A` concatenated with `B`), where `A` and `B` are valid strings, or
    - It can be written as `(A)`, where `A` is a valid string.

    ## Examples

    ```
    Input: s = "lee(t(c)o)de)"
    Output: "lee(t(c)o)de"
    Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
    ```

    ```
    Input: s = "a)b(c)d"
    Output: "ab(c)d"
    ```

    ```
    Input: s = "))(("
    Output: "\"
    Explanation: An empty string is also valid.
    ```

    ## Constraints

    - `1 <= s.length <= 10^5`
    - `s[i]` is either `'('` , `')'`, or lowercase English letter.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def min_remove_to_make_valid(self, s: str) -> str:
            raise NotImplementedError('Implement min_remove_to_make_valid')

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
