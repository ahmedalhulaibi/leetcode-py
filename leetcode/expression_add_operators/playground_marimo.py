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
    # 282. Expression Add Operators

    **Hard** · Math, String, Backtracking

    Given a string `num` that contains only digits and an integer `target`, return **all possibilities** to insert the binary operators `'+'`, `'-'`, and/or `'*'` between the digits of `num` so that the resultant expression evaluates to the `target` value.

    Note that operands in the returned expressions **should not** contain leading zeros.

    Note that a number can contain multiple digits.

    ## Examples

    ```
    Input: num = "123", target = 6
    Output: ["1*2*3","1+2+3"]
    ```
    **Explanation:** Both `"1*2*3"` and `"1+2+3"` evaluate to 6.

    ```
    Input: num = "232", target = 8
    Output: ["2*3+2","2+3*2"]
    ```
    **Explanation:** Both `"2*3+2"` and `"2+3*2"` evaluate to 8.

    ```
    Input: num = "3456237490", target = 9191
    Output: []
    ```
    **Explanation:** There are no expressions that can be created from `"3456237490"` to evaluate to 9191.

    ## Constraints

    - `1 <= num.length <= 10`
    - `num` consists of only digits.
    - `-2^31 <= target <= 2^31 - 1`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def add_operators(self, num: str, target: int) -> list[str]:
            raise NotImplementedError('Implement add_operators')

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
