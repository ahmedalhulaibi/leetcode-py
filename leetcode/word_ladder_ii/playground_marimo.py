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
    # 126. Word Ladder II

    **Hard** · Hash Table, String, Backtracking, Breadth-First Search, Bidirectional Search

    A **transformation sequence** from word `beginWord` to word `endWord` using a dictionary `wordList` is a sequence of words `beginWord -> s1 -> s2 -> ... -> sk` such that:

    - Every adjacent pair of words differs by a single letter.
    - Every `si` for `1 <= i <= k` is in `wordList`. Note that `beginWord` does not need to be in `wordList`.
    - `sk == endWord`

    Given two words, `beginWord` and `endWord`, and a dictionary `wordList`, return *all the **shortest transformation sequences** from* `beginWord` *to* `endWord`*, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words* `[beginWord, s1, s2, ..., sk]`.

    ## Examples

    ```
    Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
    Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
    ```
    **Explanation:** There are 2 shortest transformation sequences: "hit" -> "hot" -> "dot" -> "dog" -> "cog" and "hit" -> "hot" -> "lot" -> "log" -> "cog".

    ```
    Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
    Output: []
    ```
    **Explanation:** The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

    ## Constraints

    - 1 <= beginWord.length <= 5
    - endWord.length == beginWord.length
    - 1 <= wordList.length <= 500
    - wordList[i].length == beginWord.length
    - beginWord, endWord, and wordList[i] consist of lowercase English letters.
    - beginWord != endWord
    - All the words in wordList are unique.
    - The sum of all shortest transformation sequences does not exceed 10^5.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from string import ascii_lowercase

    class Solution:

        def find_ladders(self, begin_word: str, end_word: str, word_list: list[str]) -> list[list[str]]:
            raise NotImplementedError('Implement find_ladders')

    practice_exports = {'ascii_lowercase': ascii_lowercase, 'Solution': Solution}
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
