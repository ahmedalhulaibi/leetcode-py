import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_min_operations, run_min_operations
    from solution import Solution

    return Solution, assert_min_operations, run_min_operations


@app.cell
def _():
    # Example test case
    grid = [[2, 4], [6, 8]]
    x = 2
    expected = 4
    return expected, grid, x


@app.cell
def _(Solution, grid, run_min_operations, x):
    result = run_min_operations(Solution, grid, x)
    result
    return (result,)


@app.cell
def _(assert_min_operations, expected, result):
    assert_min_operations(result, expected)
    return


if __name__ == "__main__":
    app.run()
