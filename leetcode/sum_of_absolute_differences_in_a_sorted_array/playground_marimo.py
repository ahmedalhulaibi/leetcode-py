import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_get_sum_absolute_differences, run_get_sum_absolute_differences
    from solution import Solution

    return (
        Solution,
        assert_get_sum_absolute_differences,
        run_get_sum_absolute_differences,
    )


@app.cell
def _():
    # Example test case
    nums = [2, 3, 5]
    expected = [4, 3, 5]
    return expected, nums


@app.cell
def _(Solution, nums, run_get_sum_absolute_differences):
    result = run_get_sum_absolute_differences(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_get_sum_absolute_differences, expected, result):
    assert_get_sum_absolute_differences(result, expected)
    return


if __name__ == "__main__":
    app.run()
