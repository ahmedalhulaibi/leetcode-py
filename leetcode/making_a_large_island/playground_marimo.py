import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_largest_island, run_largest_island
    from solution import Solution

    return Solution, assert_largest_island, run_largest_island


@app.cell
def _():
    # Example test case
    grid = [[1, 0], [0, 1]]
    expected = 3
    return expected, grid


@app.cell
def _(Solution, grid, run_largest_island):
    result = run_largest_island(Solution, grid)
    result
    return (result,)


@app.cell
def _(assert_largest_island, expected, result):
    assert_largest_island(result, expected)
    return


if __name__ == "__main__":
    app.run()
