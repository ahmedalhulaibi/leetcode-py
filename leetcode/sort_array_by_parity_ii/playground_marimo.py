import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_sort_array_by_parity_ii, run_sort_array_by_parity_ii
    from solution import Solution

    return (
        Solution,
        assert_sort_array_by_parity_ii,
        run_sort_array_by_parity_ii,
    )


@app.cell
def _():
    # Example test case
    nums = [4, 2, 5, 7]
    expected = [4, 5, 2, 7]
    return expected, nums


@app.cell
def _(Solution, nums, run_sort_array_by_parity_ii):
    result = run_sort_array_by_parity_ii(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_sort_array_by_parity_ii, expected, result):
    assert_sort_array_by_parity_ii(result, expected)
    return


if __name__ == "__main__":
    app.run()
