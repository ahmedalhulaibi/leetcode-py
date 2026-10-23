import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_max_value_of_coins, run_max_value_of_coins
    from solution import Solution

    return Solution, assert_max_value_of_coins, run_max_value_of_coins


@app.cell
def _():
    # Example test case
    piles = [[1, 100, 3], [7, 8, 9]]
    k = 2
    expected = 101
    return expected, k, piles


@app.cell
def _(Solution, k, piles, run_max_value_of_coins):
    result = run_max_value_of_coins(Solution, piles, k)
    result
    return (result,)


@app.cell
def _(assert_max_value_of_coins, expected, result):
    assert_max_value_of_coins(result, expected)
    return


if __name__ == "__main__":
    app.run()
