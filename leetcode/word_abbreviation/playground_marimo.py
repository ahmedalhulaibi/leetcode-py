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
    # 527. Word Abbreviation

    **Hard** · Greedy, Trie, Array, String, Sorting

    Given an array of **distinct** strings `words`, return the minimal possible **abbreviations** for every word.

    The following are the rules for a string abbreviation:

    1. The **initial** abbreviation for each word is: the first character, then the number of characters in between, followed by the last character.
    2. If more than one word shares the **same** abbreviation, then perform the following operation:
       - **Increase** the prefix (characters in the first part) of each of their abbreviations by `1`.
         - For example, say you start with the words `["abcdef","abndef"]` both initially abbreviated as `"a4f"`. Then, a sequence of operations would be `["a4f","a4f"]` -> `["ab3f","ab3f"]` -> `["abc2f","abn2f"]`.
       - This operation is repeated until every abbreviation is **unique**.
    3. At the end, if an abbreviation did not make a word shorter, then keep it as the original word.

    ## Examples

    ```
    Input: words = ["like","god","internal","me","internet","interval","intension","face","intrusion"]
    Output: ["l2e","god","internal","me","i6t","interval","inte4n","f2e","intr4n"]
    ```

    ```
    Input: words = ["aa","aaa"]
    Output: ["aa","aaa"]
    ```

    ## Constraints

    - `1 <= words.length <= 400`
    - `2 <= words[i].length <= 400`
    - `words[i]` consists of lowercase English letters.
    - All the strings of `words` are **unique**.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def words_abbreviation(self, words: list[str]) -> list[str]:
            raise NotImplementedError('Implement words_abbreviation')

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
