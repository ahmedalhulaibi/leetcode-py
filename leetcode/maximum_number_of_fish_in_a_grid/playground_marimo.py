import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_max_fish, run_find_max_fish
    from solution import Solution

    return Solution, assert_find_max_fish, run_find_max_fish


@app.cell
def _():
    # Example test case
    grid = [[0, 2, 1, 0], [4, 0, 0, 3], [1, 0, 0, 4], [0, 3, 2, 0]]
    expected = 7
    return expected, grid


@app.cell
def _(Solution, grid, run_find_max_fish):
    result = run_find_max_fish(Solution, grid)
    result
    return (result,)


@app.cell
def _(assert_find_max_fish, expected, result):
    assert_find_max_fish(result, expected)
    return


if __name__ == "__main__":
    app.run()
