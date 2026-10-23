import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_max_number, run_max_number
    from solution import Solution

    return Solution, assert_max_number, run_max_number


@app.cell
def _():
    # Example test case
    nums1 = [3, 4, 6, 5]
    nums2 = [9, 1, 2, 5, 8, 3]
    k = 5
    expected = [9, 8, 6, 5, 3]
    return expected, k, nums1, nums2


@app.cell
def _(Solution, k, nums1, nums2, run_max_number):
    result = run_max_number(Solution, nums1, nums2, k)
    result
    return (result,)


@app.cell
def _(assert_max_number, expected, result):
    assert_max_number(result, expected)
    return


if __name__ == "__main__":
    app.run()
