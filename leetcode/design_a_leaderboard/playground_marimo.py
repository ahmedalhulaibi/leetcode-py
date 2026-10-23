import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_leaderboard, run_leaderboard
    from solution import Leaderboard

    return Leaderboard, assert_leaderboard, run_leaderboard


@app.cell
def _():
    # Example test case
    operations = [
        "Leaderboard",
        "add_score",
        "add_score",
        "add_score",
        "add_score",
        "add_score",
        "top",
        "reset",
        "reset",
        "add_score",
        "top",
    ]
    inputs = [[], [1, 73], [2, 56], [3, 39], [4, 51], [5, 4], [1], [1], [2], [2, 51], [3]]
    expected = [None, None, None, None, None, None, 73, None, None, None, 141]
    return expected, inputs, operations


@app.cell
def _(Leaderboard, inputs, operations, run_leaderboard):
    result, board = run_leaderboard(Leaderboard, operations, inputs)
    print(result)
    board
    return (result,)


@app.cell
def _(assert_leaderboard, expected, result):
    assert_leaderboard(result, expected)
    return


if __name__ == "__main__":
    app.run()
