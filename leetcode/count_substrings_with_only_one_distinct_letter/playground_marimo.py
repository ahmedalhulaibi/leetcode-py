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
    # 1180. Count Substrings with Only One Distinct Letter

    **Easy** · Math, String

    Given a string `s`, return *the number of substrings that have only **one distinct** letter*.

    ## Examples

    ```
    Input: s = "aaaba"
    Output: 8
    Explanation: The substrings with one distinct letter are "aaa", "aa", "a", "b".
    "aaa" occurs 1 time.
    "aa" occurs 2 times.
    "a" occurs 4 times.
    "b" occurs 1 time.
    So the answer is 1 + 2 + 4 + 1 = 8.
    ```

    ```
    Input: s = "aaaaaaaaaa"
    Output: 55
    ```

    ## Constraints

    - 1 <= s.length <= 1000
    - `s` consists of only lowercase English letters.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def count_letters(self, s: str) -> int:
            raise NotImplementedError('Implement count_letters')

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
