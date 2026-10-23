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
    # 906. Super Palindromes

    **Hard** · Math, String, Enumeration

    Let's say a positive integer is a **super-palindrome** if it is a palindrome, and it is also the square of a palindrome.

    Given two positive integers <code>left</code> and <code>right</code> represented as strings, return <em>the number of <strong>super-palindromes</strong> integers in the inclusive range</em> <code>[left, right]</code>.

    ## Examples

    ```
    Input: left = "4", right = "1000"
    Output: 4
    Explanation: 4, 9, 121, and 484 are superpalindromes.
    Note that 676 is not a superpalindrome: 26 * 26 = 676, but 26 is not a palindrome.
    ```

    ```
    Input: left = "1", right = "2"
    Output: 1
    ```

    ## Constraints

    - 1 &lt;= left.length, right.length &lt;= 18
    - left and right consist of only digits.
    - left and right cannot have leading zeros.
    - left and right represent integers in the range [1, 10<sup>18</sup> - 1].
    - left is less than or equal to right.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def super_palindromes_in_range(self, left: str, right: str) -> int:
            raise NotImplementedError('Implement super_palindromes_in_range')

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
