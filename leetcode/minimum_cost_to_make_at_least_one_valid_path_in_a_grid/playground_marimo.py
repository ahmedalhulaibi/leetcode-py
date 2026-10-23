import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_min_cost, run_min_cost
    from solution import Solution

    return Solution, assert_min_cost, run_min_cost


@app.cell
def _():
    # Example test case
    grid = [[1, 1, 3], [3, 2, 2], [1, 1, 4]]
    expected = 0
    return expected, grid


@app.cell
def _(Solution, grid, run_min_cost):
    result = run_min_cost(Solution, grid)
    result
    return (result,)


@app.cell
def _(assert_min_cost, expected, result):
    assert_min_cost(result, expected)
    return


if __name__ == "__main__":
    app.run()
