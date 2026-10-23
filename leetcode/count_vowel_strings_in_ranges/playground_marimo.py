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
    # 2559. Count Vowel Strings in Ranges

    **Medium** · Array, String, Prefix Sum

    You are given a <strong>0-indexed</strong> array of strings <code>words</code> and a 2D array of integers <code>queries</code>.

    Each query <code>queries[i] = [l<sub>i</sub>, r<sub>i</sub>]</code> asks us to find the number of strings present at the indices ranging from <code>l<sub>i</sub></code> to <code>r<sub>i</sub></code> (both <strong>inclusive</strong>) of <code>words</code> that start and end with a vowel.

    Return <em>an array </em><code>ans</code><em> of size </em><code>queries.length</code><em>, where </em><code>ans[i]</code><em> is the answer to the </em><code>i</code><sup>th</sup><em> query</em>.

    <strong>Note</strong> that the vowel letters are <code>'a'</code>, <code>'e'</code>, <code>'i'</code>, <code>'o'</code>, and <code>'u'</code>.

    ## Examples

    ```
    Input: words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]
    Output: [2,3,0]
    Explanation: The strings starting and ending with a vowel are "aba", "ece", "aa" and "e".
    The answer to the query [0,2] is 2 (strings "aba" and "ece").
    The answer to the query [1,4] is 3 (strings "ece", "aa", "e").
    The answer to the query [1,1] is 0.
    We return [2,3,0].
    ```

    ```
    Input: words = ["a","e","i"], queries = [[0,2],[0,1],[2,2]]
    Output: [3,2,1]
    Explanation: Every string satisfies the conditions, so we return [3,2,1].
    ```

    ## Constraints

    - 1 <= words.length <= 10^5
    - 1 <= words[i].length <= 40
    - words[i] consists only of lowercase English letters.
    - sum(words[i].length) <= 3 * 10^5
    - 1 <= queries.length <= 10^5
    - 0 <= l<sub>i</sub> <= r<sub>i</sub> < words.length



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def vowel_strings(self, words: list[str], queries: list[list[int]]) -> list[int]:
            raise NotImplementedError('Implement vowel_strings')

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
