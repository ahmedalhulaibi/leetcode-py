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
    nums = [1, 2, 3, 3, 2, 2]
    expected = 2
    return expected, nums


@app.cell
def _(Solution, nums, run_longest_subarray):
    result = run_longest_subarray(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_longest_subarray, expected, result):
    assert_longest_subarray(result, expected)
    return


if __name__ == "__main__":
    app.run()
