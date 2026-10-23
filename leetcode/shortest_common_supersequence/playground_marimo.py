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
    # 1092. Shortest Common Supersequence

    **Hard** · String, Dynamic Programming

    Given two strings <code>str1</code> and <code>str2</code>, return <em>the shortest string that has both </em><code>str1</code><em> and </em><code>str2</code><em> as <strong>subsequences</strong></em>. If there are multiple valid strings, return <strong>any</strong> of them.

    A string <code>s</code> is a <strong>subsequence</strong> of string <code>t</code> if deleting some number of characters from <code>t</code> (possibly <code>0</code>) results in the string <code>s</code>.

    ## Examples

    ```
    Input: str1 = "abac", str2 = "cab"
    Output: "cabac"
    Explanation: str1 = "abac" is a subsequence of "cabac" because we can delete the first "c". str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac". The answer provided is the shortest such string that satisfies these properties.
    ```

    ```
    Input: str1 = "aaaaaaaa", str2 = "aaaaaaaa"
    Output: "aaaaaaaa"
    ```

    ## Constraints

    - <code>1 &lt;= str1.length, str2.length &lt;= 1000</code>
    - <code>str1</code> and <code>str2</code> consist of lowercase English letters.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def shortest_common_supersequence(self, str1: str, str2: str) -> str:
            raise NotImplementedError('Implement shortest_common_supersequence')

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
