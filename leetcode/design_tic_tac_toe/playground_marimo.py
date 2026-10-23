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
    # 348. Design Tic-Tac-Toe

    **Medium** · Design, Array, Hash Table, Matrix, Simulation

    Assume the following rules are for the tic-tac-toe game on an `n x n` board between two players:

    1. A move is guaranteed to be valid and is placed on an empty block.
    2. Once a winning condition is reached, no more moves are allowed.
    3. A player who succeeds in placing `n` of their marks in a horizontal, vertical, or diagonal row wins the game.

    Implement the `TicTacToe` class:

    - `TicTacToe(int n)` Initializes the object the size of the board `n`.
    - `int move(int row, int col, int player)` Indicates that the player with id `player` plays at the cell `(row, col)` of the board. The move is guaranteed to be a valid move, and the two players alternate in making moves. Return
        - `0` if there is **no winner** after the move,
        - `1` if **player 1** is the winner after the move, or
        - `2` if **player 2** is the winner after the move.

    ## Examples

    ```
    Input
    ["TicTacToe", "move", "move", "move", "move", "move", "move", "move"]
    [[3], [0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1, 1]]
    Output
    [null, 0, 0, 0, 0, 0, 0, 1]

    Explanation
    TicTacToe ticTacToe = new TicTacToe(3);
    Assume that player 1 is "X" and player 2 is "O" in the board.
    ticTacToe.move(0, 0, 1); // return 0 (no one wins)
    |X| | |
    | | | |    // Player 1 makes a move at (0, 0).
    | | | |

    ticTacToe.move(0, 2, 2); // return 0 (no one wins)
    |X| |O|
    | | | |    // Player 2 makes a move at (0, 2).
    | | | |

    ticTacToe.move(2, 2, 1); // return 0 (no one wins)
    |X| |O|
    | | | |    // Player 1 makes a move at (2, 2).
    | | |X|

    ticTacToe.move(1, 1, 2); // return 0 (no one wins)
    |X| |O|
    | |O| |    // Player 2 makes a move at (1, 1).
    | | |X|

    ticTacToe.move(2, 0, 1); // return 0 (no one wins)
    |X| |O|
    | |O| |    // Player 1 makes a move at (2, 0).
    |X| |X|

    ticTacToe.move(1, 0, 2); // return 0 (no one wins)
    |X| |O|
    |O|O| |    // Player 2 makes a move at (1, 0).
    |X| |X|

    ticTacToe.move(2, 1, 1); // return 1 (player 1 wins)
    |X| |O|
    |O|O| |    // Player 1 makes a move at (2, 1).
    |X|X|X|
    ```

    ## Constraints

    - `2 <= n <= 100`
    - `player` is `1` or `2`.
    - `0 <= row, col < n`
    - `(row, col)` are **unique** for each different call to `move`.
    - At most `n^2` calls will be made to `move`.

    **Follow-up:** Could you do better than `O(n^2)` per `move()` operation?

    ## Your solution

    Implement the unfinished methods below, then press **Run tests**.
    """)
    return


@app.cell
def _():
    class TicTacToe:

        def __init__(self, n: int) -> None:
            raise NotImplementedError('Implement __init__')

        def move(self, row: int, col: int, player: int) -> int:
            raise NotImplementedError('Implement move')

    practice_exports = {'TicTacToe': TicTacToe}
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
