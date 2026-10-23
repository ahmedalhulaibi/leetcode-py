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
    # 419. Battleships in a Board

    **Medium** · Array, Depth-First Search, Matrix

    Given an `m x n` matrix `board` where each cell is a battleship `'X'` or empty `'.'`, return the number of the battleships on `board`.

    Battleships can only be placed horizontally or vertically on `board`. In other words, they can only be made of the shape `1 x k` (`1` row, `k` columns) or `k x 1` (`k` rows, `1` column), where `k` can be of any size. At least one horizontal or vertical cell separates between two battleships (i.e., there are no adjacent battleships).

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2024/06/21/image.png)

    ```
    Input: board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
    Output: 2
    ```

    ```
    Input: board = [["."]]
    Output: 0
    ```

    ## Constraints

    - m == board.length
    - n == board[i].length
    - 1 <= m, n <= 200
    - board[i][j] is either '.' or 'X'.

    Follow up: Could you do it in one-pass, using only O(1) extra memory and without modifying the values of board?



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def count_battleships(self, board: list[list[str]]) -> int:
            raise NotImplementedError('Implement count_battleships')

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
