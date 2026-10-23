import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_minimum_time, run_minimum_time
    from solution import Solution

    return Solution, assert_minimum_time, run_minimum_time


@app.cell
def _():
    # Example test case
    grid = [[0, 1, 3, 2], [5, 1, 2, 5], [4, 3, 8, 6]]
    expected = 7
    return expected, grid


@app.cell
def _(Solution, grid, run_minimum_time):
    result = run_minimum_time(Solution, grid)
    result
    return (result,)


@app.cell
def _(assert_minimum_time, expected, result):
    assert_minimum_time(result, expected)
    return


if __name__ == "__main__":
    app.run()
