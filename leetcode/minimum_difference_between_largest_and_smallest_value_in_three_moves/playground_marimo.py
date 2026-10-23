import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_min_difference, run_min_difference
    from solution import Solution

    return Solution, assert_min_difference, run_min_difference


@app.cell
def _():
    # Example test case
    nums = [1, 5, 0, 10, 14]
    expected = 1
    return expected, nums


@app.cell
def _(Solution, nums, run_min_difference):
    result = run_min_difference(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_min_difference, expected, result):
    assert_min_difference(result, expected)
    return


if __name__ == "__main__":
    app.run()
