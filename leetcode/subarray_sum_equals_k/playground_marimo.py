import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_subarray_sum, run_subarray_sum
    from solution import Solution

    return Solution, assert_subarray_sum, run_subarray_sum


@app.cell
def _():
    # Example test case
    nums = [1, 1, 1]
    k = 2
    expected = 2
    return expected, k, nums


@app.cell
def _(Solution, k, nums, run_subarray_sum):
    result = run_subarray_sum(Solution, nums, k)
    result
    return (result,)


@app.cell
def _(assert_subarray_sum, expected, result):
    assert_subarray_sum(result, expected)
    return


if __name__ == "__main__":
    app.run()
