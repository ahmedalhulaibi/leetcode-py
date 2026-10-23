import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_maximum_minimum_path, run_maximum_minimum_path
    from solution import Solution

    return Solution, assert_maximum_minimum_path, run_maximum_minimum_path


@app.cell
def _():
    # Example test case
    grid = [[5, 4, 5], [1, 2, 6], [7, 4, 6]]
    expected = 4
    return expected, grid


@app.cell
def _(Solution, grid, run_maximum_minimum_path):
    result = run_maximum_minimum_path(Solution, grid)
    result
    return (result,)


@app.cell
def _(assert_maximum_minimum_path, expected, result):
    assert_maximum_minimum_path(result, expected)
    return


if __name__ == "__main__":
    app.run()
