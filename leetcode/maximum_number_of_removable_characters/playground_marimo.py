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
    # 1898. Maximum Number of Removable Characters

    **Medium** · Array, Two Pointers, String, Binary Search

    You are given two strings `s` and `p` where `p` is a subsequence of `s`. You are also given a **distinct 0-indexed** integer array `removable` containing a subset of indices of `s` (`s` is also **0-indexed**).

    You want to choose an integer `k` (`0 <= k <= removable.length`) such that, after removing `k` characters from `s` using the **first** `k` indices in `removable`, `p` is still a subsequence of `s`. More formally, you will mark the character at `s[removable[i]]` for each `0 <= i < k`, then remove all marked characters and check if `p` is still a subsequence.

    Return *the **maximum** `k` you can choose such that `p` is still a subsequence of `s` after the removals*.

    A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

    ## Examples

    ```
    Input: s = "abcacb", p = "ab", removable = [3,1,0]
    Output: 2
    ```
    **Explanation:** After removing the characters at indices 3 and 1, `"abcacb"` becomes `"accb"`. `"ab"` is a subsequence of `"accb"`. If we remove the characters at indices 3, 1, and 0, `"abcacb"` becomes `"ccb"`, and `"ab"` is no longer a subsequence. Hence, the maximum k is 2.

    ```
    Input: s = "abcbddddd", p = "abcd", removable = [3,2,1,4,5,6]
    Output: 1
    ```
    **Explanation:** After removing the character at index 3, `"abcbddddd"` becomes `"abcddddd"`. `"abcd"` is a subsequence of `"abcddddd"`.

    ```
    Input: s = "abcab", p = "abc", removable = [0,1,2,3,4]
    Output: 0
    ```
    **Explanation:** If you remove the first index in the array removable, `"abc"` is no longer a subsequence.

    ## Constraints

    - `1 <= p.length <= s.length <= 10^5`
    - `0 <= removable.length < s.length`
    - `0 <= removable[i] < s.length`
    - `p` is a subsequence of `s`.
    - `s` and `p` both consist of lowercase English letters.
    - The elements in `removable` are distinct.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def maximum_removals(self, s: str, p: str, removable: list[int]) -> int:
            raise NotImplementedError('Implement maximum_removals')

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
