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
    # 782. Transform to Chessboard

    **Hard** · Array, Math, Bit Manipulation, Matrix

    You are given an `n x n` binary grid `board`. In each move, you can swap any two rows with each other, or any two columns with each other.

    Return the minimum number of moves to transform the board into a chessboard board. If the task is impossible, return `-1`.

    A chessboard board is a board where no `0`'s and no `1`'s are 4-directionally adjacent.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2021/06/29/chessboard1-grid.jpg)

    ```
    Input: board = [[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]
    Output: 2
    Explanation: One potential sequence of moves is shown.
    The first move swaps the first and second column.
    The second move swaps the second and third row.
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2021/06/29/chessboard2-grid.jpg)

    ```
    Input: board = [[0,1],[1,0]]
    Output: 0
    Explanation: Also note that the board with 0 in the top left corner, is also a valid chessboard.
    ```

    ![Example 3](https://assets.leetcode.com/uploads/2021/06/29/chessboard3-grid.jpg)

    ```
    Input: board = [[1,0],[1,0]]
    Output: -1
    Explanation: No matter what sequence of moves you make, you cannot end with a valid chessboard.
    ```

    ## Constraints

    - n == board.length
    - n == board[i].length
    - 2 <= n <= 30
    - board[i][j] is either 0 or 1.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def moves_to_chessboard(self, board: list[list[int]]) -> int:
            raise NotImplementedError('Implement moves_to_chessboard')

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
