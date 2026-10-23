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
    # 866. Prime Palindrome

    **Medium** · Math, Number Theory, Primality Test

    Given an integer `n`, return *the smallest prime palindrome* greater than or equal to `n`.

    An integer is **prime** if it has exactly two divisors: `1` and itself. Note that `1` is not a prime number.

    - For example, `2`, `3`, `5`, `7`, `11`, and `13` are all primes.

    An integer is a **palindrome** if it reads the same from left to right as it does from right to left.

    - For example, `101` and `12321` are palindromes.

    The test cases are generated so that the answer always exists and is in the range `[2, 2 * 10^8]`.

    ## Examples

    ```
    Input: n = 6
    Output: 7
    ```

    ```
    Input: n = 8
    Output: 11
    ```

    ```
    Input: n = 13
    Output: 101
    ```

    ## Constraints

    - 1 <= n <= 10<sup>8</sup>



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def prime_palindrome(self, n: int) -> int:
            raise NotImplementedError('Implement prime_palindrome')

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
