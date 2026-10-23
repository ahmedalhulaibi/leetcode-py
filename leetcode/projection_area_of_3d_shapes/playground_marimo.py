import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_projection_area, run_projection_area
    from solution import Solution

    return Solution, assert_projection_area, run_projection_area


@app.cell
def _():
    # Example test case
    grid = [[1, 2], [3, 4]]
    expected = 17
    return expected, grid


@app.cell
def _(Solution, grid, run_projection_area):
    result = run_projection_area(Solution, grid)
    result
    return (result,)


@app.cell
def _(assert_projection_area, expected, result):
    assert_projection_area(result, expected)
    return


if __name__ == "__main__":
    app.run()
