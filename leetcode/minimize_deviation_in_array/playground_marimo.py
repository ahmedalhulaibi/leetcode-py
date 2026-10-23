import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_minimum_deviation, run_minimum_deviation
    from solution import Solution

    return Solution, assert_minimum_deviation, run_minimum_deviation


@app.cell
def _():
    # Example test case
    nums = [1, 2, 3, 4]
    expected = 1
    return expected, nums


@app.cell
def _(Solution, nums, run_minimum_deviation):
    result = run_minimum_deviation(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_minimum_deviation, expected, result):
    assert_minimum_deviation(result, expected)
    return


if __name__ == "__main__":
    app.run()
