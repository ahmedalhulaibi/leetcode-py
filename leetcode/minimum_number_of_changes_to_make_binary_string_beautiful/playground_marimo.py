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
    # 2914. Minimum Number of Changes to Make Binary String Beautiful

    **Medium** · String

    <p>You are given a <strong>0-indexed</strong> binary string <code>s</code> having an even length.</p>

    <p>A string is <strong>beautiful</strong> if it&#39;s possible to partition it into one or more substrings such that:</p>

    <ul>
        <li>Each substring has an <strong>even length</strong>.</li>
        <li>Each substring contains <strong>only</strong> <code>1</code>&#39;s or <strong>only</strong> <code>0</code>&#39;s.</li>
    </ul>

    <p>You can change any character in <code>s</code> to <code>0</code> or <code>1</code>.</p>

    <p>Return <em>the <strong>minimum</strong> number of changes required to make the string </em><code>s</code> <em>beautiful</em>.</p>

    ## Examples

    ```
    Input: s = "1001"
    Output: 2
    ```
    **Explanation:** We change s[1] to 1 and s[3] to 0 to get string "1100".
    It can be seen that the string "1100" is beautiful because we can partition it into "11|00".
    It can be proven that 2 is the minimum number of changes needed to make the string beautiful.

    ```
    Input: s = "10"
    Output: 1
    ```
    **Explanation:** We change s[1] to 1 to get string "11".
    It can be seen that the string "11" is beautiful because we can partition it into "11".
    It can be proven that 1 is the minimum number of changes needed to make the string beautiful.

    ```
    Input: s = "0000"
    Output: 0
    ```
    **Explanation:** We don&#39;t need to make any changes as the string "0000" is beautiful already.

    ## Constraints

    - `2 <= s.length <= 10^5`
    - `s` has an even length.
    - `s[i]` is either `'0'` or `'1'`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def min_changes(self, s: str) -> int:
            raise NotImplementedError('Implement min_changes')

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
