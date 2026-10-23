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
    nums = [1, 2, 3, 4, 5]
    expected = [1, 2, 4, 5, 3]
    return expected, nums


@app.cell
def _(Solution, nums, run_rearrange_array):
    result = run_rearrange_array(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_rearrange_array, expected, result):
    assert_rearrange_array(result, expected)
    return


if __name__ == "__main__":
    app.run()
