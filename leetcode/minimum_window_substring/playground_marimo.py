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
    # 76. Minimum Window Substring

    **Hard** · Hash Table, String, Sliding Window

    Given two strings `s` and `t` of lengths `m` and `n` respectively, return the **minimum window substring** of `s` such that every character in `t` (including duplicates) is included in the window. If there is no such substring, return the empty string `"\"`.

    The testcases will be generated such that the answer is unique.

    ## Examples

    ```
    Input: s = "ADOBECODEBANC", t = "ABC"
    Output: "BANC"
    ```
    **Explanation:** The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

    ```
    Input: s = "a", t = "a"
    Output: "a"
    ```
    **Explanation:** The entire string s is the minimum window.

    ```
    Input: s = "a", t = "aa"
    Output: "\"
    ```
    **Explanation:** Both 'a's from t must be included in the window. Since the largest window of s only has one 'a', return empty string.

    ## Constraints

    - `m == s.length`
    - `n == t.length`
    - `1 <= m, n <= 10^5`
    - `s` and `t` consist of uppercase and lowercase English letters.

    **Follow up:** Could you find an algorithm that runs in `O(m + n)` time?

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def min_window(self, s: str, t: str) -> str:
            raise NotImplementedError('Implement min_window')

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
