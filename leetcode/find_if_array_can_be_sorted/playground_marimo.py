import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_can_sort_array, run_can_sort_array
    from solution import Solution

    return Solution, assert_can_sort_array, run_can_sort_array


@app.cell
def _():
    # Example test case
    nums = [8, 4, 2, 30, 15]
    expected = True
    return expected, nums


@app.cell
def _(Solution, nums, run_can_sort_array):
    result = run_can_sort_array(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_can_sort_array, expected, result):
    assert_can_sort_array(result, expected)
    return


if __name__ == "__main__":
    app.run()
