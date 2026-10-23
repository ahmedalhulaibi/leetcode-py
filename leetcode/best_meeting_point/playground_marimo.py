import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_min_total_distance, run_min_total_distance
    from solution import Solution

    return Solution, assert_min_total_distance, run_min_total_distance


@app.cell
def _():
    # Example test case
    grid = [[1, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]
    expected = 6
    return expected, grid


@app.cell
def _(Solution, grid, run_min_total_distance):
    result = run_min_total_distance(Solution, grid)
    result
    return (result,)


@app.cell
def _(assert_min_total_distance, expected, result):
    assert_min_total_distance(result, expected)
    return


if __name__ == "__main__":
    app.run()
