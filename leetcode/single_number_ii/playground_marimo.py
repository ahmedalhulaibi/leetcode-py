import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    from helpers import assert_single_number, run_single_number
    from solution import Solution

    return Solution, assert_single_number, run_single_number


@app.cell
def _():
    # Example test case
    nums = [2, 2, 3, 2]
    expected = 3
    return expected, nums


@app.cell
def _(Solution, nums, run_single_number):
    result = run_single_number(Solution, nums)
    result
    return (result,)


@app.cell
def _(assert_single_number, expected, result):
    assert_single_number(result, expected)
    return


if __name__ == "__main__":
    app.run()
