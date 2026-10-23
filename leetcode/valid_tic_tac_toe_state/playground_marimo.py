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
    # 794. Valid Tic-Tac-Toe State

    **Medium** · Array, Matrix

    Given a Tic-Tac-Toe board as a string array `board`, return `true` if and only if it is possible to reach this board position during the course of a valid tic-tac-toe game.

    The board is a `3 x 3` array that consists of characters `' '`, `'X'`, and `'O'`. The `' '` character represents an empty square.

    Here are the rules of Tic-Tac-Toe:

    - Players take turns placing characters into empty squares `' '`.
    - The first player always places `'X'` characters, while the second player always places `'O'` characters.
    - `'X'` and `'O'` characters are always placed into empty squares, never filled ones.
    - The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
    - The game also ends if all squares are non-empty.
    - No more moves can be played if the game is over.

    ## Examples

    ![Example 1](https://assets.leetcode.com/uploads/2021/05/15/tictactoe1-grid.jpg)

    ```
    Input: board = ["O  ","   ","   "]
    Output: false
    Explanation: The first player always plays "X".
    ```

    ![Example 2](https://assets.leetcode.com/uploads/2021/05/15/tictactoe2-grid.jpg)

    ```
    Input: board = ["XOX"," X ","   "]
    Output: false
    Explanation: Players take turns making moves.
    ```

    ![Example 3](https://assets.leetcode.com/uploads/2021/05/15/tictactoe4-grid.jpg)

    ```
    Input: board = ["XOX","O O","XOX"]
    Output: true
    ```

    ## Constraints

    - board.length == 3
    - board[i].length == 3
    - `board[i][j]` is either `'X'`, `'O'`, or `' '`.



    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class Solution:

        def valid_tic_tac_toe(self, board: list[str]) -> bool:
            raise NotImplementedError('Implement valid_tic_tac_toe')

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
