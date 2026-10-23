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
    # 172. Factorial Trailing Zeroes

    **Medium** · Math

    Given an integer <code>n</code>, return <em>the number of trailing zeroes in </em><code>n!</code>.

    <p>Note that <code>n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1</code>.</p>

    ## Examples

    ```
    Input: n = 3
    Output: 0
    Explanation: 3! = 6, no trailing zero.
    ```

    ```
    Input: n = 5
    Output: 1
    Explanation: 5! = 120, one trailing zero.
    ```

    ```
    Input: n = 0
    Output: 0
    ```

    ## Constraints

    - 0 <= n <= 10^4

    <p><strong>Follow up:</strong> Could you write a solution that works in logarithmic time complexity?</p>



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def trailing_zeroes(self, n: int) -> int:
            raise NotImplementedError('Implement trailing_zeroes')

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
