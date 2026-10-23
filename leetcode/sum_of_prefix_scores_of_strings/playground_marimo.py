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
    # 2416. Sum of Prefix Scores of Strings

    **Hard** · Array, String, Trie, Counting

    You are given an array `words` of size `n` consisting of non-empty strings.

    We define the **score** of a string `term` as the **number** of strings `words[i]` such that `term` is a **prefix** of `words[i]`.

    - For example, if `words = ["a", "ab", "abc", "cab"]`, then the score of `"ab"` is `2`, since `"ab"` is a prefix of both `"ab"` and `"abc"`.

    Return *an array* `answer` *of size* `n` *where* `answer[i]` *is the **sum** of scores of every **non-empty** prefix of* `words[i]`.

    **Note** that a string is considered as a prefix of itself.

    ## Examples

    ```
    Input: words = ["abc","ab","bc","b"]
    Output: [5,4,3,2]
    Explanation: The answer for each string is the following:
    - "abc" has 3 prefixes: "a", "ab", and "abc".
    - There are 2 strings with the prefix "a", 2 strings with the prefix "ab", and 1 string with the prefix "abc".
    The total is answer[0] = 2 + 2 + 1 = 5.
    - "ab" has 2 prefixes: "a" and "ab".
    - There are 2 strings with the prefix "a", and 2 strings with the prefix "ab".
    The total is answer[1] = 2 + 2 = 4.
    - "bc" has 2 prefixes: "b" and "bc".
    - There are 2 strings with the prefix "b", and 1 string with the prefix "bc".
    The total is answer[2] = 2 + 1 = 3.
    - "b" has 1 prefix: "b".
    - There are 2 strings with the prefix "b".
    The total is answer[3] = 2.
    ```

    ```
    Input: words = ["abcd"]
    Output: [4]
    Explanation:
    "abcd" has 4 prefixes: "a", "ab", "abc", and "abcd".
    Each prefix has a score of one, so the total is answer[0] = 1 + 1 + 1 + 1 = 4.
    ```

    ## Constraints

    - 1 <= words.length <= 1000
    - 1 <= words[i].length <= 1000
    - words[i] consists of lowercase English letters.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def sum_prefix_scores(self, words: list[str]) -> list[int]:
            raise NotImplementedError('Implement sum_prefix_scores')

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
