import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_game_of_life, run_game_of_life
    from solution import Solution

    return Solution, assert_game_of_life, run_game_of_life


@app.cell
def _():
    # Example test case
    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    expected = [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]
    return board, expected


@app.cell
def _(Solution, board, run_game_of_life):
    result = run_game_of_life(Solution, board)
    result
    return (result,)


@app.cell
def _(assert_game_of_life, expected, result):
    assert_game_of_life(result, expected)
    return


if __name__ == "__main__":
    app.run()
