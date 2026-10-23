import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_missing_ranges, run_find_missing_ranges
    from solution import Solution

    return Solution, assert_find_missing_ranges, run_find_missing_ranges


@app.cell
def _():
    # Example test case
    nums = [0, 1, 3, 50, 75]
    lower = 0
    upper = 99
    expected = [[2, 2], [4, 49], [51, 74], [76, 99]]
    return expected, lower, nums, upper


@app.cell
def _(Solution, lower, nums, run_find_missing_ranges, upper):
    result = run_find_missing_ranges(Solution, nums, lower, upper)
    result
    return (result,)


@app.cell
def _(assert_find_missing_ranges, expected, result):
    assert_find_missing_ranges(result, expected)
    return


if __name__ == "__main__":
    app.run()
