import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_best_closing_time, run_best_closing_time
    from solution import Solution

    return Solution, assert_best_closing_time, run_best_closing_time


@app.cell
def _():
    # Example test case
    customers = "YYNY"
    expected = 2
    return customers, expected


@app.cell
def _(Solution, customers, run_best_closing_time):
    result = run_best_closing_time(Solution, customers)
    result
    return (result,)


@app.cell
def _(assert_best_closing_time, expected, result):
    assert_best_closing_time(result, expected)
    return


if __name__ == "__main__":
    app.run()
