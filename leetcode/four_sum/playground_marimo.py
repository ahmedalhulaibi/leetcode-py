import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_four_sum, run_four_sum
    from solution import Solution

    return Solution, assert_four_sum, run_four_sum


@app.cell
def _():
    # Example test case
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    expected = [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
    return expected, nums, target


@app.cell
def _(Solution, nums, run_four_sum, target):
    result = run_four_sum(Solution, nums, target)
    result
    return (result,)


@app.cell
def _(assert_four_sum, expected, result):
    assert_four_sum(result, expected)
    return


if __name__ == "__main__":
    app.run()
