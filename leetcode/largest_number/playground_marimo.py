import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_largest_number, run_largest_number
    from solution import Solution

    return Solution, assert_largest_number, run_largest_number


@app.cell
def _():
    # Example test case
    nums = [3, 30, 34, 5, 9]
    expected = "9534330"
    return expected, nums


@app.cell
def _(Solution, nums, run_largest_number):
    result = run_largest_number(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_largest_number, expected, result):
    assert_largest_number(result, expected)
    return


if __name__ == "__main__":
    app.run()
