import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_sorted_squares, run_sorted_squares
    from solution import Solution

    return Solution, assert_sorted_squares, run_sorted_squares


@app.cell
def _():
    # Example test case
    nums = [-4, -1, 0, 3, 10]
    expected = [0, 1, 9, 16, 100]
    return expected, nums


@app.cell
def _(Solution, nums, run_sorted_squares):
    result = run_sorted_squares(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_sorted_squares, expected, result):
    assert_sorted_squares(result, expected)
    return


if __name__ == "__main__":
    app.run()
