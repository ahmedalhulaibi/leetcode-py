import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_num_rook_captures, run_num_rook_captures
    from solution import Solution

    return Solution, assert_num_rook_captures, run_num_rook_captures


@app.cell
def _():
    # Example test case
    board = [
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", "p", ".", ".", ".", "."],
        [".", ".", ".", "R", ".", ".", ".", "p"],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", "p", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
    ]
    expected = 3
    return board, expected


@app.cell
def _(Solution, board, run_num_rook_captures):
    result = run_num_rook_captures(Solution, board)
    result
    return (result,)


@app.cell
def _(assert_num_rook_captures, expected, result):
    assert_num_rook_captures(result, expected)
    return


if __name__ == "__main__":
    app.run()
