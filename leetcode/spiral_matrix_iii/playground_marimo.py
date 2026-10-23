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
    # 885. Spiral Matrix III

    **Medium** · Array, Matrix, Simulation

    You start at the cell <code>(rStart, cStart)</code> of an <code>rows x cols</code> grid facing east. The northwest corner is at the first row and column in the grid, and the southeast corner is at the last row and column.</p>

    <p>You will walk in a clockwise spiral shape to visit every position in this grid. Whenever you move outside the grid's boundary, we continue our walk outside the grid (but may return to the grid boundary later.). Eventually, we reach all <code>rows * cols</code> spaces of the grid.</p>

    <p>Return an array of coordinates representing the positions of the grid in the order you visited them.</p>

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2018/08/24/example_1.png)

    ```
    Input: rows = 5, cols = 6, rStart = 1, cStart = 4
    Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2018/08/24/example_2.png)

    ```
    Input: rows = 1, cols = 4, rStart = 0, cStart = 0
    Output: [[0,0],[0,1],[0,2],[0,3]]
    ```

    ## Constraints

    - 1 <= rows, cols <= 100
    - 0 <= rStart < rows
    - 0 <= cStart < cols



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def spiral_matrix_iii(self, rows: int, cols: int, r_start: int, c_start: int) -> list[list[int]]:
            raise NotImplementedError('Implement spiral_matrix_iii')

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
