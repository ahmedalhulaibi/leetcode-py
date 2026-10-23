import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_num_subarray_bounded_max, run_num_subarray_bounded_max
    from solution import Solution

    return (
        Solution,
        assert_num_subarray_bounded_max,
        run_num_subarray_bounded_max,
    )


@app.cell
def _():
    # Example test case
    nums = [2, 1, 4, 3]
    left = 2
    right = 3
    expected = 3
    return expected, left, nums, right


@app.cell
def _(Solution, left, nums, right, run_num_subarray_bounded_max):
    result = run_num_subarray_bounded_max(Solution, nums, left, right)
    result
    return (result,)


@app.cell
def _(assert_num_subarray_bounded_max, expected, result):
    assert_num_subarray_bounded_max(result, expected)
    return


if __name__ == "__main__":
    app.run()
