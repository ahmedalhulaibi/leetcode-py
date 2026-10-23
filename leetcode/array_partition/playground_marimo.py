import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_array_pair_sum, run_array_pair_sum
    from solution import Solution

    return Solution, assert_array_pair_sum, run_array_pair_sum


@app.cell
def _():
    # Example test case
    nums = [1, 4, 3, 2]
    expected = 4
    return expected, nums


@app.cell
def _(Solution, nums, run_array_pair_sum):
    result = run_array_pair_sum(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_array_pair_sum, expected, result):
    assert_array_pair_sum(result, expected)
    return


if __name__ == "__main__":
    app.run()
