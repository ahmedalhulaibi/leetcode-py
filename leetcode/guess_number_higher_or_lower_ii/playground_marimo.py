import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_get_money_amount, run_get_money_amount
    from solution import Solution

    return Solution, assert_get_money_amount, run_get_money_amount


@app.cell
def _():
    # Example test case
    n = 10
    expected = 16
    return expected, n


@app.cell
def _(Solution, n, run_get_money_amount):
    result = run_get_money_amount(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_get_money_amount, expected, result):
    assert_get_money_amount(result, expected)
    return


if __name__ == "__main__":
    app.run()
