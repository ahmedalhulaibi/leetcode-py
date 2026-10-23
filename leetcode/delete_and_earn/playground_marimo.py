import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_delete_and_earn, run_delete_and_earn
    from solution import Solution

    return Solution, assert_delete_and_earn, run_delete_and_earn


@app.cell
def _():
    # Example test case
    nums = [3, 4, 2]
    expected = 6
    return expected, nums


@app.cell
def _(Solution, nums, run_delete_and_earn):
    result = run_delete_and_earn(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_delete_and_earn, expected, result):
    assert_delete_and_earn(result, expected)
    return


if __name__ == "__main__":
    app.run()
