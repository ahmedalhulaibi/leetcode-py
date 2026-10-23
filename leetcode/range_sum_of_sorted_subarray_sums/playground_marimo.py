import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_range_sum, run_range_sum
    from solution import Solution

    return Solution, assert_range_sum, run_range_sum


@app.cell
def _():
    # Example test case
    nums: list[int] = [1, 2, 3, 4]
    n = 4
    left = 1
    right = 5
    expected = 13
    return expected, left, n, nums, right


@app.cell
def _(Solution, left, n, nums: list[int], right, run_range_sum):
    result = run_range_sum(Solution, nums, n, left, right)
    result
    return (result,)


@app.cell
def _(assert_range_sum, expected, result):
    assert_range_sum(result, expected)
    return


if __name__ == "__main__":
    app.run()
