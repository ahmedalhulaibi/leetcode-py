import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_maximum_gap, run_maximum_gap
    from solution import Solution

    return Solution, assert_maximum_gap, run_maximum_gap


@app.cell
def _():
    # Example test case
    nums = [3, 6, 9, 1]
    expected = 3
    return expected, nums


@app.cell
def _(Solution, nums, run_maximum_gap):
    result = run_maximum_gap(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_maximum_gap, expected, result):
    assert_maximum_gap(result, expected)
    return


if __name__ == "__main__":
    app.run()
