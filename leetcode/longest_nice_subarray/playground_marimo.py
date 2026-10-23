import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_longest_nice_subarray, run_longest_nice_subarray
    from solution import Solution

    return Solution, assert_longest_nice_subarray, run_longest_nice_subarray


@app.cell
def _():
    # Example test case
    nums = [1, 3, 8, 48, 10]
    expected = 3
    return expected, nums


@app.cell
def _(Solution, nums, run_longest_nice_subarray):
    result = run_longest_nice_subarray(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_longest_nice_subarray, expected, result):
    assert_longest_nice_subarray(result, expected)
    return


if __name__ == "__main__":
    app.run()
