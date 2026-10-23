import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_regions_by_slashes, run_regions_by_slashes
    from solution import Solution

    return Solution, assert_regions_by_slashes, run_regions_by_slashes


@app.cell
def _():
    # Example test case
    grid = [" /", "/ "]
    expected = 2
    return expected, grid


@app.cell
def _(Solution, grid, run_regions_by_slashes):
    result = run_regions_by_slashes(Solution, grid)
    result
    return (result,)


@app.cell
def _(assert_regions_by_slashes, expected, result):
    assert_regions_by_slashes(result, expected)
    return


if __name__ == "__main__":
    app.run()
