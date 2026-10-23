import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_candy_crush, run_candy_crush
    from solution import Solution

    return Solution, assert_candy_crush, run_candy_crush


@app.cell
def _():
    # Example test case
    board = [[1, 3, 5, 5, 2], [3, 4, 3, 3, 1], [3, 2, 4, 5, 2], [2, 4, 4, 5, 5], [1, 4, 4, 1, 1]]
    expected = [[1, 3, 0, 0, 0], [3, 4, 0, 5, 2], [3, 2, 0, 3, 1], [2, 4, 0, 5, 2], [1, 4, 3, 1, 1]]
    return board, expected


@app.cell
def _(Solution, board, run_candy_crush):
    result = run_candy_crush(Solution, board)
    result
    return (result,)


@app.cell
def _(assert_candy_crush, expected, result):
    assert_candy_crush(result, expected)
    return


if __name__ == "__main__":
    app.run()
