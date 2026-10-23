import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_longest_subarray, run_longest_subarray
    from solution import Solution

    return Solution, assert_longest_subarray, run_longest_subarray


@app.cell
def _():
    # Example test case
    nums = [8, 2, 4, 7]
    limit = 4
    expected = 2
    return expected, limit, nums


@app.cell
def _(Solution, limit, nums, run_longest_subarray):
    result = run_longest_subarray(Solution, nums, limit)
    result
    return (result,)


@app.cell
def _(assert_longest_subarray, expected, result):
    assert_longest_subarray(result, expected)
    return


if __name__ == "__main__":
    app.run()
