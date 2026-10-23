import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_island_perimeter, run_island_perimeter
    from solution import Solution

    return Solution, assert_island_perimeter, run_island_perimeter


@app.cell
def _():
    # Example test case
    grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
    expected = 16
    return expected, grid


@app.cell
def _(Solution, grid, run_island_perimeter):
    result = run_island_perimeter(Solution, grid)
    result
    return (result,)


@app.cell
def _(assert_island_perimeter, expected, result):
    assert_island_perimeter(result, expected)
    return


if __name__ == "__main__":
    app.run()
