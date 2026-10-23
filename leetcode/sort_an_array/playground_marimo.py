import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_sort_array, run_sort_array
    from solution import Solution

    return Solution, assert_sort_array, run_sort_array


@app.cell
def _():
    # Example test case
    nums = [5, 2, 3, 1]
    expected = [1, 2, 3, 5]
    return expected, nums


@app.cell
def _(Solution, nums, run_sort_array):
    result = run_sort_array(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_sort_array, expected, result):
    assert_sort_array(result, expected)
    return


if __name__ == "__main__":
    app.run()
