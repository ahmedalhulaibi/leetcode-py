import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_min_difference, run_find_min_difference
    from solution import Solution

    return Solution, assert_find_min_difference, run_find_min_difference


@app.cell
def _():
    # Example test case
    time_points = ["23:59", "00:00"]
    expected = 1
    return expected, time_points


@app.cell
def _(Solution, run_find_min_difference, time_points):
    result = run_find_min_difference(Solution, time_points)
    result
    return (result,)


@app.cell
def _(assert_find_min_difference, expected, result):
    assert_find_min_difference(result, expected)
    return


if __name__ == "__main__":
    app.run()
