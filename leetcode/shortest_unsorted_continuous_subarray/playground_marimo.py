import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_unsorted_subarray, run_find_unsorted_subarray
    from solution import Solution

    return Solution, assert_find_unsorted_subarray, run_find_unsorted_subarray


@app.cell
def _():
    # Example test case
    nums = [2, 6, 4, 8, 10, 9, 15]
    expected = 5
    return expected, nums


@app.cell
def _(Solution, nums, run_find_unsorted_subarray):
    result = run_find_unsorted_subarray(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_find_unsorted_subarray, expected, result):
    assert_find_unsorted_subarray(result, expected)
    return


if __name__ == "__main__":
    app.run()
