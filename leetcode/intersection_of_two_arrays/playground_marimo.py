import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_intersection, run_intersection
    from solution import Solution

    return Solution, assert_intersection, run_intersection


@app.cell
def _():
    # Example test case
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    expected = [4, 9]
    return expected, nums1, nums2


@app.cell
def _(Solution, nums1, nums2, run_intersection):
    result = run_intersection(Solution, nums1, nums2)
    result
    return (result,)


@app.cell
def _(assert_intersection, expected, result):
    assert_intersection(result, expected)
    return


if __name__ == "__main__":
    app.run()
