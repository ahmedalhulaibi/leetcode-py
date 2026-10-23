import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_minimize_error, run_minimize_error
    from solution import Solution

    return Solution, assert_minimize_error, run_minimize_error


@app.cell
def _():
    # Example test case
    prices = ["0.700", "2.800", "4.900"]
    target = 8
    expected = "1.000"
    return expected, prices, target


@app.cell
def _(Solution, prices, run_minimize_error, target):
    result = run_minimize_error(Solution, prices, target)
    result
    return (result,)


@app.cell
def _(assert_minimize_error, expected, result):
    assert_minimize_error(result, expected)
    return


if __name__ == "__main__":
    app.run()
