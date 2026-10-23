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
    # 840. Magic Squares In Grid

    **Medium** · Array, Hash Table, Math, Matrix

    A `3 x 3` magic square is a `3 x 3` grid filled with **distinct** numbers **from** `1` **to** `9` such that each row, column, and both diagonals all have the same sum.

    Given a `row x col` `grid` of integers, how many `3 x 3` magic square subgrids are there?

    **Note:** while a magic square can only contain numbers from `1` to `9`, `grid` may contain numbers up to `15`.

    ## Examples

    ```
    Input: grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
    Output: 1
    Explanation:
    The following subgrid is a 3 x 3 magic square:

    while this one is not:

    In total, there is only one magic square inside the given grid.
    ```

    ```
    Input: grid = [[8]]
    Output: 0
    ```

    ## Constraints

    - row == grid.length
    - col == grid[i].length
    - 1 <= row, col <= 10
    - 0 <= grid[i][j] <= 15



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def num_magic_squares_inside(self, grid: list[list[int]]) -> int:
            raise NotImplementedError('Implement num_magic_squares_inside')

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
