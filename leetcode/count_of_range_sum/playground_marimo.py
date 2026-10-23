import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_count_range_sum, run_count_range_sum
    from solution import Solution

    return Solution, assert_count_range_sum, run_count_range_sum


@app.cell
def _():
    # Example test case
    nums: list[int] = [-2, 5, -1]
    lower = -2
    upper = 2
    expected = 3
    return expected, lower, nums, upper


@app.cell
def _(Solution, lower, nums: list[int], run_count_range_sum, upper):
    result = run_count_range_sum(Solution, nums, lower, upper)
    result
    return (result,)


@app.cell
def _(assert_count_range_sum, expected, result):
    assert_count_range_sum(result, expected)
    return


if __name__ == "__main__":
    app.run()
