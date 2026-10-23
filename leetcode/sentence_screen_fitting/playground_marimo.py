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
    # 418. Sentence Screen Fitting

    **Medium** · Array, String, Dynamic Programming

    Given a `rows x cols` screen and a `sentence` represented as a list of strings, return *the number of times the given sentence can be fitted on the screen*.

    The order of words in the sentence must remain unchanged, and a word cannot be split into two lines. A single space must separate two consecutive words in a line.

    ## Examples

    ```
    Input: sentence = ["hello","world"], rows = 2, cols = 8
    Output: 1
    Explanation:
    hello---
    world---
    The character '-' signifies an empty space on the screen.
    ```

    ```
    Input: sentence = ["a", "bcd", "e"], rows = 3, cols = 6
    Output: 2
    Explanation:
    a-bcd-
    e-a---
    bcd-e-
    The character '-' signifies an empty space on the screen.
    ```

    ```
    Input: sentence = ["i","had","apple","pie"], rows = 4, cols = 5
    Output: 1
    Explanation:
    i-had
    apple
    pie-i
    had--
    The character '-' signifies an empty space on the screen.
    ```

    ## Constraints

    - `1 <= sentence.length`
    - `1 <= rows, cols <= 4 * 10^4`
    - `1 <= sentence[i].length <= 10`
    - `sentence[i]` consists of only lower-case English letters.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def words_typing(self, sentence: list[str], rows: int, cols: int) -> int:
            raise NotImplementedError('Implement words_typing')

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
