import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_split_array_same_average, run_split_array_same_average
    from solution import Solution

    return (
        Solution,
        assert_split_array_same_average,
        run_split_array_same_average,
    )


@app.cell
def _():
    # Example test case
    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    expected = True
    return expected, nums


@app.cell
def _(Solution, nums, run_split_array_same_average):
    result = run_split_array_same_average(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_split_array_same_average, expected, result):
    assert_split_array_same_average(result, expected)
    return


if __name__ == "__main__":
    app.run()
