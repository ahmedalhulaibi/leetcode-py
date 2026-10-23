import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_merge_arrays, run_merge_arrays
    from solution import Solution

    return Solution, assert_merge_arrays, run_merge_arrays


@app.cell
def _():
    # Example test case
    nums1 = [[1, 2], [2, 3], [4, 5]]
    nums2 = [[1, 4], [3, 2], [4, 1]]
    expected = [[1, 6], [2, 3], [3, 2], [4, 6]]
    return expected, nums1, nums2


@app.cell
def _(Solution, nums1, nums2, run_merge_arrays):
    result = run_merge_arrays(Solution, nums1, nums2)
    result
    return (result,)


@app.cell
def _(assert_merge_arrays, expected, result):
    assert_merge_arrays(result, expected)
    return


if __name__ == "__main__":
    app.run()
