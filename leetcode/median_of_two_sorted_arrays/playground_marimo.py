import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_median_sorted_arrays, run_find_median_sorted_arrays
    from solution import Solution

    return (
        Solution,
        assert_find_median_sorted_arrays,
        run_find_median_sorted_arrays,
    )


@app.cell
def _():
    # Example test case
    nums1 = [1, 3]
    nums2 = [2]
    expected = 2.0
    return expected, nums1, nums2


@app.cell
def _(Solution, nums1, nums2, run_find_median_sorted_arrays):
    result = run_find_median_sorted_arrays(Solution, nums1, nums2)
    result
    return (result,)


@app.cell
def _(assert_find_median_sorted_arrays, expected, result):
    assert_find_median_sorted_arrays(result, expected)
    return


if __name__ == "__main__":
    app.run()
