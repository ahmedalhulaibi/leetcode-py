import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_frequency_sort, run_frequency_sort
    from solution import Solution

    return Solution, assert_frequency_sort, run_frequency_sort


@app.cell
def _():
    # Example test case
    nums = [1, 1, 2, 2, 2, 3]
    expected = [3, 1, 1, 2, 2, 2]
    return expected, nums


@app.cell
def _(Solution, nums, run_frequency_sort):
    result = run_frequency_sort(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_frequency_sort, expected, result):
    assert_frequency_sort(result, expected)
    return


if __name__ == "__main__":
    app.run()
