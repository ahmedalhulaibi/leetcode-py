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
    # 880. Decoded String at Index

    **Medium** · String, Stack

    You are given an encoded string `s`. To decode the string to a tape, the encoded string is read one character at a time and the following steps are taken:

    - If the character read is a letter, that letter is written onto the tape.
    - If the character read is a digit `d`, the entire current tape is repeatedly written `d - 1` more times in total.

    Given an integer `k`, return the `k^th` letter (**1-indexed**) in the decoded string.

    ## Examples

    ```
    Input: s = "leet2code3", k = 10
    Output: "o"
    Explanation: The decoded string is "leetleetcodeleetleetcodeleetleetcode".
    The 10th letter in the string is "o".
    ```

    ```
    Input: s = "ha22", k = 5
    Output: "h"
    Explanation: The decoded string is "hahahaha".
    The 5th letter is "h".
    ```

    ```
    Input: s = "a2345678999999999999999", k = 1
    Output: "a"
    Explanation: The decoded string is "a" repeated 8301530446056247680 times.
    The 1st letter is "a".
    ```

    ## Constraints

    - 2 <= s.length <= 100
    - s consists of lowercase English letters and digits 2 through 9.
    - s starts with a letter.
    - 1 <= k <= 10^9
    - It is guaranteed that k is less than or equal to the length of the decoded string.
    - The decoded string is guaranteed to have less than 2^63 letters.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def decode_at_index(self, s: str, k: int) -> str:
            raise NotImplementedError('Implement decode_at_index')

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
