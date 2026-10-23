import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_prison_after_n_days, run_prison_after_n_days
    from solution import Solution

    return Solution, assert_prison_after_n_days, run_prison_after_n_days


@app.cell
def _():
    # Example test case
    cells = [0, 1, 0, 1, 1, 0, 0, 1]
    n = 7
    expected = [0, 0, 1, 1, 0, 0, 0, 0]
    return cells, expected, n


@app.cell
def _(Solution, cells, n, run_prison_after_n_days):
    result = run_prison_after_n_days(Solution, cells, n)
    result
    return (result,)


@app.cell
def _(assert_prison_after_n_days, expected, result):
    assert_prison_after_n_days(result, expected)
    return


if __name__ == "__main__":
    app.run()
