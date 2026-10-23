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
    # 87. Scramble String

    **Hard** · String, Dynamic Programming

    We can scramble a string s to get a string t using the following algorithm:

    1. If the length of the string is 1, stop.
    2. If the length of the string is > 1, do the following:
        1. Split the string into two non-empty substrings at a random index, i.e., if the string is `s`, divide it to `x` and `y` where `s = x + y`.
        2. Randomly decide to swap the two substrings or to keep them in the same order. i.e., after this step, `s` may become `s = x + y` or `s = y + x`.
        3. Apply step 1 recursively on each of the two substrings `x` and `y`.

    Given two strings `s1` and `s2` of **the same length**, return `true` if `s2` is a scrambled string of `s1`, otherwise, return `false`.

    ## Examples

    ```
    Input: s1 = "great", s2 = "rgeat"
    Output: true
    ```
    **Explanation:** One possible scenario applied on `s1` is:
    `"great" --> "gr/eat"` // divide at random index.
    `"gr/eat" --> "gr/eat"` // random decision is not to swap the two substrings and keep them in order.
    `"gr/eat" --> "g/r / e/at"` // apply the same algorithm recursively on both substrings. divide at random index each of them.
    `"g/r / e/at" --> "r/g / e/at"` // random decision was to swap the first substring and to keep the second substring in the same order.
    `"r/g / e/at" --> "r/g / e/ a/t"` // again apply the algorithm recursively, divide "at" to "a/t".
    `"r/g / e/ a/t" --> "r/g / e/ a/t"` // random decision is to keep both substrings in the same order.
    The algorithm stops now, and the result string is `"rgeat"` which is `s2`.
    As one possible scenario led `s1` to be scrambled to `s2`, we return `true`.

    ```
    Input: s1 = "abcde", s2 = "caebd"
    Output: false
    ```

    ```
    Input: s1 = "a", s2 = "a"
    Output: true
    ```

    ## Constraints

    - s1.length == s2.length
    - 1 <= s1.length <= 30
    - s1 and s2 consist of lowercase English letters.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def is_scramble(self, s1: str, s2: str) -> bool:
            raise NotImplementedError('Implement is_scramble')

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
