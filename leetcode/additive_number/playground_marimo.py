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
    # 306. Additive Number

    **Medium** · String, Backtracking

    An <strong>additive number</strong> is a string whose digits can form an <strong>additive sequence</strong>.

    <p>A valid <strong>additive sequence</strong> should contain <strong>at least</strong> three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.</p>

    <p>Given a string containing only digits, return <code>true</code> if it is an <strong>additive number</strong> or <code>false</code> otherwise.</p>

    ## Examples

    ```
    Input: "112358"
    Output: true
    Explanation: The digits can form an additive sequence: 1, 1, 2, 3, 5, 8.
    1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
    ```

    ```
    Input: "199100199"
    Output: true
    Explanation: The additive sequence is: 1, 99, 100, 199.
    1 + 99 = 100, 99 + 100 = 199
    ```

    ```
    Input: "1023"
    Output: false
    Explanation: No valid additive sequence exists.
    ```

    ## Constraints

    - `1 <= num.length <= 35`
    - `num` consists only of digits.


    <p><strong>Note:</strong> Numbers in the additive sequence <strong>cannot</strong> have leading zeros, so sequence <code>1, 2, 03</code> or <code>1, 02, 3</code> is invalid.</p>

    **Follow up:** How would you handle overflow for very large input integers?

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def is_additive_number(self, num: str) -> bool:
            raise NotImplementedError('Implement is_additive_number')

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
