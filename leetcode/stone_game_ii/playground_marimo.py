import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_stone_game_ii, run_stone_game_ii
    from solution import Solution

    return Solution, assert_stone_game_ii, run_stone_game_ii


@app.cell
def _():
    # Example test case
    piles = [2, 7, 9, 4, 4]
    expected = 10
    return expected, piles


@app.cell
def _(Solution, piles, run_stone_game_ii):
    result = run_stone_game_ii(Solution, piles)
    result
    return (result,)


@app.cell
def _(assert_stone_game_ii, expected, result):
    assert_stone_game_ii(result, expected)
    return


if __name__ == "__main__":
    app.run()
