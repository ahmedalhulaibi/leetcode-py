import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_sum_subarray_mins, run_sum_subarray_mins
    from solution import Solution

    return Solution, assert_sum_subarray_mins, run_sum_subarray_mins


@app.cell
def _():
    # Example test case
    arr = [3, 1, 2, 4]
    expected = 17
    return arr, expected


@app.cell
def _(Solution, arr, run_sum_subarray_mins):
    result = run_sum_subarray_mins(Solution, arr)
    result
    return (result,)


@app.cell
def _(assert_sum_subarray_mins, expected, result):
    assert_sum_subarray_mins(result, expected)
    return


if __name__ == "__main__":
    app.run()
