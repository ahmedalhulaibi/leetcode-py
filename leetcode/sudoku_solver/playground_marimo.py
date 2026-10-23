import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_solve_sudoku, run_solve_sudoku
    from solution import Solution

    return Solution, assert_solve_sudoku, run_solve_sudoku


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
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    return (board,)


@app.cell
def _(Solution, board, run_solve_sudoku):
    result = run_solve_sudoku(Solution, board)
    result
    return (result,)


@app.cell
def _(assert_solve_sudoku, board, result):
    assert_solve_sudoku(result, board)
    return


if __name__ == "__main__":
    app.run()
