import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_buy_choco, run_buy_choco
    from solution import Solution

    return Solution, assert_buy_choco, run_buy_choco


@app.cell
def _():
    # Example test case
    prices = [1, 2, 2]
    money = 3
    expected = 0
    return expected, money, prices


@app.cell
def _(Solution, money, prices, run_buy_choco):
    result = run_buy_choco(Solution, prices, money)
    result
    return (result,)


@app.cell
def _(assert_buy_choco, expected, result):
    assert_buy_choco(result, expected)
    return


if __name__ == "__main__":
    app.run()
