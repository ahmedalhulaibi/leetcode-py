import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_min_knight_moves, run_min_knight_moves
    from solution import Solution

    return Solution, assert_min_knight_moves, run_min_knight_moves


@app.cell
def _():
    # Example test case
    x = 2
    y = 1
    expected = 1
    return expected, x, y


@app.cell
def _(Solution, run_min_knight_moves, x, y):
    result = run_min_knight_moves(Solution, x, y)
    result
    return (result,)


@app.cell
def _(assert_min_knight_moves, expected, result):
    assert_min_knight_moves(result, expected)
    return


if __name__ == "__main__":
    app.run()
