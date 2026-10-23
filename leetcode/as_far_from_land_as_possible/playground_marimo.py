import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_max_distance, run_max_distance
    from solution import Solution

    return Solution, assert_max_distance, run_max_distance


@app.cell
def _():
    # Example test case
    grid = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    expected = 2
    return expected, grid


@app.cell
def _(Solution, grid, run_max_distance):
    result = run_max_distance(Solution, grid)
    result
    return (result,)


@app.cell
def _(assert_max_distance, expected, result):
    assert_max_distance(result, expected)
    return


if __name__ == "__main__":
    app.run()
