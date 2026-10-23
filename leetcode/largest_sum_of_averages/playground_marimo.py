import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_largest_sum_of_averages, run_largest_sum_of_averages
    from solution import Solution

    return (
        Solution,
        assert_largest_sum_of_averages,
        run_largest_sum_of_averages,
    )


@app.cell
def _():
    # Example test case
    nums = [9, 1, 2, 3, 9]
    k = 3
    expected = 20.0
    return expected, k, nums


@app.cell
def _(Solution, k, nums, run_largest_sum_of_averages):
    result = run_largest_sum_of_averages(Solution, nums, k)
    result
    return (result,)


@app.cell
def _(assert_largest_sum_of_averages, expected, result):
    assert_largest_sum_of_averages(result, expected)
    return


if __name__ == "__main__":
    app.run()
