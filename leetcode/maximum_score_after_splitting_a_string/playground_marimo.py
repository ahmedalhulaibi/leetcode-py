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
    # 1422. Maximum Score After Splitting a String

    **Easy** · String, Prefix Sum

    Given a string `s` of zeros and ones, return the maximum score after splitting the string into two **non-empty** substrings (i.e. left substring and right substring).

    The score after splitting a string is the number of **zeros** in the **left** substring plus the number of **ones** in the **right** substring.

    ## Examples

    ```
    Input: s = "011101"
    Output: 5
    ```
    **Explanation:** All possible ways of splitting `s` into two non-empty substrings are: `left = "0"` and `right = "11101"`, score = 1 + 4 = 5; `left = "01"` and `right = "1101"`, score = 1 + 3 = 4; `left = "011"` and `right = "101"`, score = 1 + 2 = 3; `left = "0111"` and `right = "01"`, score = 1 + 1 = 2; `left = "01110"` and `right = "1"`, score = 2 + 1 = 3.

    ```
    Input: s = "00111"
    Output: 5
    ```
    **Explanation:** When `left = "00"` and `right = "111"`, we get the maximum score = 2 + 3 = 5.

    ```
    Input: s = "1111"
    Output: 3
    ```

    ## Constraints

    - `2 <= s.length <= 500`
    - The string `s` consists of characters `'0'` and `'1'` only.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def max_score(self, s: str) -> int:
            raise NotImplementedError('Implement max_score')

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
