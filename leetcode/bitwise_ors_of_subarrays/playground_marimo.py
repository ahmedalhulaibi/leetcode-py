import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_subarray_bitwise_ors, run_subarray_bitwise_ors
    from solution import Solution

    return Solution, assert_subarray_bitwise_ors, run_subarray_bitwise_ors


@app.cell
def _():
    # Example test case
    arr = [1, 1, 2]
    expected = 3
    return arr, expected


@app.cell
def _(Solution, arr, run_subarray_bitwise_ors):
    result = run_subarray_bitwise_ors(Solution, arr)
    result
    return (result,)


@app.cell
def _(assert_subarray_bitwise_ors, expected, result):
    assert_subarray_bitwise_ors(result, expected)
    return


if __name__ == "__main__":
    app.run()
