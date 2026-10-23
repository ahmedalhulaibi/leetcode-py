import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_oranges_rotting, run_oranges_rotting
    from solution import Solution

    return Solution, assert_oranges_rotting, run_oranges_rotting


@app.cell
def _():
    # Example test case
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    expected = 4
    return expected, grid


@app.cell
def _(Solution, grid, run_oranges_rotting):
    result = run_oranges_rotting(Solution, grid)
    result
    return (result,)


@app.cell
def _(assert_oranges_rotting, expected, result):
    assert_oranges_rotting(result, expected)
    return


if __name__ == "__main__":
    app.run()
