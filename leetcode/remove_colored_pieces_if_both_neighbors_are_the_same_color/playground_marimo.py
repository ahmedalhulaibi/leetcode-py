import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_winner_of_game, run_winner_of_game
    from solution import Solution

    return Solution, assert_winner_of_game, run_winner_of_game


@app.cell
def _():
    # Example test case
    colors = "AAABABB"
    expected = True
    return colors, expected


@app.cell
def _(Solution, colors, run_winner_of_game):
    result = run_winner_of_game(Solution, colors)
    result
    return (result,)


@app.cell
def _(assert_winner_of_game, expected, result):
    assert_winner_of_game(result, expected)
    return


if __name__ == "__main__":
    app.run()
