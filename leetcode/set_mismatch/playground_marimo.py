import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_error_nums, run_find_error_nums
    from solution import Solution

    return Solution, assert_find_error_nums, run_find_error_nums


@app.cell
def _():
    # Example test case
    nums: list[int] = [1, 2, 2, 4]
    expected = [2, 3]
    return expected, nums


@app.cell
def _(Solution, nums: list[int], run_find_error_nums):
    result = run_find_error_nums(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_find_error_nums, expected, result):
    assert_find_error_nums(result, expected)
    return


if __name__ == "__main__":
    app.run()
