import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_arrange_coins, run_arrange_coins
    from solution import Solution

    return Solution, assert_arrange_coins, run_arrange_coins


@app.cell
def _():
    # Example test case
    n = 5
    expected = 2
    return expected, n


@app.cell
def _(Solution, n, run_arrange_coins):
    result = run_arrange_coins(Solution, n)
    result
    return (result,)


@app.cell
def _(assert_arrange_coins, expected, result):
    assert_arrange_coins(result, expected)
    return


if __name__ == "__main__":
    app.run()
