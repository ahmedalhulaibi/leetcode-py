import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_rob, run_rob
    from solution import Solution

    return Solution, assert_rob, run_rob


@app.cell
def _():
    # Example test case
    nums = [2, 7, 9, 3, 1]
    expected = 12
    return expected, nums


@app.cell
def _(Solution, nums, run_rob):
    result = run_rob(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_rob, expected, result):
    assert_rob(result, expected)
    return


if __name__ == "__main__":
    app.run()
