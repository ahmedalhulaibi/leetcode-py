import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_smallest_range, run_smallest_range
    from solution import Solution

    return Solution, assert_smallest_range, run_smallest_range


@app.cell
def _():
    # Example test case
    nums = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
    expected = [20, 24]
    return expected, nums


@app.cell
def _(Solution, nums, run_smallest_range):
    result = run_smallest_range(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_smallest_range, expected, result):
    assert_smallest_range(result, expected)
    return


if __name__ == "__main__":
    app.run()
