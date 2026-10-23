import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_moves_to_chessboard, run_moves_to_chessboard
    from solution import Solution

    return Solution, assert_moves_to_chessboard, run_moves_to_chessboard


@app.cell
def _():
    # Example test case
    board = [[0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1]]
    expected = 2
    return board, expected


@app.cell
def _(Solution, board, run_moves_to_chessboard):
    result = run_moves_to_chessboard(Solution, board)
    result
    return (result,)


@app.cell
def _(assert_moves_to_chessboard, expected, result):
    assert_moves_to_chessboard(result, expected)
    return


if __name__ == "__main__":
    app.run()
