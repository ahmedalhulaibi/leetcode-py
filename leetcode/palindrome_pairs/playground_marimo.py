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
    # 336. Palindrome Pairs

    **Hard** · Array, Hash Table, String, Trie

    You are given a **0-indexed** array of **unique** strings `words`.

    A **palindrome pair** is a pair of integers `(i, j)` such that:

    - `0 <= i, j < words.length`,
    - `i != j`, and
    - `words[i] + words[j]` (the concatenation of the two strings) is a palindrome.

    Return an array of all the palindrome pairs of `words`.

    You must write an algorithm with `O(sum of words[i].length)` runtime complexity.

    ## Examples

    ```
    Input: words = ["abcd","dcba","lls","s","sssll"]
    Output: [[0,1],[1,0],[3,2],[2,4]]
    Explanation: The palindromes are ["abcddcba","dcbaabcd","slls","llssssll"]
    ```

    ```
    Input: words = ["bat","tab","cat"]
    Output: [[0,1],[1,0]]
    Explanation: The palindromes are ["battab","tabbat"]
    ```

    ```
    Input: words = ["a","\"]
    Output: [[0,1],[1,0]]
    Explanation: The palindromes are ["a","a"]
    ```

    ## Constraints

    - 1 <= words.length <= 5000
    - 0 <= words[i].length <= 300
    - `words[i]` consists of lowercase English letters.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def palindrome_pairs(self, words: list[str]) -> list[list[int]]:
            raise NotImplementedError('Implement palindrome_pairs')

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
