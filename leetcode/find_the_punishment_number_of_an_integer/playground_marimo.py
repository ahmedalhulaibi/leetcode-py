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
    # 2698. Find the Punishment Number of an Integer

    **Medium** · Math, Backtracking

    Given a positive integer `n`, return *the **punishment number*** of `n`.

    The **punishment number** of `n` is defined as the sum of the squares of all integers `i` such that:

    - `1 <= i <= n`
    - The decimal representation of `i * i` can be partitioned into contiguous substrings such that the sum of the integer values of these substrings equals `i`.

    ## Examples

    ```
    Input: n = 10
    Output: 182
    Explanation: There are exactly 3 integers i in the range [1, 10] that satisfy the conditions in the statement:
    - 1 since 1 * 1 = 1
    - 9 since 9 * 9 = 81 and 81 can be partitioned into 8 and 1 with a sum equal to 8 + 1 == 9.
    - 10 since 10 * 10 = 100 and 100 can be partitioned into 10 and 0 with a sum equal to 10 + 0 == 10.
    Hence, the punishment number of 10 is 1 + 81 + 100 = 182
    ```

    ```
    Input: n = 37
    Output: 1478
    Explanation: There are exactly 4 integers i in the range [1, 37] that satisfy the conditions in the statement:
    - 1 since 1 * 1 = 1.
    - 9 since 9 * 9 = 81 and 81 can be partitioned into 8 + 1.
    - 10 since 10 * 10 = 100 and 100 can be partitioned into 10 + 0.
    - 36 since 36 * 36 = 1296 and 1296 can be partitioned into 1 + 29 + 6.
    Hence, the punishment number of 37 is 1 + 81 + 100 + 1296 = 1478
    ```

    ## Constraints

    - 1 <= n <= 1000



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def punishment_number(self, n: int) -> int:
            raise NotImplementedError('Implement punishment_number')

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
