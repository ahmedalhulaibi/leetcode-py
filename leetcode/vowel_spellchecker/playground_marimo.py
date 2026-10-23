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
    # 966. Vowel Spellchecker

    **Medium** · Array, Hash Table, String

    Given a `wordlist`, we want to implement a spellchecker that converts a query word into a correct word.

    For a given query word, the spell checker handles two categories of spelling mistakes:

    - Capitalization: If the query matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the case in the wordlist.
    - Vowel Errors: If after replacing the vowels (`'a'`, `'e'`, `'i'`, `'o'`, `'u'`) of the query word with any vowel individually, it matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the match in the wordlist.

    In addition, the spell checker operates under the following precedence rules:

    - When the query exactly matches a word in the wordlist (case-sensitive), you should return the same word back.
    - When the query matches a word up to capitalization, you should return the first such match in the wordlist.
    - When the query matches a word up to vowel errors, you should return the first such match in the wordlist.
    - If the query has no matches in the wordlist, you should return the empty string.

    Given some queries, return a list of words `answer`, where `answer[i]` is the correct word for `query = queries[i]`.

    ## Examples

    ```
    Input: wordlist = ["KiTe","kite","hare","Hare"], queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
    Output: ["kite","KiTe","KiTe","Hare","hare","\","\","KiTe","\","KiTe"]
    ```

    ```
    Input: wordlist = ["yellow"], queries = ["YellOw"]
    Output: ["yellow"]
    ```

    ## Constraints

    - 1 <= wordlist.length, queries.length <= 5000
    - 1 <= wordlist[i].length, queries[i].length <= 7
    - wordlist[i] and queries[i] consist only of English letters.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def spellchecker(self, wordlist: list[str], queries: list[str]) -> list[str]:
            raise NotImplementedError('Implement spellchecker')

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
