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
    # 564. Find the Closest Palindrome

    **Hard** · Math, String

    Given a string `n` representing an integer, return *the closest integer (not including itself), which is a palindrome*. If there is a tie, return *the smaller one*.

    The closest is defined as the absolute difference minimized between two integers.

    ## Examples

    ```
    Input: n = "123"
    Output: "121"
    ```

    ```
    Input: n = "1"
    Output: "0"
    ```
    **Explanation:** 0 and 2 are the closest palindromes but we return the smallest which is 0.

    ## Constraints

    - `1 <= n.length <= 18`
    - `n` consists of only digits.
    - `n` does not have leading zeros.
    - `n` is representing an integer in the range `[1, 10^18 - 1]`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def nearest_palindromic(self, n: str) -> str:
            raise NotImplementedError('Implement nearest_palindromic')

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
