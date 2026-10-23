import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_smallest_range_i, run_smallest_range_i
    from solution import Solution

    return Solution, assert_smallest_range_i, run_smallest_range_i


@app.cell
def _():
    # Example test case
    nums = [1]
    k = 0
    expected = 0
    return expected, k, nums


@app.cell
def _(Solution, k, nums, run_smallest_range_i):
    result = run_smallest_range_i(Solution, nums, k)
    result
    return (result,)


@app.cell
def _(assert_smallest_range_i, expected, result):
    assert_smallest_range_i(result, expected)
    return


if __name__ == "__main__":
    app.run()
