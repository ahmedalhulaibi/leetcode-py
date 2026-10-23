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
    # 139. Word Break

    **Medium** · Array, Hash Table, String, Dynamic Programming, Trie, Memoization

    Given a string `s` and a dictionary of strings `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of one or more dictionary words.

    **Note** that the same word in the dictionary may be reused multiple times in the segmentation.

    ## Examples

    ```
    Input: s = "leetcode", wordDict = ["leet","code"]
    Output: true
    ```
    **Explanation:** Return true because "leetcode" can be segmented as "leet code".

    ```
    Input: s = "applepenapple", wordDict = ["apple","pen"]
    Output: true
    ```
    **Explanation:** Return true because "applepenapple" can be segmented as "apple pen apple".
    Note that you are allowed to reuse a dictionary word.

    ```
    Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
    Output: false
    ```

    ## Constraints

    - `1 <= s.length <= 300`
    - `1 <= wordDict.length <= 1000`
    - `1 <= wordDict[i].length <= 20`
    - `s` and `wordDict[i]` consist of only lowercase English letters.
    - All the strings of `wordDict` are **unique**.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def word_break(self, s: str, word_dict: list[str]) -> bool:
            raise NotImplementedError('Implement word_break')

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
