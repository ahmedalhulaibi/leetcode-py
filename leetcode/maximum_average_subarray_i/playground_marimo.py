import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_find_max_average, run_find_max_average
    from solution import Solution

    return Solution, assert_find_max_average, run_find_max_average


@app.cell
def _():
    # Example test case
    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    expected = 12.75
    return expected, k, nums


@app.cell
def _(Solution, k, nums, run_find_max_average):
    result = run_find_max_average(Solution, nums, k)
    result
    return (result,)


@app.cell
def _(assert_find_max_average, expected, result):
    assert_find_max_average(result, expected)
    return


if __name__ == "__main__":
    app.run()
