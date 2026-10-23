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
    # 926. Flip String to Monotone Increasing

    **Medium** · String, Dynamic Programming, Greedy

    <p>A binary string is monotone increasing if it consists of some number of <code>0</code>&#39;s (possibly none), followed by some number of <code>1</code>&#39;s (also possibly none).</p>

    <p>You are given a binary string <code>s</code>. You can flip <code>s[i]</code> changing it from <code>0</code> to <code>1</code> or from <code>1</code> to <code>0</code>.</p>

    <p>Return <em>the minimum number of flips to make </em><code>s</code><em> monotone increasing</em>.</p>

    ## Examples

    ```
    Input: s = "00110"
    Output: 1
    Explanation: We flip the last digit to get 00111.
    ```

    ```
    Input: s = "010110"
    Output: 2
    Explanation: We flip to get 011111, or alternatively 000111.
    ```

    ```
    Input: s = "00011000"
    Output: 2
    Explanation: We flip to get 00000000.
    ```

    ## Constraints

    - 1 &lt;= s.length &lt;= 10^5
    - s[i] is either &#39;0&#39; or &#39;1&#39;.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def min_flips_mono_increasing(self, s: str) -> int:
            raise NotImplementedError('Implement min_flips_mono_increasing')

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
