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
    # 2696. Minimum String Length After Removing Substrings

    **Easy** · String, Stack, Simulation

    You are given a string `s` consisting only of uppercase English letters.

    You can apply some operations to this string where, in one operation, you can remove any occurrence of one of the substrings `"AB"` or `"CD"` from `s`.

    Return the minimum possible length of the resulting string that you can obtain.

    Note that the string concatenates after removing the substring and could produce new `"AB"` or `"CD"` substrings.

    ## Examples

    ```
    Input: s = "ABFCACDB"
    Output: 2
    Explanation: We can do the following operations:
    - Remove the substring "ABFCACDB", so s = "FCACDB".
    - Remove the substring "FCACDB", so s = "FCAB".
    - Remove the substring "FCAB", so s = "FC".
    So the resulting length of the string is 2.
    It can be shown that it is the minimum length that we can obtain.
    ```

    ```
    Input: s = "ACBBD"
    Output: 5
    Explanation: We cannot do any operations on the string so the length remains the same.
    ```

    ## Constraints

    - 1 <= s.length <= 100
    - s consists only of uppercase English letters.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def min_length(self, s: str) -> int:
            raise NotImplementedError('Implement min_length')

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
