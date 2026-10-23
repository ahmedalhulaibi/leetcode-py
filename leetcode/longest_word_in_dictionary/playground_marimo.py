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
    # 720. Longest Word in Dictionary

    **Medium** · Array, Hash Table, String, Trie, Sorting

    Given an array of strings `words` representing an English Dictionary, return *the longest word in* `words` *that can be built one character at a time by other words in* `words`.

    If there is more than one possible answer, return the longest word with the smallest lexicographical order. If there is no answer, return the empty string.

    Note that the word should be built from left to right with each additional character being added to the end of a previous word.

    ## Examples

    ```
    Input: words = ["w","wo","wor","worl","world"]
    Output: "world"
    ```
    **Explanation:** The word `"world"` can be built one character at a time by `"w"`, `"wo"`, `"wor"`, and `"worl"`.

    ```
    Input: words = ["a","banana","app","appl","ap","apply","apple"]
    Output: "apple"
    ```
    **Explanation:** Both `"apply"` and `"apple"` can be built from other words in the dictionary. However, `"apple"` is lexicographically smaller than `"apply"`.

    ## Constraints

    - `1 <= words.length <= 1000`
    - `1 <= words[i].length <= 30`
    - `words[i]` consists of lowercase English letters.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def longest_word(self, words: list[str]) -> str:
            raise NotImplementedError('Implement longest_word')

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
