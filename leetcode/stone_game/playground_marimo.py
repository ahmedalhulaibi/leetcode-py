import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_stone_game, run_stone_game
    from solution import Solution

    return Solution, assert_stone_game, run_stone_game


@app.cell
def _():
    # Example test case
    piles = [5, 3, 4, 5]
    expected = True
    return expected, piles


@app.cell
def _(Solution, piles, run_stone_game):
    result = run_stone_game(Solution, piles)
    result
    return (result,)


@app.cell
def _(assert_stone_game, expected, result):
    assert_stone_game(result, expected)
    return


if __name__ == "__main__":
    app.run()
