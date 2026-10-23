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
    # 758. Bold Words in String

    **Medium** · Trie, Array, Hash Table, String, String Matching

    Given an array of keywords `words` and a string `s`, make all appearances of all keywords `words[i]` in `s` bold. Any letters between `<b>` and `</b>` tags become bold.

    Return `s` *after adding the bold tags*. The returned string should use the least number of tags possible, and the tags should form a valid combination.

    ## Examples

    ```
    Input: words = ["ab","bc"], s = "aabcd"
    Output: "a<b>abc</b>d"
    Explanation: Note that returning "a<b>a<b>b</b>c</b>d" would use more tags, so it is incorrect.
    ```

    ```
    Input: words = ["ab","cb"], s = "aabcd"
    Output: "a<b>ab</b>cd"
    ```

    ## Constraints

    - `1 <= s.length <= 500`
    - `0 <= words.length <= 50`
    - `1 <= words[i].length <= 10`
    - `s` and `words[i]` consist of lowercase English letters.

    **Note:** This question is the same as [616: Add Bold Tag in String](https://leetcode.com/problems/add-bold-tag-in-string/description/).

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def bold_words(self, words: list[str], s: str) -> str:
            raise NotImplementedError('Implement bold_words')

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
