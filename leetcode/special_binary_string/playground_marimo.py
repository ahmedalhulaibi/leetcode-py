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
    # 761. Special Binary String

    **Hard** · String, Divide and Conquer, Sorting

    Special binary strings are binary strings with the following two properties:

    - The number of 0's is equal to the number of 1's.
    - Every prefix of the binary string has at least as many 1's as 0's.

    You are given a special binary string `s`.

    A move consists of choosing two consecutive, non-empty, special substrings of `s`, and swapping them. Two strings are consecutive if the last character of the first string is exactly one index before the first character of the second string.

    Return the lexicographically largest resulting string possible after applying the mentioned operations on the string.

    ## Examples

    ```
    Input: s = "11011000"
    Output: "11100100"
    Explanation: The strings "10" [occuring at s[1]] and "1100" [at s[3]] are swapped.
    This is the lexicographically largest string possible after some number of swaps.
    ```

    ```
    Input: s = "10"
    Output: "10"
    ```

    ## Constraints

    - 1 <= s.length <= 50
    - s[i] is either '0' or '1'.
    - s is a special binary string.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def make_largest_special(self, s: str) -> str:
            raise NotImplementedError('Implement make_largest_special')

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
