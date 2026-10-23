import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_max_sub_array, run_max_sub_array
    from solution import Solution

    return Solution, assert_max_sub_array, run_max_sub_array


@app.cell
def _():
    # Example test case
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    expected = 6
    return expected, nums


@app.cell
def _(Solution, nums, run_max_sub_array):
    result = run_max_sub_array(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_max_sub_array, expected, result):
    assert_max_sub_array(result, expected)
    return


if __name__ == "__main__":
    app.run()
