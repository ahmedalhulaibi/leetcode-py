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
    # 1220. Count Vowels Permutation

    **Hard** · Dynamic Programming

    Given an integer `n`, your task is to count how many strings of length `n` can be formed under the following rules:

    - Each character is a lower case vowel (`'a'`, `'e'`, `'i'`, `'o'`, `'u'`)
    - Each vowel `'a'` may only be followed by an `'e'`.
    - Each vowel `'e'` may only be followed by an `'a'` or an `'i'`.
    - Each vowel `'i'` **may not** be followed by another `'i'`.
    - Each vowel `'o'` may only be followed by an `'i'` or a `'u'`.
    - Each vowel `'u'` may only be followed by an `'a'`.

    Since the answer may be too large, return it modulo `10^9 + 7`.

    ## Examples

    ```
    Input: n = 1
    Output: 5
    Explanation: All possible strings are: "a", "e", "i" , "o" and "u".
    ```

    ```
    Input: n = 2
    Output: 10
    Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".
    ```

    ```
    Input: n = 5
    Output: 68
    ```

    ## Constraints

    - `1 <= n <= 2 * 10^4`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def count_vowel_permutation(self, n: int) -> int:
            raise NotImplementedError('Implement count_vowel_permutation')

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
