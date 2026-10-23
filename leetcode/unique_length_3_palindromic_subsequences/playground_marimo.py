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
    # 1930. Unique Length-3 Palindromic Subsequences

    **Medium** · Hash Table, String, Bit Manipulation, Prefix Sum

    Given a string s, return the number of unique palindromes of length three that are a subsequence of s.

    Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.

    A palindrome is a string that reads the same forwards and backwards.

    A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

    - For example, `"ace"` is a subsequence of `"abcde"`.

    ## Examples

    ```
    Input: s = "aabca"
    Output: 3
    Explanation: The 3 palindromic subsequences of length 3 are:
    - "aba" (subsequence of "aabca")
    - "aaa" (subsequence of "aabca")
    - "aca" (subsequence of "aabca")
    ```

    ```
    Input: s = "adc"
    Output: 0
    Explanation: There are no palindromic subsequences of length 3 in "adc".
    ```

    ```
    Input: s = "bbcbaba"
    Output: 4
    Explanation: The 4 palindromic subsequences of length 3 are:
    - "bbb" (subsequence of "bbcbaba")
    - "bcb" (subsequence of "bbcbaba")
    - "bab" (subsequence of "bbcbaba")
    - "aba" (subsequence of "bbcbaba")
    ```

    ## Constraints

    - 3 <= s.length <= 10^5
    - s consists of only lowercase English letters.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def count_palindromic_subsequence(self, s: str) -> int:
            raise NotImplementedError('Implement count_palindromic_subsequence')

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
