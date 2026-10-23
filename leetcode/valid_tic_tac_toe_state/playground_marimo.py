import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_valid_tic_tac_toe, run_valid_tic_tac_toe
    from solution import Solution

    return Solution, assert_valid_tic_tac_toe, run_valid_tic_tac_toe


@app.cell
def _():
    # Example test case
    board = ["XOX", "O O", "XOX"]
    expected = True
    return board, expected


@app.cell
def _(Solution, board, run_valid_tic_tac_toe):
    result = run_valid_tic_tac_toe(Solution, board)
    result
    return (result,)


@app.cell
def _(assert_valid_tic_tac_toe, expected, result):
    assert_valid_tic_tac_toe(result, expected)
    return


if __name__ == "__main__":
    app.run()
