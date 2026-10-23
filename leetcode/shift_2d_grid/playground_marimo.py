import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_shift_grid, run_shift_grid
    from solution import Solution

    return Solution, assert_shift_grid, run_shift_grid


@app.cell
def _():
    # Example test case
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    k = 1
    expected = [[9, 1, 2], [3, 4, 5], [6, 7, 8]]
    return expected, grid, k


@app.cell
def _(Solution, grid, k, run_shift_grid):
    result = run_shift_grid(Solution, grid, k)
    result
    return (result,)


@app.cell
def _(assert_shift_grid, expected, result):
    assert_shift_grid(result, expected)
    return


if __name__ == "__main__":
    app.run()
