import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_three_sum_closest, run_three_sum_closest
    from solution import Solution

    return Solution, assert_three_sum_closest, run_three_sum_closest


@app.cell
def _():
    # Example test case
    nums = [-1, 2, 1, -4]
    target = 1
    expected = 2
    return expected, nums, target


@app.cell
def _(Solution, nums, run_three_sum_closest, target):
    result = run_three_sum_closest(Solution, nums, target)
    result
    return (result,)


@app.cell
def _(assert_three_sum_closest, expected, result):
    assert_three_sum_closest(result, expected)
    return


if __name__ == "__main__":
    app.run()
