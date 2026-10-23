import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_count_battleships, run_count_battleships
    from solution import Solution

    return Solution, assert_count_battleships, run_count_battleships


@app.cell
def _():
    # Example test case
    board = [["X", ".", ".", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]]
    expected = 2
    return board, expected


@app.cell
def _(Solution, board, run_count_battleships):
    result = run_count_battleships(Solution, board)
    result
    return (result,)


@app.cell
def _(assert_count_battleships, expected, result):
    assert_count_battleships(result, expected)
    return


if __name__ == "__main__":
    app.run()
