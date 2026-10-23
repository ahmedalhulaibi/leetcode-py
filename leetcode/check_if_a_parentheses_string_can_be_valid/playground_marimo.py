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
    # 2116. Check if a Parentheses String Can Be Valid

    **Medium** · String, Stack, Greedy, Bracket Sequences

    A parentheses string is a **non-empty** string consisting only of `'('` and `')'`. It is valid if **any** of the following conditions is **true**:

    - It is `()`.
    - It can be written as `AB` (`A` concatenated with `B`), where `A` and `B` are valid parentheses strings.
    - It can be written as `(A)`, where `A` is a valid parentheses string.

    You are given a parentheses string `s` and a string `locked`, both of length `n`. `locked` is a binary string consisting only of `'0'`s and `'1'`s. For **each** index `i` of `locked`,

    - If `locked[i]` is `'1'`, you **cannot** change `s[i]`.
    - But if `locked[i]` is `'0'`, you **can** change `s[i]` to either `'('` or `')'`.

    Return `true` if you can make `s` a valid parentheses string. Otherwise, return `false`.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2021/11/06/eg1.png)

    ```
    Input: s = "))()))", locked = "010100"
    Output: true
    Explanation: locked[1] == '1' and locked[3] == '1', so we cannot change s[1] or s[3].
    We change s[0] and s[4] to '(' while leaving s[2] and s[5] unchanged to make s valid.
    ```

    ```
    Input: s = "()()", locked = "0000"
    Output: true
    Explanation: We do not need to make any changes because s is already valid.
    ```

    ```
    Input: s = ")", locked = "0"
    Output: false
    Explanation: locked permits us to change s[0].
    Changing s[0] to either '(' or ')' will not make s valid.
    ```

    ```
    Input: s = "(((())(((())", locked = "111111010111"
    Output: true
    Explanation: locked permits us to change s[6] and s[8].
    We change s[6] and s[8] to ')' to make s valid.
    ```

    ## Constraints

    - `n == s.length == locked.length`
    - `1 <= n <= 10^5`
    - `s[i]` is either `'('` or `')'`.
    - `locked[i]` is either `'0'` or `'1'`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def can_be_valid(self, s: str, locked: str) -> bool:
            raise NotImplementedError('Implement can_be_valid')

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
