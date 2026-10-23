import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_three_sum_smaller, run_three_sum_smaller
    from solution import Solution

    return Solution, assert_three_sum_smaller, run_three_sum_smaller


@app.cell
def _():
    # Example test case
    nums = [-2, 0, 1, 3]
    target = 2
    expected = 2
    return expected, nums, target


@app.cell
def _(Solution, nums, run_three_sum_smaller, target):
    result = run_three_sum_smaller(Solution, nums, target)
    result
    return (result,)


@app.cell
def _(assert_three_sum_smaller, expected, result):
    assert_three_sum_smaller(result, expected)
    return


if __name__ == "__main__":
    app.run()
