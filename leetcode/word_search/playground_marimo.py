import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_exist, run_exist
    from solution import Solution

    return Solution, assert_exist, run_exist


@app.cell
def _():
    # Example test case
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    expected = True
    return board, expected, word


@app.cell
def _(Solution, board, run_exist, word):
    result = run_exist(Solution, board, word)
    result
    return (result,)


@app.cell
def _(assert_exist, expected, result):
    assert_exist(result, expected)
    return


if __name__ == "__main__":
    app.run()
