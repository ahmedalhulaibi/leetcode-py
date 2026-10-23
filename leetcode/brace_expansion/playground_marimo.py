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
    # 1087. Brace Expansion

    **Medium** · String, Backtracking, Breadth-First Search

    You are given a string `s` representing a list of words. Each letter in the word has one or more options.

    - If there is one option, the letter is represented as is.
    - If there is more than one option, then curly braces delimit the options. For example, `"{a,b,c}"` represents options `["a", "b", "c"]`.

    For example, if `s = "a{b,c}"`, the first character is always `'a'`, but the second character can be `'b'` or `'c'`. The original list is `["ab", "ac"]`.

    Return all words that can be formed in this manner, sorted in **lexicographical order**.

    ## Examples

    ```
    Input: s = "{a,b}c{d,e}f"
    Output: ["acdf","acef","bcdf","bcef"]
    ```

    ```
    Input: s = "abcd"
    Output: ["abcd"]
    ```

    ## Constraints

    - 1 <= s.length <= 50
    - s consists of curly brackets '{}', commas ',', and lowercase English letters.
    - s is guaranteed to be a valid input.
    - There are no nested curly brackets.
    - All characters inside a pair of consecutive opening and ending curly brackets are different.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def expand(self, s: str) -> list[str]:
            raise NotImplementedError('Implement expand')

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
