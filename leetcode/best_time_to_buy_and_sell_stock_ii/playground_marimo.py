import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_max_profit, run_max_profit
    from solution import Solution

    return Solution, assert_max_profit, run_max_profit


@app.cell
def _():
    # Example test case
    prices = [7, 1, 5, 3, 6, 4]
    expected = 7
    return expected, prices


@app.cell
def _(Solution, prices, run_max_profit):
    result = run_max_profit(Solution, prices)
    result
    return (result,)


@app.cell
def _(assert_max_profit, expected, result):
    assert_max_profit(result, expected)
    return


if __name__ == "__main__":
    app.run()
