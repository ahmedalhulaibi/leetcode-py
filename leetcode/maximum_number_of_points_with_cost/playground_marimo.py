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
    points = [[1, 2, 3], [1, 5, 1], [3, 1, 1]]
    expected = 9
    return expected, points


@app.cell
def _(Solution, points, run_max_points):
    result = run_max_points(Solution, points)
    result
    return (result,)


@app.cell
def _(assert_max_points, expected, result):
    assert_max_points(result, expected)
    return


if __name__ == "__main__":
    app.run()
