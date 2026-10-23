import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_ship_within_days, run_ship_within_days
    from solution import Solution

    return Solution, assert_ship_within_days, run_ship_within_days


@app.cell
def _():
    # Example test case
    weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    days = 5
    expected = 15
    return days, expected, weights


@app.cell
def _(Solution, days, run_ship_within_days, weights):
    result = run_ship_within_days(Solution, weights, days)
    result
    return (result,)


@app.cell
def _(assert_ship_within_days, expected, result):
    assert_ship_within_days(result, expected)
    return


if __name__ == "__main__":
    app.run()
