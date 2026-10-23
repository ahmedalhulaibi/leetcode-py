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
    # 967. Numbers With Same Consecutive Differences

    **Medium** · Backtracking, Breadth-First Search

    Given two integers `n` and `k`, return an array of all the integers of length `n` where the difference between every two consecutive digits is `k`. You may return the answer in any order.

    Note that the integers should not have leading zeros. Integers as `02` and `043` are not allowed.

    ## Examples

    ```
    Input: n = 3, k = 7
    Output: [181,292,707,818,929]
    Explanation: Note that 070 is not a valid number, because it has leading zeroes.
    ```

    ```
    Input: n = 2, k = 1
    Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
    ```

    ## Constraints

    - `2 <= n <= 9`
    - `0 <= k <= 9`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def nums_same_consec_diff(self, n: int, k: int) -> list[int]:
            raise NotImplementedError('Implement nums_same_consec_diff')

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
