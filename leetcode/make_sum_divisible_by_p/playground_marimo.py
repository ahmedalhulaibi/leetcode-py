import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_min_subarray, run_min_subarray
    from solution import Solution

    return Solution, assert_min_subarray, run_min_subarray


@app.cell
def _():
    # Example test case
    nums = [3, 1, 4, 2]
    p = 6
    expected = 1
    return expected, nums, p


@app.cell
def _(Solution, nums, p, run_min_subarray):
    result = run_min_subarray(Solution, nums, p)
    result
    return (result,)


@app.cell
def _(assert_min_subarray, expected, result):
    assert_min_subarray(result, expected)
    return


if __name__ == "__main__":
    app.run()
