import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_solve, run_solve
    from solution import Solution

    return Solution, assert_solve, run_solve


@app.cell
def _():
    # Example test case
    board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
    expected = [["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "O", "X", "X"]]
    return board, expected


@app.cell
def _(Solution, board, run_solve):
    result = run_solve(Solution, board)
    result
    return (result,)


@app.cell
def _(assert_solve, expected, result):
    assert_solve(result, expected)
    return


if __name__ == "__main__":
    app.run()
