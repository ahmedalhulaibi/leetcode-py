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
    # 161. One Edit Distance

    **Medium** · Two Pointers, String

    Given two strings `s` and `t`, return `true` if they are both one edit distance apart, otherwise return `false`.

    A string `s` is said to be one distance apart from a string `t` if you can:

    - Insert exactly one character into `s` to get `t`.
    - Delete exactly one character from `s` to get `t`.
    - Replace exactly one character of `s` to get `t`.

    ## Examples

    ```
    Input: s = "ab", t = "acb"
    Output: true
    Explanation: We can insert 'c' into s to get t.
    ```

    ```
    Input: s = "cab", t = "ad"
    Output: false
    Explanation: We cannot get t from s by only one step.
    ```

    ```
    Input: s = "1203", t = "1213"
    Output: true
    Explanation: We can replace '0' with '1' to get t.
    ```

    ## Constraints

    - 0 <= s.length, t.length <= 10^4
    - s and t consist of lowercase letters, uppercase letters, and digits



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def is_one_edit_distance(self, s: str, t: str) -> bool:
            raise NotImplementedError('Implement is_one_edit_distance')

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
