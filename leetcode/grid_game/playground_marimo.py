import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_grid_game, run_grid_game
    from solution import Solution

    return Solution, assert_grid_game, run_grid_game


@app.cell
def _():
    # Example test case
    grid = [[2, 5, 4], [1, 5, 1]]
    expected = 4
    return expected, grid


@app.cell
def _(Solution, grid, run_grid_game):
    result = run_grid_game(Solution, grid)
    result
    return (result,)


@app.cell
def _(assert_grid_game, expected, result):
    assert_grid_game(result, expected)
    return


if __name__ == "__main__":
    app.run()
