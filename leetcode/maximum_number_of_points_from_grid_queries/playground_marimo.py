import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_max_points, run_max_points
    from solution import Solution

    return Solution, assert_max_points, run_max_points


@app.cell
def _():
    # Example test case
    grid = [[1, 2, 3], [2, 5, 7], [3, 5, 1]]
    queries = [5, 6, 2]
    expected = [5, 8, 1]
    return expected, grid, queries


@app.cell
def _(Solution, grid, queries, run_max_points):
    result = run_max_points(Solution, grid, queries)
    result
    return (result,)


@app.cell
def _(assert_max_points, expected, result):
    assert_max_points(result, expected)
    return


if __name__ == "__main__":
    app.run()
