import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_missing_number, run_missing_number
    from solution import Solution

    return Solution, assert_missing_number, run_missing_number


@app.cell
def _():
    # Example test case
    nums = [3, 0, 1]
    expected = 2
    return expected, nums


@app.cell
def _(Solution, nums, run_missing_number):
    result = run_missing_number(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_missing_number, expected, result):
    assert_missing_number(result, expected)
    return


if __name__ == "__main__":
    app.run()
