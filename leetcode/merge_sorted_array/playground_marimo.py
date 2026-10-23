import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_merge, run_merge
    from solution import Solution

    return Solution, assert_merge, run_merge


@app.cell
def _():
    # Example test case
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    expected = [1, 2, 2, 3, 5, 6]
    return expected, m, n, nums1, nums2


@app.cell
def _(Solution, m, n, nums1, nums2, run_merge):
    result = run_merge(Solution, nums1, m, nums2, n)
    result
    return (result,)


@app.cell
def _(assert_merge, expected, result):
    assert_merge(result, expected)
    return


if __name__ == "__main__":
    app.run()
