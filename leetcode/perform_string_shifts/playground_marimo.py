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
    # 1427. Perform String Shifts

    **Easy** · Array, Math, String

    You are given a string `s` containing lowercase English letters, and a matrix `shift`, where `shift[i] = [direction<sub>i</sub>, amount<sub>i</sub>]`:

    - `direction<sub>i</sub>` can be `0` (for left shift) or `1` (for right shift).
    - `amount<sub>i</sub>` is the amount by which string `s` is to be shifted.
    - A left shift by 1 means remove the first character of `s` and append it to the end.
    - Similarly, a right shift by 1 means remove the last character of `s` and add it to the beginning.

    Return the final string after all operations.

    ## Examples

    ```
    Input: s = "abc", shift = [[0,1],[1,2]]
    Output: "cab"
    Explanation:
    [0,1] means shift to left by 1. "abc" -> "bca"
    [1,2] means shift to right by 2. "bca" -> "cab"
    ```

    ```
    Input: s = "abcdefg", shift = [[1,1],[1,1],[0,2],[1,3]]
    Output: "efgabcd"
    Explanation:
    [1,1] means shift to right by 1. "abcdefg" -> "gabcdef"
    [1,1] means shift to right by 1. "gabcdef" -> "fgabcde"
    [0,2] means shift to left by 2. "fgabcde" -> "abcdefg"
    [1,3] means shift to right by 3. "abcdefg" -> "efgabcd"
    ```

    ## Constraints

    - `1 <= s.length <= 100`
    - `s` only contains lower case English letters.
    - `1 <= shift.length <= 100`
    - `shift[i].length == 2`
    - `direction<sub>i</sub>` is either `0` or `1`.
    - `0 <= amount<sub>i</sub> <= 100`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def string_shift(self, s: str, shift: list[list[int]]) -> str:
            raise NotImplementedError('Implement string_shift')

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
