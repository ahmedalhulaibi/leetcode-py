import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_num_subarray_product_less_than_k, run_num_subarray_product_less_than_k
    from solution import Solution

    return (
        Solution,
        assert_num_subarray_product_less_than_k,
        run_num_subarray_product_less_than_k,
    )


@app.cell
def _():
    # Example test case
    nums = [10, 5, 2, 6]
    k = 100
    expected = 8
    return expected, k, nums


@app.cell
def _(Solution, k, nums, run_num_subarray_product_less_than_k):
    result = run_num_subarray_product_less_than_k(Solution, nums, k)
    result
    return (result,)


@app.cell
def _(assert_num_subarray_product_less_than_k, expected, result):
    assert_num_subarray_product_less_than_k(result, expected)
    return


if __name__ == "__main__":
    app.run()
