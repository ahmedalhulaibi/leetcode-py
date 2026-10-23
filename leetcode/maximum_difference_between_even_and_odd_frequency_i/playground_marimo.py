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
    # 3442. Maximum Difference Between Even and Odd Frequency I

    **Easy** · Hash Table, String, Counting

    You are given a string `s` consisting of lowercase English letters.

    Your task is to find the **maximum** difference `diff = freq(a1) - freq(a2)` between the frequency of characters `a1` and `a2` in the string such that:

    - `a1` has an **odd frequency** in the string.
    - `a2` has an **even frequency** in the string.

    Return this **maximum** difference.

    ## Examples

    ```
    Input: s = "aaaaabbc"
    Output: 3
    Explanation: The character 'a' has an odd frequency of 5, and 'b' has an even frequency of 2.
    The maximum difference is 5 - 2 = 3.
    ```

    ```
    Input: s = "abcabcab"
    Output: 1
    Explanation: The character 'a' has an odd frequency of 3, and 'c' has an even frequency of 2.
    The maximum difference is 3 - 2 = 1.
    ```

    ## Constraints

    - `3 <= s.length <= 100`
    - `s` consists only of lowercase English letters.
    - `s` contains at least one character with an odd frequency and one with an even frequency.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def max_difference(self, s: str) -> int:
            raise NotImplementedError('Implement max_difference')

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
