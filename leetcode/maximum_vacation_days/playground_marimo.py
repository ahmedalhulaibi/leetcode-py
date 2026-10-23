import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_max_vacation_days, run_max_vacation_days
    from solution import Solution

    return Solution, assert_max_vacation_days, run_max_vacation_days


@app.cell
def _():
    # Example test case
    flights = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
    days = [[1, 3, 1], [6, 0, 3], [3, 3, 3]]
    expected = 12
    return days, expected, flights


@app.cell
def _(Solution, days, flights, run_max_vacation_days):
    result = run_max_vacation_days(Solution, flights, days)
    result
    return (result,)


@app.cell
def _(assert_max_vacation_days, expected, result):
    assert_max_vacation_days(result, expected)
    return


if __name__ == "__main__":
    app.run()
