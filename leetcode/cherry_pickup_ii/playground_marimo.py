import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_cherry_pickup, run_cherry_pickup
    from solution import Solution

    return Solution, assert_cherry_pickup, run_cherry_pickup


@app.cell
def _():
    # Example test case
    grid = [[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]]
    expected = 24
    return expected, grid


@app.cell
def _(Solution, grid, run_cherry_pickup):
    result = run_cherry_pickup(Solution, grid)
    result
    return (result,)


@app.cell
def _(assert_cherry_pickup, expected, result):
    assert_cherry_pickup(result, expected)
    return


if __name__ == "__main__":
    app.run()
