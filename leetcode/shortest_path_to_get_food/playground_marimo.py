import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_get_food, run_get_food
    from solution import Solution

    return Solution, assert_get_food, run_get_food


@app.cell
def _():
    # Example test case
    grid = [
        ["X", "X", "X", "X", "X", "X"],
        ["X", "*", "O", "O", "O", "X"],
        ["X", "O", "O", "#", "O", "X"],
        ["X", "X", "X", "X", "X", "X"],
    ]
    expected = 3
    return expected, grid


@app.cell
def _(Solution, grid, run_get_food):
    result = run_get_food(Solution, grid)
    result
    return (result,)


@app.cell
def _(assert_get_food, expected, result):
    assert_get_food(result, expected)
    return


if __name__ == "__main__":
    app.run()
