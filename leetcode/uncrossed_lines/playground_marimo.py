import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_max_uncrossed_lines, run_max_uncrossed_lines
    from solution import Solution

    return Solution, assert_max_uncrossed_lines, run_max_uncrossed_lines


@app.cell
def _():
    # Example test case
    nums1 = [1, 4, 2]
    nums2 = [1, 2, 4]
    expected = 2
    return expected, nums1, nums2


@app.cell
def _(Solution, nums1, nums2, run_max_uncrossed_lines):
    result = run_max_uncrossed_lines(Solution, nums1, nums2)
    result
    return (result,)


@app.cell
def _(assert_max_uncrossed_lines, expected, result):
    assert_max_uncrossed_lines(result, expected)
    return


if __name__ == "__main__":
    app.run()
