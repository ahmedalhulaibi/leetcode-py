import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_max_coins, run_max_coins
    from solution import Solution

    return Solution, assert_max_coins, run_max_coins


@app.cell
def _():
    # Example test case
    nums = [3, 1, 5, 8]
    expected = 167
    return expected, nums


@app.cell
def _(Solution, nums, run_max_coins):
    result = run_max_coins(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_max_coins, expected, result):
    assert_max_coins(result, expected)
    return


if __name__ == "__main__":
    app.run()
