import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_largest_divisible_subset, run_largest_divisible_subset
    from solution import Solution

    return (
        Solution,
        assert_largest_divisible_subset,
        run_largest_divisible_subset,
    )


@app.cell
def _():
    # Example test case
    nums = [1, 2, 4, 8]
    expected = [1, 2, 4, 8]
    return expected, nums


@app.cell
def _(Solution, nums, run_largest_divisible_subset):
    result = run_largest_divisible_subset(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_largest_divisible_subset, expected, result):
    assert_largest_divisible_subset(result, expected)
    return


if __name__ == "__main__":
    app.run()
