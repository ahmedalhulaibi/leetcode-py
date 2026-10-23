import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_constrained_subset_sum, run_constrained_subset_sum
    from solution import Solution

    return Solution, assert_constrained_subset_sum, run_constrained_subset_sum


@app.cell
def _():
    # Example test case
    nums = [10, 2, -10, 5, 20]
    k = 2
    expected = 37
    return expected, k, nums


@app.cell
def _(Solution, k, nums, run_constrained_subset_sum):
    result = run_constrained_subset_sum(Solution, nums, k)
    result
    return (result,)


@app.cell
def _(assert_constrained_subset_sum, expected, result):
    assert_constrained_subset_sum(result, expected)
    return


if __name__ == "__main__":
    app.run()
