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
    mo.md(r"""
    # 916. Word Subsets

    **Medium** · Array, Hash Table, String

    You are given two string arrays <code>words1</code> and <code>words2</code>.</p>

    <p>A string <code>b</code> is a <strong>subset</strong> of string <code>a</code> if every letter in <code>b</code> occurs in <code>a</code> including multiplicity.</p>

    <ul>
        <li>For example, <code>"wrr"</code> is a subset of <code>"warrior"</code> but is not a subset of <code>"world"</code>.</li>
    </ul>

    <p>A string <code>a</code> from <code>words1</code> is <strong>universal</strong> if for every string <code>b</code> in <code>words2</code>, <code>b</code> is a subset of <code>a</code>.</p>

    <p>Return an array of all the <strong>universal</strong> strings in <code>words1</code>. You may return the answer in <strong>any order</strong>.</p>

    ## Examples

    ```
    Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]
    Output: ["facebook","google","leetcode"]
    ```

    ```
    Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["l","o"]
    Output: ["google","leetcode"]
    ```

    ## Constraints

    - 1 <= words1.length, words2.length <= 10^4
    - 1 <= words1[i].length, words2[i].length <= 10
    - words1[i] and words2[i] consist only of lowercase English letters.
    - All the strings of words1 are unique.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from collections import Counter

    class Solution:

        def word_subsets(self, words1: list[str], words2: list[str]) -> list[str]:
            raise NotImplementedError('Implement word_subsets')

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
