import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_count_days, run_count_days
    from solution import Solution

    return Solution, assert_count_days, run_count_days


@app.cell
def _():
    # Example test case
    days = 10
    meetings = [[5, 7], [1, 3], [9, 10]]
    expected = 2
    return days, expected, meetings


@app.cell
def _(Solution, days, meetings, run_count_days):
    result = run_count_days(Solution, days, meetings)
    result
    return (result,)


@app.cell
def _(assert_count_days, expected, result):
    assert_count_days(result, expected)
    return


if __name__ == "__main__":
    app.run()
