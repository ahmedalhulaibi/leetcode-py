import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_rearrange_array, run_rearrange_array
    from solution import Solution

    return Solution, assert_rearrange_array, run_rearrange_array


@app.cell
def _():
    # Example test case
    nums = [3, 1, -2, -5, 2, -4]
    expected = [3, -2, 1, -5, 2, -4]
    return expected, nums


@app.cell
def _(Solution, expected, nums, run_rearrange_array):
    result = run_rearrange_array(Solution, nums, expected)
    result
    return (result,)


@app.cell
def _(assert_rearrange_array, expected, result):
    assert_rearrange_array(result, expected)
    return


if __name__ == "__main__":
    app.run()
