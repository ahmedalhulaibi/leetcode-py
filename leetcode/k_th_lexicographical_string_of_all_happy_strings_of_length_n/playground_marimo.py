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
    # 1415. The k-th Lexicographical String of All Happy Strings of Length n

    **Medium** · String, Backtracking

    A **happy string** is a string that:

    - consists only of letters of the set `['a', 'b', 'c']`.
    - `s[i] != s[i + 1]` for all values of `i` from `1` to `s.length - 1` (string is 1-indexed).

    For example, strings **"abc", "ac", "b"** and **"abcbabcbcb"** are all happy strings and strings **"aa", "baa"** and **"ababbc"** are not happy strings.

    Given two integers `n` and `k`, consider a list of all happy strings of length `n` sorted in lexicographical order.

    Return *the kth string* of this list or return an *empty string* if there are less than `k` happy strings of length `n`.

    ## Examples

    ```
    Input: n = 1, k = 3
    Output: "c"
    Explanation: The list ["a", "b", "c"] contains all happy strings of length 1. The third string is "c".
    ```

    ```
    Input: n = 1, k = 4
    Output: "\"
    Explanation: There are only 3 happy strings of length 1.
    ```

    ```
    Input: n = 3, k = 9
    Output: "cab"
    Explanation: There are 12 different happy strings of length 3 ["aba", "abc", "aca", "acb", "bab", "bac", "bca", "bcb", "cab", "cac", "cba", "cbc"]. You will find the 9th string = "cab".
    ```

    ## Constraints

    - `1 <= n <= 10`
    - `1 <= k <= 100`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def get_happy_string(self, n: int, k: int) -> str:
            raise NotImplementedError('Implement get_happy_string')

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
