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
    # 616. Add Bold Tag in String

    **Medium** · Trie, Array, Hash Table, String, String Matching

    You are given a string `s` and an array of strings `words`.

    You should add a closed pair of bold tag `<b>` and `</b>` to wrap the substrings in `s` that exist in `words`.

    - If two such substrings overlap, you should wrap them together with only one pair of closed bold-tag.
    - If two substrings wrapped by bold tags are consecutive, you should combine them.

    Return `s` after adding the bold tags.

    ## Examples

    ```
    Input: s = "abcxyz123", words = ["abc","123"]
    Output: "<b>abc</b>xyz<b>123</b>"
    Explanation: The two strings of words are substrings of s as following: "abcxyz123". We add <b> before each substring and </b> after each substring.
    ```

    ```
    Input: s = "aaabbb", words = ["aa","b"]
    Output: "<b>aaabbb</b>"
    ```

    ## Constraints

    - `1 <= s.length <= 1000`
    - `0 <= words.length <= 100`
    - `1 <= words[i].length <= 1000`
    - `s` and `words[i]` consist of English letters and digits.
    - All the values of `words` are **unique**.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def add_bold_tag(self, s: str, words: list[str]) -> str:
            raise NotImplementedError('Implement add_bold_tag')

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
