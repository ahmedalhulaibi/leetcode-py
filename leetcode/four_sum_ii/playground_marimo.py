import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_four_sum_count, run_four_sum_count
    from solution import Solution

    return Solution, assert_four_sum_count, run_four_sum_count


@app.cell
def _():
    # Example test case
    nums1 = [1, 2]
    nums2 = [-2, -1]
    nums3 = [-1, 2]
    nums4 = [0, 2]
    expected = 2
    return expected, nums1, nums2, nums3, nums4


@app.cell
def _(Solution, nums1, nums2, nums3, nums4, run_four_sum_count):
    result = run_four_sum_count(Solution, nums1, nums2, nums3, nums4)
    result
    return (result,)


@app.cell
def _(assert_four_sum_count, expected, result):
    assert_four_sum_count(result, expected)
    return


if __name__ == "__main__":
    app.run()
