import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_surface_area, run_surface_area
    from solution import Solution

    return Solution, assert_surface_area, run_surface_area


@app.cell
def _():
    # Example test case
    grid = [[1, 2], [3, 4]]
    expected = 34
    return expected, grid


@app.cell
def _(Solution, grid, run_surface_area):
    result = run_surface_area(Solution, grid)
    result
    return (result,)


@app.cell
def _(assert_surface_area, expected, result):
    assert_surface_area(result, expected)
    return


if __name__ == "__main__":
    app.run()
