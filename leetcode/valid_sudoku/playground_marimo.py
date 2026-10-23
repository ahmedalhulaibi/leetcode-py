import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_is_valid_sudoku, run_is_valid_sudoku
    from solution import Solution

    return Solution, assert_is_valid_sudoku, run_is_valid_sudoku


@app.cell
def _():
    # Example test case
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", ".", ".", ".", "7", "9"],
    ]
    expected = True
    return board, expected


@app.cell
def _(Solution, board, run_is_valid_sudoku):
    result = run_is_valid_sudoku(Solution, board)
    result
    return (result,)


@app.cell
def _(assert_is_valid_sudoku, expected, result):
    assert_is_valid_sudoku(result, expected)
    return


if __name__ == "__main__":
    app.run()
