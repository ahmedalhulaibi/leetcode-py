import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_pivot_array, run_pivot_array
    from solution import Solution

    return Solution, assert_pivot_array, run_pivot_array


@app.cell
def _():
    # Example test case
    nums = [9, 12, 5, 10, 14, 3, 10]
    pivot = 10
    expected = [9, 5, 3, 10, 10, 12, 14]
    return expected, nums, pivot


@app.cell
def _(Solution, nums, pivot, run_pivot_array):
    result = run_pivot_array(Solution, nums, pivot)
    result
    return (result,)


@app.cell
def _(assert_pivot_array, expected, result):
    assert_pivot_array(result, expected)
    return


if __name__ == "__main__":
    app.run()
