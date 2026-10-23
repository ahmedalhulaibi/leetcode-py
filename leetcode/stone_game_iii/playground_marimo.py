import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_stone_game_iii, run_stone_game_iii
    from solution import Solution

    return Solution, assert_stone_game_iii, run_stone_game_iii


@app.cell
def _():
    # Example test case
    stone_value = [1, 2, 3, 7]
    expected = "Bob"
    return expected, stone_value


@app.cell
def _(Solution, run_stone_game_iii, stone_value):
    result = run_stone_game_iii(Solution, stone_value)
    result
    return (result,)


@app.cell
def _(assert_stone_game_iii, expected, result):
    assert_stone_game_iii(result, expected)
    return


if __name__ == "__main__":
    app.run()
