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
    # 3045. Count Prefix and Suffix Pairs II

    **Hard** · Array, String, Trie, Rolling Hash, String Matching, Hash Function, Z Algorithm

    You are given a 0-indexed string array words.

    Let's define a boolean function isPrefixAndSuffix that takes two strings, str1 and str2:

    - isPrefixAndSuffix(str1, str2) returns true if str1 is both a prefix and a suffix of str2, and false otherwise.

    For example, isPrefixAndSuffix("aba", "ababa") is true because "aba" is a prefix of "ababa" and also a suffix, but isPrefixAndSuffix("abc", "abcd") is false.

    Return an integer denoting the number of index pairs (i, j) such that i < j, and isPrefixAndSuffix(words[i], words[j]) is true.

    ## Examples

    ```
    Input: words = ["a","aba","ababa","aa"]
    Output: 4
    ```
    **Explanation:** The counted index pairs are (0, 1), (0, 2), (0, 3) and (1, 2).

    ```
    Input: words = ["pa","papa","ma","mama"]
    Output: 2
    ```
    **Explanation:** The counted index pairs are (0, 1) and (2, 3).

    ```
    Input: words = ["abab","ab"]
    Output: 0
    ```

    ## Constraints

    - 1 <= words.length <= 10^5
    - 1 <= words[i].length <= 10^5
    - words[i] consists only of lowercase English letters.
    - The sum of the lengths of all words[i] does not exceed 5 * 10^5.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from typing import Any

    class Solution:

        def count_prefix_and_suffix_pairs(self, words: list[str]) -> int:
            raise NotImplementedError('Implement count_prefix_and_suffix_pairs')

    practice_exports = {'Any': Any, 'Solution': Solution}
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
