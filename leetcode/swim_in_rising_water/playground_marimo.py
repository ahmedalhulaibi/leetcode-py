import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_swim_in_water, run_swim_in_water
    from solution import Solution

    return Solution, assert_swim_in_water, run_swim_in_water


@app.cell
def _():
    # Example test case
    grid = [[0, 2], [1, 3]]
    expected = 3
    return expected, grid


@app.cell
def _(Solution, grid, run_swim_in_water):
    result = run_swim_in_water(Solution, grid)
    result
    return (result,)


@app.cell
def _(assert_swim_in_water, expected, result):
    assert_swim_in_water(result, expected)
    return


if __name__ == "__main__":
    app.run()
