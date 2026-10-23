import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_min_days, run_min_days
    from solution import Solution

    return Solution, assert_min_days, run_min_days


@app.cell
def _():
    # Example test case
    n = 10
    expected = 4
    return expected, n


@app.cell
def _(Solution, n, run_min_days):
    result = run_min_days(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_min_days, expected, result):
    assert_min_days(result, expected)
    return


if __name__ == "__main__":
    app.run()
