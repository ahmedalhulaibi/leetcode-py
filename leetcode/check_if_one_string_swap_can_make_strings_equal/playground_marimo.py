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
    # 1790. Check if One String Swap Can Make Strings Equal

    **Easy** · Hash Table, String, Counting

    You are given two strings `s1` and `s2` of equal length. A **string swap** is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

    Return `true` if it is possible to make both strings equal by performing **at most one string swap** on **exactly one** of the strings. Otherwise, return `false`.

    ## Examples

    ```
    Input: s1 = "bank", s2 = "kanb"
    Output: true
    Explanation: For example, swap the first character with the last character of s2 to make "bank".
    ```

    ```
    Input: s1 = "attack", s2 = "defend"
    Output: false
    Explanation: It is impossible to make them equal with one string swap.
    ```

    ```
    Input: s1 = "kelb", s2 = "kelb"
    Output: true
    Explanation: The two strings are already equal, so no string swap operation is required.
    ```

    ## Constraints

    - 1 <= s1.length, s2.length <= 100
    - s1.length == s2.length
    - s1 and s2 consist of only lowercase English letters.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def are_almost_equal(self, s1: str, s2: str) -> bool:
            raise NotImplementedError('Implement are_almost_equal')

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
