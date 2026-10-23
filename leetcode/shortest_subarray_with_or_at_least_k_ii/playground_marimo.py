import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_minimum_subarray_length, run_minimum_subarray_length
    from solution import Solution

    return (
        Solution,
        assert_minimum_subarray_length,
        run_minimum_subarray_length,
    )


@app.cell
def _():
    # Example test case
    nums = [2, 1, 8]
    k = 10
    expected = 3
    return expected, k, nums


@app.cell
def _(Solution, k, nums, run_minimum_subarray_length):
    result = run_minimum_subarray_length(Solution, nums, k)
    result
    return (result,)


@app.cell
def _(assert_minimum_subarray_length, expected, result):
    assert_minimum_subarray_length(result, expected)
    return


if __name__ == "__main__":
    app.run()
