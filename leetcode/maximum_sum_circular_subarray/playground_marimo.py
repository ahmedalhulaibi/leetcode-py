import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_max_subarray_sum_circular, run_max_subarray_sum_circular
    from solution import Solution

    return (
        Solution,
        assert_max_subarray_sum_circular,
        run_max_subarray_sum_circular,
    )


@app.cell
def _():
    # Example test case
    nums = [5, -3, 5]
    expected = 10
    return expected, nums


@app.cell
def _(Solution, nums, run_max_subarray_sum_circular):
    result = run_max_subarray_sum_circular(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_max_subarray_sum_circular, expected, result):
    assert_max_subarray_sum_circular(result, expected)
    return


if __name__ == "__main__":
    app.run()
