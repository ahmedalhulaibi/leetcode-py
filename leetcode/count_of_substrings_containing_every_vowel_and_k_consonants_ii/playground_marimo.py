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
    # 3306. Count of Substrings Containing Every Vowel and K Consonants II

    **Medium** · Hash Table, String, Sliding Window

    You are given a string <code>word</code> and a <strong>non-negative</strong> integer <code>k</code>.

    Return the total number of <span data-keyword="substring-nonempty">substrings</span> of <code>word</code> that contain every vowel (<code>'a'</code>, <code>'e'</code>, <code>'i'</code>, <code>'o'</code>, and <code>'u'</code>) <strong>at least</strong> once and <strong>exactly</strong> <code>k</code> consonants.

    ## Examples

    ```
    Input: word = "aeioqq", k = 1
    Output: 0
    Explanation: There is no substring with every vowel.
    ```

    ```
    Input: word = "aeiou", k = 0
    Output: 1
    Explanation: The only substring with every vowel and zero consonants is word[0..4], which is "aeiou".
    ```

    ```
    Input: word = "ieaouqqieaouqq", k = 1
    Output: 3
    Explanation: The substrings with every vowel and one consonant are:
    - word[0..5], which is "ieaouq".
    - word[6..11], which is "qieaou".
    - word[7..12], which is "ieaouq".
    ```

    ## Constraints

    - 5 <= word.length <= 2 * 10^5
    - word consists only of lowercase English letters.
    - 0 <= k <= word.length - 5



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def count_of_substrings(self, word: str, k: int) -> int:
            raise NotImplementedError('Implement count_of_substrings')

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
