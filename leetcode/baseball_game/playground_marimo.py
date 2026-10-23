import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_cal_points, run_cal_points
    from solution import Solution

    return Solution, assert_cal_points, run_cal_points


@app.cell
def _():
    # Example test case
    operations = ["5", "2", "C", "D", "+"]
    expected = 30
    return expected, operations


@app.cell
def _(Solution, operations, run_cal_points):
    result = run_cal_points(Solution, operations)
    result
    return (result,)


@app.cell
def _(assert_cal_points, expected, result):
    assert_cal_points(result, expected)
    return


if __name__ == "__main__":
    app.run()
