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
    # 2486. Append Characters to String to Make Subsequence

    **Medium** · Two Pointers, String, Greedy

    You are given two strings `s` and `t` consisting of only lowercase English letters.

    Return the minimum number of characters that need to be appended to the end of `s` so that `t` becomes a subsequence of `s`.

    A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

    ## Examples

    ```
    Input: s = "coaching", t = "coding"
    Output: 4
    Explanation: Append the characters "ding" to the end of s so that s = "coachingding".
    Now, t is a subsequence of s ("coachingding").
    It can be shown that appending any 3 characters to the end of s will never make t a subsequence.
    ```

    ```
    Input: s = "abcde", t = "a"
    Output: 0
    Explanation: t is already a subsequence of s ("abcde").
    ```

    ```
    Input: s = "z", t = "abcde"
    Output: 5
    Explanation: Append the characters "abcde" to the end of s so that s = "zabcde".
    Now, t is a subsequence of s ("zabcde").
    It can be shown that appending any 4 characters to the end of s will never make t a subsequence.
    ```

    ## Constraints

    - 1 <= s.length, t.length <= 10^5
    - s and t consist only of lowercase English letters.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def append_characters(self, s: str, t: str) -> int:
            raise NotImplementedError('Implement append_characters')

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
