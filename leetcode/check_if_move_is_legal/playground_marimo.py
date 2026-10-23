import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_check_move, run_check_move
    from solution import Solution

    return Solution, assert_check_move, run_check_move


@app.cell
def _():
    # Example test case
    board: list[list[str]] = [
        [".", ".", ".", "B", ".", ".", ".", "."],
        [".", ".", ".", "W", ".", ".", ".", "."],
        [".", ".", ".", "W", ".", ".", ".", "."],
        [".", ".", ".", "W", ".", ".", ".", "."],
        ["W", "B", "B", ".", "W", "W", "W", "B"],
        [".", ".", ".", "B", ".", ".", ".", "."],
        [".", ".", ".", "B", ".", ".", ".", "."],
        [".", ".", ".", "W", ".", ".", ".", "."],
    ]
    r_move = 4
    c_move = 3
    color = "B"
    expected = True
    return board, c_move, color, expected, r_move


@app.cell
def _(Solution, board: list[list[str]], c_move, color, r_move, run_check_move):
    result = run_check_move(Solution, board, r_move, c_move, color)
    result
    return (result,)


@app.cell
def _(assert_check_move, expected, result):
    assert_check_move(result, expected)
    return


if __name__ == "__main__":
    app.run()
