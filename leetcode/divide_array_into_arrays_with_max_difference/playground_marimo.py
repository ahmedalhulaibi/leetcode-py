import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_divide_array, run_divide_array
    from solution import Solution

    return Solution, assert_divide_array, run_divide_array


@app.cell
def _():
    # Example test case
    nums = [1, 3, 4, 8, 7, 9, 3, 5, 1]
    k = 2
    expected = [[1, 1, 3], [3, 4, 5], [7, 8, 9]]
    return expected, k, nums


@app.cell
def _(Solution, k, nums, run_divide_array):
    result = run_divide_array(Solution, nums, k)
    result
    return (result,)


@app.cell
def _(assert_divide_array, expected, k, result):
    assert_divide_array(result, expected, k)
    return


if __name__ == "__main__":
    app.run()
