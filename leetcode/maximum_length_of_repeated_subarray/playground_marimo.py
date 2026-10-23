import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_length, run_find_length
    from solution import Solution

    return Solution, assert_find_length, run_find_length


@app.cell
def _():
    # Example test case
    nums1 = [1, 2, 3, 2, 1]
    nums2 = [3, 2, 1, 4, 7]
    expected = 3
    return expected, nums1, nums2


@app.cell
def _(Solution, nums1, nums2, run_find_length):
    result = run_find_length(Solution, nums1, nums2)
    result
    return (result,)


@app.cell
def _(assert_find_length, expected, result):
    assert_find_length(result, expected)
    return


if __name__ == "__main__":
    app.run()
