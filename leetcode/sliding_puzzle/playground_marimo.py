import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_sliding_puzzle, run_sliding_puzzle
    from solution import Solution

    return Solution, assert_sliding_puzzle, run_sliding_puzzle


@app.cell
def _():
    # Example test case
    board = [[1, 2, 3], [4, 0, 5]]
    expected = 1
    return board, expected


@app.cell
def _(Solution, board, run_sliding_puzzle):
    result = run_sliding_puzzle(Solution, board)
    result
    return (result,)


@app.cell
def _(assert_sliding_puzzle, expected, result):
    assert_sliding_puzzle(result, expected)
    return


if __name__ == "__main__":
    app.run()
