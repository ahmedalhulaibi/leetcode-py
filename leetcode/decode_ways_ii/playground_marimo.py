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
    # 639. Decode Ways II

    **Hard** · String, Dynamic Programming

    A message containing letters from A-Z can be encoded into numbers using the following mapping:

    ```
    'A' -> "1"
    'B' -> "2"
    ...
    'Z' -> "26"
    ```

    To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

    - "AAJF" with the grouping (1 1 10 6)
    - "KJF" with the grouping (11 10 6)

    Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

    In addition to the mapping above, an encoded message may contain the '*' character, which can represent any digit from '1' to '9' ('0' is excluded). For example, the encoded message "1*" may represent any of the encoded messages "11", "12", "13", "14", "15", "16", "17", "18", or "19". Decoding "1*" is equivalent to decoding any of the encoded messages it can represent.

    Given a string s consisting of digits and '*' characters, return the number of ways to decode it.

    Since the answer may be very large, return it modulo 10^9 + 7.

    ## Examples

    ```
    Input: s = "*"
    Output: 9
    Explanation: The encoded message can represent any of the encoded messages "1" through "9". Each of these can be decoded to the strings "A" through "I" respectively. Hence, there are a total of 9 ways to decode "*".
    ```

    ```
    Input: s = "1*"
    Output: 18
    Explanation: The encoded message can represent any of the encoded messages "11" through "19". Each of these encoded messages have 2 ways to be decoded (e.g. "11" can be decoded to "AA" or "K"). Hence, there are a total of 9 * 2 = 18 ways to decode "1*".
    ```

    ```
    Input: s = "2*"
    Output: 15
    Explanation: The encoded message can represent any of the encoded messages "21" through "29". "21" through "26" have 2 ways of being decoded, but "27" through "29" only have 1 way. Hence, there are a total of (6 * 2) + (3 * 1) = 15 ways to decode "2*".
    ```

    ## Constraints

    - 1 <= s.length <= 10^5
    - s[i] is a digit or '*'.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def num_decodings(self, s: str) -> int:
            raise NotImplementedError('Implement num_decodings')

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
