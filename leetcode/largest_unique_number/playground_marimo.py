import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_largest_unique_number, run_largest_unique_number
    from solution import Solution

    return Solution, assert_largest_unique_number, run_largest_unique_number


@app.cell
def _():
    # Example test case
    nums = [5, 7, 3, 9, 4, 9, 8, 3, 1]
    expected = 8
    return expected, nums


@app.cell
def _(Solution, nums, run_largest_unique_number):
    result = run_largest_unique_number(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_largest_unique_number, expected, result):
    assert_largest_unique_number(result, expected)
    return


if __name__ == "__main__":
    app.run()
