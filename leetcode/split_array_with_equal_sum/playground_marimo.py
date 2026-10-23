import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_split_array, run_split_array
    from solution import Solution

    return Solution, assert_split_array, run_split_array


@app.cell
def _():
    # Example test case
    nums = [1, 2, 1, 2, 1, 2, 1]
    expected = True
    return expected, nums


@app.cell
def _(Solution, nums, run_split_array):
    result = run_split_array(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_split_array, expected, result):
    assert_split_array(result, expected)
    return


if __name__ == "__main__":
    app.run()
