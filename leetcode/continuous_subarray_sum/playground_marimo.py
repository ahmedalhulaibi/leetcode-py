import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_check_subarray_sum, run_check_subarray_sum
    from solution import Solution

    return Solution, assert_check_subarray_sum, run_check_subarray_sum


@app.cell
def _():
    # Example test case
    nums = [23, 2, 4, 6, 7]
    k = 6
    expected = True
    return expected, k, nums


@app.cell
def _(Solution, k, nums, run_check_subarray_sum):
    result = run_check_subarray_sum(Solution, nums, k)
    result
    return (result,)


@app.cell
def _(assert_check_subarray_sum, expected, result):
    assert_check_subarray_sum(result, expected)
    return


if __name__ == "__main__":
    app.run()
