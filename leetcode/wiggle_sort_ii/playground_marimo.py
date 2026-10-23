import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_wiggle_sort, run_wiggle_sort
    from solution import Solution

    return Solution, assert_wiggle_sort, run_wiggle_sort


@app.cell
def _():
    # Example test case
    nums = [1, 5, 1, 1, 6, 4]
    expected = [1, 5, 1, 1, 6, 4]
    return expected, nums


@app.cell
def _(Solution, nums, run_wiggle_sort):
    result = run_wiggle_sort(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_wiggle_sort, expected, result):
    assert_wiggle_sort(result, expected)
    return


if __name__ == "__main__":
    app.run()
