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
    # 1255. Maximum Score Words Formed by Letters

    **Hard** · Array, Hash Table, String, Dynamic Programming, Backtracking, Bit Manipulation, Counting, Bitmask

    Given a list of words, list of  single letters (might be repeating) and score of every character.

    Return the maximum score of any valid set of words formed by using the given letters (words[i] cannot be used two or more times).

    It is not necessary to use all characters in <code>letters</code> and each letter can only be used once. Score of letters <code>'a'</code>, <code>'b'</code>, <code>'c'</code>, ... ,<code>'z'</code> is given by <code>score[0]</code>, <code>score[1]</code>, ... , <code>score[25]</code> respectively.

    ## Examples

    ```
    Input: words = ["dog","cat","dad","good"], letters = ["a","a","c","d","d","d","g","o","o"], score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
    Output: 23
    Explanation:
    Score  a=1, c=9, d=5, g=3, o=2
    Given letters, we can form the words "dad" (5+1+5) and "good" (3+2+2+5) with a score of 23.
    Words "dad" and "dog" only get a score of 21.
    ```

    ```
    Input: words = ["xxxz","ax","bx","cx"], letters = ["z","a","b","c","x","x","x"], score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]
    Output: 27
    Explanation:
    Score  a=4, b=4, c=4, x=5, z=10
    Given letters, we can form the words "ax" (4+5), "bx" (4+5) and "cx" (4+5) with a score of 27.
    Word "xxxz" only get a score of 25.
    ```

    ```
    Input: words = ["leetcode"], letters = ["l","e","t","c","o","d"], score = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]
    Output: 0
    Explanation:
    Letter "e" can only be used once.
    ```

    ## Constraints

    - 1 <= words.length <= 14
    - 1 <= words[i].length <= 15
    - 1 <= letters.length <= 100
    - letters[i].length == 1
    - score.length == 26
    - 0 <= score[i] <= 10
    - words[i], letters[i] contains only lower case English letters.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from collections import Counter

    class Solution:

        def max_score_words(self, words: list[str], letters: list[str], score: list[int]) -> int:
            raise NotImplementedError('Implement max_score_words')

    practice_exports = {'Counter': Counter, 'Solution': Solution}
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
