import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_zero_filled_subarray, run_zero_filled_subarray
    from solution import Solution

    return Solution, assert_zero_filled_subarray, run_zero_filled_subarray


@app.cell
def _():
    # Example test case
    nums = [1, 3, 0, 0, 2, 0, 0, 4]
    expected = 6
    return expected, nums


@app.cell
def _(Solution, nums, run_zero_filled_subarray):
    result = run_zero_filled_subarray(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_zero_filled_subarray, expected, result):
    assert_zero_filled_subarray(result, expected)
    return


if __name__ == "__main__":
    app.run()
