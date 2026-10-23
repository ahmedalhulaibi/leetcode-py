import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_closed_islands, run_closed_islands
    from solution import Solution

    return Solution, assert_closed_islands, run_closed_islands


@app.cell
def _():
    # Example test case
    grid = [
        [1, 1, 1, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 1, 1, 0],
        [1, 0, 1, 0, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 0],
    ]
    expected = 2
    return expected, grid


@app.cell
def _(Solution, grid, run_closed_islands):
    result = run_closed_islands(Solution, grid)
    result
    return (result,)


@app.cell
def _(assert_closed_islands, expected, result):
    assert_closed_islands(result, expected)
    return


if __name__ == "__main__":
    app.run()
