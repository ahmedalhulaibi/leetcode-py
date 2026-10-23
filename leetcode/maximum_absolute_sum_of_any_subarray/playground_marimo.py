import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_max_absolute_sum, run_max_absolute_sum
    from solution import Solution

    return Solution, assert_max_absolute_sum, run_max_absolute_sum


@app.cell
def _():
    # Example test case
    nums = [1, -3, 2, 3, -4]
    expected = 5
    return expected, nums


@app.cell
def _(Solution, nums, run_max_absolute_sum):
    result = run_max_absolute_sum(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_max_absolute_sum, expected, result):
    assert_max_absolute_sum(result, expected)
    return


if __name__ == "__main__":
    app.run()
