import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_sort_array_by_parity, run_sort_array_by_parity
    from solution import Solution

    return Solution, assert_sort_array_by_parity, run_sort_array_by_parity


@app.cell
def _():
    # Example test case
    nums = [3, 1, 2, 4]
    expected = [2, 4, 3, 1]
    return expected, nums


@app.cell
def _(Solution, nums, run_sort_array_by_parity):
    result = run_sort_array_by_parity(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_sort_array_by_parity, expected, result):
    assert_sort_array_by_parity(result, expected)
    return


if __name__ == "__main__":
    app.run()
