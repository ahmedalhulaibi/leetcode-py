import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_two_sum, run_two_sum
    from solution import Solution

    return Solution, assert_two_sum, run_two_sum


@app.cell
def _():
    # Example test case
    nums = [2, 7, 11, 15]
    target = 9
    expected = [0, 1]
    return expected, nums, target


@app.cell
def _(Solution, nums, run_two_sum, target):
    result = run_two_sum(Solution, nums, target)
    result
    return (result,)


@app.cell
def _(assert_two_sum, expected, result):
    assert_two_sum(result, expected)
    return


if __name__ == "__main__":
    app.run()
