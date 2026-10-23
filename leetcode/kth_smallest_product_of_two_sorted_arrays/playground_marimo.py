import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_kth_smallest_product, run_kth_smallest_product
    from solution import Solution

    return Solution, assert_kth_smallest_product, run_kth_smallest_product


@app.cell
def _():
    # Example test case
    nums1 = [2, 5]
    nums2 = [3, 4]
    k = 2
    expected = 8
    return expected, k, nums1, nums2


@app.cell
def _(Solution, k, nums1, nums2, run_kth_smallest_product):
    result = run_kth_smallest_product(Solution, nums1, nums2, k)
    result
    return (result,)


@app.cell
def _(assert_kth_smallest_product, expected, result):
    assert_kth_smallest_product(result, expected)
    return


if __name__ == "__main__":
    app.run()
