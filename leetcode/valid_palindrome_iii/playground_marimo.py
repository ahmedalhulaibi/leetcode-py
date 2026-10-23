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
    # 1216. Valid Palindrome III

    **Hard** · String, Dynamic Programming

    Given a string `s` and an integer `k`, return `true` if `s` is a `k`**-palindrome**.

    A string is `k`**-palindrome** if it can be transformed into a palindrome by removing at most `k` characters from it.

    ## Examples

    ```
    Input: s = "abcdeca", k = 2
    Output: true
    ```
    **Explanation:** Remove 'b' and 'e' characters.

    ```
    Input: s = "abbababa", k = 1
    Output: true
    ```

    ## Constraints

    - `1 <= s.length <= 1000`
    - `s` consists of only lowercase English letters.
    - `1 <= k <= s.length`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def is_valid_palindrome(self, s: str, k: int) -> bool:
            raise NotImplementedError('Implement is_valid_palindrome')

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
