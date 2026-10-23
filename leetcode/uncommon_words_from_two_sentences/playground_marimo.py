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
    # 884. Uncommon Words from Two Sentences

    **Easy** · Hash Table, String, Counting

    A <strong>sentence</strong> is a string of single-space separated words where each word consists only of lowercase English letters.</p>

    <p>A word is <strong>uncommon</strong> if it appears exactly once in one of the sentences, and <strong>does not appear</strong> in the other sentence.</p>

    <p>Given two sentences <code>s1</code> and <code>s2</code>, return <em>a list of all the <strong>uncommon words</strong></em>. You may return the answer in any order.

    ## Examples

    ```
    Input: s1 = "this apple is sweet", s2 = "this apple is sour"
    Output: ["sweet","sour"]
    ```

    ```
    Input: s1 = "apple apple", s2 = "banana"
    Output: ["banana"]
    ```

    ## Constraints

    - 1 <= s1.length, s2.length <= 200
    - s1 and s2 consist of lowercase English letters and spaces.
    - s1 and s2 do not have leading or trailing spaces.
    - All the words in s1 and s2 are separated by a single space.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    from collections import Counter

    class Solution:

        def uncommon_from_sentences(self, s1: str, s2: str) -> list[str]:
            raise NotImplementedError('Implement uncommon_from_sentences')

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
