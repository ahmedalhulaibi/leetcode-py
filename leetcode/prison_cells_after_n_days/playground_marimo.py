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
    # 957. Prison Cells After N Days

    **Medium** · Array, Hash Table, Math, Bit Manipulation

    There are `8` prison cells in a row and each cell is either occupied or vacant.

    Each day, whether the cell is occupied or vacant changes according to the following rules:

    - If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
    - Otherwise, it becomes vacant.

    Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.

    You are given an integer array `cells` where `cells[i] == 1` if the `ith` cell is occupied and `cells[i] == 0` if the `ith` cell is vacant, and you are given an integer `n`.

    Return the state of the prison after `n` days (i.e., `n` such changes described above).

    ## Examples

    ```
    Input: cells = [0,1,0,1,1,0,0,1], n = 7
    Output: [0,0,1,1,0,0,0,0]
    Explanation: The following table summarizes the state of the prison on each day:
    Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
    Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
    Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
    Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
    Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
    Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
    Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
    Day 7: [0, 0, 1, 1, 0, 0, 0, 0]
    ```

    ```
    Input: cells = [1,0,0,1,0,0,1,0], n = 1000000000
    Output: [0,0,1,1,1,1,1,0]
    ```

    ## Constraints

    - cells.length == 8
    - cells[i] is either 0 or 1.
    - 1 <= n <= 10^9

    **Follow up:** Could you solve it with `O(1)` extra space with respect to the number of days?

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def prison_after_n_days(self, cells: list[int], n: int) -> list[int]:
            raise NotImplementedError('Implement prison_after_n_days')

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
