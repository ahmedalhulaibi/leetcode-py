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
    # 125. Valid Palindrome

    **Easy** · Two Pointers, String

    A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

    Given a string `s`, return `true` if it is a **palindrome**, or `false` otherwise.

    ## Examples

    ```
    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    ```
    **Explanation:** "amanaplanacanalpanama" is a palindrome.

    ```
    Input: s = "race a car"
    Output: false
    ```
    **Explanation:** "raceacar" is not a palindrome.

    ```
    Input: s = " "
    Output: true
    ```
    **Explanation:** s is an empty string "\" after removing non-alphanumeric characters. Since an empty string reads the same forward and backward, it is a palindrome.

    ## Constraints

    - `1 <= s.length <= 2 * 10^5`
    - `s` consists only of printable ASCII characters.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def is_palindrome(self, s: str) -> bool:
            raise NotImplementedError('Implement is_palindrome')

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
