import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_min_swap, run_min_swap
    from solution import Solution

    return Solution, assert_min_swap, run_min_swap


@app.cell
def _():
    # Example test case
    nums1 = [1, 3, 5, 4]
    nums2 = [1, 2, 3, 7]
    expected = 1
    return expected, nums1, nums2


@app.cell
def _(Solution, nums1, nums2, run_min_swap):
    result = run_min_swap(Solution, nums1, nums2)
    result
    return (result,)


@app.cell
def _(assert_min_swap, expected, result):
    assert_min_swap(result, expected)
    return


if __name__ == "__main__":
    app.run()
