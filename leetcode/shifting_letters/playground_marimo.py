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
    # 848. Shifting Letters

    **Medium** · Array, String, Prefix Sum

    You are given a string `s` of lowercase English letters and an integer array `shifts` of the same length.

    Call the `shift()` of a letter, the next letter in the alphabet, (wrapping around so that `'z'` becomes `'a'`).

    - For example, `shift('a') = 'b'`, `shift('t') = 'u'`, and `shift('z') = 'a'`.

    Now for each `shifts[i] = x`, we want to shift the first `i + 1` letters of `s`, `x` times.

    Return *the final string after all such shifts to s are applied*.

    ## Examples

    ```
    Input: s = "abc", shifts = [3,5,9]
    Output: "rpl"
    Explanation: We start with "abc".
    After shifting the first 1 letters of s by 3, we have "dbc".
    After shifting the first 2 letters of s by 5, we have "igc".
    After shifting the first 3 letters of s by 9, we have "rpl", the answer.
    ```

    ```
    Input: s = "aaa", shifts = [1,2,3]
    Output: "gfd"
    ```

    ## Constraints

    - 1 <= s.length <= 10^5
    - s consists of lowercase English letters.
    - shifts.length == s.length
    - 0 <= shifts[i] <= 10^9



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def shifting_letters(self, s: str, shifts: list[int]) -> str:
            raise NotImplementedError('Implement shifting_letters')

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
