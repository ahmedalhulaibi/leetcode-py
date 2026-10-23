import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_special_array, run_special_array
    from solution import Solution

    return Solution, assert_special_array, run_special_array


@app.cell
def _():
    # Example test case
    nums = [3, 5]
    expected = 2
    return expected, nums


@app.cell
def _(Solution, nums, run_special_array):
    result = run_special_array(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_special_array, expected, result):
    assert_special_array(result, expected)
    return


if __name__ == "__main__":
    app.run()
