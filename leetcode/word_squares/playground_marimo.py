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
    # 425. Word Squares

    **Hard** · Trie, Array, String, Backtracking

    Given an array of **unique** strings `words`, return all the [word squares](https://en.wikipedia.org/wiki/Word_square) you can build from `words`. The same word from `words` can be used **multiple times**. You can return the answer in **any order**.

    A sequence of strings forms a valid **word square** if the `k^th` row and column read the same string, where `0 <= k < max(numRows, numColumns)`.

    For example, the word sequence `["ball","area","lead","lady"]` forms a word square because each word reads the same both horizontally and vertically.

    ## Examples

    ```
    Input: words = ["area","lead","wall","lady","ball"]
    Output: [["ball","area","lead","lady"],["wall","area","lead","lady"]]
    Explanation:
    The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
    ```

    ```
    Input: words = ["abat","baba","atan","atal"]
    Output: [["baba","abat","baba","atal"],["baba","abat","baba","atan"]]
    Explanation:
    The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
    ```

    ## Constraints

    - `1 <= words.length <= 1000`
    - `1 <= words[i].length <= 4`
    - All `words[i]` have the same length.
    - `words[i]` consists of only lowercase English letters.
    - All `words[i]` are **unique**.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def word_squares(self, words: list[str]) -> list[list[str]]:
            raise NotImplementedError('Implement word_squares')

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
