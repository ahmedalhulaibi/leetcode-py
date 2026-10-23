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
    # 3174. Clear Digits

    **Easy** · String, Stack, Simulation

    You are given a string `s`.

    Your task is to remove **all** digits by doing this operation repeatedly:

    - Delete the *first* digit and the **closest** non-digit character to its *left*.

    Return the resulting string after removing all digits.

    **Note** that the operation *cannot* be performed on a digit that does not have any non-digit character to its left.

    ## Examples

    ```
    Input: s = "abc"
    Output: "abc"
    Explanation: There is no digit in the string.
    ```

    ```
    Input: s = "cb34"
    Output: "\"
    Explanation: First, we apply the operation on s[2], and s becomes "c4".
    Then we apply the operation on s[1], and s becomes "\".
    ```

    ## Constraints

    - `1 <= s.length <= 100`
    - `s` consists only of lowercase English letters and digits.
    - The input is generated such that it is possible to delete all digits.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def clear_digits(self, s: str) -> str:
            raise NotImplementedError('Implement clear_digits')

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
