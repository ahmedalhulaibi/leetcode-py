import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_three_sum, run_three_sum
    from solution import Solution

    return Solution, assert_three_sum, run_three_sum


@app.cell
def _():
    # Example test case
    nums = [-1, 0, 1, 2, -1, -4]
    expected = [[-1, -1, 2], [-1, 0, 1]]
    return expected, nums


@app.cell
def _(Solution, nums, run_three_sum):
    result = run_three_sum(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_three_sum, expected, result):
    assert_three_sum(result, expected)
    return


if __name__ == "__main__":
    app.run()
