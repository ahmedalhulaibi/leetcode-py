import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_change, run_change
    from solution import Solution

    return Solution, assert_change, run_change


@app.cell
def _():
    # Example test case
    amount = 5
    coins = [1, 2, 5]
    expected = 4
    return amount, coins, expected


@app.cell
def _(Solution, amount, coins, run_change):
    result = run_change(Solution, amount, coins)
    result
    return (result,)


@app.cell
def _(assert_change, expected, result):
    assert_change(result, expected)
    return


if __name__ == "__main__":
    app.run()
