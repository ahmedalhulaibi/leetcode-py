import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_difference, run_find_difference
    from solution import Solution

    return Solution, assert_find_difference, run_find_difference


@app.cell
def _():
    # Example test case
    nums1 = [1, 2, 3]
    nums2 = [2, 4, 6]
    expected = [[1, 3], [4, 6]]
    return expected, nums1, nums2


@app.cell
def _(Solution, nums1, nums2, run_find_difference):
    result = run_find_difference(Solution, nums1, nums2)
    result
    return (result,)


@app.cell
def _(assert_find_difference, expected, result):
    assert_find_difference(result, expected)
    return


if __name__ == "__main__":
    app.run()
