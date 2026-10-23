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
    # 964. Least Operators to Express Number

    **Hard** · Math, Dynamic Programming, Memoization

    Given a single positive integer `x`, we will write an expression of the form `x (op1) x (op2) x (op3) x ...` where each operator `op1`, `op2`, etc. is either addition, subtraction, multiplication, or division (`+`, `-`, `*`, or `/`). For example, with `x = 3`, we might write `3 * 3 / 3 + 3 - 3` which is a value of `3`.

    When writing such an expression, we adhere to the following conventions:

    - The division operator (`/`) returns rational numbers.
    - There are no parentheses placed anywhere.
    - We use the usual order of operations: multiplication and division happen before addition and subtraction.
    - It is not allowed to use the unary negation operator (`-`). For example, `x - x` is a valid expression as it only uses subtraction, but `-x + x` is not because it uses negation.

    We would like to write an expression with the least number of operators such that the expression equals the given `target`. Return the least number of operators used.

    ## Examples

    ```
    Input: x = 3, target = 19
    Output: 5
    Explanation: 3 * 3 + 3 * 3 + 3 / 3.
    The expression contains 5 operations.
    ```

    ```
    Input: x = 5, target = 501
    Output: 8
    Explanation: 5 * 5 * 5 * 5 - 5 * 5 * 5 + 5 / 5.
    The expression contains 8 operations.
    ```

    ```
    Input: x = 100, target = 100000000
    Output: 3
    Explanation: 100 * 100 * 100 * 100.
    The expression contains 3 operations.
    ```

    ## Constraints

    - `2 <= x <= 100`
    - `1 <= target <= 2 * 10^8`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def least_ops_express_target(self, x: int, target: int) -> int:
            raise NotImplementedError('Implement least_ops_express_target')

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
