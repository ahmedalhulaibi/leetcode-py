import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_dot_product, run_dot_product
    from solution import SparseVector

    return SparseVector, assert_dot_product, run_dot_product


@app.cell
def _():
    # Example test case
    nums1 = [1, 0, 0, 2, 3]
    nums2 = [0, 3, 0, 4, 0]
    expected = 8
    return expected, nums1, nums2


@app.cell
def _(SparseVector, nums1, nums2, run_dot_product):
    result = run_dot_product(SparseVector, nums1, nums2)
    result
    return (result,)


@app.cell
def _(assert_dot_product, expected, result):
    assert_dot_product(result, expected)
    return


if __name__ == "__main__":
    app.run()
