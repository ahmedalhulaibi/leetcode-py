import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_final_prices, run_final_prices
    from solution import Solution

    return Solution, assert_final_prices, run_final_prices


@app.cell
def _():
    # Example test case
    prices = [8, 4, 6, 2, 3]
    expected = [4, 2, 4, 2, 3]
    return expected, prices


@app.cell
def _(Solution, prices, run_final_prices):
    result = run_final_prices(Solution, prices)
    result
    return (result,)


@app.cell
def _(assert_final_prices, expected, result):
    assert_final_prices(result, expected)
    return


if __name__ == "__main__":
    app.run()
