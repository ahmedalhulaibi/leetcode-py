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
    # 917. Reverse Only Letters

    **Easy** · Two Pointers, String

    Given a string `s`, reverse the string according to the following rules:

    - All the characters that are not English letters remain in the same position.
    - All the English letters (lowercase or uppercase) should be reversed.

    Return `s` *after reversing it*.

    ## Examples

    ```
    Input: s = "ab-cd"
    Output: "dc-ba"
    ```

    ```
    Input: s = "a-bC-dEf-ghIj"
    Output: "j-Ih-gfE-dCba"
    ```

    ```
    Input: s = "Test1ng-Leet=code-Q!"
    Output: "Qedo1ct-eeLg=ntse-T!"
    ```

    ## Constraints

    - 1 <= s.length <= 100
    - s consists of characters with ASCII values in the range [33, 122].
    - s does not contain '"' or '\\'.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def reverse_only_letters(self, s: str) -> str:
            raise NotImplementedError('Implement reverse_only_letters')

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
