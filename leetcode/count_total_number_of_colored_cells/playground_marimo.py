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
    # 2579. Count Total Number of Colored Cells

    **Medium** · Math

    There exists an infinitely large two-dimensional grid of uncolored unit cells. You are given a positive integer `n`, indicating that you must do the following routine for `n` minutes:

    - At the first minute, color **any** arbitrary unit cell blue.
    - Every minute thereafter, color blue **every** uncolored cell that touches a blue cell.

    Return *the number of **colored cells** at the end of* `n` *minutes*.

    ## Examples

    ![Example](https://assets.leetcode.com/uploads/2023/01/10/example-copy-2.png)

    ```
    Input: n = 1
    Output: 1
    Explanation: After 1 minute, there is only 1 blue cell, so we return 1.
    ```

    ```
    Input: n = 2
    Output: 5
    Explanation: After 2 minutes, there are 4 colored cells on the boundary and 1 in the center, so we return 5.
    ```

    ## Constraints

    - 1 <= n <= 10^5



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def colored_cells(self, n: int) -> int:
            raise NotImplementedError('Implement colored_cells')

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
