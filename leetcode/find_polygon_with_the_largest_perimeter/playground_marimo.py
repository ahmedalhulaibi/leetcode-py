import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_largest_perimeter, run_largest_perimeter
    from solution import Solution

    return Solution, assert_largest_perimeter, run_largest_perimeter


@app.cell
def _():
    # Example test case
    nums = [5, 5, 5]
    expected = 15
    return expected, nums


@app.cell
def _(Solution, nums, run_largest_perimeter):
    result = run_largest_perimeter(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_largest_perimeter, expected, result):
    assert_largest_perimeter(result, expected)
    return


if __name__ == "__main__":
    app.run()
