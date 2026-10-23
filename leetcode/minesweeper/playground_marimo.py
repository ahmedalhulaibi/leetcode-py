import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_update_board, run_update_board
    from solution import Solution

    return Solution, assert_update_board, run_update_board


@app.cell
def _():
    # Example test case
    board = [
        ["E", "E", "E", "E", "E"],
        ["E", "E", "M", "E", "E"],
        ["E", "E", "E", "E", "E"],
        ["E", "E", "E", "E", "E"],
    ]
    click = [3, 0]
    expected = [
        ["B", "1", "E", "1", "B"],
        ["B", "1", "M", "1", "B"],
        ["B", "1", "1", "1", "B"],
        ["B", "B", "B", "B", "B"],
    ]
    return board, click, expected


@app.cell
def _(Solution, board, click, run_update_board):
    result = run_update_board(Solution, board, click)
    result
    return (result,)


@app.cell
def _(assert_update_board, expected, result):
    assert_update_board(result, expected)
    return


if __name__ == "__main__":
    app.run()
