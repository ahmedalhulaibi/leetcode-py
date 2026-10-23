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
    # 727. Minimum Window Subsequence

    **Hard** · String, Dynamic Programming, Sliding Window

    Given strings `s1` and `s2`, return the minimum contiguous substring part of `s1`, so that `s2` is a subsequence of the part.

    If there is no such window in `s1` that covers all characters in `s2`, return the empty string `"\"`. If there are multiple such minimum-length windows, return the one with the **left-most starting index**.

    A subsequence of a string is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

    ## Examples

    ```
    Input: s1 = "abcdebdde", s2 = "bde"
    Output: "bcde"
    Explanation: "bcde" is the answer because it occurs before "bdde" which has the same length.
    "deb" is not a smaller window because the elements of s2 in the window must occur in order.
    ```

    ```
    Input: s1 = "jmeqksfrsdcmsiwvaovztaqenprpvnbstl", s2 = "u"
    Output: "\"
    ```

    ## Constraints

    - 1 <= s1.length <= 2 * 10^4
    - 1 <= s2.length <= 100
    - s1 and s2 consist of lowercase English letters.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def min_window(self, s1: str, s2: str) -> str:
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
