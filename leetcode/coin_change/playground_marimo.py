import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_coin_change, run_coin_change
    from solution import Solution

    return Solution, assert_coin_change, run_coin_change


@app.cell
def _():
    # Example test case
    coins = [1, 2, 5]
    amount = 11
    expected = 3
    return amount, coins, expected


@app.cell
def _(Solution, amount, coins, run_coin_change):
    result = run_coin_change(Solution, coins, amount)
    result
    return (result,)


@app.cell
def _(assert_coin_change, expected, result):
    assert_coin_change(result, expected)
    return


if __name__ == "__main__":
    app.run()
