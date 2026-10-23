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
    # 393. UTF-8 Validation

    **Medium** · Array, Bit Manipulation

    Given an integer array `data` representing the data, return whether it is a valid UTF-8 encoding (i.e. it translates to a sequence of valid UTF-8 encoded characters).

    A character in UTF8 can be from 1 to 4 bytes long, subjected to the following rules:

    1. For a 1-byte character, the first bit is a `0`, followed by its Unicode code.
    2. For an n-bytes character, the first `n` bits are all one's, the `n + 1` bit is `0`, followed by `n - 1` bytes with the most significant 2 bits being `10`.

    This is how the UTF-8 encoding would work:

    ```
         Number of Bytes   |        UTF-8 Octet Sequence
                           |              (binary)
       --------------------+-----------------------------------------
                1          |   0xxxxxxx
                2          |   110xxxxx 10xxxxxx
                3          |   1110xxxx 10xxxxxx 10xxxxxx
                4          |   11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
    ```

    `x` denotes a bit in the binary form of a byte that may be either `0` or `1`.

    **Note:** The input is an array of integers. Only the **least significant 8 bits** of each integer is used to store the data. This means each integer represents only 1 byte of data.

    ## Examples

    ```
    Input: data = [197,130,1]
    Output: true
    Explanation: data represents the octet sequence: 11000101 10000010 00000001.
    It is a valid utf-8 encoding for a 2-bytes character followed by a 1-byte character.
    ```

    ```
    Input: data = [235,140,4]
    Output: false
    Explanation: data represented the octet sequence: 11101011 10001100 00000100.
    The first 3 bits are all one's and the 4th bit is 0 means it is a 3-bytes character.
    The next byte is a continuation byte which starts with 10 and that's correct.
    But the second continuation byte does not start with 10, so it is invalid.
    ```

    ## Constraints

    - 1 <= data.length <= 2 * 10^4
    - 0 <= data[i] <= 255



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def valid_utf8(self, data: list[int]) -> bool:
            raise NotImplementedError('Implement valid_utf8')

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
