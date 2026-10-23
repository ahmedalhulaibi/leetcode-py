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
    # 8. String to Integer (atoi)

    **Medium** · String

    Implement the `my_atoi(string s)` function, which converts a string to a 32-bit signed integer.

    The algorithm for `my_atoi(string s)` is as follows:

    1. **Whitespace**: Ignore any leading whitespace (` `).
    2. **Signedness**: Determine the sign by checking if the next character is `-` or `+`, assuming positivity if neither present.
    3. **Conversion**: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
    4. **Rounding**: If the integer is out of the 32-bit signed integer range `[-2^31, 2^31 - 1]`, then round the integer to remain in the range. Specifically, integers less than `-2^31` should be rounded to `-2^31`, and integers greater than `2^31 - 1` should be rounded to `2^31 - 1`.

    Return the integer as the final result.

    ## Examples

    ```
    Input: s = "42"
    Output: 42
    ```
    **Explanation:**
    ```
    The underlined characters are what is read in and the caret is the current reader position.
    Step 1: "42" (no characters read because there is no leading whitespace)
             ^
    Step 2: "42" (no characters read because there is neither a '-' nor '+')
             ^
    Step 3: "42" ("42" is read in)
               ^
    ```

    ```
    Input: s = "   -042"
    Output: -42
    ```
    **Explanation:**
    ```
    Step 1: "   -042" (leading whitespace is read and ignored)
                ^
    Step 2: "   -042" ('-' is read, so the result should be negative)
                 ^
    Step 3: "   -042" ("042" is read in, leading zeros ignored in the result)
                   ^
    ```

    ```
    Input: s = "1337c0d3"
    Output: 1337
    ```
    **Explanation:**
    ```
    Step 1: "1337c0d3" (no characters read because there is no leading whitespace)
             ^
    Step 2: "1337c0d3" (no characters read because there is neither a '-' nor '+')
             ^
    Step 3: "1337c0d3" ("1337" is read in; reading stops because the next character is a non-digit)
                 ^
    ```

    ```
    Input: s = "0-1"
    Output: 0
    ```
    **Explanation:**
    ```
    Step 1: "0-1" (no characters read because there is no leading whitespace)
             ^
    Step 2: "0-1" (no characters read because there is neither a '-' nor '+')
             ^
    Step 3: "0-1" ("0" is read in; reading stops because the next character is a non-digit)
              ^
    ```

    ```
    Input: s = "words and 987"
    Output: 0
    ```
    **Explanation:** Reading stops at the first non-digit character 'w'.

    ## Constraints

    - `0 <= s.length <= 200`
    - `s` consists of English letters (lower-case and upper-case), digits (0-9), ` `, `+`, `-`, and `.`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def my_atoi(self, s: str) -> int:
            raise NotImplementedError('Implement my_atoi')

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
