import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_subset_xor_sum, run_subset_xor_sum
    from solution import Solution

    return Solution, assert_subset_xor_sum, run_subset_xor_sum


@app.cell
def _():
    # Example test case
    nums = [1, 3]
    expected = 6
    return expected, nums


@app.cell
def _(Solution, nums, run_subset_xor_sum):
    result = run_subset_xor_sum(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_subset_xor_sum, expected, result):
    assert_subset_xor_sum(result, expected)
    return


if __name__ == "__main__":
    app.run()
