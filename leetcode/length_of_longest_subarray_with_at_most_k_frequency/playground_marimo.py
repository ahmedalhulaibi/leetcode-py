import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_max_subarray_length, run_max_subarray_length
    from solution import Solution

    return Solution, assert_max_subarray_length, run_max_subarray_length


@app.cell
def _():
    # Example test case
    nums = [1, 2, 3, 1, 2, 3, 1, 2]
    k = 2
    expected = 6
    return expected, k, nums


@app.cell
def _(Solution, k, nums, run_max_subarray_length):
    result = run_max_subarray_length(Solution, nums, k)
    result
    return (result,)


@app.cell
def _(assert_max_subarray_length, expected, result):
    assert_max_subarray_length(result, expected)
    return


if __name__ == "__main__":
    app.run()
