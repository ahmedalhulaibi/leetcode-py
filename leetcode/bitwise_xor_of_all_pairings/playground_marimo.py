import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_xor_all_nums, run_xor_all_nums
    from solution import Solution

    return Solution, assert_xor_all_nums, run_xor_all_nums


@app.cell
def _():
    # Example test case
    nums1 = [2, 1, 3]
    nums2 = [10, 2, 5, 0]
    expected = 13
    return expected, nums1, nums2


@app.cell
def _(Solution, nums1, nums2, run_xor_all_nums):
    result = run_xor_all_nums(Solution, nums1, nums2)
    result
    return (result,)


@app.cell
def _(assert_xor_all_nums, expected, result):
    assert_xor_all_nums(result, expected)
    return


if __name__ == "__main__":
    app.run()
