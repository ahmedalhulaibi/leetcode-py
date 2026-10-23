import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_largest_local, run_largest_local
    from solution import Solution

    return Solution, assert_largest_local, run_largest_local


@app.cell
def _():
    # Example test case
    grid = [[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]]
    expected = [[9, 9], [8, 6]]
    return expected, grid


@app.cell
def _(Solution, grid, run_largest_local):
    result = run_largest_local(Solution, grid)
    result
    return (result,)


@app.cell
def _(assert_largest_local, expected, result):
    assert_largest_local(result, expected)
    return


if __name__ == "__main__":
    app.run()
