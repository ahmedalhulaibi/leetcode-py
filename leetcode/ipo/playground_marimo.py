import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_maximized_capital, run_find_maximized_capital
    from solution import Solution

    return Solution, assert_find_maximized_capital, run_find_maximized_capital


@app.cell
def _():
    # Example test case
    k = 2
    w = 0
    profits = [1, 2, 3]
    capital = [0, 1, 1]
    expected = 4
    return capital, expected, k, profits, w


@app.cell
def _(Solution, capital, k, profits, run_find_maximized_capital, w):
    result = run_find_maximized_capital(Solution, k, w, profits, capital)
    result
    return (result,)


@app.cell
def _(assert_find_maximized_capital, expected, result):
    assert_find_maximized_capital(result, expected)
    return


if __name__ == "__main__":
    app.run()
