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
    # 1215. Stepping Numbers

    **Medium** · Breadth-First Search, Math, Backtracking

    A **stepping number** is an integer such that all of its adjacent digits have an absolute difference of exactly `1`.

    - For example, `321` is a **stepping number** while `421` is not.

    Given two integers `low` and `high`, return *a sorted list of all the **stepping numbers** in the inclusive range* `[low, high]`.

    ## Examples

    ```
    Input: low = 0, high = 21
    Output: [0,1,2,3,4,5,6,7,8,9,10,12,21]
    ```

    ```
    Input: low = 10, high = 15
    Output: [10,12]
    ```

    ## Constraints

    - `0 <= low <= high <= 2 * 10^9`



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def count_stepping_numbers(self, low: int, high: int) -> list[int]:
            raise NotImplementedError('Implement count_stepping_numbers')

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
