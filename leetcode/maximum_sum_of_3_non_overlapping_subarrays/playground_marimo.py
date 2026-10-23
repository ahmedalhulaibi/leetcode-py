import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_max_sum_of_three_subarrays, run_max_sum_of_three_subarrays
    from solution import Solution

    return (
        Solution,
        assert_max_sum_of_three_subarrays,
        run_max_sum_of_three_subarrays,
    )


@app.cell
def _():
    # Example test case
    nums = [1, 2, 1, 2, 6, 7, 5, 1]
    k = 2
    expected = [0, 3, 5]
    return expected, k, nums


@app.cell
def _(Solution, k, nums, run_max_sum_of_three_subarrays):
    result = run_max_sum_of_three_subarrays(Solution, nums, k)
    result
    return (result,)


@app.cell
def _(assert_max_sum_of_three_subarrays, expected, result):
    assert_max_sum_of_three_subarrays(result, expected)
    return


if __name__ == "__main__":
    app.run()
