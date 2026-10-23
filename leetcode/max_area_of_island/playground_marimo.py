import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_max_area_of_island, run_max_area_of_island
    from solution import Solution

    return Solution, assert_max_area_of_island, run_max_area_of_island


@app.cell
def _():
    # Example test case
    grid = [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    ]
    expected = 6
    return expected, grid


@app.cell
def _(Solution, grid, run_max_area_of_island):
    result = run_max_area_of_island(Solution, grid)
    result
    return (result,)


@app.cell
def _(assert_max_area_of_island, expected, result):
    assert_max_area_of_island(result, expected)
    return


if __name__ == "__main__":
    app.run()
