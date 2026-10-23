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
    # 1165. Single-Row Keyboard

    **Easy** · Hash Table, String

    There is a special keyboard with **all keys in a single row**.

    Given a string `keyboard` of length `26` indicating the layout of the keyboard (indexed from `0` to `25`). Initially, your finger is at index `0`. To type a character, you have to move your finger to the index of the desired character. The time taken to move your finger from index `i` to index `j` is `|i - j|`.

    You want to type a string `word`. Write a function to calculate how much time it takes to type it with one finger.

    ## Examples

    ```
    Input: keyboard = "abcdefghijklmnopqrstuvwxyz", word = "cba"
    Output: 4
    Explanation: The index moves from 0 to 2 to write 'c' then to 1 to write 'b' then to 0 again to write 'a'.
    Total time = 2 + 1 + 1 = 4.
    ```

    ```
    Input: keyboard = "pqrstuvwxyzabcdefghijklmno", word = "leetcode"
    Output: 73
    ```

    ## Constraints

    - keyboard.length == 26
    - keyboard contains each English lowercase letter exactly once in some order.
    - 1 <= word.length <= 10^4
    - word[i] is an English lowercase letter.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def calculate_time(self, keyboard: str, word: str) -> int:
            raise NotImplementedError('Implement calculate_time')

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
