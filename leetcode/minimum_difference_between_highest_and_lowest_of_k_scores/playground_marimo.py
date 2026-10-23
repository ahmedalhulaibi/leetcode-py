import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_minimum_difference, run_minimum_difference
    from solution import Solution

    return Solution, assert_minimum_difference, run_minimum_difference


@app.cell
def _():
    # Example test case
    nums = [9, 4, 1, 7]
    k = 2
    expected = 2
    return expected, k, nums


@app.cell
def _(Solution, k, nums, run_minimum_difference):
    result = run_minimum_difference(Solution, nums, k)
    result
    return (result,)


@app.cell
def _(assert_minimum_difference, expected, result):
    assert_minimum_difference(result, expected)
    return


if __name__ == "__main__":
    app.run()
