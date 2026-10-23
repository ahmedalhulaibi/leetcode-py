import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_snakes_and_ladders, run_snakes_and_ladders
    from solution import Solution

    return Solution, assert_snakes_and_ladders, run_snakes_and_ladders


@app.cell
def _():
    # Example test case
    board = [
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 35, -1, -1, 13, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 15, -1, -1, -1, -1],
    ]
    expected = 4
    return board, expected


@app.cell
def _(Solution, board, run_snakes_and_ladders):
    result = run_snakes_and_ladders(Solution, board)
    result
    return (result,)


@app.cell
def _(assert_snakes_and_ladders, expected, result):
    assert_snakes_and_ladders(result, expected)
    return


if __name__ == "__main__":
    app.run()
